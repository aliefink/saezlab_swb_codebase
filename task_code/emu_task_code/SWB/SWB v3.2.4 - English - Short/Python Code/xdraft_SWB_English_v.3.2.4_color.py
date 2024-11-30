#!/usr/bin/env python
# -*- coding: utf-8 -*-


from psychopy import visual, core, event, gui
from datetime import datetime
from decimal import *
import os, random, time, numpy, csv

'''constants'''

#Subject Gui
subinfo={"Participant ID": '',"Timing": '8',"Ratefreq": '3',"CB": '0'}
        
if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID"]).OK:
    core.quit()

#Core elements
mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='white')
scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
clock=core.Clock()
scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
myMouse=event.Mouse(visible=False,win=mywin)

stime=time.strftime("%H:%M:%S")

#Lists & inputs
ID=subinfo["Participant ID"]
timing=int(subinfo["Timing"])
ratefreq=int(subinfo["Ratefreq"])
colorblind=int(subinfo["CB"])
ratesave=[]


#write/load paths
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
data_path=os.path.join(basepath, 'Data')+ os.sep
sequence_path=os.path.join(basepath, 'Sequence')+ os.sep
img_path=os.path.join(basepath,'Images')+ os.sep

#colors
#Black (0,0,0)
#Yellow (255,255,0)
#Grey (224,224,224)
#Green (0,255,0)
#Red (255,0,0)
#Purple (128,0,128)
#Silver (192,192,192)

if colorblind==1:
    corrColor=(128,0,128)
    incorrColor=(192,192,192)
    hiddenColor=(224,224,224)
    baseColor=(0,0,0)
    selectColor=(255,255,0)
    revealColor=(0,0,255)
    
else:
    corrColor=(0,255,0)
    incorrColor=(255,0,0)
    hiddenColor=(224,224,224)
    baseColor=(0,0,0)
    selectColor=(255,255,0)
    revealColor=(0,0,255)



#objects
os.chdir(img_path)
practicetxt=visual.TextStim(mywin,height=1.5,font='Ariel',wrapWidth=35,text="You will now play a few practice rounds. These will not count towards your prize, use them to get familiar with the game. Once you've completed the practice and are confident you understand the game, will we move on to the game itself.",colorSpace='rgb255',color=(0,0,0))
tasktxt=visual.TextStim(mywin,height=2.5,font='Ariel',wrapWidth=45,text="You will now complete the real task",colorSpace='rgb255',color=(0,0,0))
eot=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="End of the Task" ,colorSpace='rgb255',color=(0,0,0))
eot=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="End of the Task" ,colorSpace='rgb255',color=(0,0,0))
pause=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="Pause" ,colorSpace='rgb255',color=(0,0,0))
repeat=visual.TextStim(mywin,height=2,font='Ariel',wrapWidth=35,text="This concludes the practice rounds. To repeat the practice press the 'r' key. Otherwise press 'Spacebar' to continue.",colorSpace='rgb255',color=(0,0,0))
grey_fix=visual.Rect(mywin,width=0.05,height=1,pos=[0,0],lineWidth=0.5,fillColorSpace='rgb255',fillColor=[110,110,110])
grey_fix_2=visual.Rect(mywin,width=1,height=0.05,pos=[0,0],lineWidth=0.5,fillColorSpace='rgb255',fillColor=[110,110,110])
pass_inst=visual.TextStim(win=mywin,pos=[0,-14],height=1,wrapWidth=35,text="(Press Spacebar or left click to Continue)",color='black')
message=visual.TextStim(win=mywin,pos=[0,0],wrapWidth=35,height=1.5,text="In this game you will be given the choice between two bets, a safe bet and a risky bet. The safe bet will always give you the amount displayed. The risky bet has two outcomes, one better than your safe bet and one worse. On each trial you can gain or lose money. At the end of the experiment we will show you how well you did.", color='black')
faster=visual.TextStim(win=mywin,pos=[0,0],height=3,text='Please respond faster',colorSpace='rgb255',color=(0,0,0))
rectangle=visual.Rect(win=mywin,width=7.5,height=7.5,pos=[-24.6,-15],fillColor='black')
LeftBox=visual.Rect(mywin,width=24,height=34,lineWidth=3.0,pos=(-9,0),lineColor='black')
RightBox=visual.Rect(mywin,width=24,height=34,lineWidth=3.0,pos=(15,0),lineColor='black')


#Left Side Stims
highbetleft=visual.TextStim(win=mywin,pos=[-9,10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
lowbetleft=visual.TextStim(win=mywin,pos=[-9,-10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
guaranteedright=visual.TextStim(win=mywin,pos=[16,0],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
guaranteedrightbox=visual.Rect(win=mywin,pos=[16,0],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
highbetboxleft=visual.Rect(win=mywin,pos=[-9,10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
lowbetboxleft=visual.Rect(win=mywin,pos=[-9,-10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
Won_left=visual.TextStim(win=mywin,pos=[-9,0],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))
Lose_left=visual.TextStim(win=mywin,pos=[-9,0],height=2.5,text=None,colorSpace='rgb255',color=(255,0,0))
safe_left=visual.TextStim(win=mywin,wrapWidth=15,pos=[-9,9],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))

#Right Side Stims
highbetright=visual.TextStim(win=mywin,pos=[16,10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
lowbetright=visual.TextStim(win=mywin,pos=[16,-10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
highbetboxright=visual.Rect(win=mywin,pos=[16,10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
lowbetboxright=visual.Rect(win=mywin,pos=[16,-10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
guaranteedleft=visual.TextStim(win=mywin,pos=[-9,0],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
guaranteedleftbox=visual.Rect(win=mywin,pos=[-9,0],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
Won_right=visual.TextStim(win=mywin,pos=[16,0],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))
Lose_right=visual.TextStim(win=mywin,pos=[16,0],height=2.5,text=None,colorSpace='rgb255',color=(255,0,0))
safe_right=visual.TextStim(win=mywin,wrapWidth=15,pos=[16,9],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))

#Reward stim
Rewardbox=visual.Rect(win=mywin,width=7.5,height=7.5,lineWidth=3.5,pos=[-24.6,13],fillColorSpace='rgb255',fillColor=(211,211,211))
Reward_value=visual.TextStim(win=mywin,pos=[-25.25,12],height=2.5,text=None,colorSpace='rgb255',color=(0,0,0))
Reward_title=visual.TextStim(win=mywin,pos=[-25.3,14.5],height=2,text='Total',colorSpace='rgb255',color=(0,0,0))



#Trail types
gamble_left=[LeftBox,RightBox,Rewardbox,highbetleft,lowbetleft,highbetboxleft,lowbetboxleft,guaranteedrightbox,guaranteedright,rectangle]
gamble_right=[LeftBox,RightBox,Rewardbox,highbetright,lowbetright,highbetboxright,lowbetboxright,guaranteedleftbox,guaranteedleft,rectangle,Rewardbox]
wingamble_left=[LeftBox,RightBox,Rewardbox,Won_left,highbetleft,lowbetleft,highbetboxleft,lowbetboxleft,guaranteedrightbox,guaranteedright,rectangle,Rewardbox]
losegamble_left=[LeftBox,RightBox,Rewardbox,Lose_left,highbetleft,lowbetleft,highbetboxleft,lowbetboxleft,guaranteedrightbox,guaranteedright,rectangle,Rewardbox]
wingamble_right=[LeftBox,RightBox,Rewardbox,Won_right,highbetright,lowbetright,highbetboxright,lowbetboxright,guaranteedleftbox,guaranteedleft,rectangle,Rewardbox]
losegamble_right=[LeftBox,RightBox,Rewardbox,Lose_right,highbetright,lowbetright,highbetboxright,lowbetboxright,guaranteedleftbox,guaranteedleft,rectangle,Rewardbox]
Reward=[Reward_value,Reward_title]

#Mood Stimuli
happy=visual.ImageStim(mywin, size= [5,5],pos=[16,-9],image='happy.jpg')
sad=visual.ImageStim(mywin, size= [5,5],pos=[-16,-9],image='unhappy.jpg')
happytxt= visual.TextStim(win=mywin,pos=[16,-5],height=1.5,text='Very Happy',colorSpace='rgb255',color=(0,0,0))
unhappytxt= visual.TextStim(win=mywin,pos=[-16,-5],height=1.5,text='Very Unhappy',colorSpace='rgb255',color=(0,0,0))
ratingprompt=visual.TextStim(win=mywin,pos=[0,9],wrapWidth=40,height=2.5,text='How happy are you at this moment?',color='black')
baseratingprompt=visual.TextStim(win=mywin,pos=[0,7],wrapWidth=40,height=2.5,text='Taken all together, how happy are you with your life these days?',color='black')
ratingitems=[happy,sad,ratingprompt,happytxt,unhappytxt]
baseratingitems=[happy,sad,baseratingprompt,happytxt,unhappytxt]

#BDI Stimuli
#Old code
#Prompts=['Sadness','Pessimism','Past Failure','Loss of Pleasure','Guilty Feelings','Punishment Feelings','Self-Dislike','Self-Criticalness','Suicidal Thoughts or Wishes','Crying','Agitation','Loss of Interest','Indecisiveness','Worthlessness','Loss of Energy','Irritability','Concentration Difficulty','Tiredness or Fatigue','Changes In Sleeping Pattern','Changes in Appetite']
#Choices1=['1 I do not feel sad.','1 I am not discouraged about my future.','1 I do not feel like a failure.','1 I get as much pleasure as I ever did from the things I enjoy.','1 I don not feel particularly guilty.','1 I do not feel I am being punished.','1 I feel the same about myself as ever.','1 I do not criticize or blame myself more than usual.','1 I do not have any thoughts of killing myself.','1 I do not cry any more than I used to.','1 I am no more restless or wound up than usual.','1 I have not lost interest in other people or activities.','1 I make decisions about as well as ever.','1 I do not feel I am worthless.','1 I have as much energy as ever.','1 I am no more irritable than usual.','1 I can concentrate as well as ever.','1 I am no more tired or fatigued than usual.','1 I have not noticed any recent change in my interest in sex.','1 I have not experienced any change in my sleeping patterns.','1 I have not experienced any change in my appetite.'] 
#Choices2=['2 1 feel sad much of the time.','2 I feel more discouraged about my future than I used to be.','2 I have failed more than I should have.','2 I do not enjoy things as much as I used to.','2 I feel guilty over many things I have done or should have done.','2 I feel I may be punished.','2 I have lost confidence in myself.','2 I am more critical of myself than I used to be.','2 I have thoughts of killing myself, but I would not carry them out.','2 I cry more than I used to.’,’2 I feel more restless or wound up than usual.','2 I am less interested in other people or things than before.','2 I find it more difficult to make decisions than usual.','2 I do not consider myself as worthwhile and useful as I used to.','2 I have less energy than I used to have.','2 I am more irritable than usual.','2 I can not concentrate as well as usual.','2 I get more tired or fatigued more easily than usual.','2 I am.less interested in sex than I used to be.','2 I sleep somewhat more or less than usual.','2 My appetite is somewhat less or greater than usual.']
#Choices3=['3 I am sad all the time.','3 I do not expect things to work out for me.','3 As I look back, I see a lot of failures.','3 I get very little pleasure from the things I used to enjoy. ','3 I feel quite guilty most of the time.','3 I expect to be punished.','3 I am disappointed in myself.','3 I criticize myself for all of my faults.','3 I would like to kill myself.','3 I cry over every little thing.','3 I am so restless or agitated that it is hard to stay still.','3 I have lost most of my interest in other people or things.','3 I have much greater difficulty in making decisions than I used to.','3 I feel more worthless as compared to other people.','3 I do not have enough energy to do very much.','3 I am much more irritable than usual.','3 It is hard to keep my mind on anything for very long.','3 I am too tired or fatigued to do a lot of the things 1 used to do.','3 I am much less interested in sex now.','3 I sleep a lot more or less than usual.','3 My appetite is much less or greater than usual.'] 
#Choices4=['4 1 am so sad or unhappy that I can not stand it.','4 I feel my future is hopeless and will only get worse.','4 I feel I am a total failure as a person.','4 I can not get any pleasure from the things I used to enjoy.','4 I feel guilty all of the time.','4 I feel I am being punished.','4 I dislike myself.','4 I blame myself for everything bad that happens.','4 I would kill myself if I had the chance.','4 I feel like crying, but I can not.','4 I am so restless or agitated that I have to keep moving or doing something.','4 It is hard to get interested in anything.','4 I have trouble making any decisions.','4 I feel utterly worthless.','4 I do not have enough energy to do anything.','4 I am irritable all the time.','4 I find I can not concentrate on anything.','4 I am too tired or fatigued to do most of the things I used to do.','4 I have lost interest in sex completely.','4 I sleep most of the day, or I wake up 1-2 hours early and can not get back to sleep.','4 I have no appetite at all, or I crave food all the time.']

Prompts=['Sadness', 'Pessimism', 'Past Failure', 'Loss of Pleasure', 'Guilty Feelings', 'Punishment Feelings',' Self-Dislike',' Self-Criticalness',' Suicidal Thoughts or Wishes',' Crying',' Agitation',' Loss of Interest',' Indecisiveness',' Worthlessness',' Loss of Energy',' Changes In Sleeping Pattern','Irritability',' Changes in Appetite',' Concentration Difficulty',' Tiredness or Fatigue','Loss of Interest in Sex']
Choices1=['1 I do not feel sad.','1 I am not discouraged about my future.','1 I do not feel like a failure.','1 I get as much pleasure as I ever did from the things I enjoy.','1 I do not feel particularly guilty.','1 I do not feel I am being punished.','1 I feel the same about myself as ever.','1 I do not criticize or blame myself more than usual.','1 I do not have any thoughts of killing myself.','1 I do not cry any more than I used to.','1 I am no more restless or wound up than usual.', '1 I have not lost interest in other people or activities.','1 I make decisions about as well as ever.','1 I do not feel I am worthless.','1 I have as much energy as ever.','1 I have not experienced any change in my sleeping patterns ','1 I am no more irritable than usual.','1 I have not experienced any change in my appetite.','1 I can concentrate as well as ever.','1 I am no more tired or fatigued than usual.','1 I have not noticed any recent change in my interest in sex.'] 
Choices2=['2 I feel sad much of the time.','2 I feel more discouraged about my future than I used to be.','2 I have failed more than I should have.','2 I do not enjoy things as much as I used to.','2 I feel guilty over many things I have done or should have done.','2 I feel I may be punished.','2 I have lost confidence in myself.','2 I am more critical of myself than I used to be.','2 I have thoughts of killing myself, but I would not carry them out.','2 I cry more than I used to.','2 I feel more restless or wound up than usual.','2 I am less interested in other people or things than before.','2 I find it more difficult to make decisions than usual.','2 I do not consider myself as worthwhile and useful as I used to.','2 I have less energy than I used to have.','2 I sleep somewhat more or somewhat less than usual.','2 I am more irritable than usual.','2 My appetite is somewhat less or somewhat greater than usual.','2 I cannot concentrate as well as usual.','2 I get more tired or fatigued more easily than usual.','2 I am less interested in sex than I used to be.'] 
Choices3=['3 I am sad all the time.','3 I do not expect things to work out for me.','3 As I look back, I see a lot of failures.','3 I get very little pleasure from the things I used to enjoy. ','3 I feel quite guilty most of the time.','3 I expect to be punished.','3 I am disappointed in myself.','3 I criticize myself for all of my faults.','3 I would like to kill myself.','3 I cry over every little thing.','3 I am so restless or agitated that it is hard to stay still.','3 I have lost most of my interest in other people or things.','3 I have much greater difficulty in making decisions than I used to.','3 I feel more worthless as compared to other people.','3 I do not have enough energy to do very much.','3 I sleep a lot more or a lot less than usual.','3 I am much more irritable than usual.','3 My appetite is much less or much greater than usual.','3 It is hard to keep my mind on anything for very long.','3 I am too tired or fatigued to do a lot of the things I used to do.','3 I am much less interested in sex now.'] 
Choices4=['4 I am so sad or unhappy that I cannot stand it.','4 I feel my future is hopeless and will only get worse.','4 I feel I am a total failure as a person.','4 I cannot get any pleasure from the things I used to enjoy.','4 I feel guilty all of the time.','4 I feel I am being punished.','4 I dislike myself.','4 I blame myself for everything bad that happens.','4 I would kill myself if I had the chance.','4 I feel like crying, but I cannot.','4 I am so restless or agitated that I have to keep moving or doing something.','4 It is hard to get interested in anything.','4 I have trouble making any decisions.','4 I feel utterly worthless.','4 I do not have enough energy to do anything.','4 I sleep most of the day, or I wake up 1-2 hours early and cannot get back to sleep.','4 I am irritable all the time.','4 I have no appetite at all, or I crave food all the time.','4 I find I cannot concentrate on anything.','4 I am too tired or fatigued to do most of the things I used to do.','4 I have lost interest in sex completely.']


Questionaire=Instructions=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="Survey" ,colorSpace='rgb255',color='black')

BDI_Instruct=visual.TextStim(mywin,height=1,font='Ariel',wrapWidth=35,text="This questionnaire contains 21 questions. Please read them all carefully, then choose the answer that best reflects how you've been feeling during the past two weeks, including today. Select your response using the number keys (1-4). If several answers seem appropriate, choose the higher number." ,colorSpace='rgb255',color=(0,0,0))
Prompt=visual.TextStim(mywin,height=2,pos=[0,12],font='Ariel',wrapWidth=120,text='' ,color='black')
Choice1=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-20,6],font='Ariel',wrapWidth=35,text='',color='black')
Choice2=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-20,0],font='Ariel',wrapWidth=35,text='',color='black')
Choice3=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-20,-6],font='Ariel',wrapWidth=35,text='',color='black')
Choice4=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-20,-12],font='Ariel',wrapWidth=35,text='',color='black')


#BDI Lists
Question=[Prompt,Choice1,Choice2,Choice3,Choice4]

def BDI_Task():
    #BDI Task
    Questionaire.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys()
    
    #Instructions.draw()
    #pass_inst.draw()
    #mywin.flip()
    #event.waitKeys()
    
    BDI_Instruct.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys()
    
    Score=0
    bsave=[]
    for i in range(0,len(Prompts)):
        Prompt.text=Prompts[i]
        Choice1.text=Choices1[i]
        Choice2.text=Choices2[i]
        Choice3.text=Choices3[i]
        Choice4.text=Choices4[i]
        
        for l in range(int(scrnHz*(600))):
            keypress=event.getKeys(keyList=['1','2','3','4','q'])
            
            if keypress:
                break
            else:
                drawing(Question)
                mywin.flip()
    
        if keypress==['1']:
            Score=Score+0
            chosen=0
            bsave.append([Prompt.text,Choice1.text,Choice2.text,Choice3.text,Choice4.text,chosen,str(Score)])
        elif keypress==['2']:
            Score=Score+1
            chosen=1
            bsave.append([Prompt.text,Choice1.text,Choice2.text,Choice3.text,Choice4.text,chosen,str(Score)])
        elif keypress==['3']:
            Score=Score+2
            chosen=2
            bsave.append([Prompt.text,Choice1.text,Choice2.text,Choice3.text,Choice4.text,chosen,str(Score)])
        elif keypress==['4']:
            Score=Score+3
            chosen=3
            bsave.append([Prompt.text,Choice1.text,Choice2.text,Choice3.text,Choice4.text,chosen,str(Score)])
        elif keypress==['q']:
            chosen='quit'
            bsave.append([Prompt.text,Choice1.text,Choice2.text,Choice3.text,Choice4.text,chosen,str(Score)])
            bget_data(bsave)
            core.quit()
    
    bget_data(bsave)
    

def basemood(count,trialcount,ratesave,type):
    ratingScale = visual.RatingScale(mywin,scale=None,size=1.3,low=0,high=10,tickMarks=[0,1,2,3,4,5,6,7,8,9,10],acceptPreText='Choose',tickHeight=2,markerStart=5,markerColor='Red',noMouse=True,acceptKeys=['space','down'])
    ratingOnset=clock.getTime()
    while ratingScale.noResponse:
        ratingScale.draw()
        drawing(baseratingitems)
        mywin.flip()
    rating = ratingScale.getRating()
    ratingtime = clock.getTime()-ratingOnset
    ratesave.append([count,trialcount,type,rating,ratingOnset,ratingtime])
    
def mood(count,trialcount,ratesave,type):
    ratingScale = visual.RatingScale(mywin,scale=None,size=1.3,low=0,high=10,tickMarks=[0,1,2,3,4,5,6,7,8,9,10],acceptPreText='Choose',tickHeight=2,markerStart=5,markerColor='Red',noMouse=True,acceptKeys=['space','down'])
    ratingOnset=clock.getTime()
    while ratingScale.noResponse:
        ratingScale.draw()
        drawing(ratingitems)
        mywin.flip()
    rating = ratingScale.getRating()
    ratingtime = clock.getTime()-ratingOnset
    ratesave.append([count,trialcount,type,rating,ratingOnset,ratingtime])
        
    
def pracmood(count,trialcount,ratesave,type):
    ratingScale = visual.RatingScale(mywin,scale=None,size=1.3,low=0,high=10,tickMarks=[0,1,2,3,4,5,6,7,8,9,10],acceptPreText='Choose',tickHeight=2,markerStart=5,markerColor='Red',noMouse=True,acceptKeys=['space','down'])
    ratingOnset=clock.getTime()
    while ratingScale.noResponse:
        ratingScale.draw()
        drawing(ratingitems)
        mywin.flip()
    rating = ratingScale.getRating()
    ratingtime = clock.getTime()-ratingOnset
    

def instructions():
    message.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])
    

def task(trials,save):
    TotalProfit=10
    Profit=0
    count=0
    trialcount=0
    random.shuffle(trials)
    tasktxt.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])
    type='task'
    for t in trials:
        trialcount=trialcount+1
        TrialOnset=clock.getTime()
        lowbetboxright.lineColor=(0,0,0)
        highbetboxright.lineColor=(0,0,0)
        lowbetboxleft.lineColor=(0,0,0)
        highbetboxleft.lineColor=(0,0,0)
        guaranteedleftbox.lineColor=(0,0,0)
        guaranteedrightbox.lineColor=(0,0,0)
        lowbetright.color=(0,0,0)
        highbetright.color=(0,0,0)
        lowbetleft.color=(0,0,0)
        highbetleft.color=(0,0,0)
        guaranteedleft.color=(0,0,0)
        guaranteedright.color=(0,0,0)
        Reward_value.text='$' + str(TotalProfit)
        
        if trialcount==1:
            basemood(count,trialcount,ratesave,type)
        
        if t[6]=='left':
            guaranteedright.text= '$' + str(t[2])
            if t[7]=='top':
                highbetleft.text= '$' + str(t[4])
                lowbetleft.text= '$' + str(t[3])
            elif t[7]=='bottom':
                highbetleft.text= '$' + str(t[3])
                lowbetleft.text= '$' + str(t[4])
                
            event.clearEvents()
            ChoiceOnset=clock.getTime()
            for l in range(int(scrnHz*(timing))):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                
                if keypress:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[1,0,0]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[0,0,1]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                    
                else:
                    drawing(gamble_left)
                    Reward_value.text='$' + str(TotalProfit)
                    drawing(Reward)
                    mywin.flip()
                    
            if not keypress and buttons==[0,0,0]:
                faster.draw()
                RT=0
                DecisionOnset=clock.getTime()
                FeedbackOnset=0
                Profit=0
                Outcome='NaN'
                Choice='NaN'
                ChoicePos='NaN'
                mywin.flip()
                core.wait(float(t[8]))
                
            else:
                if buttons==[1,0,0]:
                    keypress=['left']
                elif buttons==[0,0,1]:
                    keypress=['right']
                    
                if keypress==['left']:
                    highbetboxleft.lineColor=selectColor
                    lowbetboxleft.lineColor=selectColor
                    guaranteedrightbox.lineColor=hiddenColor
                    guaranteedright.color=hiddenColor
                    choicePos='left'
                    gambleChoice='gamble'
                    drawing(gamble_left)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[5]=='top':
                            highbetboxleft.lineColor=corrColor
                            lowbetboxleft.lineColor=hiddenColor
                            lowbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=corrColor
                            highbetboxleft.lineColor=hiddenColor
                            highbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                    else:
                        if t[5]=='top':
                            highbetboxleft.lineColor=incorrColor
                            lowbetboxleft.lineColor=hiddenColor
                            lowbetboxleft.lineColor=hiddenColor
                            if t[1]=='mix':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=incorrColor
                            highbetboxleft.lineColor=hiddenColor
                            highbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                            
                elif keypress==['right']:
                    highbetboxleft.lineColor=hiddenColor
                    highbetleft.color=hiddenColor
                    lowbetboxleft.lineColor=hiddenColor
                    lowbetleft.color=hiddenColor
                    guaranteedrightbox.lineColor=selectColor
                    guaranteedright.color=baseColor
                    choicePos='right'
                    gambleChoice='safe'
                    drawing(gamble_left)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[1]=='mix':
                            safe_right.color=baseColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_right.color=corrColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_right.color=incorrColor
                            safe_right.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        safe_right.draw()
                        drawing(gamble_left)
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text= '$' + str(TotalProfit)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                            
                            
                        if t[5]=='top':
                            highbetboxleft.lineColor=revealColor
                            highbetleft.color=baseColor
                            lowbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=incorrColor
                            
                            if t[1]=='mix':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_left)
                            drawing(Reward)
                            mywin.flip()
                            Outcome='bad'
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=revealColor
                            lowbetleft.color=baseColor
                            highbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=incorrColor
                            if t[1]=='mix':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            drawing(losegamble_left)
                            drawing(Reward)
                            Profit=float(t[2])
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                    else:
                        if t[1]=='mix':
                            safe_right.color=baseColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_right.color=corrColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_right.color=incorrColor
                            safe_right.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        drawing(gamble_left)
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        drawing(Reward)
                        safe_right.draw()
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxleft.lineColor=revealColor
                            highbetleft.color=baseColor
                            lowbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=corrColor
                            
                            if t[1]=='mix':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=revealColor
                            lowbetleft.color=baseColor
                            highbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=corrColor
                            if t[1]=='mix':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)

                elif keypress==['q']:
                    get_data(save)
                    get_rate(ratesave)
                    core.quit()
                
                elif keypress==['p']:
                    pause.draw()
                    mywin.flip()
                    profit=0
                    choicePos='skip'
                    gambleChoice='skip'
                    event.waitKeys(keyList='p')
                    trials.append(t)
                    
                    

        elif t[6]=='right':
            ChoiceOnset=clock.getTime()
            guaranteedleft.text= '$' + str(t[2])
            if t[7]=='top':
                highbetright.text= '$' + str(t[4])
                lowbetright.text= '$' + str(t[3])
            elif t[7]=='bottom':
                highbetright.text= '$' + str(t[3])
                lowbetright.text= '$' + str(t[4])
            
            for l in range(int(scrnHz*5)):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                if keypress:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[1,0,0]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[0,0,1]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                    
                else:
                    drawing(gamble_right)
                    drawing(Reward)
                    mywin.flip()
                    
            if not keypress and buttons==[0,0,0]:
                faster.draw()
                RT=0
                DecisionOnset=clock.getTime()
                FeedbackOnset=0
                Profit=0
                Outcome='Nan'
                choicePos='NaN'
                gambleChoice='NaN'
                mywin.flip()
                core.wait(float(t[8]))
                
            else:
                if buttons==[1,0,0]:
                    keypress=['left']
                elif buttons==[0,0,1]:
                    keypress=['right']
                    
                if keypress==['right']:
                    highbetboxright.lineColor=selectColor
                    lowbetboxright.lineColor=selectColor
                    guaranteedleftbox.lineColor=hiddenColor
                    guaranteedleft.color=hiddenColor
                    choicePos='right'
                    gambleChoice='gamble'
                    drawing(gamble_right)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[5]=='top':
                            highbetboxright.lineColor=corrColor
                            lowbetboxright.lineColor=hiddenColor
                            lowbetright.color=hiddenColor
                            if t[1]=='mix':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=corrColor
                            highbetboxright.lineColor=hiddenColor
                            highbetright.color=hiddenColor
                            if t[1]=='mix':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                    else:
                        if t[5]=='top':
                            highbetboxright.lineColor==incorrColor
                            lowbetboxright.lineColor=hiddenColor
                            lowbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=incorrColor
                            highbetboxright.lineColor=hiddenColor
                            highbetright.color=hiddenColor
                            if t[1]=='mix':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        
                elif keypress==['left']:
                    highbetboxright.lineColor=hiddenColor
                    highbetright.color=hiddenColor
                    lowbetboxright.lineColor=hiddenColor
                    lowbetright.color=hiddenColor
                    guaranteedleftbox.lineColor=selectColor
                    guaranteedleft.color=baseColor
                    choicePos='left'
                    gambleChoice='safe'
                    drawing(gamble_right)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[1]=='mix':
                            safe_left.color=baseColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=corrColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=incorrColor
                            safe_left.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        drawing(gamble_right)
                        safe_left.draw()
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxright.lineColor=revealColor
                            highbetright.color=baseColor
                            lowbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=incorrColor
                            if t[1]=='mix':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(128,0,128)
                            lowbetright.color=(0,0,0)
                            highbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(255,0,0)
                            if t[1]=='mix':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            

                    else:
                        if t[1]=='mix':
                            safe_left.color=baseColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=corrColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=incorrColor
                            safe_left.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        drawing(gamble_right)
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        drawing(Reward)
                        safe_left.draw()
                        mywin.flip()
                        core.wait(2.0)
                    
                        if t[5]=='top':
                            highbetboxright.lineColor=revealColor
                            highbetright.color=baseColor
                            lowbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=corrColor
                            if t[1]=='mix':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=revealColor
                            lowbetright.color=baseColor
                            highbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=corrColor
                            if t[1]=='mix':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        
                elif keypress==['q']:
                    get_data(save)
                    get_rate(ratesave)
                    core.quit()
               
                elif keypress==['p']:
                    pause.draw()
                    mywin.flip()
                    profit=0
                    choicePos='skip'
                    gambleChoice='skip'
                    event.waitKeys(keyList='p')
                    trials.append(t)
                    
        save.append([trialcount,t[0],t[1],TrialOnset,ChoiceOnset,DecisionOnset,FeedbackOnset,RT,t[2],t[3],t[4],t[7],t[6],choicePos,gambleChoice,Outcome,Profit,TotalProfit])
        

        grey_fix.draw()
        grey_fix_2.draw()
        mywin.flip()
        keypress=[]
        core.wait(float(t[8]))
        
        if int(trialcount)%ratefreq==0:
            mood(count,trialcount,ratesave,type)

           
        
    get_rate(ratesave)
    get_data(save)
    congrats=visual.TextStim(win=mywin,pos=[0,0],wrapWidth=35,height=3,text='Thank you for playing! Your final score was: $' + str(TotalProfit), color='black')
    congrats.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])
   
def practice(trials,save):
    TotalProfit=10
    Profit=0
    count=0
    trialcount=0
    type='practice'
    practicetxt.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])
    for t in trials:
        trialcount=trialcount+1
        TrialOnset=clock.getTime()
        lowbetboxright.lineColor=(0,0,0)
        highbetboxright.lineColor=(0,0,0)
        lowbetboxleft.lineColor=(0,0,0)
        highbetboxleft.lineColor=(0,0,0)
        guaranteedleftbox.lineColor=(0,0,0)
        guaranteedrightbox.lineColor=(0,0,0)
        lowbetright.color=(0,0,0)
        highbetright.color=(0,0,0)
        lowbetleft.color=(0,0,0)
        highbetleft.color=(0,0,0)
        guaranteedleft.color=(0,0,0)
        guaranteedright.color=(0,0,0)
        Reward_value.text='$' + str(TotalProfit)
        
        if t[6]=='left':
            guaranteedright.text= '$' + str(t[2])
            if t[7]=='top':
                highbetleft.text= '$' + str(t[4])
                lowbetleft.text= '$' + str(t[3])
            elif t[7]=='bottom':
                highbetleft.text= '$' + str(t[3])
                lowbetleft.text= '$' + str(t[4])
                
            event.clearEvents()
            ChoiceOnset=clock.getTime()
            for l in range(int(scrnHz*(timing))):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                
                if keypress:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[1,0,0]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[0,0,1]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                    
                else:
                    drawing(gamble_left)
                    drawing(Reward)
                    drawing(Reward)
                    mywin.flip()
                    
            if not keypress and buttons==[0,0,0]:
                faster.draw()
                RT=0
                DecisionOnset=clock.getTime()
                FeedbackOnset=0
                Profit=0
                Outcome='NaN'
                Choice='NaN'
                ChoicePos='NaN'
                mywin.flip()
                core.wait(float(t[8]))
                
            else:
                if buttons==[1,0,0]:
                    keypress=['left']
                elif buttons==[0,0,1]:
                    keypress=['right']
                    
                if keypress==['left']:
                    highbetboxleft.lineColor=selectColor
                    lowbetboxleft.lineColor=selectColor
                    guaranteedrightbox.lineColor=hiddenColor
                    guaranteedright.color=hiddenColor
                    choicePos='left'
                    gambleChoice='gamble'
                    drawing(gamble_left)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[5]=='top':
                            highbetboxleft.lineColor=corrColor
                            lowbetboxleft.lineColor=hiddenColor
                            lowbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=corrColor
                            highbetboxleft.lineColor=hiddenColor
                            highbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_left.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                    else:
                        if t[5]=='top':
                            highbetboxleft.lineColor=incorrColor
                            lowbetboxleft.lineColor=hiddenColor
                            lowbetboxleft.lineColor=hiddenColor
                            if t[1]=='mix':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=incorrColor
                            highbetboxleft.lineColor=hiddenColor
                            highbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_left.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                            
                elif keypress==['right']:
                    highbetboxleft.lineColor=hiddenColor
                    highbetleft.color=hiddenColor
                    lowbetboxleft.lineColor=hiddenColor
                    lowbetleft.color=hiddenColor
                    guaranteedrightbox.lineColor=selectColor
                    choicePos='right'
                    gambleChoice='safe'
                    drawing(gamble_left)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[1]=='mix':
                            safe_right.color=baseColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_right.color=incorrColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_right.color=incorrColor
                            safe_right.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_right.draw()
                        drawing(gamble_left)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxleft.lineColor=revealColor
                            highbetleft.color=baseColor
                            lowbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=incorrColor
                            
                            if t[1]=='mix':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_left)
                            drawing(Reward)
                            mywin.flip()
                            Outcome='bad'
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=revealColor
                            lowbetleft.color=baseColor
                            highbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=incorrColor
                            if t[1]=='mix':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='gain':
                                Lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            elif t[1]=='loss':
                                Lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                Lose_left.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                    else:
                        if t[1]=='mix':
                            safe_right.color=baseColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_right.color=corrColor
                            safe_right.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_right.color=incorrColor
                            safe_right.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_right.draw()
                        drawing(gamble_left)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxleft.lineColor=revealColor
                            highbetleft.color=baseColor
                            lowbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=corrColor
                            
                            if t[1]=='mix':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=revealColor
                            lowbetleft.color=baseColor
                            highbetboxleft.lineColor=hiddenColor
                            guaranteedrightbox.lineColor=corrColor
                            if t[1]=='mix':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='gain':
                                Won_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            elif t[1]=='loss':
                                Won_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                Won_left.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)

                elif keypress==['q']:
                    core.quit()
                
                elif keypress==['p']:
                    pause.draw()
                    profit=0
                    choicePos='skip'
                    gambleChoice='skip'
                    mywin.flip()
                    event.waitKeys(keyList='p')
                    trials.append(t)
                    
                    

        elif t[6]=='right':
            ChoiceOnset=clock.getTime()
            guaranteedleft.text= '$' + str(t[2])
            if t[7]=='top':
                highbetright.text= '$' + str(t[4])
                lowbetright.text= '$' + str(t[3])
            elif t[7]=='bottom':
                highbetright.text= '$' + str(t[3])
                lowbetright.text= '$' + str(t[4])
            
            for l in range(int(scrnHz*5)):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                if keypress:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[1,0,0]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                elif buttons==[0,0,1]:
                    DecisionOnset=clock.getTime()
                    RT=DecisionOnset-ChoiceOnset
                    break
                    
                else:
                    drawing(gamble_right)
                    drawing(Reward)
                    mywin.flip()
                    
            if not keypress and buttons==[0,0,0]:
                faster.draw()
                RT=0
                DecisionOnset=clock.getTime()
                FeedbackOnset=0
                Profit=0
                Outcome='Nan'
                choicePos='NaN'
                gambleChoice='NaN'
                mywin.flip()
                core.wait(float(t[8]))
                
            else:
                if buttons==[1,0,0]:
                    keypress=['left']
                elif buttons==[0,0,1]:
                    keypress=['right']
                    
                if keypress==['right']:
                    highbetboxright.lineColor=selectColor
                    lowbetboxright.lineColor=selectColor
                    guaranteedleftbox.lineColor=hiddenColor
                    guaranteedleft.color=hiddenColor
                    choicePos='right'
                    gambleChoice='gamble'
                    drawing(gamble_right)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[5]=='top':
                            highbetboxright.lineColor=corrColor
                            lowbetboxright.lineColor=hiddenColor
                            lowbetright.color=hiddenColor
                            if t[1]=='mix':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=corrColor
                            highbetboxright.lineColor=hiddenColor
                            highbetright.color=hiddenColor
                            if t[1]=='mix':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You won $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You lost $ ' + str(abs(Decimal(t[4]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                    else:
                        if t[5]=='top':
                            highbetboxright.lineColor==incorrColor
                            lowbetboxright.lineColor=hiddenColor
                            lowbetleft.color=hiddenColor
                            if t[1]=='mix':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=incorrColor
                            highbetboxright.lineColor=hiddenColor
                            highbetright.color=hiddenColor
                            if t[1]=='mix':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You won $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You lost $ ' + str(abs(Decimal(t[3]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        
                elif keypress==['left']:
                    highbetboxright.lineColor=hiddenColor
                    highbetright.color=hiddenColor
                    lowbetboxright.lineColor=hiddenColor
                    lowbetright.color=hiddenColor
                    guaranteedleftbox.lineColor=selectColor
                    choicePos='left'
                    gambleChoice='safe'
                    drawing(gamble_right)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[1]=='mix':
                            safe_left.color=baseColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=incorrColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=incorrColor
                            safe_left.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_left.draw()
                        drawing(gamble_right)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxright.lineColor=revealColor
                            highbetright.color=baseColor
                            lowbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=incorrColor
                            if t[1]=='mix':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=revealColor
                            lowbetright.color=baseColor
                            highbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=incorrColor
                            if t[1]=='mix':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='gain':
                                Lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            elif t[1]=='loss':
                                Lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                Lose_right.color=incorrColor
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            

                    else:
                        if t[1]=='mix':
                            safe_left.color=baseColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=corrColor
                            safe_left.text='You won $ ' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=incorrColor
                            safe_left.text='You lost $ ' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_left.draw()
                        drawing(gamble_right)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxright.lineColor=revealColor
                            highbetright.color=baseColor
                            lowbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=corrColor
                            if t[1]=='mix':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=revealColor
                            lowbetright.color=baseColor
                            highbetboxright.lineColor=hiddenColor
                            guaranteedleftbox.lineColor=corrColor
                            if t[1]=='mix':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='gain':
                                Won_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            elif t[1]=='loss':
                                Won_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                Won_right.color=corrColor
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        
                elif keypress==['q']:
                    core.quit()
               
                elif keypress==['p']:
                    pause.draw()
                    mywin.flip()
                    profit=0
                    choicePos='skip'
                    gambleChoice='skip'
                    event.waitKeys(keyList='p')
                    trials.append(t)
                      
           
        grey_fix.draw()
        grey_fix_2.draw()
        mywin.flip()
        keypress=[]
        core.wait(float(t[8]))
    
        if int(trialcount)%ratefreq==0:
            pracmood(count,trialcount,ratesave,type)
    
def get_data(Save):
    end_time=time.strftime("%Y%m%d-%H%M%S")
    etime=time.strftime("%H:%M:%S")
    header=['Round','Trial Num','TrialType','TrialOnset','ChoiceOnset','DecisionOnset','Feedback Onset','RT','Safe Bet','Low Bet','High Bet','High Bet Pos','Gamble Pos','Choice Pos','Gamble Choice','Outcome','Profit','TotalProfit']
    savFrac= open(data_path + subinfo['Participant ID'] + '_' + end_time + '.txt', 'w')
    for i in header:
        savFrac.write(i)
        savFrac.write('\t')
    savFrac.write('\n')
    for l in Save:
        for x in range(len(l)):
            savFrac.write(str(l[x]))
            savFrac.write('\t')
        savFrac.write('\n')
    savFrac.write('\n')
    savFrac.write("Start Time: ")
    savFrac.write(str(stime))
    savFrac.write("\n")
    savFrac.write("End Time: ")
    savFrac.write(str(etime))
    
def get_rate(Save):
    end_time=time.strftime("%Y%m%d-%H%M%S")
    etime=time.strftime("%H:%M:%S")
    header=['Round','Trial','Type','Rating','RatingOnset','RT']
    savFrac= open(data_path + subinfo['Participant ID'] + '_Rate_'  + end_time + '.txt', 'w')
    for i in header:
        savFrac.write(i)
        savFrac.write('\t')
    savFrac.write('\n')
    for l in Save:
        for x in range(len(l)):
            savFrac.write(str(l[x]))
            savFrac.write('\t')
        savFrac.write('\n')
    savFrac.write('\n')
    savFrac.write("Start Time: ")
    savFrac.write(str(stime))
    savFrac.write("\n")
    savFrac.write("End Time: ")
    savFrac.write(str(etime))
    
def bget_data(Save):
    etime=time.strftime("%Y%m%d-%H%M%S")
    header=['Prompt','Choice 0','Choice 1','Choice 2','Choice 3','Chosen','BDI Score']
    savFrac= open(data_path + subinfo['Participant ID'] + '_BDI_' + etime + '.txt', 'w')
    for i in header:
        savFrac.write(i)
        savFrac.write('\t')
    savFrac.write('\n')
    for l in Save:
        for x in range(len(l)):
            savFrac.write(str(l[x]))
            savFrac.write('\t')
        savFrac.write('\n')

def drawing(l):
    for item in l:
        item.draw()
        
def get_trials():
    os.chdir(sequence_path)
    prac=1
    save=[]
    gamble_trials=[]
    practice_trials=[]
    gamble_csv='gamble_choices.csv'
    practice_csv='practice_choices.csv'

    with open(gamble_csv, newline='') as csv_file:
        next(csv_file)
        for row in csv.reader(csv_file, delimiter=','):
            trial=row
            gamble_trials.append(trial)
    with open(practice_csv, newline='') as csv_file:
        next(csv_file)
        for row in csv.reader(csv_file, delimiter=','):
            ptrial=row
            practice_trials.append(ptrial)
    os.chdir(img_path)
    
    BDI_Task()
    while prac==1:
        practice(practice_trials,save)
        event.clearEvents()
        for l in range(int(scrnHz*60)):
            keypress=event.getKeys(keyList=['r','space','q'])
            if keypress:
                break
            else:
                repeat.draw()
                mywin.flip()
        if not keypress:
            pass
        else:
            if keypress==['r']:
                prac=1
            elif keypress==['space']:
                prac=0
            elif keypress==['q']:
                core.quit()
    task(gamble_trials,save)
    get_data(save)
    eot.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])



if __name__ == '__main__':
    get_trials()
    