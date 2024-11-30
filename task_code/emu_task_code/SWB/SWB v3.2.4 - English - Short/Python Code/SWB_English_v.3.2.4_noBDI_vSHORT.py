#!/usr/bin/env python
# -*- coding: utf-8 -*-

from psychopy import visual, core, event, gui
from datetime import datetime
from decimal import *
import os, random, time, numpy, csv

'''constants'''

#Subject Gui
subinfo={"Participant ID": '',"Instruction":'yes',"Timing": '8',"Ratefreq": '3'}
        
if not gui.DlgFromDict(dictionary=subinfo, order=["Participant ID","Instruction","Timing","Ratefreq"]).OK:
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
instruction=subinfo["Instruction"]
ID=subinfo["Participant ID"]
timing=int(subinfo["Timing"])
ratefreq=int(subinfo["Ratefreq"])
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

#objects
os.chdir(img_path)
practicetxt=visual.TextStim(mywin,height=1.5,font='Ariel',wrapWidth=35,text="You will now play a few practice rounds. These will not count towards your prize, use them to get familiar with the game. Once you've completed the practice and are confident you understand the game, will we move on to the game itself.",colorSpace='rgb255',color=(0,0,0))
tasktxt=visual.TextStim(mywin,height=2.5,font='Ariel',wrapWidth=45,text="You will now complete the real task",colorSpace='rgb255',color=(0,0,0))
eot=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="End of the Task" ,colorSpace='rgb255',color=(0,0,0))
pause=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="Pause" ,colorSpace='rgb255',color=(0,0,0))
repeat=visual.TextStim(mywin,height=2,font='Ariel',wrapWidth=35,text="This concludes the practice rounds. To repeat the practice press the 'r' key. Otherwise press 'Spacebar' to continue.",colorSpace='rgb255',color=(0,0,0))
grey_fix=visual.Rect(mywin,width=0.05,height=1,pos=[0,0],lineWidth=0.5,fillColorSpace='rgb255',fillColor=[110,110,110])
grey_fix_2=visual.Rect(mywin,width=1,height=0.05,pos=[0,0],lineWidth=0.5,fillColorSpace='rgb255',fillColor=[110,110,110])
pass_inst=visual.TextStim(win=mywin,pos=[0,-14],height=1,wrapWidth=35,text="(Press Spacebar)",color='black')
message=visual.TextStim(win=mywin,pos=[0,0],wrapWidth=35,height=1.5,text="In this game you will be given the choice between two bets, a safe bet and a risky bet. The safe bet will always give you the amount displayed. The risky bet has two outcomes, one better than your safe bet and one worse. On each trial you can gain or lose money. At the end of the experiment we will show you how well you did.", color='black')
faster=visual.TextStim(win=mywin,pos=[0,0],height=3,text='Please respond faster',colorSpace='rgb255',color=(0,0,0))
halfTime=visual.TextStim(win=mywin,height=2.5,font='Ariel',wrapWidth=45,text="You are half way through! You can take a break now if you wish so. When you are ready to resume, press Spacebar.",colorSpace='rgb255',color=(0,0,0))
rectangle=visual.Rect(win=mywin,width=7.5,height=7.5,pos=[-24.6,-15],fillColor='black')
LeftBox=visual.Rect(mywin,width=24,height=34,lineWidth=3.0,pos=(-9,0),lineColor='black')
RightBox=visual.Rect(mywin,width=24,height=34,lineWidth=3.0,pos=(15,0),lineColor='black')


#Instructions
SWB_S1=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S1.jpg')
SWB_S2=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S2.jpg')
SWB_S3=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S3.jpg')
SWB_S4=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S4.jpg')
SWB_S5=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S5.jpg')
SWB_S6=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S6.jpg')
SWB_S7=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S7.jpg')
SWB_S8=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S8.jpg')
SWB_S9=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S9.jpg')
SWB_S10=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S10.jpg')
SWB_S11=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S11.jpg')
SWB_S12=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S12.jpg')
SWB_S13=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S13.jpg')
SWB_S14=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S14.jpg')
SWB_S15=visual.ImageStim(mywin,size=[50,30],pos=[0,0],image='SWB_S15.jpg')
inst_list=[SWB_S1,SWB_S2,SWB_S3,SWB_S4,SWB_S5,SWB_S6,SWB_S7,SWB_S8,SWB_S9,SWB_S10,SWB_S11,SWB_S12,SWB_S14,SWB_S15]

#Left Side Stims
highbetleft=visual.TextStim(win=mywin,pos=[-9,10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
lowbetleft=visual.TextStim(win=mywin,pos=[-9,-10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
guaranteedright=visual.TextStim(win=mywin,pos=[16,0],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
guaranteedrightbox=visual.Rect(win=mywin,pos=[16,0],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
highbetboxleft=visual.Rect(win=mywin,pos=[-9,10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
lowbetboxleft=visual.Rect(win=mywin,pos=[-9,-10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
win_left=visual.TextStim(win=mywin,pos=[-9,0],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))
lose_left=visual.TextStim(win=mywin,pos=[-9,0],height=2.5,text=None,colorSpace='rgb255',color=(255,0,0))
safe_left=visual.TextStim(win=mywin,wrapWidth=15,pos=[-9,9],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))

#Right Side Stims
highbetright=visual.TextStim(win=mywin,pos=[16,10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
lowbetright=visual.TextStim(win=mywin,pos=[16,-10],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
highbetboxright=visual.Rect(win=mywin,pos=[16,10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
lowbetboxright=visual.Rect(win=mywin,pos=[16,-10],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
guaranteedleft=visual.TextStim(win=mywin,pos=[-9,0],height=4,text=None,colorSpace='rgb255',color=(0,0,0))
guaranteedleftbox=visual.Rect(win=mywin,pos=[-9,0],width=13,height=9,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0))
win_right=visual.TextStim(win=mywin,pos=[16,0],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))
lose_right=visual.TextStim(win=mywin,pos=[16,0],height=2.5,text=None,colorSpace='rgb255',color=(255,0,0))
safe_right=visual.TextStim(win=mywin,wrapWidth=15,pos=[16,9],height=2.5,text=None,colorSpace='rgb255',color=(0,255,0))

#Reward stim
Rewardbox=visual.Rect(win=mywin,width=7.5,height=7.5,lineWidth=3.5,pos=[-24.6,13],fillColorSpace='rgb255',fillColor=(211,211,211))
Reward_value=visual.TextStim(win=mywin,pos=[-25.25,12],height=1.5,text=None,colorSpace='rgb255',color=(0,0,0))
Reward_title=visual.TextStim(win=mywin,pos=[-25.3,14.5],height=2,text='Total',colorSpace='rgb255',color=(0,0,0))


#Trail types
gamble_left=[LeftBox,RightBox,Rewardbox,highbetleft,lowbetleft,highbetboxleft,lowbetboxleft,guaranteedrightbox,guaranteedright,rectangle]
gamble_right=[LeftBox,RightBox,Rewardbox,highbetright,lowbetright,highbetboxright,lowbetboxright,guaranteedleftbox,guaranteedleft,rectangle]
wingamble_left=[LeftBox,RightBox,Rewardbox,win_left,highbetleft,lowbetleft,highbetboxleft,lowbetboxleft,guaranteedrightbox,guaranteedright,rectangle]
losegamble_left=[LeftBox,RightBox,Rewardbox,lose_left,highbetleft,lowbetleft,highbetboxleft,lowbetboxleft,guaranteedrightbox,guaranteedright,rectangle]
wingamble_right=[LeftBox,RightBox,Rewardbox,win_right,highbetright,lowbetright,highbetboxright,lowbetboxright,guaranteedleftbox,guaranteedleft,rectangle]
losegamble_right=[LeftBox,RightBox,Rewardbox,lose_right,highbetright,lowbetright,highbetboxright,lowbetboxright,guaranteedleftbox,guaranteedleft,rectangle]
Reward=[Reward_value,Reward_title]

#Mood Stimuli
happy=visual.ImageStim(mywin, size= [5,5],pos=[17,-9],image='happy.jpg')
sad=visual.ImageStim(mywin, size= [5,5],pos=[-18,-9],image='unhappy.jpg')
happytxt= visual.TextStim(win=mywin,pos=[17,-5],height=1.5,text='Very Happy',colorSpace='rgb255',color=(0,0,0))
unhappytxt= visual.TextStim(win=mywin,pos=[-18,-5],height=1.5,text='Very Unhappy',colorSpace='rgb255',color=(0,0,0))
ratingprompt=visual.TextStim(win=mywin,pos=[0,9],wrapWidth=40,height=2.5,text='How happy are you at this moment?',color='black')
baseratingprompt=visual.TextStim(win=mywin,pos=[0,7],wrapWidth=40,height=2.5,text='Taken all together, how happy are you with your life these days?',color='black')
rprompt=visual.TextStim(win=mywin,pos=[0,7],wrapWidth=40,height=2.5,text='How happy are you at this moment?',color='black')
pressSpacebar=visual.TextStim(win=mywin,pos=[0,-15],text='Press Spacebar to continue.',color='grey')
Ratings=visual.Rect(win=mywin,pos=[0,-8.5],width=25,height=0.1,lineWidth=3.5,lineColorSpace='rgb255',lineColor=(0,0,0)) #visual.Rect() creates a rectangle of given width and height as a special case of a ShapeStim
Decision=visual.TextStim(mywin,height=2,pos=[0,-10.5],text="50",color='black')
cArrow=visual.ImageStim(mywin,size=[2,2],pos=[0,-4.5],image='cArrow.jpg')


ratingitems=[happy,sad,ratingprompt,happytxt,unhappytxt,pressSpacebar]
baseratingitems=[happy,sad,baseratingprompt,happytxt,unhappytxt,pressSpacebar]
rScale=[Ratings,cArrow,happy,sad,rprompt,happytxt,unhappytxt,pressSpacebar]
baseScale=[Ratings,cArrow,happy,sad,baseratingprompt,happytxt,unhappytxt,pressSpacebar]


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
    


def basemood(vcount,vsave):
    vcount=vcount+1
    confirm=0
    aPos=0 #arrow's position
    scale=0.25
    ratingOnset=clock.getTime()
    while confirm==0:
        buttons=myMouse.clickReset()
        buttons=myMouse.getPressed()
        keypress=event.getKeys(keyList=['space','q'])
        
        if buttons==[1,0,0]:
            if aPos*4==-49:
                pass
            else:
                aPos=aPos-scale
                cArrow.pos=[aPos,-4.5]
                Decision.text= str(int(aPos*4+50))
                drawing(baseScale)
                mywin.flip()
            core.wait(0.1)
            
        elif buttons==[0,0,1]:
            if aPos*4==50.0:
                pass
            else:
                aPos=aPos+scale
                cArrow.pos=[aPos,-4.5]
                Decision.text= str(int(aPos*4+50))
                drawing(baseScale)
                mywin.flip()
            core.wait(0.1)
        
        elif keypress==['space']:
            cArrow.pos=[aPos,-4.5]
            Decision.text=str(int(aPos*4+50))
            ratingtime = clock.getTime()-ratingOnset
            rating=Decision.text
            vsave.append([vcount,rating,ratingOnset,ratingtime])
            confirm=1
            aPos=0
            cArrow.pos=[aPos,-4.5]
            Decision.text=str(int(aPos*4+50))
            mywin.flip()
            
        elif keypress=='q':
            core.quit()
            
        else:
            drawing(baseScale)
            mywin.flip()
            
    grey_fix.draw()
    grey_fix_2.draw()
    mywin.flip()
    core.wait(1.0)

def pracmood(vcount,vsave2):
    vcount=vcount+1
    confirm=0
    aPos=0
    scale=0.25
    ratingOnset=clock.getTime()
    while confirm==0:
        buttons=myMouse.clickReset()
        buttons=myMouse.getPressed()
        keypress=event.getKeys(keyList=['space','q'])
        
        if buttons==[1,0,0]:
            if aPos*4==-49:
                pass
            else:
                aPos=aPos-scale
                cArrow.pos=[aPos,-4.5]
                Decision.text= str(int(aPos*4+50))
                drawing(rScale)
                mywin.flip()

            core.wait(0.1)
            
        elif buttons==[0,0,1]:
            if aPos*4==50.0:
                pass
            else:
                aPos=aPos+scale
                cArrow.pos=[aPos,-4.5]
                Decision.text= str(int(aPos*4+50))
                drawing(rScale)
                mywin.flip()

            core.wait(0.1)
        
        elif keypress==['space']:
            cArrow.pos=[aPos,-4.5]
            Decision.text=str(int(aPos*4+50))
            ratingtime = clock.getTime()-ratingOnset
            rating=Decision.text
            confirm=1
            aPos=0
            cArrow.pos=[aPos,-4.5]
            Decision.text=str(int(aPos*4+50))
            mywin.flip()
            
        elif keypress=='q':
            core.quit()
            
        else:
            drawing(rScale)
            mywin.flip()
            
    grey_fix.draw()
    grey_fix_2.draw()
    mywin.flip()
    core.wait(1.0)

        

def mood(vcount,vsave):
    vcount=vcount+1
    confirm=0
    aPos=0
    scale=0.25
    ratingOnset=clock.getTime()
    while confirm==0:
        buttons=myMouse.clickReset()
        buttons=myMouse.getPressed()
        keypress=event.getKeys(keyList=['space','q'])
        
        if buttons==[1,0,0]:
            if aPos*4==-49:
                pass
            else:
                aPos=aPos-scale
                cArrow.pos=[aPos,-4.5]
                Decision.text= str(int(aPos*4+50))
                drawing(rScale)
                mywin.flip()

            core.wait(0.1)
            
        elif buttons==[0,0,1]:
            if aPos*4==50.0:
                pass
            else:
                aPos=aPos+scale
                cArrow.pos=[aPos,-4.5]
                Decision.text= str(int(aPos*4+50))
                drawing(rScale)
                mywin.flip()

            core.wait(0.1)
        
        elif keypress==['space']:
            cArrow.pos=[aPos,-4.5]
            Decision.text=str(int(aPos*4+50))
            ratingtime = clock.getTime()-ratingOnset
            rating=Decision.text
            vsave.append([vcount,rating,ratingOnset,ratingtime])
            confirm=1
            aPos=0
            cArrow.pos=[aPos,-4.5]
            Decision.text=str(int(aPos*4+50))
            mywin.flip()
            
        elif keypress=='q':
            core.quit()
            
        else:
            drawing(rScale)
            mywin.flip()
            
    grey_fix.draw()
    grey_fix_2.draw()
    mywin.flip()
    core.wait(1.0)

        

def get_vdata(Save):
    end_time=time.strftime("%Y%m%d-%H%M%S")
    etime=time.strftime("%H:%M:%S")
    header=['Round','Rating','Onset','RT']
    savFrac= open(data_path + subinfo['Participant ID'] + '_' + 'mood_'+ end_time + '.txt', 'w')
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


def instructions():
    for l in inst_list:
        l.draw()
        mywin.flip()
        event.waitKeys(keyList=['space'])
    

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
        
        if trialcount==76:
            halfTime.draw()
            mywin.flip()
            event.waitKeys(keyList=['space'])
            type='break'

        
        if t[6]=='left': #if Risk side is left
            guaranteedright.text= '$' + str(t[2])
            if t[7]=='top': #if bet 2 side is top
                highbetleft.text= '$' + str(t[4]) #t[4] is Bet 2 value
                lowbetleft.text= '$' + str(t[3]) #t[3] is Bet 1 value
            elif t[7]=='bottom':
                highbetleft.text= '$' + str(t[3])
                lowbetleft.text= '$' + str(t[4])
                
            event.clearEvents()
            ChoiceOnset=clock.getTime()
            for l in range(int(scrnHz*(timing))):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                
                if (keypress) or (buttons == [1,0,0]) or (buttons == [0,0,1]) :
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
                    
                if keypress==['left']: #i.e., t[6] == keypress -> chose to gamble
                    highbetboxleft.lineColor=(255,255,0)
                    lowbetboxleft.lineColor=(255,255,0)
                    guaranteedrightbox.lineColor=(224,224,224)
                    guaranteedright.color=(224,224,224)
                    choicePos='left'
                    gambleChoice='gamble'
                    drawing(gamble_left)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]: #if outcome == bet 2 side (the better of the two gamble coutcomes)
                        if t[5]=='top':
                            highbetboxleft.lineColor=(0,255,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            lowbetleft.color=(224,224,224)
                            if t[1]=='mix': #bet 2 in a "mix" trial is always a positive value
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain': #bet 2 in gain is always a positive value
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss': #bet 2 in gain is always $0
                                win_left.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom': #feedback is similar to 511-531
                            lowbetboxleft.lineColor=(0,255,0)
                            highbetboxleft.lineColor=(224,224,224)
                            highbetleft.color=(224,224,224)
                            if t[1]=='mix':
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain':
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss':
                                win_left.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                    else: #outcome is bet 1, not bet 2
                        if t[5]=='top':
                            highbetboxleft.lineColor=(255,0,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            lowbetboxleft.lineColor=(224,224,224)
                            if t[1]=='mix': #outcome is always a negative value
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain': #outcome is always $0
                                lose_left.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss': #outcome is a negative value larger in magnitude than safe choice
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=(255,0,0)
                            highbetboxleft.lineColor=(224,224,224)
                            highbetleft.color=(224,224,224)
                            if t[1]=='mix': #feedback is similar to 556-576
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_left.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                            
                elif keypress==['right']: #i.e, Risk side is left while choice is right
                    highbetboxleft.lineColor=(224,224,224)
                    highbetleft.color=(224,224,224)
                    lowbetboxleft.lineColor=(224,224,224)
                    lowbetleft.color=(224,224,224)
                    guaranteedrightbox.lineColor=(255,255,0)
                    guaranteedright.color=(0,0,0)
                    choicePos='right'
                    gambleChoice='safe'
                    drawing(gamble_left)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]: #if counterfactual outcome is bet 2
                        if t[1]=='mix': #safe choice/bet in "mix" is always $0
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain': #safe bet in "gain" is always a positive value
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss': #safe bet in "loss" is always a negative value
                            safe_right.color=(0,0,0)
                            safe_right.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        safe_right.draw()
                        drawing(gamble_left)
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text= '$' + str(TotalProfit)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                            
                            
                        if t[5]=='top': #if bet 2 is top
                            highbetboxleft.lineColor=(128,0,128)
                            highbetleft.color=(0,0,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(255,0,0)
                            
                            if t[1]=='mix': #bet 2 in mix is always positive value
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain': #bet 2 in gain is always positive value
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss': #bet 2 in loss is always $0
                                lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[2])
                            drawing(losegamble_left)
                            drawing(Reward)
                            mywin.flip()
                            Outcome='bad'
                            core.wait(3.5)
                            
                        elif t[5]=='bottom': #if bet 2 is bottom; feedback is similar to 634-654
                            lowbetboxleft.lineColor=(128,0,128)
                            lowbetleft.color=(0,0,0)
                            highbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(255,0,0)
                            if t[1]=='mix':
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Profit=float(t[2])
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                    else: #if counterfactual outcome is bet 1
                        if t[1]=='mix': #safe bet, always $0
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain': #safe bet, always positive
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss': #safe bet, always negative
                            safe_right.color=(0,0,0)
                            safe_right.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        drawing(gamble_left)
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        drawing(Reward)
                        safe_right.draw()
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top': #counterfactual outcome on top
                            highbetboxleft.lineColor=(128,0,128)
                            highbetleft.color=(0,0,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(0,255,0)
                            
                            if t[1]=='mix': #bet 1, always negative
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain': #bet 1, always 0
                                win_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss': #bet 1, always negative
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom': #counterfactual outcome at bottom; feedback similar to 696-716
                            lowbetboxleft.lineColor=(128,0,128)
                            lowbetleft.color=(0,0,0)
                            highbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(0,255,0)
                            if t[1]=='mix':
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain':
                                win_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss':
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)

                elif keypress==['q']:
                    get_data(save)
                    #get_rate(ratesave)
                    core.quit()
                
                elif keypress==['p']:
                    pause.draw()
                    mywin.flip()
                    profit=0
                    choicePos='skip'
                    gambleChoice='skip'
                    event.waitKeys(keyList='p')
                    trials.append(t)
                    
                    

        elif t[6]=='right': #Risk side is right
            ChoiceOnset=clock.getTime()
            guaranteedleft.text= '$' + str(t[2])
            if t[7]=='top':
                highbetright.text= '$' + str(t[4])
                lowbetright.text= '$' + str(t[3])
            elif t[7]=='bottom':
                highbetright.text= '$' + str(t[3])
                lowbetright.text= '$' + str(t[4])
            
            event.clearEvents()
            for l in range(int(scrnHz*(timing))):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                if keypress or buttons==[1,0,0] or buttons==[0,0,1]:
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
                    
                if keypress==['right']: #keypress == risk side == right
                    highbetboxright.lineColor=(255,255,0)
                    lowbetboxright.lineColor=(255,255,0)
                    guaranteedleftbox.lineColor=(224,224,224)
                    guaranteedleft.color=(224,224,224)
                    choicePos='right'
                    gambleChoice='gamble'
                    drawing(gamble_right)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]: #outcome is bet 2
                        if t[5]=='top':
                            highbetboxright.lineColor=(0,255,0)
                            lowbetboxright.lineColor=(224,224,224)
                            lowbetright.color=(224,224,224)
                            if t[1]=='mix':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss': # $0
                                win_right.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(0,255,0)
                            highbetboxright.lineColor=(224,224,224)
                            highbetright.color=(224,224,224)
                            if t[1]=='mix':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss':
                                win_right.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                    else: #outcome is not bet 2, but bet 1
                        if t[5]=='top':
                            highbetboxright.lineColor==(255,0,0)
                            lowbetboxright.lineColor=(224,244,244)
                            lowbetleft.color=(224,224,224)
                            if t[1]=='mix':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain': # $0
                                lose_right.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss': #trial 144 could fall here
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(255,0,0)
                            highbetboxright.lineColor=(224,224,224)
                            highbetright.color=(224,224,224)
                            if t[1]=='mix':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain': # $0
                                lose_right.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            
                        
                elif keypress==['left']: #risk side is right, but keypress == left == safe bet
                    highbetboxright.lineColor=(224,224,224)
                    highbetright.color=(224,224,224)
                    lowbetboxright.lineColor=(224,224,224)
                    lowbetright.color=(224,224,224)
                    guaranteedleftbox.lineColor=(255,255,0)
                    guaranteedleft.color=(0,0,0)
                    choicePos='left'
                    gambleChoice='safe'
                    drawing(gamble_right)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]: #counterfactual outcome is bet 2
                        if t[1]=='mix': # $0
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=(0,0,0)
                            safe_left.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        drawing(gamble_right)
                        safe_left.draw()
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxright.lineColor=(128,0,128)
                            highbetright.color=(0,0,0)
                            lowbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(255,0,0)
                            if t[1]=='mix':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss': # $0
                                lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
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
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss': # $0
                                lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.5)
                            

                    else: #counterfactual outcome is bet 1
                        if t[1]=='mix': #safe bet in mix is always $0
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=(0,0,0)
                            safe_left.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        drawing(gamble_right)
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        drawing(Reward)
                        safe_left.draw()
                        mywin.flip()
                        core.wait(2.0)
                    
                        if t[5]=='top':
                            highbetboxright.lineColor=(128,0,128)
                            highbetright.color=(0,0,0)
                            lowbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(0,255,0)
                            if t[1]=='mix': #bet 1 in mix is always negative
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain': # $0
                                win_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss': #trial 144 could fall here
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(128,0,128)
                            lowbetright.color=(0,0,0)
                            highbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(0,255,0)
                            if t[1]=='mix':
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain':
                                win_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss':
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.5)
                            
                        
                elif keypress==['q']:
                    get_data(save)
                    #get_rate(ratesave)
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
        
#        if int(trialcount)%ratefreq==0:
#            mood(trialcount,ratesave)

           
        
    #get_rate(ratesave)
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
#    if trialcount==0:
#        basemood(trialcount,ratesave)
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
                    highbetboxleft.lineColor=(255,255,0)
                    lowbetboxleft.lineColor=(255,255,0)
                    guaranteedrightbox.lineColor=(224,224,224)
                    guaranteedright.color=(224,224,224)
                    choicePos='left'
                    gambleChoice='gamble'
                    drawing(gamble_left)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]: #gamble, outcome is bet 2
                        if t[5]=='top':
                            highbetboxleft.lineColor=(0,255,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            lowbetleft.color=(224,224,224)
                            if t[1]=='mix':
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain':
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss': # $0
                                win_left.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=(0,255,0)
                            highbetboxleft.lineColor=(224,224,224)
                            highbetleft.color=(224,224,224)
                            if t[1]=='mix':
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain':
                                win_left.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss': # $0
                                win_left.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_left.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                    else: #gamble, outcome's bet 1
                        if t[5]=='top':
                            highbetboxleft.lineColor=(255,0,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            lowbetboxleft.lineColor=(224,224,224)
                            if t[1]=='mix':
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain': # $0
                                lose_left.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=(255,0,0)
                            highbetboxleft.lineColor=(224,224,224)
                            highbetleft.color=(224,224,224)
                            if t[1]=='mix':
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_left.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_left.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                            
                elif keypress==['right']:
                    highbetboxleft.lineColor=(224,224,224)
                    highbetleft.color=(224,224,224)
                    lowbetboxleft.lineColor=(224,224,224)
                    lowbetleft.color=(224,224,224)
                    guaranteedrightbox.lineColor=(255,255,0)
                    choicePos='right'
                    gambleChoice='safe'
                    drawing(gamble_left)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]: #safe bet; counterfactual outcome is bet 2
                        if t[1]=='mix': # $0
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_right.color=(0,0,0)
                            safe_right.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_right.draw()
                        drawing(gamble_left)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top': #counterfactual, bet 2
                            highbetboxleft.lineColor=(128,0,128)
                            highbetleft.color=(0,0,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(255,0,0)
                            
                            if t[1]=='mix':
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss': # $0
                                lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[2])
                            drawing(losegamble_left)
                            drawing(Reward)
                            mywin.flip()
                            Outcome='bad'
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=(128,0,128)
                            lowbetleft.color=(0,0,0)
                            highbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(255,0,0)
                            if t[1]=='mix':
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_left.text='You would have won $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_left.text='You would have lost $' + str(abs(Decimal(t[4]))) +'!'
                                lose_left.color=(255,0,0)
                            Profit=float(t[2])
                            drawing(losegamble_left)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                    else: #safe bet; counterfactual outcome is bet 1
                        if t[1]=='mix': # $0
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_right.color=(0,0,0)
                            safe_right.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_right.color=(0,0,0)
                            safe_right.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_right.draw()
                        drawing(gamble_left)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top': #counterfactual, bet 1
                            highbetboxleft.lineColor=(128,0,128)
                            highbetleft.color=(0,0,0)
                            lowbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(0,255,0)
                            
                            if t[1]=='mix':
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain': # $0
                                win_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss':
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            Profit=float(t[2])
                            drawing(wingamble_left)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxleft.lineColor=(128,0,128)
                            lowbetleft.color=(0,0,0)
                            highbetboxleft.lineColor=(224,224,224)
                            guaranteedrightbox.lineColor=(0,255,0)
                            if t[1]=='mix':
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='gain': # $0
                                win_left.text='You would have won $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
                            elif t[1]=='loss':
                                win_left.text='You would have lost $' + str(abs(Decimal(t[3]))) +'!'
                                win_left.color=(0,255,0)
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
                    
                    

        elif t[6]=='right': #risk side is right
            ChoiceOnset=clock.getTime()
            guaranteedleft.text= '$' + str(t[2])
            if t[7]=='top':
                highbetright.text= '$' + str(t[4])
                lowbetright.text= '$' + str(t[3])
            elif t[7]=='bottom':
                highbetright.text= '$' + str(t[3])
                lowbetright.text= '$' + str(t[4])
            
            event.clearEvents()
            for l in range(int(scrnHz*(timing))):
                keypress=event.getKeys(keyList=['left','right','q','p'])
                buttons=myMouse.clickReset()
                buttons=myMouse.getPressed()
                
                if keypress or buttons==[1,0,0] or buttons==[0,0,1]:
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
                    
                if keypress==['right']: #risk side is right
                    highbetboxright.lineColor=(255,255,0)
                    lowbetboxright.lineColor=(255,255,0)
                    guaranteedleftbox.lineColor=(224,224,224)
                    guaranteedleft.color=(224,224,224)
                    choicePos='right'
                    gambleChoice='gamble'
                    drawing(gamble_right)
                    drawing(Reward)
                    mywin.flip()
                    core.wait(2.0)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[5]=='top':
                            highbetboxright.lineColor=(0,255,0)
                            lowbetboxright.lineColor=(224,224,224)
                            lowbetright.color=(224,224,224)
                            if t[1]=='mix':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss': # $0
                                win_right.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(0,255,0)
                            highbetboxright.lineColor=(224,224,224)
                            highbetright.color=(224,224,224)
                            if t[1]=='mix':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain':
                                win_right.text='You won $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss': # $0
                                win_right.text='You lost $' + str(abs(Decimal(t[4]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[4])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                    else: #gamble, outcome is bet 1
                        if t[5]=='top':
                            highbetboxright.lineColor==(255,0,0)
                            lowbetboxright.lineColor=(224,244,244)
                            lowbetleft.color=(224,224,224)
                            if t[1]=='mix':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain': # $0
                                lose_right.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(255,0,0)
                            highbetboxright.lineColor=(224,224,224)
                            highbetright.color=(224,224,224)
                            if t[1]=='mix':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain': # $0
                                lose_right.text='You won $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_right.text='You lost $' + str(abs(Decimal(t[3]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[3])
                            TotalProfit=round(TotalProfit+Profit,2)
                            Reward_value.text='$' + str(TotalProfit)
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        
                elif keypress==['left']: #risk side is right; chose safe bet
                    highbetboxright.lineColor=(224,224,224)
                    highbetright.color=(224,224,224)
                    lowbetboxright.lineColor=(224,224,224)
                    lowbetright.color=(224,224,224)
                    guaranteedleftbox.lineColor=(255,255,0)
                    choicePos='left'
                    gambleChoice='safe'
                    drawing(gamble_right)
                    drawing(Reward)
                    FeedbackOnset=clock.getTime()
                    
                    if t[5]==t[7]:
                        if t[1]=='mix': # $0
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=(0,0,0)
                            safe_left.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_left.draw()
                        drawing(gamble_right)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top': #counterfactual is bet 2
                            highbetboxright.lineColor=(128,0,128)
                            highbetright.color=(0,0,0)
                            lowbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(255,0,0)
                            if t[1]=='mix':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss': # $0
                                lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(128,0,128)
                            lowbetright.color=(0,0,0)
                            highbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(255,0,0)
                            if t[1]=='mix':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='gain':
                                lose_right.text='You would have won $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            elif t[1]=='loss':
                                lose_right.text='You would have lost $' + str(abs(Decimal(t[4]))) + '!'
                                lose_right.color=(255,0,0)
                            Profit=float(t[2])
                            drawing(losegamble_right)
                            drawing(Reward)
                            Outcome='bad'
                            mywin.flip()
                            core.wait(3.0)
                            

                    else: #counterfactual is bet 1
                        if t[1]=='mix': # $0
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='gain':
                            safe_left.color=(0,0,0)
                            safe_left.text='You won $' + str(abs(Decimal(t[2]))) +'!'
                        elif t[1]=='loss':
                            safe_left.color=(0,0,0)
                            safe_left.text='You lost $' + str(abs(Decimal(t[2]))) +'!'
                        Profit=float(t[2])
                        TotalProfit=round(TotalProfit+Profit,2)
                        Reward_value.text='$' + str(TotalProfit)
                        safe_left.draw()
                        drawing(gamble_right)
                        drawing(Reward)
                        mywin.flip()
                        core.wait(2.0)
                        
                        if t[5]=='top':
                            highbetboxright.lineColor=(128,0,128)
                            highbetright.color=(0,0,0)
                            lowbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(0,255,0)
                            if t[1]=='mix':
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain': # $0
                                win_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss':
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            Profit=float(t[2])
                            drawing(wingamble_right)
                            drawing(Reward)
                            Outcome='good'
                            mywin.flip()
                            core.wait(3.0)
                            
                        elif t[5]=='bottom':
                            lowbetboxright.lineColor=(128,0,128)
                            lowbetright.color=(0,0,0)
                            highbetboxright.lineColor=(224,224,224)
                            guaranteedleftbox.lineColor=(0,255,0)
                            if t[1]=='mix':
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='gain':
                                win_right.text='You would have won $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
                            elif t[1]=='loss':
                                win_right.text='You would have lost $' + str(abs(Decimal(t[3]))) + '!'
                                win_right.color=(0,255,0)
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
#    
#        if int(trialcount)%ratefreq==0:
#            vsave2=[]
#            pracmood(0,vsave2)
    
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
    header=['Round','Rating','RatingOnset','RT']
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
    prac=1
    save=[]
    vsave=[]
    gamble_trials=[]
    practice_trials=[]
    vcount=0
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
    #sub-timeline
    #BDI_Task()
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
    # get_data(save) #line 1068, at the end of def task(trials,save), already saves all task data. This second save is redundant. 
    eot.draw() #end of task
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])


#timeline
if __name__ == '__main__':
    if instruction=='yes':
        instructions()
    elif instruction=='no':
        pass
    get_trials()
    