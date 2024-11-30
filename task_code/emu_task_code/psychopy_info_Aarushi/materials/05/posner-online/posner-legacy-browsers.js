/*************** 
 * Posner Test *
 ***************/

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height',
  waitBlanking: true
});

// store info about the experiment session:
let expName = 'posner';  // from the Builder filename that created this script
let expInfo = {'session': '001', 'participant': ''};

// Start code blocks for 'Before Experiment'
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructRoutineBegin());
flowScheduler.add(instructRoutineEachFrame());
flowScheduler.add(instructRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(thanksRoutineBegin());
flowScheduler.add(thanksRoutineEachFrame());
flowScheduler.add(thanksRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'conditions.xlsx', 'path': 'conditions.xlsx'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2021.1.4';
  expInfo['OS'] = window.navigator.platform;

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}


var instructClock;
var instructText;
var instructEnd;
var ITIClock;
var fixationITI;
var trialClock;
var cue;
var target;
var key_resp_2;
var thanksClock;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruct"
  instructClock = new util.Clock();
  instructText = new visual.TextStim({
    win: psychoJS.window,
    name: 'instructText',
    text: "Press the left and right keys as\nto indicate the side where\nyou saw the green square.\n\nTry to respond as quickly and accurately as you can.\n\nPress any key when you're ready to start",
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  instructEnd = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI"
  ITIClock = new util.Clock();
  fixationITI = new visual.ShapeStim ({
    win: psychoJS.window, name: 'fixationITI', units : 'height', 
    vertices: 'cross', size:[0.05, 0.05],
    ori: 0, pos: [0, 0],
    lineWidth: 2, lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  cue = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cue', units : 'height', 
    vertices: [[-[0.2, 0.2][0]/2.0, -[0.2, 0.2][1]/2.0], [+[0.2, 0.2][0]/2.0, -[0.2, 0.2][1]/2.0], [0, [0.2, 0.2][1]/2.0]],
    ori: 1.0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: 0, interpolate: true,
  });
  
  target = new visual.Rect ({
    win: psychoJS.window, name: 'target', units : 'height', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color('SeaGreen'),
    fillColor: new util.Color('MediumSeaGreen'),
    opacity: 1, depth: -1, interpolate: true,
  });
  
  key_resp_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "thanks"
  thanksClock = new util.Clock();
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _instructEnd_allKeys;
var instructComponents;
function instructRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'instruct'-------
    t = 0;
    instructClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    instructEnd.keys = undefined;
    instructEnd.rt = undefined;
    _instructEnd_allKeys = [];
    // keep track of which components have finished
    instructComponents = [];
    instructComponents.push(instructText);
    instructComponents.push(instructEnd);
    
    instructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instructRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'instruct'-------
    // get current time
    t = instructClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *instructText* updates
    if (t >= 0.0 && instructText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructText.tStart = t;  // (not accounting for frame time here)
      instructText.frameNStart = frameN;  // exact frame index
      
      instructText.setAutoDraw(true);
    }

    
    // *instructEnd* updates
    if (t >= 0.0 && instructEnd.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      instructEnd.tStart = t;  // (not accounting for frame time here)
      instructEnd.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { instructEnd.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { instructEnd.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { instructEnd.clearEvents(); });
    }

    if (instructEnd.status === PsychoJS.Status.STARTED) {
      let theseKeys = instructEnd.getKeys({keyList: [], waitRelease: false});
      _instructEnd_allKeys = _instructEnd_allKeys.concat(theseKeys);
      if (_instructEnd_allKeys.length > 0) {
        instructEnd.keys = _instructEnd_allKeys[_instructEnd_allKeys.length - 1].name;  // just the last key pressed
        instructEnd.rt = _instructEnd_allKeys[_instructEnd_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instructComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instructRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'instruct'-------
    instructComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    instructEnd.stop();
    // the Routine "instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var trials;
var currentLoop;
function trialsLoopBegin(trialsLoopScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 5, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'conditions.xlsx',
    seed: undefined, name: 'trials'
  });
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment
  currentLoop = trials;  // we're now the current loop

  // Schedule all the trials in the trialList:
  trials.forEach(function() {
    const snapshot = trials.getSnapshot();

    trialsLoopScheduler.add(importConditions(snapshot));
    trialsLoopScheduler.add(ITIRoutineBegin(snapshot));
    trialsLoopScheduler.add(ITIRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(ITIRoutineEnd(snapshot));
    trialsLoopScheduler.add(trialRoutineBegin(snapshot));
    trialsLoopScheduler.add(trialRoutineEachFrame(snapshot));
    trialsLoopScheduler.add(trialRoutineEnd(snapshot));
    trialsLoopScheduler.add(endLoopIteration(trialsLoopScheduler, snapshot));
  });

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}


var ITIComponents;
function ITIRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'ITI'-------
    t = 0;
    ITIClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    ITIComponents = [];
    ITIComponents.push(fixationITI);
    
    ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ITIRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'ITI'-------
    // get current time
    t = ITIClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *fixationITI* updates
    if (t >= 0.0 && fixationITI.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      fixationITI.tStart = t;  // (not accounting for frame time here)
      fixationITI.frameNStart = frameN;  // exact frame index
      
      fixationITI.setAutoDraw(true);
    }

    frameRemains = 0.0 + (Math.random() + 1) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (fixationITI.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      fixationITI.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ITIComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITIRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'ITI'-------
    ITIComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "ITI" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var _key_resp_2_allKeys;
var trialComponents;
function trialRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'trial'-------
    t = 0;
    trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    cue.setOri(cueOri);
    target.setPos([targetX, 0]);
    key_resp_2.keys = undefined;
    key_resp_2.rt = undefined;
    _key_resp_2_allKeys = [];
    // keep track of which components have finished
    trialComponents = [];
    trialComponents.push(cue);
    trialComponents.push(target);
    trialComponents.push(key_resp_2);
    
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'trial'-------
    // get current time
    t = trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cue* updates
    if (t >= 0.0 && cue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cue.tStart = t;  // (not accounting for frame time here)
      cue.frameNStart = frameN;  // exact frame index
      
      cue.setAutoDraw(true);
    }

    if (cue.status === PsychoJS.Status.STARTED && frameN >= (cue.frameNStart + 12)) {
      cue.setAutoDraw(false);
    }
    
    // *target* updates
    if (frameN >= 12 && target.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      target.tStart = t;  // (not accounting for frame time here)
      target.frameNStart = frameN;  // exact frame index
      
      target.setAutoDraw(true);
    }

    if (target.status === PsychoJS.Status.STARTED && t >= (target.tStart + 1.0)) {
      target.setAutoDraw(false);
    }
    
    // *key_resp_2* updates
    if (frameN >= 12 && key_resp_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp_2.tStart = t;  // (not accounting for frame time here)
      key_resp_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp_2.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp_2.clearEvents(); });
    }

    if (key_resp_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp_2.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _key_resp_2_allKeys = _key_resp_2_allKeys.concat(theseKeys);
      if (_key_resp_2_allKeys.length > 0) {
        key_resp_2.keys = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].name;  // just the last key pressed
        key_resp_2.rt = _key_resp_2_allKeys[_key_resp_2_allKeys.length - 1].rt;
        // was this correct?
        if (key_resp_2.keys == corrAns) {
            key_resp_2.corr = 1;
        } else {
            key_resp_2.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function trialRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'trial'-------
    trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (key_resp_2.keys === undefined) {
      if (['None','none',undefined].includes(corrAns)) {
         key_resp_2.corr = 1;  // correct non-response
      } else {
         key_resp_2.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for thisExp (ExperimentHandler)
    psychoJS.experiment.addData('key_resp_2.keys', key_resp_2.keys);
    psychoJS.experiment.addData('key_resp_2.corr', key_resp_2.corr);
    if (typeof key_resp_2.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp_2.rt', key_resp_2.rt);
        routineTimer.reset();
        }
    
    key_resp_2.stop();
    // the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


var thanksComponents;
function thanksRoutineBegin(snapshot) {
  return function () {
    //------Prepare to start Routine 'thanks'-------
    t = 0;
    thanksClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    thanksComponents = [];
    
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function thanksRoutineEachFrame(snapshot) {
  return function () {
    //------Loop for each frame of Routine 'thanks'-------
    // get current time
    t = thanksClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    thanksComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function thanksRoutineEnd(snapshot) {
  return function () {
    //------Ending Routine 'thanks'-------
    thanksComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "thanks" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    return Scheduler.Event.NEXT;
  };
}


function endLoopIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        const thisTrial = snapshot.getCurrentTrial();
        if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
          psychoJS.experiment.nextEntry(snapshot);
        }
      }
    return Scheduler.Event.NEXT;
    }
  };
}


function importConditions(currentLoop) {
  return function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
