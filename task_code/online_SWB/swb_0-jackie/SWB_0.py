#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.2.4),
    on Tue Aug  8 11:14:15 2023
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

import psychopy
psychopy.useVersion('2022.2.4')


# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from define_variables
total = 10
maxTime = 8
# Run 'Before Experiment' code from countHowHappy
trialN = 1
doHowHappy = 0


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.2.4'
expName = 'SWB_debug'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
# --- Show participant info dialog --
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/alexandrafink/Documents/GraduateSchool/SaezLab/SWB/online_SWB/swb_0-master/SWB_0.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# --- Setup the Window ---
win = visual.Window(
    size=[1536, 864], fullscr=False, screen=0, 
    winType='pyglet', allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
win.mouseVisible = True
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# --- Setup input devices ---
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# --- Initialize components for Routine "defined" ---
# Run 'Begin Experiment' code from define_variables
safecolor = 'black'
topcolor = 'black'
bottomcolor = 'black'

safey = 0
safex = .25
gambletop = .25
gamblebottom = -.25
gamblex = -.25
winy=.2

total = 10




# --- Initialize components for Routine "Welcome" ---
welcomeText1 = visual.TextStim(win=win, name='welcomeText1',
    text='Hello!\n\nYou will be participating in a gambling task that could result in a Cash Reward based on your performance. \n\nIn each trial, you will have the option between a safe bet or a gamble. If you select the safe bet, you will receive that amount of money. You will then be shown what you would have received if you had chosen the gamble. \n\nPress SPACEBAR to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_to_continue = keyboard.Keyboard()

# --- Initialize components for Routine "Welcome2" ---
welcomeText2 = visual.TextStim(win=win, name='welcomeText2',
    text='If you select the gamble, you will have a 50/50 chance at earning more or less money than the safe bet. The safe bet can be negative, positive, or zero. \n\nYou will make your selection by using with a mouse. A Total Score will be presented in the top left corner of the screen. You will receive the total amount at the end of the experiment.\n\nPress SPACEBAR to begin the experiment',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
space_to_continue_2 = keyboard.Keyboard()

# --- Initialize components for Routine "SetupGraphics" ---

# --- Initialize components for Routine "Cue" ---
LeftHalf = visual.Rect(
    win=win, name='LeftHalf',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
RightHalf = visual.Rect(
    win=win, name='RightHalf',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
Safe = visual.Rect(
    win=win, name='Safe',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Top = visual.Rect(
    win=win, name='Top',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Bottom = visual.Rect(
    win=win, name='Bottom',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
SafeText = visual.TextStim(win=win, name='SafeText',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
TopText = visual.TextStim(win=win, name='TopText',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
BottomText = visual.TextStim(win=win, name='BottomText',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-8.0);
Total = visual.Rect(
    win=win, name='Total',
    width=(0.1, 0.2)[0], height=(0.1, 0.2)[1],
    ori=0.0, pos=(-.45, .3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0,0,0],
    opacity=None, depth=-9.0, interpolate=True)
Win = visual.TextStim(win=win, name='Win',
    text='',
    font='Open Sans',
    pos=(-.45, .3), height=0.03, wrapWidth=0.22, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
Keys = keyboard.Keyboard()
Mouse = event.Mouse(win=win)
x, y = [None, None]
Mouse.mouseClock = core.Clock()

# --- Initialize components for Routine "Calculate" ---

# --- Initialize components for Routine "SelectionShown" ---
LeftHalf_2 = visual.Rect(
    win=win, name='LeftHalf_2',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=1.0, depth=0.0, interpolate=True)
RightHalf_2 = visual.Rect(
    win=win, name='RightHalf_2',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
Safe_2 = visual.Rect(
    win=win, name='Safe_2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-2.0, interpolate=True)
Top_2 = visual.Rect(
    win=win, name='Top_2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Bottom_2 = visual.Rect(
    win=win, name='Bottom_2',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
SafeText_2 = visual.TextStim(win=win, name='SafeText_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-5.0);
TopText_2 = visual.TextStim(win=win, name='TopText_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
BottomText_2 = visual.TextStim(win=win, name='BottomText_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
Total_2 = visual.Rect(
    win=win, name='Total_2',
    width=(0.1, 0.2)[0], height=(0.1, 0.2)[1],
    ori=0.0, pos=(-.45, .3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0,0,0],
    opacity=None, depth=-8.0, interpolate=True)
Win_2 = visual.TextStim(win=win, name='Win_2',
    text='',
    font='Open Sans',
    pos=(-.45, .3), height=0.03, wrapWidth=0.22, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-9.0);
WinMsg = visual.TextStim(win=win, name='WinMsg',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.04, wrapWidth=0.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);

# --- Initialize components for Routine "GambleRevealed" ---
LeftHalf_3 = visual.Rect(
    win=win, name='LeftHalf_3',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0.0, pos=(-.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=1.0, depth=-1.0, interpolate=True)
RightHalf_3 = visual.Rect(
    win=win, name='RightHalf_3',
    width=(0.5, 0.8)[0], height=(0.5, 0.8)[1],
    ori=0.0, pos=(.25, 0), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='black', fillColor='white',
    opacity=1.0, depth=-2.0, interpolate=True)
Safe_3 = visual.Rect(
    win=win, name='Safe_3',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-3.0, interpolate=True)
Top_3 = visual.Rect(
    win=win, name='Top_3',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-4.0, interpolate=True)
Bottom_3 = visual.Rect(
    win=win, name='Bottom_3',
    width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
    ori=0.0, pos=[0,0], anchor='center',
    lineWidth=5.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
    opacity=None, depth=-5.0, interpolate=True)
SafeText_3 = visual.TextStim(win=win, name='SafeText_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-6.0);
TopText_3 = visual.TextStim(win=win, name='TopText_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-7.0);
BottomText_3 = visual.TextStim(win=win, name='BottomText_3',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.06, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=1.0, 
    languageStyle='LTR',
    depth=-8.0);
Total_3 = visual.Rect(
    win=win, name='Total_3',
    width=(0.1, 0.2)[0], height=(0.1, 0.2)[1],
    ori=0.0, pos=(-.45, .3), anchor='center',
    lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor=[0,0,0],
    opacity=None, depth=-9.0, interpolate=True)
Win_3 = visual.TextStim(win=win, name='Win_3',
    text='',
    font='Open Sans',
    pos=(-.45, .3), height=0.03, wrapWidth=0.22, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-10.0);
WinMsg_2 = visual.TextStim(win=win, name='WinMsg_2',
    text='',
    font='Open Sans',
    pos=[0,0], height=0.04, wrapWidth=0.2, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-11.0);

# --- Initialize components for Routine "Timeout" ---
timeoutText = visual.TextStim(win=win, name='timeoutText',
    text='Please respond faster',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "HowHappy" ---
HowHappySlider = visual.Slider(win=win, name='HowHappySlider',
    startValue=None, size=(1.0, 0.1), pos=(0, -0.2), units=None,
    labels=None, ticks=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10), granularity=0.0,
    style='rating', styleTweaks=('labels45',), opacity=None,
    labelColor='LightGray', markerColor='black', lineColor='White', colorSpace='rgb',
    font='Open Sans', labelHeight=0.05,
    flip=False, ori=0.0, depth=-1, readOnly=False)
UnHappy = visual.TextStim(win=win, name='UnHappy',
    text='Very Unhappy',
    font='Open Sans',
    pos=(-.6, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
Happy = visual.TextStim(win=win, name='Happy',
    text='Very Happy',
    font='Open Sans',
    pos=(.6, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-3.0);
SliderKeyboard = keyboard.Keyboard()
SpacetoExit = visual.TextStim(win=win, name='SpacetoExit',
    text='Press SPACEBAR to Continue',
    font='Open Sans',
    pos=(0, -.4), height=0.04, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# --- Initialize components for Routine "Fixation" ---
Cross = visual.TextStim(win=win, name='Cross',
    text='+',
    font='Open Sans',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0.0, 
    color='black', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# --- Initialize components for Routine "ThankYou" ---
exitText = visual.TextStim(win=win, name='exitText',
    text='[This is the exit screen]\n\nThank you for participating in our study!\n\nwhat else goes here?',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.Clock()  # to track time remaining of each (possibly non-slip) routine 

# --- Prepare to start Routine "defined" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
definedComponents = []
for thisComponent in definedComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "defined" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in definedComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "defined" ---
for thisComponent in definedComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "defined" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Welcome" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_to_continue.keys = []
space_to_continue.rt = []
_space_to_continue_allKeys = []
# keep track of which components have finished
WelcomeComponents = [welcomeText1, space_to_continue]
for thisComponent in WelcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText1* updates
    if welcomeText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText1.frameNStart = frameN  # exact frame index
        welcomeText1.tStart = t  # local t and not account for scr refresh
        welcomeText1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText1, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeText1.started')
        welcomeText1.setAutoDraw(True)
    
    # *space_to_continue* updates
    if space_to_continue.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_to_continue.frameNStart = frameN  # exact frame index
        space_to_continue.tStart = t  # local t and not account for scr refresh
        space_to_continue.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_to_continue, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('space_to_continue.started', t)
        space_to_continue.status = STARTED
        # keyboard checking is just starting
        space_to_continue.clock.reset()  # now t=0
    if space_to_continue.status == STARTED:
        theseKeys = space_to_continue.getKeys(keyList=['space','return'], waitRelease=False)
        _space_to_continue_allKeys.extend(theseKeys)
        if len(_space_to_continue_allKeys):
            space_to_continue.keys = _space_to_continue_allKeys[-1].name  # just the last key pressed
            space_to_continue.rt = _space_to_continue_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome" ---
for thisComponent in WelcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# --- Prepare to start Routine "Welcome2" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
space_to_continue_2.keys = []
space_to_continue_2.rt = []
_space_to_continue_2_allKeys = []
# keep track of which components have finished
Welcome2Components = [welcomeText2, space_to_continue_2]
for thisComponent in Welcome2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "Welcome2" ---
while continueRoutine:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *welcomeText2* updates
    if welcomeText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        welcomeText2.frameNStart = frameN  # exact frame index
        welcomeText2.tStart = t  # local t and not account for scr refresh
        welcomeText2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(welcomeText2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'welcomeText2.started')
        welcomeText2.setAutoDraw(True)
    
    # *space_to_continue_2* updates
    if space_to_continue_2.status == NOT_STARTED and t >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        space_to_continue_2.frameNStart = frameN  # exact frame index
        space_to_continue_2.tStart = t  # local t and not account for scr refresh
        space_to_continue_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(space_to_continue_2, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.addData('space_to_continue_2.started', t)
        space_to_continue_2.status = STARTED
        # keyboard checking is just starting
        space_to_continue_2.clock.reset()  # now t=0
    if space_to_continue_2.status == STARTED:
        theseKeys = space_to_continue_2.getKeys(keyList=['space','return'], waitRelease=False)
        _space_to_continue_2_allKeys.extend(theseKeys)
        if len(_space_to_continue_2_allKeys):
            space_to_continue_2.keys = _space_to_continue_2_allKeys[-1].name  # just the last key pressed
            space_to_continue_2.rt = _space_to_continue_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in Welcome2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "Welcome2" ---
for thisComponent in Welcome2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "Welcome2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trialControl = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('control_files/trialControlwRating_test.csv'),
    seed=None, name='trialControl')
thisExp.addLoop(trialControl)  # add the loop to the experiment
thisTrialControl = trialControl.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrialControl.rgb)
if thisTrialControl != None:
    for paramName in thisTrialControl:
        exec('{} = thisTrialControl[paramName]'.format(paramName))

for thisTrialControl in trialControl:
    currentLoop = trialControl
    # abbreviate parameter names if possible (e.g. rgb = thisTrialControl.rgb)
    if thisTrialControl != None:
        for paramName in thisTrialControl:
            exec('{} = thisTrialControl[paramName]'.format(paramName))
    
    # --- Prepare to start Routine "SetupGraphics" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from AdjustPosition
    if RiskSide == 'left':
        safex = .25
        gamblex = -.25
    else:
        safex = -.25
        gamblex = .25
    
    topAmt='$%0.2f'%(TopAmt)
    bottomAmt='$%0.2f'%(BottomAmt)
    certainAmt='$%0.2f'%(CertainAmt)
    
    totalWin='Total\n$%0.2f'%(total)
    
    event.clearEvents(Keys)
    # keep track of which components have finished
    SetupGraphicsComponents = []
    for thisComponent in SetupGraphicsComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "SetupGraphics" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SetupGraphicsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "SetupGraphics" ---
    for thisComponent in SetupGraphicsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "SetupGraphics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Cue" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # Run 'Begin Routine' code from trialTimer
    startTime = globalClock.getTime()
    revealRoutines = 1;
    timeoutRoutine = 0; 
    Safe.setPos((safex,safey))
    Top.setPos((gamblex, gambletop))
    Bottom.setPos((gamblex, gamblebottom))
    SafeText.setPos((safex, safey))
    SafeText.setText(certainAmt)
    TopText.setPos((gamblex, gambletop))
    TopText.setText(topAmt)
    BottomText.setPos((gamblex, gamblebottom))
    BottomText.setText(bottomAmt)
    Win.setText(totalWin)
    Keys.keys = []
    Keys.rt = []
    _Keys_allKeys = []
    # setup some python lists for storing info about the Mouse
    Mouse.clicked_name = []
    gotValidClick = False  # until a click is received
    # keep track of which components have finished
    CueComponents = [LeftHalf, RightHalf, Safe, Top, Bottom, SafeText, TopText, BottomText, Total, Win, Keys, Mouse]
    for thisComponent in CueComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Cue" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from trialTimer
        #increment trial counter each frame
        if globalClock.getTime() - startTime >= maxTime:
            #LCTTrials.finished = True; #what is this for?
            revealRoutines = 0;
            timeoutRoutine = 1; 
            continueRoutine = False;
        
        # *LeftHalf* updates
        if LeftHalf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            LeftHalf.frameNStart = frameN  # exact frame index
            LeftHalf.tStart = t  # local t and not account for scr refresh
            LeftHalf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(LeftHalf, 'tStartRefresh')  # time at next scr refresh
            LeftHalf.setAutoDraw(True)
        
        # *RightHalf* updates
        if RightHalf.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            RightHalf.frameNStart = frameN  # exact frame index
            RightHalf.tStart = t  # local t and not account for scr refresh
            RightHalf.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(RightHalf, 'tStartRefresh')  # time at next scr refresh
            RightHalf.setAutoDraw(True)
        
        # *Safe* updates
        if Safe.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Safe.frameNStart = frameN  # exact frame index
            Safe.tStart = t  # local t and not account for scr refresh
            Safe.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Safe, 'tStartRefresh')  # time at next scr refresh
            Safe.setAutoDraw(True)
        
        # *Top* updates
        if Top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Top.frameNStart = frameN  # exact frame index
            Top.tStart = t  # local t and not account for scr refresh
            Top.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Top, 'tStartRefresh')  # time at next scr refresh
            Top.setAutoDraw(True)
        
        # *Bottom* updates
        if Bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Bottom.frameNStart = frameN  # exact frame index
            Bottom.tStart = t  # local t and not account for scr refresh
            Bottom.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Bottom, 'tStartRefresh')  # time at next scr refresh
            Bottom.setAutoDraw(True)
        
        # *SafeText* updates
        if SafeText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            SafeText.frameNStart = frameN  # exact frame index
            SafeText.tStart = t  # local t and not account for scr refresh
            SafeText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(SafeText, 'tStartRefresh')  # time at next scr refresh
            SafeText.setAutoDraw(True)
        
        # *TopText* updates
        if TopText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TopText.frameNStart = frameN  # exact frame index
            TopText.tStart = t  # local t and not account for scr refresh
            TopText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TopText, 'tStartRefresh')  # time at next scr refresh
            TopText.setAutoDraw(True)
        
        # *BottomText* updates
        if BottomText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            BottomText.frameNStart = frameN  # exact frame index
            BottomText.tStart = t  # local t and not account for scr refresh
            BottomText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(BottomText, 'tStartRefresh')  # time at next scr refresh
            BottomText.setAutoDraw(True)
        
        # *Total* updates
        if Total.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Total.frameNStart = frameN  # exact frame index
            Total.tStart = t  # local t and not account for scr refresh
            Total.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Total, 'tStartRefresh')  # time at next scr refresh
            Total.setAutoDraw(True)
        
        # *Win* updates
        if Win.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Win.frameNStart = frameN  # exact frame index
            Win.tStart = t  # local t and not account for scr refresh
            Win.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Win, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Win.started')
            Win.setAutoDraw(True)
        
        # *Keys* updates
        waitOnFlip = False
        if Keys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Keys.frameNStart = frameN  # exact frame index
            Keys.tStart = t  # local t and not account for scr refresh
            Keys.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Keys, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Keys.started')
            Keys.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(Keys.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(Keys.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if Keys.status == STARTED and not waitOnFlip:
            theseKeys = Keys.getKeys(keyList=['left','right'], waitRelease=False)
            _Keys_allKeys.extend(theseKeys)
            if len(_Keys_allKeys):
                Keys.keys = _Keys_allKeys[-1].name  # just the last key pressed
                Keys.rt = _Keys_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # *Mouse* updates
        if Mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Mouse.frameNStart = frameN  # exact frame index
            Mouse.tStart = t  # local t and not account for scr refresh
            Mouse.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Mouse, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.addData('Mouse.started', t)
            Mouse.status = STARTED
            Mouse.mouseClock.reset()
            prevButtonState = Mouse.getPressed()  # if button is down already this ISN'T a new click
        if Mouse.status == STARTED:  # only update if started and not finished!
            buttons = Mouse.getPressed()
            if buttons != prevButtonState:  # button state changed?
                prevButtonState = buttons
                if sum(buttons) > 0:  # state changed to a new click
                    # check if the mouse was inside our 'clickable' objects
                    gotValidClick = False
                    try:
                        iter([RightHalf,LeftHalf])
                        clickableList = [RightHalf,LeftHalf]
                    except:
                        clickableList = [[RightHalf,LeftHalf]]
                    for obj in clickableList:
                        if obj.contains(Mouse):
                            gotValidClick = True
                            Mouse.clicked_name.append(obj.name)
                    if gotValidClick:  
                        continueRoutine = False  # abort routine on response
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in CueComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Cue" ---
    for thisComponent in CueComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if Keys.keys in ['', [], None]:  # No response was made
        Keys.keys = None
    trialControl.addData('Keys.keys',Keys.keys)
    if Keys.keys != None:  # we had a response
        trialControl.addData('Keys.rt', Keys.rt)
    # store data for trialControl (TrialHandler)
    x, y = Mouse.getPos()
    buttons = Mouse.getPressed()
    if sum(buttons):
        # check if the mouse was inside our 'clickable' objects
        gotValidClick = False
        try:
            iter([RightHalf,LeftHalf])
            clickableList = [RightHalf,LeftHalf]
        except:
            clickableList = [[RightHalf,LeftHalf]]
        for obj in clickableList:
            if obj.contains(Mouse):
                gotValidClick = True
                Mouse.clicked_name.append(obj.name)
    trialControl.addData('Mouse.x', x)
    trialControl.addData('Mouse.y', y)
    trialControl.addData('Mouse.leftButton', buttons[0])
    trialControl.addData('Mouse.midButton', buttons[1])
    trialControl.addData('Mouse.rightButton', buttons[2])
    if len(Mouse.clicked_name):
        trialControl.addData('Mouse.clicked_name', Mouse.clicked_name[0])
    # Run 'End Routine' code from countHowHappy
    if trialN  >= 3:
        trialN = 1
        doHowHappy = 1
    else:
        trialN +=1
        doHowHappy = 0
    # the Routine "Cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    revealLoop = data.TrialHandler(nReps=revealRoutines, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='revealLoop')
    thisExp.addLoop(revealLoop)  # add the loop to the experiment
    thisRevealLoop = revealLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisRevealLoop.rgb)
    if thisRevealLoop != None:
        for paramName in thisRevealLoop:
            exec('{} = thisRevealLoop[paramName]'.format(paramName))
    
    for thisRevealLoop in revealLoop:
        currentLoop = revealLoop
        # abbreviate parameter names if possible (e.g. rgb = thisRevealLoop.rgb)
        if thisRevealLoop != None:
            for paramName in thisRevealLoop:
                exec('{} = thisRevealLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Calculate" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from DetermineColor
        # This section is for the mouse selection
        # choose safe
        if (RiskSide=='right') and Mouse.isPressedIn(LeftHalf):
            safecolor = 'yellow'
            topcolor = 'black'
            bottomcolor = 'black'
            Gamble = False
            # choose gamble
        elif (RiskSide=='right') and Mouse.isPressedIn(RightHalf):
            safecolor = 'black'
            topcolor = 'yellow'
            bottomcolor = 'yellow'
            Gamble = True
            #choose gamble
        elif (RiskSide=='left') and Mouse.isPressedIn(LeftHalf):
            safecolor = 'black'
            topcolor = 'yellow'
            bottomcolor = 'yellow'
            Gamble = True
            # choose safe
        elif (RiskSide=='left') and Mouse.isPressedIn(RightHalf):
            safecolor = 'yellow'
            topcolor = 'black'
            bottomcolor = 'black'
            Gamble = False
            
            
        # This section is for the keyboard selection
        # choose safe
        if (RiskSide=='right') and event.getKeys(['left']):
            safecolor = 'yellow'
            topcolor = 'black'
            bottomcolor = 'black'
            Gamble = False
        # choose gamble
        elif (RiskSide=='right') and event.getKeys(['right']):
            safecolor = 'black'
            topcolor = 'yellow'
            bottomcolor = 'yellow'
            Gamble = True
         # choose gamble
        elif (RiskSide=='left') and event.getKeys(['left']):
            safecolor = 'black'
            topcolor = 'yellow'
            bottomcolor = 'yellow'
            Gamble = True
        # choose safe
        elif (RiskSide=='left') and event.getKeys(['right']):
            safecolor = 'yellow'
            topcolor = 'black'
            bottomcolor = 'black'
            Gamble = False
         # set the Gamble Outcome
        if Outcome == 'top':
            GambleAmt = TopAmt
            OtherAmt = BottomAmt
        else:
            GambleAmt = BottomAmt
            OtherAmt = TopAmt
        # Set Outcome for this trial   
        if Gamble:
            Change = GambleAmt
        else:
            Change = CertainAmt
            #only update total now if safebet
            total = total + Change     
            totalWin='Total\n$%0.2f'%(total)
        
            
        winColor = 'black'
        if Gamble:
            winText ='' #if chose Gamble - don't display anything (only want to show safebet here
        else:
            if Change > 0:
                winText ='You won $%0.2f!'%(Change)
               # winColor = 'green'
            elif Change == 0:
                winText ='You got $%0.2f!'%(Change)
              #  winColor = 'black'
            else:
                winText ='You lost $%0.2f!'%(Change)
               # winColor = 'red'
        
        
        # keep track of which components have finished
        CalculateComponents = []
        for thisComponent in CalculateComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Calculate" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in CalculateComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Calculate" ---
        for thisComponent in CalculateComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "Calculate" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "SelectionShown" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        Safe_2.setPos((safex,safey))
        Safe_2.setLineColor(safecolor)
        Top_2.setPos((gamblex, gambletop))
        Top_2.setLineColor(topcolor)
        Bottom_2.setPos((gamblex, gamblebottom))
        Bottom_2.setLineColor(bottomcolor)
        SafeText_2.setPos((safex, safey))
        SafeText_2.setText(certainAmt)
        TopText_2.setPos((gamblex, gambletop))
        TopText_2.setText(topAmt)
        BottomText_2.setPos((gamblex, gamblebottom))
        BottomText_2.setText(bottomAmt)
        Win_2.setText(totalWin)
        WinMsg.setColor(winColor, colorSpace='rgb')
        WinMsg.setPos((safex,winy))
        WinMsg.setText(winText)
        # keep track of which components have finished
        SelectionShownComponents = [LeftHalf_2, RightHalf_2, Safe_2, Top_2, Bottom_2, SafeText_2, TopText_2, BottomText_2, Total_2, Win_2, WinMsg]
        for thisComponent in SelectionShownComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "SelectionShown" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LeftHalf_2* updates
            if LeftHalf_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LeftHalf_2.frameNStart = frameN  # exact frame index
                LeftHalf_2.tStart = t  # local t and not account for scr refresh
                LeftHalf_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LeftHalf_2, 'tStartRefresh')  # time at next scr refresh
                LeftHalf_2.setAutoDraw(True)
            if LeftHalf_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LeftHalf_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    LeftHalf_2.tStop = t  # not accounting for scr refresh
                    LeftHalf_2.frameNStop = frameN  # exact frame index
                    LeftHalf_2.setAutoDraw(False)
            
            # *RightHalf_2* updates
            if RightHalf_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RightHalf_2.frameNStart = frameN  # exact frame index
                RightHalf_2.tStart = t  # local t and not account for scr refresh
                RightHalf_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RightHalf_2, 'tStartRefresh')  # time at next scr refresh
                RightHalf_2.setAutoDraw(True)
            if RightHalf_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RightHalf_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    RightHalf_2.tStop = t  # not accounting for scr refresh
                    RightHalf_2.frameNStop = frameN  # exact frame index
                    RightHalf_2.setAutoDraw(False)
            
            # *Safe_2* updates
            if Safe_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Safe_2.frameNStart = frameN  # exact frame index
                Safe_2.tStart = t  # local t and not account for scr refresh
                Safe_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Safe_2, 'tStartRefresh')  # time at next scr refresh
                Safe_2.setAutoDraw(True)
            if Safe_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Safe_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Safe_2.tStop = t  # not accounting for scr refresh
                    Safe_2.frameNStop = frameN  # exact frame index
                    Safe_2.setAutoDraw(False)
            
            # *Top_2* updates
            if Top_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Top_2.frameNStart = frameN  # exact frame index
                Top_2.tStart = t  # local t and not account for scr refresh
                Top_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Top_2, 'tStartRefresh')  # time at next scr refresh
                Top_2.setAutoDraw(True)
            if Top_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Top_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Top_2.tStop = t  # not accounting for scr refresh
                    Top_2.frameNStop = frameN  # exact frame index
                    Top_2.setAutoDraw(False)
            
            # *Bottom_2* updates
            if Bottom_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Bottom_2.frameNStart = frameN  # exact frame index
                Bottom_2.tStart = t  # local t and not account for scr refresh
                Bottom_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Bottom_2, 'tStartRefresh')  # time at next scr refresh
                Bottom_2.setAutoDraw(True)
            if Bottom_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Bottom_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Bottom_2.tStop = t  # not accounting for scr refresh
                    Bottom_2.frameNStop = frameN  # exact frame index
                    Bottom_2.setAutoDraw(False)
            
            # *SafeText_2* updates
            if SafeText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SafeText_2.frameNStart = frameN  # exact frame index
                SafeText_2.tStart = t  # local t and not account for scr refresh
                SafeText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SafeText_2, 'tStartRefresh')  # time at next scr refresh
                SafeText_2.setAutoDraw(True)
            if SafeText_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SafeText_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    SafeText_2.tStop = t  # not accounting for scr refresh
                    SafeText_2.frameNStop = frameN  # exact frame index
                    SafeText_2.setAutoDraw(False)
            
            # *TopText_2* updates
            if TopText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TopText_2.frameNStart = frameN  # exact frame index
                TopText_2.tStart = t  # local t and not account for scr refresh
                TopText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TopText_2, 'tStartRefresh')  # time at next scr refresh
                TopText_2.setAutoDraw(True)
            if TopText_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TopText_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    TopText_2.tStop = t  # not accounting for scr refresh
                    TopText_2.frameNStop = frameN  # exact frame index
                    TopText_2.setAutoDraw(False)
            
            # *BottomText_2* updates
            if BottomText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BottomText_2.frameNStart = frameN  # exact frame index
                BottomText_2.tStart = t  # local t and not account for scr refresh
                BottomText_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BottomText_2, 'tStartRefresh')  # time at next scr refresh
                BottomText_2.setAutoDraw(True)
            if BottomText_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BottomText_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    BottomText_2.tStop = t  # not accounting for scr refresh
                    BottomText_2.frameNStop = frameN  # exact frame index
                    BottomText_2.setAutoDraw(False)
            
            # *Total_2* updates
            if Total_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Total_2.frameNStart = frameN  # exact frame index
                Total_2.tStart = t  # local t and not account for scr refresh
                Total_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Total_2, 'tStartRefresh')  # time at next scr refresh
                Total_2.setAutoDraw(True)
            if Total_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Total_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Total_2.tStop = t  # not accounting for scr refresh
                    Total_2.frameNStop = frameN  # exact frame index
                    Total_2.setAutoDraw(False)
            
            # *Win_2* updates
            if Win_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Win_2.frameNStart = frameN  # exact frame index
                Win_2.tStart = t  # local t and not account for scr refresh
                Win_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Win_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Win_2.started')
                Win_2.setAutoDraw(True)
            if Win_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Win_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Win_2.tStop = t  # not accounting for scr refresh
                    Win_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Win_2.stopped')
                    Win_2.setAutoDraw(False)
            
            # *WinMsg* updates
            if WinMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WinMsg.frameNStart = frameN  # exact frame index
                WinMsg.tStart = t  # local t and not account for scr refresh
                WinMsg.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WinMsg, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'WinMsg.started')
                WinMsg.setAutoDraw(True)
            if WinMsg.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > WinMsg.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    WinMsg.tStop = t  # not accounting for scr refresh
                    WinMsg.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'WinMsg.stopped')
                    WinMsg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in SelectionShownComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "SelectionShown" ---
        for thisComponent in SelectionShownComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # Run 'End Routine' code from code
        if Gamble:
            if Change > 0:  #compare GambleAmt vs OtherAmt
                winText ='You won $%0.2f!'%(Change)
                winColor = 'limegreen'
            elif Change < 0:
                winText ='You lost $%0.2f!'%(Change)
                winColor = 'red'
            else: #change, i.e. gambleamt = 0
                if GambleAmt > OtherAmt: #compare GambleAmt vs OtherAmt
                    winText ='You won $%0.2f!'%(Change)
                    winColor = 'limegreen'
                elif GambleAmt < OtherAmt:
                    winText ='You lost $%0.2f!'%(Change)
                    winColor = 'red'
                else:
                    winText = 'how did you get here? $%0.2f!'%(GambleAmt)
                    winColor = 'magenta'
        else:
            if (GambleAmt > CertainAmt):
                safecolor = 'red'
                winText ='You would have won $%0.2f!'%(GambleAmt)
                winColor = 'red'
            else:
                safecolor = 'limegreen'
                winText ='You would have lost $%0.2f!'%(GambleAmt)
                winColor = 'limegreen'
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # --- Prepare to start Routine "GambleRevealed" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from RevealGamble
        #if Gamble: #skip click error is small
        #    continueRoutine = False
        
        if Gamble:
        #if chose Gamble:
            #add outcome to total:
            total = total + Change     
            totalWin='Total\n$%0.2f'%(total)
            if (Outcome=='top') and (TopAmt>BottomAmt):
                #gamble top was a win
                topcolor = 'limegreen'
                bottomcolor = 'black'
            elif (Outcome=='top') and (TopAmt<BottomAmt):
                #gamble top resulted in loss
                topcolor = 'red'
                bottomcolor = 'black'
            elif (Outcome=='bottom') and (BottomAmt>TopAmt):
                #gamble bottom was a win
                topcolor = 'black'
                bottomcolor = 'limegreen'
            elif (Outcome=='bottom') and (BottomAmt<TopAmt):
                #gamble bottom resulted in loss
                topcolor = 'black'
                bottomcolor = 'red'
        else:
        #if chose safebet : purple and black
            if (Outcome=='top'):
                #gamble top was a win
                topcolor = 'mediumorchid'
                bottomcolor = 'black'
            else:
                #gamble bottom was a win
                topcolor = 'black'
                bottomcolor = 'mediumorchid'
        
        Safe_3.setPos((safex,safey))
        Safe_3.setLineColor(safecolor)
        Top_3.setPos((gamblex, gambletop))
        Top_3.setLineColor(topcolor)
        Bottom_3.setPos((gamblex, gamblebottom))
        Bottom_3.setLineColor(bottomcolor)
        SafeText_3.setPos((safex, safey))
        SafeText_3.setText(certainAmt)
        TopText_3.setPos((gamblex, gambletop))
        TopText_3.setText(topAmt)
        BottomText_3.setPos((gamblex, gamblebottom))
        BottomText_3.setText(bottomAmt)
        Win_3.setText(totalWin)
        WinMsg_2.setColor(winColor, colorSpace='rgb')
        WinMsg_2.setPos((gamblex,0))
        WinMsg_2.setText(winText)
        # keep track of which components have finished
        GambleRevealedComponents = [LeftHalf_3, RightHalf_3, Safe_3, Top_3, Bottom_3, SafeText_3, TopText_3, BottomText_3, Total_3, Win_3, WinMsg_2]
        for thisComponent in GambleRevealedComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "GambleRevealed" ---
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *LeftHalf_3* updates
            if LeftHalf_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                LeftHalf_3.frameNStart = frameN  # exact frame index
                LeftHalf_3.tStart = t  # local t and not account for scr refresh
                LeftHalf_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(LeftHalf_3, 'tStartRefresh')  # time at next scr refresh
                LeftHalf_3.setAutoDraw(True)
            if LeftHalf_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > LeftHalf_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    LeftHalf_3.tStop = t  # not accounting for scr refresh
                    LeftHalf_3.frameNStop = frameN  # exact frame index
                    LeftHalf_3.setAutoDraw(False)
            
            # *RightHalf_3* updates
            if RightHalf_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                RightHalf_3.frameNStart = frameN  # exact frame index
                RightHalf_3.tStart = t  # local t and not account for scr refresh
                RightHalf_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(RightHalf_3, 'tStartRefresh')  # time at next scr refresh
                RightHalf_3.setAutoDraw(True)
            if RightHalf_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > RightHalf_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    RightHalf_3.tStop = t  # not accounting for scr refresh
                    RightHalf_3.frameNStop = frameN  # exact frame index
                    RightHalf_3.setAutoDraw(False)
            
            # *Safe_3* updates
            if Safe_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Safe_3.frameNStart = frameN  # exact frame index
                Safe_3.tStart = t  # local t and not account for scr refresh
                Safe_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Safe_3, 'tStartRefresh')  # time at next scr refresh
                Safe_3.setAutoDraw(True)
            if Safe_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Safe_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Safe_3.tStop = t  # not accounting for scr refresh
                    Safe_3.frameNStop = frameN  # exact frame index
                    Safe_3.setAutoDraw(False)
            
            # *Top_3* updates
            if Top_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Top_3.frameNStart = frameN  # exact frame index
                Top_3.tStart = t  # local t and not account for scr refresh
                Top_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Top_3, 'tStartRefresh')  # time at next scr refresh
                Top_3.setAutoDraw(True)
            if Top_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Top_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Top_3.tStop = t  # not accounting for scr refresh
                    Top_3.frameNStop = frameN  # exact frame index
                    Top_3.setAutoDraw(False)
            
            # *Bottom_3* updates
            if Bottom_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Bottom_3.frameNStart = frameN  # exact frame index
                Bottom_3.tStart = t  # local t and not account for scr refresh
                Bottom_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Bottom_3, 'tStartRefresh')  # time at next scr refresh
                Bottom_3.setAutoDraw(True)
            if Bottom_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Bottom_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Bottom_3.tStop = t  # not accounting for scr refresh
                    Bottom_3.frameNStop = frameN  # exact frame index
                    Bottom_3.setAutoDraw(False)
            
            # *SafeText_3* updates
            if SafeText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                SafeText_3.frameNStart = frameN  # exact frame index
                SafeText_3.tStart = t  # local t and not account for scr refresh
                SafeText_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SafeText_3, 'tStartRefresh')  # time at next scr refresh
                SafeText_3.setAutoDraw(True)
            if SafeText_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > SafeText_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    SafeText_3.tStop = t  # not accounting for scr refresh
                    SafeText_3.frameNStop = frameN  # exact frame index
                    SafeText_3.setAutoDraw(False)
            
            # *TopText_3* updates
            if TopText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TopText_3.frameNStart = frameN  # exact frame index
                TopText_3.tStart = t  # local t and not account for scr refresh
                TopText_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TopText_3, 'tStartRefresh')  # time at next scr refresh
                TopText_3.setAutoDraw(True)
            if TopText_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TopText_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    TopText_3.tStop = t  # not accounting for scr refresh
                    TopText_3.frameNStop = frameN  # exact frame index
                    TopText_3.setAutoDraw(False)
            
            # *BottomText_3* updates
            if BottomText_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                BottomText_3.frameNStart = frameN  # exact frame index
                BottomText_3.tStart = t  # local t and not account for scr refresh
                BottomText_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(BottomText_3, 'tStartRefresh')  # time at next scr refresh
                BottomText_3.setAutoDraw(True)
            if BottomText_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > BottomText_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    BottomText_3.tStop = t  # not accounting for scr refresh
                    BottomText_3.frameNStop = frameN  # exact frame index
                    BottomText_3.setAutoDraw(False)
            
            # *Total_3* updates
            if Total_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Total_3.frameNStart = frameN  # exact frame index
                Total_3.tStart = t  # local t and not account for scr refresh
                Total_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Total_3, 'tStartRefresh')  # time at next scr refresh
                Total_3.setAutoDraw(True)
            if Total_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Total_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Total_3.tStop = t  # not accounting for scr refresh
                    Total_3.frameNStop = frameN  # exact frame index
                    Total_3.setAutoDraw(False)
            
            # *Win_3* updates
            if Win_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Win_3.frameNStart = frameN  # exact frame index
                Win_3.tStart = t  # local t and not account for scr refresh
                Win_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Win_3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Win_3.started')
                Win_3.setAutoDraw(True)
            if Win_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > Win_3.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    Win_3.tStop = t  # not accounting for scr refresh
                    Win_3.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Win_3.stopped')
                    Win_3.setAutoDraw(False)
            
            # *WinMsg_2* updates
            if WinMsg_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                WinMsg_2.frameNStart = frameN  # exact frame index
                WinMsg_2.tStart = t  # local t and not account for scr refresh
                WinMsg_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(WinMsg_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'WinMsg_2.started')
                WinMsg_2.setAutoDraw(True)
            if WinMsg_2.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > WinMsg_2.tStartRefresh + 2.0-frameTolerance:
                    # keep track of stop time/frame for later
                    WinMsg_2.tStop = t  # not accounting for scr refresh
                    WinMsg_2.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'WinMsg_2.stopped')
                    WinMsg_2.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in GambleRevealedComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "GambleRevealed" ---
        for thisComponent in GambleRevealedComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
    # completed revealRoutines repeats of 'revealLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    timeoutLoop = data.TrialHandler(nReps=timeoutRoutine, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='timeoutLoop')
    thisExp.addLoop(timeoutLoop)  # add the loop to the experiment
    thisTimeoutLoop = timeoutLoop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTimeoutLoop.rgb)
    if thisTimeoutLoop != None:
        for paramName in thisTimeoutLoop:
            exec('{} = thisTimeoutLoop[paramName]'.format(paramName))
    
    for thisTimeoutLoop in timeoutLoop:
        currentLoop = timeoutLoop
        # abbreviate parameter names if possible (e.g. rgb = thisTimeoutLoop.rgb)
        if thisTimeoutLoop != None:
            for paramName in thisTimeoutLoop:
                exec('{} = thisTimeoutLoop[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "Timeout" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # keep track of which components have finished
        TimeoutComponents = [timeoutText]
        for thisComponent in TimeoutComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Timeout" ---
        while continueRoutine and routineTimer.getTime() < 8.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *timeoutText* updates
            if timeoutText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                timeoutText.frameNStart = frameN  # exact frame index
                timeoutText.tStart = t  # local t and not account for scr refresh
                timeoutText.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(timeoutText, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'timeoutText.started')
                timeoutText.setAutoDraw(True)
            if timeoutText.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > timeoutText.tStartRefresh + 8.0-frameTolerance:
                    # keep track of stop time/frame for later
                    timeoutText.tStop = t  # not accounting for scr refresh
                    timeoutText.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'timeoutText.stopped')
                    timeoutText.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TimeoutComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Timeout" ---
        for thisComponent in TimeoutComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-8.000000)
    # completed timeoutRoutine repeats of 'timeoutLoop'
    
    
    # set up handler to look after randomisation of conditions etc
    HowHappyCheck = data.TrialHandler(nReps=doHowHappy, method='random', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
        seed=None, name='HowHappyCheck')
    thisExp.addLoop(HowHappyCheck)  # add the loop to the experiment
    thisHowHappyCheck = HowHappyCheck.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisHowHappyCheck.rgb)
    if thisHowHappyCheck != None:
        for paramName in thisHowHappyCheck:
            exec('{} = thisHowHappyCheck[paramName]'.format(paramName))
    
    for thisHowHappyCheck in HowHappyCheck:
        currentLoop = HowHappyCheck
        # abbreviate parameter names if possible (e.g. rgb = thisHowHappyCheck.rgb)
        if thisHowHappyCheck != None:
            for paramName in thisHowHappyCheck:
                exec('{} = thisHowHappyCheck[paramName]'.format(paramName))
        
        # --- Prepare to start Routine "HowHappy" ---
        continueRoutine = True
        routineForceEnded = False
        # update component parameters for each repeat
        # Run 'Begin Routine' code from ShowSlider
        #if Rating == 0:
        #    continueRoutine = False
        
        
        HowHappySlider.marker.size=(.05,.05)
        HowHappySlider.reset()
        SliderKeyboard.keys = []
        SliderKeyboard.rt = []
        _SliderKeyboard_allKeys = []
        # keep track of which components have finished
        HowHappyComponents = [HowHappySlider, UnHappy, Happy, SliderKeyboard, SpacetoExit]
        for thisComponent in HowHappyComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "HowHappy" ---
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *HowHappySlider* updates
            if HowHappySlider.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                HowHappySlider.frameNStart = frameN  # exact frame index
                HowHappySlider.tStart = t  # local t and not account for scr refresh
                HowHappySlider.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(HowHappySlider, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'HowHappySlider.started')
                HowHappySlider.setAutoDraw(True)
            
            # *UnHappy* updates
            if UnHappy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                UnHappy.frameNStart = frameN  # exact frame index
                UnHappy.tStart = t  # local t and not account for scr refresh
                UnHappy.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(UnHappy, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'UnHappy.started')
                UnHappy.setAutoDraw(True)
            
            # *Happy* updates
            if Happy.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Happy.frameNStart = frameN  # exact frame index
                Happy.tStart = t  # local t and not account for scr refresh
                Happy.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Happy, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Happy.started')
                Happy.setAutoDraw(True)
            
            # *SliderKeyboard* updates
            waitOnFlip = False
            if SliderKeyboard.status == NOT_STARTED and HowHappySlider.getRating():
                # keep track of start time/frame for later
                SliderKeyboard.frameNStart = frameN  # exact frame index
                SliderKeyboard.tStart = t  # local t and not account for scr refresh
                SliderKeyboard.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SliderKeyboard, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SliderKeyboard.started')
                SliderKeyboard.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(SliderKeyboard.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(SliderKeyboard.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if SliderKeyboard.status == STARTED and not waitOnFlip:
                theseKeys = SliderKeyboard.getKeys(keyList=['space'], waitRelease=False)
                _SliderKeyboard_allKeys.extend(theseKeys)
                if len(_SliderKeyboard_allKeys):
                    SliderKeyboard.keys = _SliderKeyboard_allKeys[-1].name  # just the last key pressed
                    SliderKeyboard.rt = _SliderKeyboard_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # *SpacetoExit* updates
            if SpacetoExit.status == NOT_STARTED and HowHappySlider.rating:
                # keep track of start time/frame for later
                SpacetoExit.frameNStart = frameN  # exact frame index
                SpacetoExit.tStart = t  # local t and not account for scr refresh
                SpacetoExit.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(SpacetoExit, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'SpacetoExit.started')
                SpacetoExit.setAutoDraw(True)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in HowHappyComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "HowHappy" ---
        for thisComponent in HowHappyComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        HowHappyCheck.addData('HowHappySlider.response', HowHappySlider.getRating())
        HowHappyCheck.addData('HowHappySlider.rt', HowHappySlider.getRT())
        # check responses
        if SliderKeyboard.keys in ['', [], None]:  # No response was made
            SliderKeyboard.keys = None
        HowHappyCheck.addData('SliderKeyboard.keys',SliderKeyboard.keys)
        if SliderKeyboard.keys != None:  # we had a response
            HowHappyCheck.addData('SliderKeyboard.rt', SliderKeyboard.rt)
        # the Routine "HowHappy" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed doHowHappy repeats of 'HowHappyCheck'
    
    
    # --- Prepare to start Routine "Fixation" ---
    continueRoutine = True
    routineForceEnded = False
    # update component parameters for each repeat
    # keep track of which components have finished
    FixationComponents = [Cross]
    for thisComponent in FixationComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Fixation" ---
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Cross* updates
        if Cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Cross.frameNStart = frameN  # exact frame index
            Cross.tStart = t  # local t and not account for scr refresh
            Cross.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Cross, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Cross.started')
            Cross.setAutoDraw(True)
        if Cross.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > Cross.tStartRefresh + ITI-frameTolerance:
                # keep track of stop time/frame for later
                Cross.tStop = t  # not accounting for scr refresh
                Cross.frameNStop = frameN  # exact frame index
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Cross.stopped')
                Cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in FixationComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Fixation" ---
    for thisComponent in FixationComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'trialControl'


# --- Prepare to start Routine "ThankYou" ---
continueRoutine = True
routineForceEnded = False
# update component parameters for each repeat
# keep track of which components have finished
ThankYouComponents = [exitText]
for thisComponent in ThankYouComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
frameN = -1

# --- Run Routine "ThankYou" ---
while continueRoutine and routineTimer.getTime() < 5.0:
    # get current time
    t = routineTimer.getTime()
    tThisFlip = win.getFutureFlipTime(clock=routineTimer)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *exitText* updates
    if exitText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        exitText.frameNStart = frameN  # exact frame index
        exitText.tStart = t  # local t and not account for scr refresh
        exitText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(exitText, 'tStartRefresh')  # time at next scr refresh
        # add timestamp to datafile
        thisExp.timestampOnFlip(win, 'exitText.started')
        exitText.setAutoDraw(True)
    if exitText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > exitText.tStartRefresh + 5.0-frameTolerance:
            # keep track of stop time/frame for later
            exitText.tStop = t  # not accounting for scr refresh
            exitText.frameNStop = frameN  # exact frame index
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'exitText.stopped')
            exitText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        routineForceEnded = True
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in ThankYouComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# --- Ending Routine "ThankYou" ---
for thisComponent in ThankYouComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
if routineForceEnded:
    routineTimer.reset()
else:
    routineTimer.addTime(-5.000000)

# --- End experiment ---
# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
