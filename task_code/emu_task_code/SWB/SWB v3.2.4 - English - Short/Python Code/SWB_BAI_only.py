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


#BAI Stimuli (21 items)
Prompts=['Numbness or tingling', 'Feeling hot', 'Wobbliness in legs', 'Unable to relax', 'Fear of worst happening', 'Dizzy or lightheaded', 'Heart pounding / racing', 'Unsteady', 'Terrified or afraid', 'Nervous', 'Feeling of choking', 'Hands trembling', 'Shaky / unsteady', 'Fear of losing control', 'Difficulty in breathing', 'Fear of dying', 'Scared', 'Indigestion', 'Faint / lightheaded', 'Face flushed', 'Hot / cold sweats']
Choices1=["1 - Not at all."] 
Choices2=["2 - Mildly, but it didn't bother me much."] 
Choices3=["3 - Moderately - it wasn't pleasant at times."] 
Choices4=["4 - Severely - it bothered me a lot."]


Questionaire=Instructions=visual.TextStim(mywin,height=3,font='Ariel',wrapWidth=35,text="Survey" ,colorSpace='rgb255',color='black')

#BAI_Instruct=visual.ImageStim(mywin,size=[40,40],pos=[0,0],image='BAI.jpg')
BAI_Instruct=visual.TextStim(mywin,height=2,font='Ariel',wrapWidth=35,text="You will be presented a series of common symptoms of anxiety. Please carefully read each item. Indicate how much you have been bothered by that symptom during the past month, including today, by entering the number that corresponding space in the column next to each symptom." ,colorSpace='rgb255',color='black')
Prompt=visual.TextStim(mywin,height=3,pos=[0,7],font='Ariel',wrapWidth=120,text='' ,color='black')
Choice1=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-10,3],font='Ariel',wrapWidth=35,text='',color='black')
Choice2=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-10,0],font='Ariel',wrapWidth=35,text='',color='black')
Choice3=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-10,-3],font='Ariel',wrapWidth=35,text='',color='black')
Choice4=visual.TextStim(mywin,alignHoriz='left',height=1,pos=[-10,-6],font='Ariel',wrapWidth=35,text='',color='black')

#BAI Lists
Question=[Prompt,Choice1,Choice2,Choice3,Choice4]

def BAI_Task():
    #BAI Task
    Questionaire.draw()
    pass_inst.draw() #text="(Press Spacebar)"
    mywin.flip()
    event.waitKeys()
    
    BAI_Instruct.draw()
    pass_inst.draw()
    mywin.flip()
    event.waitKeys()
    
    Score=0
    bsave=[]
    for i in range(0,len(Prompts)):
        Prompt.text=Prompts[i]
        Choice1.text=Choices1[0]
        Choice2.text=Choices2[0]
        Choice3.text=Choices3[0]
        Choice4.text=Choices4[0]
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
    header=['Prompt','Chosen','BAI Score']
    savFrac= open(data_path + subinfo['Participant ID'] + '_BAI_' + etime + '.txt', 'w')
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
    BAI_Task()
    eot.draw() #end of task
    pass_inst.draw()
    mywin.flip()
    event.waitKeys(keyList=['space','down'])


#timeline
if __name__ == '__main__':
    #BAI_Task() #runs & saves but exits abruptly!
    get_trials()  #sequences a thank you screen