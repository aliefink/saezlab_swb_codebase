from tqdm import tqdm
import numpy as np
import pandas as pd
import scipy
from scipy.stats import norm
from scipy.optimize import least_squares, minimize
from joblib import Parallel, delayed
from sklearn.metrics import r2_score
import random
from statsmodels.stats.outliers_influence import variance_inflation_factor
# from numpy.linalg import vecdot


#### Fit Mood Models with pyEM


############### SWB GLMS ################

#fit swb glm function
def swb_mood_pyEM(params,df,mood_var='norm_mood',g_type='exp', prior=None, output='npl'):

    # params is 1d array length K (gamma, intercept, coefficient/var)
    K     = len(params) # compute K for BIC/AIC equations
    g     = params[0] # temporal decay  
    b0    = params[1] # glm intercept
    b_vec = params[2:] # vector of beta coefficient estimates for each predictor category
    
    if g_type == 'exp':
        g_vec = np.array([1.0,g,g**2]) # exponential decay
    elif g_type == 'linear':
        g_vec = np.array([1.0,g,g*2]) # gam x 2 not gam ^2 for linear
    else: 
        g_vec = np.array([1.0,1.0,1.0]) # no gam exponent
        K = K-1 # update K to drop gamma in param count

    # make 1d vector of model coefficients (beta, beta*gamma, beta*gamma^2 for every reg)
    coeff_vec = np.hstack([np.array([b,b*g_vec[1],b*g_vec[2]]) for b in b_vec])
    # predictor data - array nratings x npredictors (x3 for t1,t2,t3) 
    X = df[df.columns[df.columns != mood_var]].to_numpy()
    # dot product between data matrix X [ntrials x nregressors] and betas matrix [nregressors]
    mood_dot = np.dot(X, coeff_vec)
    # add intercept to mood vec estimate
    pred_mood = mood_dot + b0

    # observed mood ratings  
    obs_mood = df[mood_var]
    # model residuals - difference in observed y, predicted y 
    resid_mood = np.subtract(obs_mood,pred_mood)

    # residual sum of squares 
    rss = np.sum(resid_mood**2)
    # std of residuals for negll equation
    resid_std = np.std(resid_mood) 
    
    # negative log likelihood with gaussian pdf fn scaled by std of residuals  
    negll = -np.sum(scipy.stats.norm.logpdf(obs_mood,loc=pred_mood,scale=resid_std))
    
    if np.isnan(negll): # won't break with bad param estimates
        negll = np.inf
    
    if output == 'npl':
        if prior is not None:  # EM-fit: P(Choices | h) * P(h | O) should be maximised, therefore same as minimizing it with negative sign
            fval = -(-negll + prior['logpdf'](params))

            if any(prior['sigma'] == 0):
                this_mu = prior['mu']
                this_sigma = prior['sigma']
                this_logprior = prior['logpdf'](params)
                print(f'mu: {this_mu}')
                print(f'sigma: {this_sigma}')
                print(f'logpdf: {this_logprior}')
                print(f'fval: {fval}')
            
            if np.isinf(fval): 
                fval = 10000000
            return fval
        else: # NLL fit 
            return negll
    
    elif output == 'rss': ## if minimizing residual sum of squares
        return rss

    elif output == 'all':
        subj_dict = {'params'     : params,
                     'reg_list'   : list(df.columns[df.columns != mood_var]),
                     'pred_mood'  : pred_mood,
                     'negll'      : negll,
                     'bic'        : K*np.log(len(pred_mood)) + 2*negll}

        return subj_dict


#fit swb glm function
def fit_swb_glm(params,df,mood_var='norm_mood',
    g_type='exp',output='negll'):
    # params is 1d array length K (gamma, intercept, coefficient/var)
    K     = len(params) # compute K for BIC/AIC equations
    g     = params[0] # temporal decay  
    b0    = params[1] # glm intercept
    b_vec = params[2:] # vector of beta coefficient estimates for each predictor category
    
    if g_type == 'exp':
        g_vec = np.array([1.0,g,g**2]) # exponential decay
    elif g_type == 'linear':
        g_vec = np.array([1.0,g,g*2]) # gam x 2 not gam ^2 for linear
    else: 
        g_vec = np.array([1.0,1.0,1.0]) # no gam exponent
        K = K-1 # update K to drop gamma in param count

    # make 1d vector of model coefficients (beta, beta*gamma, beta*gamma^2 for every reg)
    coeff_vec = np.hstack([np.array([b,b*g_vec[1],b*g_vec[2]]) for b in b_vec])
    # predictor data - array nratings x npredictors (x3 for t1,t2,t3) 
    X = df[df.columns[df.columns != mood_var]].to_numpy()
    # dot product between data matrix X [ntrials x nregressors] and betas matrix [nregressors]
    mood_dot = np.dot(X, coeff_vec)
    # add intercept to mood vec estimate
    pred_mood = mood_dot + b0
    # observed mood ratings  
    obs_mood = df[mood_var]
    # model residuals - difference in observed y, predicted y 
    resid_mood = np.subtract(obs_mood,pred_mood)
    # residual sum of squares 
    rss = np.sum(resid_mood**2)
    # std of residuals for negll equation
    resid_std = np.std(resid_mood) 
    # negative log likelihood with gaussian pdf fn scaled by std of residuals  
    negll = -np.sum(scipy.stats.norm.logpdf(obs_mood,loc=pred_mood,scale=resid_std))

    if output == 'negll':    
        return negll 

    elif output == 'rss':
        return rss

    elif output == 'all':
        subj_dict = {'params'     : params,
                     'reg_list'   : list(df.columns[df.columns != mood_var]),
                     'pred_mood'  : pred_mood,
                     'negll'      : negll,
                     'bic'        : K*np.log(len(pred_mood)) + 2*negll}

        return subj_dict


def min_negll_glm(func_obj, param_values, df, param_bounds):
    # minimize negll via MLE via gradient descent

    result = minimize(func_obj, 
                      param_values, 
                      (df),
                      bounds=param_bounds)
    return result
 
def parallel_glm_fit(min_fn, fit_fn,param_combo_guesses,param_bounds,subj_df,n_jobs=-1):
    '''
    Maximum likelihood estimation with parallel processing 

    Inputs:
        - min_fn: minimization function 
        - fit_fn: model fitting function (should return negll only)
        - param_combo_guesses: grid of initial param values for parallel min_fn runs 
        - param_bounds: min/max bounds for params in this format: (0,5),(0,5),(0,10)
        - subj_df: pandas df of subj task data
    
    Returns:
        - fit_dict: output of fit_fn

    '''

    
    ##### Minimize negll via parallel mle

    # Parallel fn :
        # Basic syntax Parallel(n_jobs,verbose) ( delayed(optim_fn)(optim_fun inputs) loop for parallel fn inputs )
        # requires Parallel & delayed from joblib
        # n_jobs=-2 - num cpus used, -1 for all, -2 for all but one, +num for specific num
        # verbose default is none, higher than 10 will give all
        # delayed() = hold memory for function to run in parallel
        # optim_fn = minimization fn
        # ()() = inputs for optim_fn in delay - negll fn, params, data, bounds
        # (()()____): iterations of initial param values 
    
    results = Parallel(n_jobs=n_jobs, verbose=5)(delayed(min_fn)(fit_fn, param_values, (subj_df), param_bounds) 
                                                 for param_values in param_combo_guesses)

    # determine optimal parameter combination from negll
    fit_dict = {}
    best_result = min(results, key=lambda x: x.fun) # use lambda function to get negll from each run in results (lambda args: expression) 
    param_fits = best_result.x
    fit_dict['best_result'] = best_result
    # run fit_fn with param_fits get best model fit info ### implement this with GLMs!
    fit_dict['subj_dict'] = fit_fn(param_fits, subj_df,output='all')
    
    
    return fit_dict

def fit_swb(params,df,n_regs,reg_list,lam_method='exp',output='rss'):

    #params is list of lambda estimate + beta estimates 
    betas = params[1:] # list of beta estimates - first index = intercept 
    lam = params[0] # lamda estimate
    K = len(params) # num free params in optimization - used to calculate BIC

    if lam_method == 'exp':
        ls = [1,lam,lam**2] #exponential lambda 
    elif lam_method == 'linear':
        ls = [1,lam,lam*2] #linear lambda 
    else: 
        betas = params # lam not being estimated - not in input params list 
        lam = [1] #lamda
        ls = [1,1,1] #none
        K = K-1 #param count is -1 because lam is not being optimized
        
    #initialize mood estimate equation     
    param_eq = 0

    for n in range(n_regs):
        b = betas[n+1] # first beta value = intercept, so need +1 for weights
        l1 = ls[0] #t-1 decay
        l2 = ls[1] #t-2 decay
        l3 = ls[2] #t-3 decay
        #regressor index for t-1,t-2,t-3
        i1 = (n*3)
        i2 = (n*3)+1
        i3 = (n*3)+2
        #regressor vars to extract from df 
        reg1 = reg_list[i1]
        reg2 = reg_list[i2]
        reg3 = reg_list[i3]
        #regresssor vectors 
        reg1_vec = np.array(df[reg1])
        reg2_vec = np.array(df[reg2])
        reg3_vec = np.array(df[reg3])

        param_eq += (b*l1*reg1_vec) + (b*l2*reg2_vec) + (b*l3*reg3_vec)

    # get the estimated mood rating from the parameter equation (plus intercept!)
    mood_est = [betas[0]]*len(df) + param_eq
    # actual mood obs
    mood_obs = np.array(df['z_rate'])
    #compute the vector of residuals
    mood_residuals = mood_obs - mood_est     # sse = np.sum((m.predict(x) - y) ** 2, axis=0) / float(x.shape[0] - x.shape[1])
    rss = np.sum(mood_residuals**2) 

    if output == 'rss':
        return rss
    
    # output for fitting 
    elif output == 'all': 
        subj_dict = {'params'     : params,
                     'reg_list'   : reg_list,
                     'lam_method' : lam_method,
                     'mood_est'   : mood_est,
                     'mood_obs'   : mood_obs,
                     'mood_resid' : mood_residuals,
                     'rss'        : rss,
                     'bic'        : K * np.log(len(mood_residuals)) - 2*np.log((rss/len(mood_residuals))),
                     'aic'        : 2*K + n*np.log(rss/len(mood_residuals))
                     } #https://stats.stackexchange.com/questions/338501/calculating-the-aicc-and-bic-with-rss-instead-of-likelihood

        return subj_dict
    

def fit_swb_pyEM(params,df,reg_list,lam_method='exp',prior=None, output='npl'):
    # reg_list is list of regressor names estimate beta values from
    # output can be rss, npl, or all
    
    var_list = reg_list[2:]
    n_regs = len(var_list)
    full_var_list = []
    for var in var_list:
        t1_col = var + '_t-1' 
        t2_col = var + '_t-2'
        t3_col = var + '_t-3'
        # add modified variable names to list - should match column names in all_subj_model_df
        full_var_list.append(t1_col)
        full_var_list.append(t2_col)
        full_var_list.append(t3_col)


    #params is list of lambda estimate + beta estimates 
    betas = params[1:] # list of beta estimates - first index = intercept 
    K = len(params) # num free params in optimization - used to calculate BIC
    lam = params[0] # lamda estimate

    #transformation for em map estimation:
    if output == 'npl':
        lam = scipy.special.expit(lam) #logistic sigmoid conversion 
        lam_bounds = [0.0000001, 1] #set upper and lower bounds
        if lam< min(lam_bounds) or lam > max(lam_bounds): #prevent estimation from parameter values outside of bounds 
            return 10000000
        
    if lam_method == 'exp':
        ls = [1,lam,lam**2] #exponential lambda 
    elif lam_method == 'linear':
        ls = [1,lam,lam*2] #linear lambda 
    else: 
        betas = params # lam not being estimated - not in input params list 
        lam = [1] #lamda
        ls = [1,1,1] #none
        K = K-1 #param count is -1 because lam is not being optimized
        
    #initialize mood estimate equation     
    param_eq = 0

    for n in range(n_regs):
        b = betas[n+1] # first beta value = intercept, so need +1 for weights
        l1 = ls[0] #t-1 decay
        l2 = ls[1] #t-2 decay
        l3 = ls[2] #t-3 decay
        #regressor index for t-1,t-2,t-3
        i1 = (n*3)
        i2 = (n*3)+1
        i3 = (n*3)+2
        #regressor vars to extract from df 
        reg1 = full_var_list[i1] #from full var list now, not reg list (reg list is just reg ids, not t-1 col names)
        reg2 = full_var_list[i2]
        reg3 = full_var_list[i3]
        #regresssor vectors 
        reg1_vec = np.array(df[reg1])
        reg2_vec = np.array(df[reg2])
        reg3_vec = np.array(df[reg3])

        param_eq += (b*l1*reg1_vec) + (b*l2*reg2_vec) + (b*l3*reg3_vec)

    # get the estimated mood rating from the parameter equation (plus intercept!)
    mood_est = [betas[0]]*len(df) + param_eq
    # actual mood obs
    mood_obs = np.array(df['z_rate'])
    #compute the vector of residuals
    mood_residuals = np.subtract(mood_obs,mood_est)#mood_obs - mood_est #np.subtract(mood_obs, mood_est))
    rss = np.sum(mood_residuals**2)

    if output == 'rss':
        return rss
    
    # output for EM MAP optimization - negative posterior likelihood from negll & likelihood of prior
    elif output == 'npl':
        if prior is not None:  # EM-fit: P(Choices | h) * P(h | O) should be maximised, therefore same as minimizing it with negative sign
            #calculate negll 
            resid_sigma = np.std(np.subtract(mood_obs, mood_est)) # std dev of residuals
            #logpdf with estimates as zero point and residual std as scale (approx -0.5N(ln(2pi))+ln(rss/n)+1)
            #https://clas.ucdenver.edu/marcelo-perraillon/sites/default/files/attached-files/week_6_mle.pdf formula on page 24
            negll = -np.sum(norm.logpdf(mood_obs, loc=mood_est, scale=resid_sigma)) #negative sum of log of pdf for mood est w current params
            #get f value from negll & likelihood of prior (posterior likelihood)
                # get negll as positive likelihood, add current model likelihood & likelihood of prior, then take neg = negative posterior likelihood
            fval = -(-negll + prior['logpdf'](params)) #np.sum(norm.logpdf(x, prior['mu'],np.sqrt(prior['sigma'])))
             
            if any(prior['sigma'] == 0):
                this_mu = prior['mu']
                this_sigma = prior['sigma']
                this_logprior = prior['logpdf'](params)
                print(f'mu: {this_mu}')
                print(f'sigma: {this_sigma}')
                print(f'logpdf: {this_logprior}')
                print(f'fval: {fval}')
            
            if np.isinf(fval): 
                fval = 10000000
            if fval is None:
                fval = 10000000
            return fval
    
    # output for fitting 
    elif output == 'all': 
        subj_dict = {'params'     : params,
                     'reg_list'   : reg_list,
                     'lam_method' : lam_method,
                     'mood_est'   : mood_est,
                     'mood_obs'   : mood_obs,
                     'mood_resid' : mood_residuals,
                     'rss'        : rss,
                     'bic'        : K * np.log(len(mood_residuals)) - 2*np.log((rss/len(mood_residuals))),
                     'aic'        : 2*K + n*np.log(rss/len(mood_residuals))
                     } #https://stats.stackexchange.com/questions/338501/calculating-the-aicc-and-bic-with-rss-instead-of-likelihood

        return subj_dict




#### option to use minimize function to minimize rss instead of least_sq optimization 


def min_rss_swb(subj_df, n_regs, reg_list, param_inits):
    
    # INPUTS:
    # model_df:     model data for subj 
    # subj_id:      subj data for fitting
    # n_regs:       number of task variables in model (ex: ev,cr,rpe = 3 n_regs)
    # reg_list:     list of column names in df as str (should be len n_regs*3, 3 trials for each variable)
    # param_inits:  list of initial parameter value combinations to iterate through - fn will run through optimization for each item in param_guesses [(nparams)(nparams)]
    # lam_method:   calculation of lam param ['exp','linear','none']


    # calculate bounds for each param init 
    n_beta_bounds = n_regs+1
    # # remove lam from bounds if none 
    # if lam_method == 'none': #remove lam from estimation + bounds input
    #     bounds = tuple([(-100,100)]*n_beta_bounds)
    # else: 
    #     bounds = tuple([(0.001,1)]+[(-10,10)]*n_beta_bounds)
    
    bounds = tuple([(0.001,1)]+[(-10,10)]*n_beta_bounds)
    
    #initialize best result & initial rss value to minimize 
    best_result = []
    rss_optim   = np.inf 

    for params in param_inits:

        # if lam_method == 'none': #remove lam from estimation + bounds input
        #     params = params[1:]
        # else:
        #     params = params

        #run minimization for each param combo in param_inits
        result = minimize(fit_swb, # objective function
                    params,
                    args=(subj_df,n_regs,reg_list), #reg_list should be in long form (3 str per n reg)
                    bounds=bounds) # arguments #method='L-BFGS-B'
        
        #extract rss from result output 
        rss = result.fun #residuals output from model
        print(rss)
        if rss < rss_optim: #goal to minimize cost function, find params that give lowest possible rss
            rss_optim = rss                
            best_result = result
            best_params = best_result.x 
    
    if rss_optim == np.inf:
        print(f'No solution for this subject rss={rss} optim={rss_optim}')
        fit_dict = {}
        fit_dict['result'] = result
        return fit_dict
    
    else:
        #fit model with optim params
        fit_dict = {}
        fit_dict['best_result'] = best_result
        fit_dict['subj_dict']   = fit_swb(best_params,subj_df,n_regs,reg_list,lam_method='exp',output='all') #run fit function to get all outputs (better than 2 separate fns)

        return fit_dict


def param_init(n_values, n_iter, upper_bound, lower_bound, method, beta_shape=0):
    #inputs:
        #n_values: how many parameter values needed
        #n_iter: how many rounds of initialization; if method = 'rand' will return dict with array n_iter x n_values; if method = 'mc_grid' will return dict with grid n_iter x n_iter for each param (n_values)
        #upper_bound: max possible parameter value
        #lower_bound: min possible parameter value
        #beta_shape: [a,b] alpha and beta values for beta distribution
        #method: rand, mc_grid

    #outputs:
        #param dict - dictionary of param_id: init values (number of values = n_values)

    if method == 'rand':
        param_array = np.zeros(shape=(n_iter,n_values))
        for iter in range(n_iter):
            for val in range(n_values):
                if iter%2==0:
                    param_array[iter,val] = random.uniform(lower_bound,lower_bound+1) #hacky way to bias random initialization to have more numbers between 0-1
                if iter%2!=0:
                    param_array[iter,val] = random.uniform(lower_bound,upper_bound)
    
    elif method == 'beta':
        a = beta_shape[0]
        b = beta_shape[1]
        N = n_iter

        param_array = (upper_bound - lower_bound) * np.random.beta(a, b, N) + lower_bound

    
    #elif method == 'mc_grid':
        #to do - make large parameter grid for monte carlo method for paramter initialization
        #arianna matlab code:             # %% Free param starting points
            # free0 = cell(nM, 1); % nM is number of models #collection of all start points that you're about to generate

            # for m = 1:nM #can do for bunch of models at once but doesn't need to be loop
            #     numStartingPoints = 10000; % Number of starting points to sample using Monte Carlo method #40k here
            #     free0{m} = zeros(numStartingPoints, nX); #empty matrix for params
            #     for s = 1:numStartingPoints 
            #         % Generate random starting point for free parameters
            #         free0{m}(s, xIndex{m}) = rand(1, length(xIndex{m})); #this is where you generate random starting point - create array for starting points and then outside of this loop through it with model - arianna constrains later! 
            #     end
            # end
    
    
    return param_array


def simulation_norm_gamble_choices(df): #to-do input column names to make this robust to standard + util 
    
    #df is task data for a single subject
    loss_df = df[df.TrialType == 'loss']
    mix_df = df[df.TrialType == 'mix']
    gain_df = df[df.TrialType == 'gain']

    #loss
    loss_dict = {}
    loss_norm = -((loss_df['LowBet'] + loss_df['HighBet'])/2)/loss_df['SafeBet']
    loss_quant = np.quantile(loss_norm,q=(0,0.2,0.4,0.6,0.8,1),axis=0)
    loss_x_axis = [np.mean(loss_quant[i:i+2],dtype=np.float64) for i in range(5)]
    loss_dec = loss_df['ChoicePred'].replace(['gamble','safe'],[1,0])
    loss_zip = list(zip(loss_norm,loss_dec))
    loss_dict['loss_norm_evs'] = np.array(loss_norm)
    loss_dict['loss_choices'] = np.array(loss_dec)
    loss_dict['loss_x_axis'] = loss_x_axis
    loss_norm_range = []
    loss_choice_props = []
    for r in range(5):
        loss_ev_range = np.array([loss_quant[r],loss_quant[r+1]])
        loss_gamble_count = [z[1] for z in loss_zip if z[0] >= loss_ev_range[0] and z[0] <= loss_ev_range[1]]
        loss_ev_num = sum(loss_gamble_count)
        loss_ev_prop = loss_ev_num/len(loss_gamble_count)
        loss_norm_range.append(loss_ev_range)
        loss_choice_props.append(loss_ev_prop)
    loss_dict['loss_norm_range'] = loss_norm_range
    loss_dict['loss_choice_props'] = loss_choice_props
    
    #mix
    mix_dict = {}
    mix_norm = ((mix_df['LowBet'] + mix_df['HighBet'])/2) #can't divide by zero
    mix_quant = np.quantile(mix_norm,q=(0,0.2,0.4,0.6,0.8,1),axis=0)
    mix_x_axis = [np.mean(mix_quant[i:i+2],dtype=np.float64) for i in range(5)]
    mix_dec = mix_df['ChoicePred'].replace(['gamble','safe'],[1,0])
    mix_zip = list(zip(mix_norm,mix_dec))
    mix_dict['mix_norm_evs'] = np.array(mix_norm)
    mix_dict['mix_choices'] = np.array(mix_dec)
    mix_dict['mix_x_axis'] = mix_x_axis
    mix_norm_range = []
    mix_choice_props = []
    for r in range(5):
        mix_ev_range = np.array([mix_quant[r],mix_quant[r+1]])
        mix_gamble_count = [z[1] for z in mix_zip if z[0] >= mix_ev_range[0] and z[0] <= mix_ev_range[1]]
        mix_ev_num = sum(mix_gamble_count)
        mix_ev_prop = mix_ev_num/len(mix_gamble_count)
        mix_norm_range.append(mix_ev_range)
        mix_choice_props.append(mix_ev_prop)
    mix_dict['mix_norm_range'] = mix_norm_range
    mix_dict['mix_choice_props'] = mix_choice_props

    
    #gain
    gain_dict = {}
    gain_norm = ((gain_df['LowBet'] + gain_df['HighBet'])/2)/gain_df['SafeBet']
    gain_quant = np.quantile(gain_norm,q=(0,0.2,0.4,0.6,0.8,1),axis=0)
    gain_x_axis = [np.mean(gain_quant[i:i+2],dtype=np.float64) for i in range(5)]
    gain_dec = gain_df['ChoicePred'].replace(['gamble','safe'],[1,0])
    gain_zip = list(zip(gain_norm,gain_dec))
    gain_dict['gain_norm_evs'] = np.array(gain_norm)
    gain_dict['gain_choices'] = np.array(gain_dec)
    gain_dict['gain_x_axis'] = gain_x_axis
    gain_norm_range = []
    gain_choice_props = []
    for r in range(5):
        gain_ev_range = np.array([gain_quant[r],gain_quant[r+1]])
        gain_gamble_count = [z[1] for z in gain_zip if z[0] >= gain_ev_range[0] and z[0] <= gain_ev_range[1]]
        gain_ev_num = sum(gain_gamble_count)
        gain_ev_prop = gain_ev_num/len(gain_gamble_count)
        gain_norm_range.append(gain_ev_range)
        gain_choice_props.append(gain_ev_prop)
    gain_dict['gain_norm_range'] = gain_norm_range
    gain_dict['gain_choice_props'] = gain_choice_props
    
    return loss_dict, mix_dict, gain_dict


def get_glm_data_all_subj(model_data_vars,subj_ids,behav_dir):
    
    #dictionary to hold all subj data
    all_subj_model_dict = {}   

    # make a list of regressor names from regressor list - each regressor needs 3 vars for t-1,t-2,t-3 trials 
    model_data_dict_keys = []
    for var in model_data_vars:
        t1_col = var + '_t-1' 
        t2_col = var + '_t-2'
        t3_col = var + '_t-3'
        model_data_dict_keys.append(t1_col)
        model_data_dict_keys.append(t2_col)
        model_data_dict_keys.append(t3_col)

    #create model data pandas df with model_data_dict_keys as column names 
    model_df_col_names = ['subj_id','round','rate','zscore_rate','bdi','bai'] + model_data_dict_keys
    all_subj_model_df = pd.DataFrame(columns = model_df_col_names)
      

    for subj_id in subj_ids:

        task_df = pd.read_csv(f'{behav_dir}{subj_id}_pt_task_data')
        rate_df = pd.read_csv(f'{behav_dir}{subj_id}_rate_data')

        # make a list of regressor names from regressor list - each regressor needs 3 vars for t-1,t-2,t-3 trials 
        model_data_dict_keys = []
        for var in model_data_vars:
            t1_col = var + '_t-1' 
            t2_col = var + '_t-2'
            t3_col = var + '_t-3'
            model_data_dict_keys.append(t1_col)
            model_data_dict_keys.append(t2_col)
            model_data_dict_keys.append(t3_col)

        #create model data dictionary with model_data_dict_keys as keys and empty lists as their values (can use append function in loop now)
        model_data_dict = {}
        for i in model_data_dict_keys:
            model_data_dict[i] = []

        # #get rating info
        round       = rate_df['Round'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:] #need index of last round 1 because some pts have multiple round 1 scores, start after last round 1 index
        rate        = rate_df['Rating'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]
        zscore_rate = rate_df['zscore_mood'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]
        bdi         = rate_df['bdi'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]
        bai         = rate_df['bai'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]


        #add subj info and non task vars to model data dict
        model_data_dict['subj_id'] = [subj_id]*50
        model_data_dict['round'] = round
        model_data_dict['rate'] = rate
        model_data_dict['zscore_rate'] = zscore_rate
        model_data_dict['bdi'] = bdi
        model_data_dict['bai'] = bai

        for r in round: #iterate through mood rating rounds (4,7,10...151)
            #calculate row index for task df
            t3 = r-4 #t-3 trial 
            t2 = r-3 #t-2 trial
            t1 = r-2 #t-1 trial
            
            for reg in model_data_vars:
                # make reg name strings for model data keys
                reg_t3_col = reg + '_t-3'
                reg_t2_col = reg + '_t-2'
                reg_t1_col = reg + '_t-1'

                model_data_dict[reg_t3_col].append(task_df[reg][t3])
                model_data_dict[reg_t2_col].append(task_df[reg][t2])
                model_data_dict[reg_t1_col].append(task_df[reg][t1])
        
        #add to master dictionary 
        all_subj_model_dict[subj_id] = model_data_dict #in case dictionary of dictionaries is easier to work with later
        #add to all_subj_model_df
        all_subj_model_df = pd.concat([all_subj_model_df,pd.DataFrame(model_data_dict)])
    
    return model_data_dict

def get_glm_data_single_subj(subj_id,behav_dir,model_data_vars):

    #load subject task data - pt data  
    task_df = pd.read_csv(f'{behav_dir}{subj_id}_pt_task_data')
    rate_df = pd.read_csv(f'{behav_dir}{subj_id}_rate_data')

    # make a list of regressor names from regressor list - each regressor needs 3 vars for t-1,t-2,t-3 trials 
    model_data_dict_keys = []
    for var in model_data_vars:
        t1_col = var + '_t-1' 
        t2_col = var + '_t-2'
        t3_col = var + '_t-3'
        model_data_dict_keys.append(t1_col)
        model_data_dict_keys.append(t2_col)
        model_data_dict_keys.append(t3_col)
    
    #create model data dictionary with model_data_dict_keys as keys and empty lists as their values (can use append function in loop now)
    model_data_dict = {}
    for i in model_data_dict_keys:
        model_data_dict[i] = []

    # #get rating info
    round  = rate_df['Round'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:] #need index of last round 1 because some pts have multiple round 1 scores, start after last round 1 index
    rate   = rate_df['Rating'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]
    z_rate = rate_df['zscore_mood'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]
    bdi    = rate_df['bdi'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]
    bai    = rate_df['bai'][max(loc for loc, val in enumerate(rate_df['Round']) if val == 1)+1:]

    #check if task data is shorter than last round idx
    task_len = len(task_df)
    if task_len < list(round)[-1]:
        round  = list(round)[:-1]
        rate   = list(rate)[:-1]
        z_rate = list(z_rate)[:-1]
        bdi    = list(bdi)[:-1]
        bai    = list(bai)[:-1]



    #add subj info and non task vars to model data dict
    model_data_dict['subj_id']  = [subj_id]*len(round)
    model_data_dict['round']    = round
    model_data_dict['rate']     = rate
    model_data_dict['z_rate']   = z_rate
    model_data_dict['bdi']      = bdi
    model_data_dict['bai']      = bai

    for r in round: #iterate through mood rating rounds (4,7,10...151)
        #calculate row index for task df
        t3 = r-4 #t-3 trial 
        t2 = r-3 #t-2 trial
        t1 = r-2 #t-1 trial
        
        for reg in model_data_vars:
            # make reg name strings for model data keys
            reg_t3_col = reg + '_t-3'
            reg_t2_col = reg + '_t-2'
            reg_t1_col = reg + '_t-1'

            model_data_dict[reg_t3_col].append(task_df[reg][t3])
            model_data_dict[reg_t2_col].append(task_df[reg][t2])
            model_data_dict[reg_t1_col].append(task_df[reg][t1])
    
    return model_data_dict

def vif_scores(df, regressor_vars):
    
    cov_data_dict = {f'{reg}':[] for reg in regressor_vars}
    
    # check if data is categorical
    for reg in regressor_vars: 
        if pd.api.types.is_numeric_dtype(df[reg]):
            cov_data_dict[reg] = df[reg]
        else: 
            # factorize categorical data into numeric dummy variables 
            cov_data_dict[reg] = pd.factorize(df[reg])[0]
    
    vif_df = pd.DataFrame(cov_data_dict)


    vif_df = vif_df.astype(float)
    vif_df = vif_df.dropna()


    vif_data = pd.DataFrame() 
    vif_data["feature"] = vif_df.columns 

    # calculating VIF for each feature 
    vif_data["VIF"] = [variance_inflation_factor(vif_df.values, i) 
                              for i in range(len(vif_df.columns))] 
    return vif_data
