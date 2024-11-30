#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2021.2.0),
    on July 16, 2021, at 11:29
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

from psychopy.hardware import keyboard



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '2021.2.0'
expName = 'stroop2'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='G:\\Shared drives\\Science\\books\\BuildingExperiments_Ed2\\materials\\exercise - solutions\\7.2 showProgress\\stroop_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Setup eyetracking
ioDevice = ioConfig = ioSession = ioServer = eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instructPractice"
instructPracticeClock = core.Clock()
instructsPracText = visual.TextBox2(
     win, text='When the words appear, press: \n\n  Left for red LETTERS \n  Down for green LETTERS \n  Right for blue LETTERS (Esc will quit)\n\nPress any key to continue', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instructsPracText',
     autoLog=True,
)
readyInstructs = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
stim = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='stim',
     autoLog=True,
)
resp = keyboard.Keyboard()
progresstext = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0.4, 0.4),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='progresstext',
     autoLog=True,
)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
corr = []
feedbackMsg = visual.TextBox2(
     win, text='', font='Arial',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='feedbackMsg',
     autoLog=True,
)

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instrText = visual.TextBox2(
     win, text='OK. Ready for the real thing?\n\nRemember, ignore the word itself; press:\nLeft for red LETTERS\nDown for green LETTERS\nRight for blue LETTERS\n(Esc will quit)\n\nPress any key to continue', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='instrText',
     autoLog=True,
)
ready = keyboard.Keyboard()

# Initialize components for Routine "trial"
trialClock = core.Clock()
stim = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='stim',
     autoLog=True,
)
resp = keyboard.Keyboard()
progresstext = visual.TextBox2(
     win, text='', font='Open Sans',
     pos=(0.4, 0.4),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='progresstext',
     autoLog=True,
)

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextBox2(
     win, text='This is the end of the experiment.\n\nThanks!', font='Open Sans',
     pos=(0, 0),     letterHeight=0.05,
     size=(None, None), borderWidth=2.0,
     color='white', colorSpace='rgb',
     opacity=None,
     bold=False, italic=False,
     lineSpacing=1.0,
     padding=0.0,
     anchor='center',
     fillColor=None, borderColor=None,
     flipHoriz=False, flipVert=False,
     editable=False,
     name='thanksText',
     autoLog=True,
)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructPractice"-------
continueRoutine = True
# update component parameters for each repeat
instructsPracText.reset()
readyInstructs.keys = []
readyInstructs.rt = []
_readyInstructs_allKeys = []
# keep track of which components have finished
instructPracticeComponents = [instructsPracText, readyInstructs]
for thisComponent in instructPracticeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructPracticeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instructPractice"-------
while continueRoutine:
    # get current time
    t = instructPracticeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructPracticeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instructsPracText* updates
    if instructsPracText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instructsPracText.frameNStart = frameN  # exact frame index
        instructsPracText.tStart = t  # local t and not account for scr refresh
        instructsPracText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instructsPracText, 'tStartRefresh')  # time at next scr refresh
        instructsPracText.setAutoDraw(True)
    
    # *readyInstructs* updates
    waitOnFlip = False
    if readyInstructs.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        readyInstructs.frameNStart = frameN  # exact frame index
        readyInstructs.tStart = t  # local t and not account for scr refresh
        readyInstructs.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(readyInstructs, 'tStartRefresh')  # time at next scr refresh
        readyInstructs.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(readyInstructs.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(readyInstructs.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if readyInstructs.status == STARTED and not waitOnFlip:
        theseKeys = readyInstructs.getKeys(keyList=None, waitRelease=False)
        _readyInstructs_allKeys.extend(theseKeys)
        if len(_readyInstructs_allKeys):
            readyInstructs.keys = _readyInstructs_allKeys[-1].name  # just the last key pressed
            readyInstructs.rt = _readyInstructs_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instructPractice"-------
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instructsPracText.started', instructsPracText.tStartRefresh)
thisExp.addData('instructsPracText.stopped', instructsPracText.tStopRefresh)
# check responses
if readyInstructs.keys in ['', [], None]:  # No response was made
    readyInstructs.keys = None
thisExp.addData('readyInstructs.keys',readyInstructs.keys)
if readyInstructs.keys != None:  # we had a response
    thisExp.addData('readyInstructs.rt', readyInstructs.rt)
thisExp.addData('readyInstructs.started', readyInstructs.tStartRefresh)
thisExp.addData('readyInstructs.stopped', readyInstructs.tStopRefresh)
thisExp.nextEntry()
# the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=2.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    stim.reset()
    stim.setColor(letterColor, colorSpace='rgb')
    stim.setText(text)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    progresstext.reset()
    progresstext.setText(str(currentLoop.thisN)+ "/" + str(currentLoop.nTotal))
    # keep track of which components have finished
    trialComponents = [stim, resp, progresstext]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim* updates
        if stim.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim.frameNStart = frameN  # exact frame index
            stim.tStart = t  # local t and not account for scr refresh
            stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
            stim.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *progresstext* updates
        if progresstext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progresstext.frameNStart = frameN  # exact frame index
            progresstext.tStart = t  # local t and not account for scr refresh
            progresstext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progresstext, 'tStartRefresh')  # time at next scr refresh
            progresstext.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('stim.started', stim.tStartRefresh)
    practice.addData('stim.stopped', stim.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for practice (TrialHandler)
    practice.addData('resp.keys',resp.keys)
    practice.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        practice.addData('resp.rt', resp.rt)
    practice.addData('resp.started', resp.tStartRefresh)
    practice.addData('resp.stopped', resp.tStopRefresh)
    practice.addData('progresstext.started', progresstext.tStartRefresh)
    practice.addData('progresstext.stopped', progresstext.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:  # stored on last run routine
      msg="Correct! RT= " + str(round(resp.rt, 3))
    else:
      msg="Oops! That was wrong"
      
    # track (up to) the last 5 trials
    corr.append(resp.corr)
    nCorr = sum(corr[-5:])
    nResps = len(corr[-5:])
    msg += '\n'+str(nCorr) + ' out of ' + str(nResps) + ' correct.'
    
    if nCorr >= 4:
      practice.finished = True
    feedbackMsg.reset()
    feedbackMsg.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedbackMsg]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *feedbackMsg* updates
        if feedbackMsg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedbackMsg.frameNStart = frameN  # exact frame index
            feedbackMsg.tStart = t  # local t and not account for scr refresh
            feedbackMsg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
            feedbackMsg.setAutoDraw(True)
        if feedbackMsg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedbackMsg.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                feedbackMsg.tStop = t  # not accounting for scr refresh
                feedbackMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
                feedbackMsg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
    practice.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
    thisExp.nextEntry()
    
# completed 2.0 repeats of 'practice'


# ------Prepare to start Routine "instruct"-------
continueRoutine = True
# update component parameters for each repeat
instrText.reset()
ready.keys = []
ready.rt = []
_ready_allKeys = []
# keep track of which components have finished
instructComponents = [instrText, ready]
for thisComponent in instructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
instructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=instructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if instrText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        instrText.frameNStart = frameN  # exact frame index
        instrText.tStart = t  # local t and not account for scr refresh
        instrText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(instrText, 'tStartRefresh')  # time at next scr refresh
        instrText.setAutoDraw(True)
    
    # *ready* updates
    waitOnFlip = False
    if ready.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ready.frameNStart = frameN  # exact frame index
        ready.tStart = t  # local t and not account for scr refresh
        ready.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
        ready.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(ready.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(ready.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if ready.status == STARTED and not waitOnFlip:
        theseKeys = ready.getKeys(keyList=None, waitRelease=False)
        _ready_allKeys.extend(theseKeys)
        if len(_ready_allKeys):
            ready.keys = _ready_allKeys[-1].name  # just the last key pressed
            ready.rt = _ready_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('instrText.started', instrText.tStartRefresh)
thisExp.addData('instrText.stopped', instrText.tStopRefresh)
# check responses
if ready.keys in ['', [], None]:  # No response was made
    ready.keys = None
thisExp.addData('ready.keys',ready.keys)
if ready.keys != None:  # we had a response
    thisExp.addData('ready.rt', ready.rt)
thisExp.addData('ready.started', ready.tStartRefresh)
thisExp.addData('ready.stopped', ready.tStopRefresh)
thisExp.nextEntry()
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=5.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('trialTypes.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "trial"-------
    continueRoutine = True
    # update component parameters for each repeat
    stim.reset()
    stim.setColor(letterColor, colorSpace='rgb')
    stim.setText(text)
    resp.keys = []
    resp.rt = []
    _resp_allKeys = []
    progresstext.reset()
    progresstext.setText(str(currentLoop.thisN)+ "/" + str(currentLoop.nTotal))
    # keep track of which components have finished
    trialComponents = [stim, resp, progresstext]
    for thisComponent in trialComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    trialClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=trialClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *stim* updates
        if stim.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            stim.frameNStart = frameN  # exact frame index
            stim.tStart = t  # local t and not account for scr refresh
            stim.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(stim, 'tStartRefresh')  # time at next scr refresh
            stim.setAutoDraw(True)
        
        # *resp* updates
        waitOnFlip = False
        if resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
            # keep track of start time/frame for later
            resp.frameNStart = frameN  # exact frame index
            resp.tStart = t  # local t and not account for scr refresh
            resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(resp, 'tStartRefresh')  # time at next scr refresh
            resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if resp.status == STARTED and not waitOnFlip:
            theseKeys = resp.getKeys(keyList=['left', 'down', 'right'], waitRelease=False)
            _resp_allKeys.extend(theseKeys)
            if len(_resp_allKeys):
                resp.keys = _resp_allKeys[-1].name  # just the last key pressed
                resp.rt = _resp_allKeys[-1].rt
                # was this correct?
                if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                    resp.corr = 1
                else:
                    resp.corr = 0
                # a response ends the routine
                continueRoutine = False
        
        # *progresstext* updates
        if progresstext.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            progresstext.frameNStart = frameN  # exact frame index
            progresstext.tStart = t  # local t and not account for scr refresh
            progresstext.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(progresstext, 'tStartRefresh')  # time at next scr refresh
            progresstext.setAutoDraw(True)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('stim.started', stim.tStartRefresh)
    trials.addData('stim.stopped', stim.tStopRefresh)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys = None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1;  # correct non-response
        else:
           resp.corr = 0;  # failed to respond (incorrectly)
    # store data for trials (TrialHandler)
    trials.addData('resp.keys',resp.keys)
    trials.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trials.addData('resp.rt', resp.rt)
    trials.addData('resp.started', resp.tStartRefresh)
    trials.addData('resp.stopped', resp.tStopRefresh)
    trials.addData('progresstext.started', progresstext.tStartRefresh)
    trials.addData('progresstext.stopped', progresstext.tStopRefresh)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 5.0 repeats of 'trials'


# ------Prepare to start Routine "thanks"-------
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
thanksText.reset()
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
thanksClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=thanksClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if thanksText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.tStart = t  # local t and not account for scr refresh
        thanksText.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(thanksText, 'tStartRefresh')  # time at next scr refresh
        thanksText.setAutoDraw(True)
    if thanksText.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > thanksText.tStartRefresh + 2-frameTolerance:
            # keep track of stop time/frame for later
            thanksText.tStop = t  # not accounting for scr refresh
            thanksText.frameNStop = frameN  # exact frame index
            win.timeOnFlip(thanksText, 'tStopRefresh')  # time at next scr refresh
            thanksText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('thanksText.started', thanksText.tStartRefresh)
thisExp.addData('thanksText.stopped', thanksText.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
