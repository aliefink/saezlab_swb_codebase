from psychopy import visual, core, event, gui
from datetime import datetime
from decimal import *
import os, random, time, numpy, csv

'''constants'''

#Subject Gui
subinfo={"Participant ID": ''}

if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID"]).OK:
    core.quit()

#Core elements
mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=True,color='white')
#mywin= visual.Window(monitor="testMonitor",units="deg",fullscr=False,size=[,],color='white')
scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
clock=core.Clock()
# scrnHz=mywin.getActualFrameRate(nIdentical=10, nMaxFrames=100, nWarmUpFrames=10, threshold=1)
myMouse=event.Mouse(visible=False,win=mywin)
stime=time.strftime("%H:%M:%S")

#Lists & inputs
ID=subinfo["Participant ID"]

#write/load paths
basepath=os.path.normpath(os.getcwd() + os.sep + os.pardir)
data_path=os.path.join(basepath, 'Data')+ os.sep
sequence_path=os.path.join(basepath, 'Sequence')+ os.sep
img_path=os.path.join(basepath,'Images')+ os.sep

#objects
os.chdir(img_path) #set image path?
pass_inst=visual.TextStim(win=mywin,pos=[0,-14],height=1,wrapWidth=35,text="(Press Spacebar)",color='black')
eot=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="Thank you!" ,colorSpace='rgb255',color=(0,0,0))


#BDI Stimuli
Prompts=['Sadness', 'Pessimism', 'Past Failure', 'Loss of Pleasure', 'Guilty Feelings', 'Punishment Feelings',' Self-Dislike',' Self-Criticalness',' Suicidal Thoughts or Wishes',' Crying',' Agitation',' Loss of Interest',' Indecisiveness',' Worthlessness',' Loss of Energy',' Changes In Sleeping Pattern','Irritability',' Changes in Appetite',' Concentration Difficulty',' Tiredness or Fatigue','Loss of Interest in Sex']
Choices1=['1 I do not feel sad.','1 I am not discouraged about my future.','1 I do not feel like a failure.','1 I get as much pleasure as I ever did from the things I enjoy.','1 I do not feel particularly guilty.','1 I do not feel I am being punished.','1 I feel the same about myself as ever.','1 I do not criticize or blame myself more than usual.','1 I do not have any thoughts of killing myself.','1 I do not cry any more than I used to.','1 I am no more restless or wound up than usual.', '1 I have not lost interest in other people or activities.','1 I make decisions about as well as ever.','1 I do not feel I am worthless.','1 I have as much energy as ever.','1 I have not experienced any change in my sleeping patterns ','1 I am no more irritable than usual.','1 I have not experienced any change in my appetite.','1 I can concentrate as well as ever.','1 I am no more tired or fatigued than usual.','1 I have not noticed any recent change in my interest in sex.'] 
Choices2=['2 I feel sad much of the time.','2 I feel more discouraged about my future than I used to be.','2 I have failed more than I should have.','2 I do not enjoy things as much as I used to.','2 I feel guilty over many things I have done or should have done.','2 I feel I may be punished.','2 I have lost confidence in myself.','2 I am more critical of myself than I used to be.','2 I have thoughts of killing myself, but I would not carry them out.','2 I cry more than I used to.','2 I feel more restless or wound up than usual.','2 I am less interested in other people or things than before.','2 I find it more difficult to make decisions than usual.','2 I do not consider myself as worthwhile and useful as I used to.','2 I have less energy than I used to have.','2 I sleep somewhat more or somewhat less than usual.','2 I am more irritable than usual.','2 My appetite is somewhat less or somewhat greater than usual.','2 I cannot concentrate as well as usual.','2 I get more tired or fatigued more easily than usual.','2 I am less interested in sex than I used to be.'] 
Choices3=['3 I am sad all the time.','3 I do not expect things to work out for me.','3 As I look back, I see a lot of failures.','3 I get very little pleasure from the things I used to enjoy. ','3 I feel quite guilty most of the time.','3 I expect to be punished.','3 I am disappointed in myself.','3 I criticize myself for all of my faults.','3 I would like to kill myself.','3 I cry over every little thing.','3 I am so restless or agitated that it is hard to stay still.','3 I have lost most of my interest in other people or things.','3 I have much greater difficulty in making decisions than I used to.','3 I feel more worthless as compared to other people.','3 I do not have enough energy to do very much.','3 I sleep a lot more or a lot less than usual.','3 I am much more irritable than usual.','3 My appetite is much less or much greater than usual.','3 It is hard to keep my mind on anything for very long.','3 I am too tired or fatigued to do a lot of the things I used to do.','3 I am much less interested in sex now.'] 
Choices4=['4 I am so sad or unhappy that I cannot stand it.','4 I feel my future is hopeless and will only get worse.','4 I feel I am a total failure as a person.','4 I cannot get any pleasure from the things I used to enjoy.','4 I feel guilty all of the time.','4 I feel I am being punished.','4 I dislike myself.','4 I blame myself for everything bad that happens.','4 I would kill myself if I had the chance.','4 I feel like crying, but I cannot.','4 I am so restless or agitated that I have to keep moving or doing something.','4 It is hard to get interested in anything.','4 I have trouble making any decisions.','4 I feel utterly worthless.','4 I do not have enough energy to do anything.','4 I sleep most of the day, or I wake up 1-2 hours early and cannot get back to sleep.','4 I am irritable all the time.','4 I have no appetite at all, or I crave food all the time.','4 I find I cannot concentrate on anything.','4 I am too tired or fatigued to do most of the things I used to do.','4 I have lost interest in sex completely.']


Questionaire=Instructions=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="Survey" ,colorSpace='rgb255',color='black')

BDI_Instruct=visual.ImageStim(mywin,size=[40,40],pos=[0,0],image='BDI.jpg')
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
    pass_inst.draw() #text="(Press Spacebar)"
    mywin.flip()
    event.waitKeys()
    
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
        event.clearEvents()
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
        elif keypress==['2']:
            Score=Score+1
            chosen=1
        elif keypress==['3']:
            Score=Score+2
            chosen=2
        elif keypress==['4']:
            Score=Score+3
            chosen=3
        elif keypress==['q']:
            chosen='quit'
            bget_data(bsave)
            core.quit()
        bsave.append([Prompt.text,chosen,str(Score)])
    bget_data(bsave)

def bget_data(Save):
    etime=time.strftime("%Y%m%d-%H%M%S")
    header=['Prompt','Chosen','BDI Score']
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
    os.chdir(img_path)
    #sub-timeline
    BDI_Task()
    eot.draw() #end of task
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])


#timeline
if __name__ == '__main__':
    #BDI_Task() #runs & saves but exits abruptly!
    get_trials()