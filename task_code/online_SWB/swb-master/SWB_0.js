/************** 
 * Swb_0 Test *
 **************/

import { core, data, sound, util, visual, hardware } from './lib/psychojs-2022.2.4.js';
const { PsychoJS } = core;
const { TrialHandler, MultiStairHandler } = data;
const { Scheduler } = util;
//some handy aliases as in the psychopy scripts;
const { abs, sin, cos, PI: pi, sqrt } = Math;
const { round } = util;


// store info about the experiment session:
let expName = 'SWB_0';  // from the Builder filename that created this script
let expInfo = {
    'participant': '',
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from define_variables
var total = 10;
var maxTime = 8;
// Run 'Before Experiment' code from countHowHappy
var trialN = 1;
var doHowHappy = 0;
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: false,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true
});
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
flowScheduler.add(definedRoutineBegin());
flowScheduler.add(definedRoutineEachFrame());
flowScheduler.add(definedRoutineEnd());
flowScheduler.add(WelcomeRoutineBegin());
flowScheduler.add(WelcomeRoutineEachFrame());
flowScheduler.add(WelcomeRoutineEnd());
flowScheduler.add(Welcome2RoutineBegin());
flowScheduler.add(Welcome2RoutineEachFrame());
flowScheduler.add(Welcome2RoutineEnd());
const trialControlLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialControlLoopBegin(trialControlLoopScheduler));
flowScheduler.add(trialControlLoopScheduler);
flowScheduler.add(trialControlLoopEnd);
flowScheduler.add(ThankYouRoutineBegin());
flowScheduler.add(ThankYouRoutineEachFrame());
flowScheduler.add(ThankYouRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'control_files/trialControlwRating.csv', 'path': 'control_files/trialControlwRating.csv'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

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


var definedClock;
var safecolor;
var topcolor;
var bottomcolor;
var safey;
var safex;
var gambletop;
var gamblebottom;
var gamblex;
var winy;
var total;
var WelcomeClock;
var welcomeText1;
var space_to_continue;
var Welcome2Clock;
var welcomeText2;
var space_to_continue_2;
var SetupGraphicsClock;
var CueClock;
var LeftHalf;
var RightHalf;
var Safe;
var Top;
var Bottom;
var SafeText;
var TopText;
var BottomText;
var Total;
var Win;
var Keys;
var Mouse;
var CalculateClock;
var SelectionShownClock;
var LeftHalf_2;
var RightHalf_2;
var Safe_2;
var Top_2;
var Bottom_2;
var SafeText_2;
var TopText_2;
var BottomText_2;
var Total_2;
var Win_2;
var WinMsg;
var GambleRevealedClock;
var LeftHalf_3;
var RightHalf_3;
var Safe_3;
var Top_3;
var Bottom_3;
var SafeText_3;
var TopText_3;
var BottomText_3;
var Total_3;
var Win_3;
var WinMsg_2;
var TimeoutClock;
var timeoutText;
var HowHappyClock;
var HowHappySlider;
var UnHappy;
var Happy;
var SliderKeyboard;
var SpacetoExit;
var FixationClock;
var Cross;
var ThankYouClock;
var exitText;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "defined"
  definedClock = new util.Clock();
  // Run 'Begin Experiment' code from define_variables
  safecolor = "black";
  topcolor = "black";
  bottomcolor = "black";
  safey = 0;
  safex = 0.25;
  gambletop = 0.25;
  gamblebottom = (- 0.25);
  gamblex = (- 0.25);
  winy = 0.2;
  total = 10;
  
  // Initialize components for Routine "Welcome"
  WelcomeClock = new util.Clock();
  welcomeText1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeText1',
    text: 'Hello!\n\nYou will be participating in a gambling task that could result in a Cash Reward based on your performance. \n\nIn each trial, you will have the option between a safe bet or a gamble. If you select the safe bet, you will receive that amount of money. You will then be shown what you would have received if you had chosen the gamble. \n\nPress SPACEBAR to continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  space_to_continue = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "Welcome2"
  Welcome2Clock = new util.Clock();
  welcomeText2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'welcomeText2',
    text: 'If you select the gamble, you will have a 50/50 chance at earning more or less money than the safe bet. The safe bet can be negative, positive, or zero. \n\nYou will make your selection by using with a mouse. A Total Score will be presented in the top left corner of the screen. You will receive the total amount at the end of the experiment.\n\nPress SPACEBAR to begin the experiment',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  space_to_continue_2 = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "SetupGraphics"
  SetupGraphicsClock = new util.Clock();
  // Initialize components for Routine "Cue"
  CueClock = new util.Clock();
  LeftHalf = new visual.Rect ({
    win: psychoJS.window, name: 'LeftHalf', 
    width: [0.5, 0.8][0], height: [0.5, 0.8][1],
    ori: 0.0, pos: [(- 0.25), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  RightHalf = new visual.Rect ({
    win: psychoJS.window, name: 'RightHalf', 
    width: [0.5, 0.8][0], height: [0.5, 0.8][1],
    ori: 0.0, pos: [0.25, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  Safe = new visual.Rect ({
    win: psychoJS.window, name: 'Safe', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Top = new visual.Rect ({
    win: psychoJS.window, name: 'Top', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  Bottom = new visual.Rect ({
    win: psychoJS.window, name: 'Bottom', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  SafeText = new visual.TextStim({
    win: psychoJS.window,
    name: 'SafeText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -6.0 
  });
  
  TopText = new visual.TextStim({
    win: psychoJS.window,
    name: 'TopText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -7.0 
  });
  
  BottomText = new visual.TextStim({
    win: psychoJS.window,
    name: 'BottomText',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -8.0 
  });
  
  Total = new visual.Rect ({
    win: psychoJS.window, name: 'Total', 
    width: [0.1, 0.2][0], height: [0.1, 0.2][1],
    ori: 0.0, pos: [(- 0.45), 0.3],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0,0,0]),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  Win = new visual.TextStim({
    win: psychoJS.window,
    name: 'Win',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.3], height: 0.03,  wrapWidth: 0.22, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  Keys = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  Mouse = new core.Mouse({
    win: psychoJS.window,
  });
  Mouse.mouseClock = new util.Clock();
  // Initialize components for Routine "Calculate"
  CalculateClock = new util.Clock();
  // Initialize components for Routine "SelectionShown"
  SelectionShownClock = new util.Clock();
  LeftHalf_2 = new visual.Rect ({
    win: psychoJS.window, name: 'LeftHalf_2', 
    width: [0.5, 0.8][0], height: [0.5, 0.8][1],
    ori: 0.0, pos: [(- 0.25), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: 0, interpolate: true,
  });
  
  RightHalf_2 = new visual.Rect ({
    win: psychoJS.window, name: 'RightHalf_2', 
    width: [0.5, 0.8][0], height: [0.5, 0.8][1],
    ori: 0.0, pos: [0.25, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  Safe_2 = new visual.Rect ({
    win: psychoJS.window, name: 'Safe_2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -2, interpolate: true,
  });
  
  Top_2 = new visual.Rect ({
    win: psychoJS.window, name: 'Top_2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Bottom_2 = new visual.Rect ({
    win: psychoJS.window, name: 'Bottom_2', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  SafeText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SafeText_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -5.0 
  });
  
  TopText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TopText_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -6.0 
  });
  
  BottomText_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'BottomText_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -7.0 
  });
  
  Total_2 = new visual.Rect ({
    win: psychoJS.window, name: 'Total_2', 
    width: [0.1, 0.2][0], height: [0.1, 0.2][1],
    ori: 0.0, pos: [(- 0.45), 0.3],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0,0,0]),
    opacity: undefined, depth: -8, interpolate: true,
  });
  
  Win_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Win_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.3], height: 0.03,  wrapWidth: 0.22, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -9.0 
  });
  
  WinMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'WinMsg',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 0.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  // Initialize components for Routine "GambleRevealed"
  GambleRevealedClock = new util.Clock();
  LeftHalf_3 = new visual.Rect ({
    win: psychoJS.window, name: 'LeftHalf_3', 
    width: [0.5, 0.8][0], height: [0.5, 0.8][1],
    ori: 0.0, pos: [(- 0.25), 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -1, interpolate: true,
  });
  
  RightHalf_3 = new visual.Rect ({
    win: psychoJS.window, name: 'RightHalf_3', 
    width: [0.5, 0.8][0], height: [0.5, 0.8][1],
    ori: 0.0, pos: [0.25, 0],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('black'),
    fillColor: new util.Color('white'),
    opacity: 1.0, depth: -2, interpolate: true,
  });
  
  Safe_3 = new visual.Rect ({
    win: psychoJS.window, name: 'Safe_3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -3, interpolate: true,
  });
  
  Top_3 = new visual.Rect ({
    win: psychoJS.window, name: 'Top_3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -4, interpolate: true,
  });
  
  Bottom_3 = new visual.Rect ({
    win: psychoJS.window, name: 'Bottom_3', 
    width: [0.2, 0.2][0], height: [0.2, 0.2][1],
    ori: 0.0, pos: [0, 0],
    lineWidth: 5.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color('white'),
    opacity: undefined, depth: -5, interpolate: true,
  });
  
  SafeText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'SafeText_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -6.0 
  });
  
  TopText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'TopText_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -7.0 
  });
  
  BottomText_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'BottomText_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.06,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: 1.0,
    depth: -8.0 
  });
  
  Total_3 = new visual.Rect ({
    win: psychoJS.window, name: 'Total_3', 
    width: [0.1, 0.2][0], height: [0.1, 0.2][1],
    ori: 0.0, pos: [(- 0.45), 0.3],
    lineWidth: 1.0, 
    colorSpace: 'rgb',
    lineColor: new util.Color('white'),
    fillColor: new util.Color([0, 0, 0]),
    opacity: undefined, depth: -9, interpolate: true,
  });
  
  Win_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'Win_3',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.45), 0.3], height: 0.03,  wrapWidth: 0.22, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -10.0 
  });
  
  WinMsg_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'WinMsg_2',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: 0.2, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -11.0 
  });
  
  // Initialize components for Routine "Timeout"
  TimeoutClock = new util.Clock();
  timeoutText = new visual.TextStim({
    win: psychoJS.window,
    name: 'timeoutText',
    text: 'Please respond faster',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "HowHappy"
  HowHappyClock = new util.Clock();
  HowHappySlider = new visual.Slider({
    win: psychoJS.window, name: 'HowHappySlider',
    startValue: undefined,
    size: [1.0, 0.1], pos: [0, (- 0.2)], ori: 0.0, units: 'height',
    labels: undefined, fontSize: 0.05, ticks: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    granularity: 0.0, style: ["RATING", "LABELS_45"],
    color: new util.Color('LightGray'), markerColor: new util.Color('black'), lineColor: new util.Color('White'), 
    opacity: undefined, fontFamily: 'Open Sans', bold: true, italic: false, depth: -1, 
    flip: false,
  });
  
  UnHappy = new visual.TextStim({
    win: psychoJS.window,
    name: 'UnHappy',
    text: 'Very Unhappy',
    font: 'Open Sans',
    units: undefined, 
    pos: [(- 0.6), 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  Happy = new visual.TextStim({
    win: psychoJS.window,
    name: 'Happy',
    text: 'Very Happy',
    font: 'Open Sans',
    units: undefined, 
    pos: [0.6, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  SliderKeyboard = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  SpacetoExit = new visual.TextStim({
    win: psychoJS.window,
    name: 'SpacetoExit',
    text: 'Press SPACEBAR to Continue',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, (- 0.4)], height: 0.04,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -5.0 
  });
  
  // Initialize components for Routine "Fixation"
  FixationClock = new util.Clock();
  Cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'Cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('black'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "ThankYou"
  ThankYouClock = new util.Clock();
  exitText = new visual.TextStim({
    win: psychoJS.window,
    name: 'exitText',
    text: '[This is the exit screen]\n\nThank you for participating in our study!\n\nwhat else goes here?',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var definedComponents;
function definedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'defined' ---
    t = 0;
    definedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    definedComponents = [];
    
    for (const thisComponent of definedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function definedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'defined' ---
    // get current time
    t = definedClock.getTime();
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
    for (const thisComponent of definedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function definedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'defined' ---
    for (const thisComponent of definedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "defined" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_to_continue_allKeys;
var WelcomeComponents;
function WelcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome' ---
    t = 0;
    WelcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_to_continue.keys = undefined;
    space_to_continue.rt = undefined;
    _space_to_continue_allKeys = [];
    // keep track of which components have finished
    WelcomeComponents = [];
    WelcomeComponents.push(welcomeText1);
    WelcomeComponents.push(space_to_continue);
    
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function WelcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome' ---
    // get current time
    t = WelcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcomeText1* updates
    if (t >= 0.0 && welcomeText1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeText1.tStart = t;  // (not accounting for frame time here)
      welcomeText1.frameNStart = frameN;  // exact frame index
      
      welcomeText1.setAutoDraw(true);
    }

    
    // *space_to_continue* updates
    if (t >= 0.0 && space_to_continue.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_continue.tStart = t;  // (not accounting for frame time here)
      space_to_continue.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      space_to_continue.clock.reset();
      space_to_continue.start();
    }

    if (space_to_continue.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_to_continue.getKeys({keyList: ['space', 'return'], waitRelease: false});
      _space_to_continue_allKeys = _space_to_continue_allKeys.concat(theseKeys);
      if (_space_to_continue_allKeys.length > 0) {
        space_to_continue.keys = _space_to_continue_allKeys[_space_to_continue_allKeys.length - 1].name;  // just the last key pressed
        space_to_continue.rt = _space_to_continue_allKeys[_space_to_continue_allKeys.length - 1].rt;
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
    for (const thisComponent of WelcomeComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function WelcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome' ---
    for (const thisComponent of WelcomeComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    space_to_continue.stop();
    // the Routine "Welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _space_to_continue_2_allKeys;
var Welcome2Components;
function Welcome2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Welcome2' ---
    t = 0;
    Welcome2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    space_to_continue_2.keys = undefined;
    space_to_continue_2.rt = undefined;
    _space_to_continue_2_allKeys = [];
    // keep track of which components have finished
    Welcome2Components = [];
    Welcome2Components.push(welcomeText2);
    Welcome2Components.push(space_to_continue_2);
    
    for (const thisComponent of Welcome2Components)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function Welcome2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Welcome2' ---
    // get current time
    t = Welcome2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *welcomeText2* updates
    if (t >= 0.0 && welcomeText2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcomeText2.tStart = t;  // (not accounting for frame time here)
      welcomeText2.frameNStart = frameN;  // exact frame index
      
      welcomeText2.setAutoDraw(true);
    }

    
    // *space_to_continue_2* updates
    if (t >= 0.0 && space_to_continue_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      space_to_continue_2.tStart = t;  // (not accounting for frame time here)
      space_to_continue_2.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      space_to_continue_2.clock.reset();
      space_to_continue_2.start();
    }

    if (space_to_continue_2.status === PsychoJS.Status.STARTED) {
      let theseKeys = space_to_continue_2.getKeys({keyList: ['space', 'return'], waitRelease: false});
      _space_to_continue_2_allKeys = _space_to_continue_2_allKeys.concat(theseKeys);
      if (_space_to_continue_2_allKeys.length > 0) {
        space_to_continue_2.keys = _space_to_continue_2_allKeys[_space_to_continue_2_allKeys.length - 1].name;  // just the last key pressed
        space_to_continue_2.rt = _space_to_continue_2_allKeys[_space_to_continue_2_allKeys.length - 1].rt;
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
    for (const thisComponent of Welcome2Components)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function Welcome2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Welcome2' ---
    for (const thisComponent of Welcome2Components) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    space_to_continue_2.stop();
    // the Routine "Welcome2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var trialControl;
function trialControlLoopBegin(trialControlLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trialControl = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'control_files/trialControlwRating.csv',
      seed: undefined, name: 'trialControl'
    });
    psychoJS.experiment.addLoop(trialControl); // add the loop to the experiment
    currentLoop = trialControl;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTrialControl of trialControl) {
      snapshot = trialControl.getSnapshot();
      trialControlLoopScheduler.add(importConditions(snapshot));
      trialControlLoopScheduler.add(SetupGraphicsRoutineBegin(snapshot));
      trialControlLoopScheduler.add(SetupGraphicsRoutineEachFrame());
      trialControlLoopScheduler.add(SetupGraphicsRoutineEnd(snapshot));
      trialControlLoopScheduler.add(CueRoutineBegin(snapshot));
      trialControlLoopScheduler.add(CueRoutineEachFrame());
      trialControlLoopScheduler.add(CueRoutineEnd(snapshot));
      const revealLoopLoopScheduler = new Scheduler(psychoJS);
      trialControlLoopScheduler.add(revealLoopLoopBegin(revealLoopLoopScheduler, snapshot));
      trialControlLoopScheduler.add(revealLoopLoopScheduler);
      trialControlLoopScheduler.add(revealLoopLoopEnd);
      const timeoutLoopLoopScheduler = new Scheduler(psychoJS);
      trialControlLoopScheduler.add(timeoutLoopLoopBegin(timeoutLoopLoopScheduler, snapshot));
      trialControlLoopScheduler.add(timeoutLoopLoopScheduler);
      trialControlLoopScheduler.add(timeoutLoopLoopEnd);
      const HowHappyCheckLoopScheduler = new Scheduler(psychoJS);
      trialControlLoopScheduler.add(HowHappyCheckLoopBegin(HowHappyCheckLoopScheduler, snapshot));
      trialControlLoopScheduler.add(HowHappyCheckLoopScheduler);
      trialControlLoopScheduler.add(HowHappyCheckLoopEnd);
      trialControlLoopScheduler.add(FixationRoutineBegin(snapshot));
      trialControlLoopScheduler.add(FixationRoutineEachFrame());
      trialControlLoopScheduler.add(FixationRoutineEnd(snapshot));
      trialControlLoopScheduler.add(trialControlLoopEndIteration(trialControlLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


var revealLoop;
function revealLoopLoopBegin(revealLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    revealLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: revealRoutines, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'revealLoop'
    });
    psychoJS.experiment.addLoop(revealLoop); // add the loop to the experiment
    currentLoop = revealLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisRevealLoop of revealLoop) {
      snapshot = revealLoop.getSnapshot();
      revealLoopLoopScheduler.add(importConditions(snapshot));
      revealLoopLoopScheduler.add(CalculateRoutineBegin(snapshot));
      revealLoopLoopScheduler.add(CalculateRoutineEachFrame());
      revealLoopLoopScheduler.add(CalculateRoutineEnd(snapshot));
      revealLoopLoopScheduler.add(SelectionShownRoutineBegin(snapshot));
      revealLoopLoopScheduler.add(SelectionShownRoutineEachFrame());
      revealLoopLoopScheduler.add(SelectionShownRoutineEnd(snapshot));
      revealLoopLoopScheduler.add(GambleRevealedRoutineBegin(snapshot));
      revealLoopLoopScheduler.add(GambleRevealedRoutineEachFrame());
      revealLoopLoopScheduler.add(GambleRevealedRoutineEnd(snapshot));
      revealLoopLoopScheduler.add(revealLoopLoopEndIteration(revealLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function revealLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(revealLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function revealLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var timeoutLoop;
function timeoutLoopLoopBegin(timeoutLoopLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    timeoutLoop = new TrialHandler({
      psychoJS: psychoJS,
      nReps: timeoutRoutine, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'timeoutLoop'
    });
    psychoJS.experiment.addLoop(timeoutLoop); // add the loop to the experiment
    currentLoop = timeoutLoop;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisTimeoutLoop of timeoutLoop) {
      snapshot = timeoutLoop.getSnapshot();
      timeoutLoopLoopScheduler.add(importConditions(snapshot));
      timeoutLoopLoopScheduler.add(TimeoutRoutineBegin(snapshot));
      timeoutLoopLoopScheduler.add(TimeoutRoutineEachFrame());
      timeoutLoopLoopScheduler.add(TimeoutRoutineEnd(snapshot));
      timeoutLoopLoopScheduler.add(timeoutLoopLoopEndIteration(timeoutLoopLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function timeoutLoopLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(timeoutLoop);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function timeoutLoopLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var HowHappyCheck;
function HowHappyCheckLoopBegin(HowHappyCheckLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    HowHappyCheck = new TrialHandler({
      psychoJS: psychoJS,
      nReps: doHowHappy, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'HowHappyCheck'
    });
    psychoJS.experiment.addLoop(HowHappyCheck); // add the loop to the experiment
    currentLoop = HowHappyCheck;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    for (const thisHowHappyCheck of HowHappyCheck) {
      snapshot = HowHappyCheck.getSnapshot();
      HowHappyCheckLoopScheduler.add(importConditions(snapshot));
      HowHappyCheckLoopScheduler.add(HowHappyRoutineBegin(snapshot));
      HowHappyCheckLoopScheduler.add(HowHappyRoutineEachFrame());
      HowHappyCheckLoopScheduler.add(HowHappyRoutineEnd(snapshot));
      HowHappyCheckLoopScheduler.add(HowHappyCheckLoopEndIteration(HowHappyCheckLoopScheduler, snapshot));
    }
    
    return Scheduler.Event.NEXT;
  }
}


async function HowHappyCheckLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(HowHappyCheck);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function HowHappyCheckLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function trialControlLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trialControl);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialControlLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var topAmt;
var bottomAmt;
var certainAmt;
var totalWin;
var SetupGraphicsComponents;
function SetupGraphicsRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SetupGraphics' ---
    t = 0;
    SetupGraphicsClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from AdjustPosition
    if ((RiskSide === "left")) {
        safex = 0.25;
        gamblex = (- 0.25);
    } else {
        safex = (- 0.25);
        gamblex = 0.25;
    }
    
    topAmt="$" + TopAmt.toFixed(2);
    bottomAmt="$" + BottomAmt.toFixed(2);
    certainAmt="$" + CertainAmt.toFixed(2);
    
    totalWin="Total\n" + total.toFixed(2);
    
    psychoJS.eventManager.clearEvents(Keys);
    
    // keep track of which components have finished
    SetupGraphicsComponents = [];
    
    for (const thisComponent of SetupGraphicsComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function SetupGraphicsRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SetupGraphics' ---
    // get current time
    t = SetupGraphicsClock.getTime();
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
    for (const thisComponent of SetupGraphicsComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SetupGraphicsRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SetupGraphics' ---
    for (const thisComponent of SetupGraphicsComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "SetupGraphics" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var startTime;
var revealRoutines;
var timeoutRoutine;
var _Keys_allKeys;
var gotValidClick;
var CueComponents;
function CueRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Cue' ---
    t = 0;
    CueClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from trialTimer
    startTime = globalClock.getTime();
    revealRoutines = 1;
    timeoutRoutine = 0;
    
    Safe.setPos([safex, safey]);
    Top.setPos([gamblex, gambletop]);
    Bottom.setPos([gamblex, gamblebottom]);
    SafeText.setPos([safex, safey]);
    SafeText.setText(certainAmt);
    TopText.setPos([gamblex, gambletop]);
    TopText.setText(topAmt);
    BottomText.setPos([gamblex, gamblebottom]);
    BottomText.setText(bottomAmt);
    Win.setText(totalWin);
    Keys.keys = undefined;
    Keys.rt = undefined;
    _Keys_allKeys = [];
    // setup some python lists for storing info about the Mouse
    Mouse.clicked_name = [];
    gotValidClick = false; // until a click is received
    // keep track of which components have finished
    CueComponents = [];
    CueComponents.push(LeftHalf);
    CueComponents.push(RightHalf);
    CueComponents.push(Safe);
    CueComponents.push(Top);
    CueComponents.push(Bottom);
    CueComponents.push(SafeText);
    CueComponents.push(TopText);
    CueComponents.push(BottomText);
    CueComponents.push(Total);
    CueComponents.push(Win);
    CueComponents.push(Keys);
    CueComponents.push(Mouse);
    
    for (const thisComponent of CueComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var prevButtonState;
var _mouseButtons;
function CueRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Cue' ---
    // get current time
    t = CueClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    // Run 'Each Frame' code from trialTimer
    if (((globalClock.getTime() - startTime) >= maxTime)) {
        revealRoutines = 0;
        timeoutRoutine = 1;
        continueRoutine = false;
    }
    
    
    // *LeftHalf* updates
    if (t >= 0.0 && LeftHalf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LeftHalf.tStart = t;  // (not accounting for frame time here)
      LeftHalf.frameNStart = frameN;  // exact frame index
      
      LeftHalf.setAutoDraw(true);
    }

    
    // *RightHalf* updates
    if (t >= 0.0 && RightHalf.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RightHalf.tStart = t;  // (not accounting for frame time here)
      RightHalf.frameNStart = frameN;  // exact frame index
      
      RightHalf.setAutoDraw(true);
    }

    
    // *Safe* updates
    if (t >= 0.0 && Safe.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Safe.tStart = t;  // (not accounting for frame time here)
      Safe.frameNStart = frameN;  // exact frame index
      
      Safe.setAutoDraw(true);
    }

    
    // *Top* updates
    if (t >= 0.0 && Top.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Top.tStart = t;  // (not accounting for frame time here)
      Top.frameNStart = frameN;  // exact frame index
      
      Top.setAutoDraw(true);
    }

    
    // *Bottom* updates
    if (t >= 0.0 && Bottom.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Bottom.tStart = t;  // (not accounting for frame time here)
      Bottom.frameNStart = frameN;  // exact frame index
      
      Bottom.setAutoDraw(true);
    }

    
    // *SafeText* updates
    if (t >= 0.0 && SafeText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SafeText.tStart = t;  // (not accounting for frame time here)
      SafeText.frameNStart = frameN;  // exact frame index
      
      SafeText.setAutoDraw(true);
    }

    
    // *TopText* updates
    if (t >= 0.0 && TopText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TopText.tStart = t;  // (not accounting for frame time here)
      TopText.frameNStart = frameN;  // exact frame index
      
      TopText.setAutoDraw(true);
    }

    
    // *BottomText* updates
    if (t >= 0.0 && BottomText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BottomText.tStart = t;  // (not accounting for frame time here)
      BottomText.frameNStart = frameN;  // exact frame index
      
      BottomText.setAutoDraw(true);
    }

    
    // *Total* updates
    if (t >= 0.0 && Total.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Total.tStart = t;  // (not accounting for frame time here)
      Total.frameNStart = frameN;  // exact frame index
      
      Total.setAutoDraw(true);
    }

    
    // *Win* updates
    if (t >= 0.0 && Win.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Win.tStart = t;  // (not accounting for frame time here)
      Win.frameNStart = frameN;  // exact frame index
      
      Win.setAutoDraw(true);
    }

    
    // *Keys* updates
    if (t >= 0.0 && Keys.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Keys.tStart = t;  // (not accounting for frame time here)
      Keys.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { Keys.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { Keys.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { Keys.clearEvents(); });
    }

    if (Keys.status === PsychoJS.Status.STARTED) {
      let theseKeys = Keys.getKeys({keyList: ['left', 'right'], waitRelease: false});
      _Keys_allKeys = _Keys_allKeys.concat(theseKeys);
      if (_Keys_allKeys.length > 0) {
        Keys.keys = _Keys_allKeys[_Keys_allKeys.length - 1].name;  // just the last key pressed
        Keys.rt = _Keys_allKeys[_Keys_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // *Mouse* updates
    if (t >= 0.0 && Mouse.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Mouse.tStart = t;  // (not accounting for frame time here)
      Mouse.frameNStart = frameN;  // exact frame index
      
      Mouse.status = PsychoJS.Status.STARTED;
      Mouse.mouseClock.reset();
      prevButtonState = Mouse.getPressed();  // if button is down already this ISN'T a new click
      }
    if (Mouse.status === PsychoJS.Status.STARTED) {  // only update if started and not finished!
      _mouseButtons = Mouse.getPressed();
      if (!_mouseButtons.every( (e,i,) => (e == prevButtonState[i]) )) { // button state changed?
        prevButtonState = _mouseButtons;
        if (_mouseButtons.reduce( (e, acc) => (e+acc) ) > 0) { // state changed to a new click
          // check if the mouse was inside our 'clickable' objects
          gotValidClick = false;
          for (const obj of [RightHalf,LeftHalf]) {
            if (obj.contains(Mouse)) {
              gotValidClick = true;
              Mouse.clicked_name.push(obj.name)
            }
          }
          if (gotValidClick === true) { // abort routine on response
            continueRoutine = false;
          }
        }
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
    for (const thisComponent of CueComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var _mouseXYs;
var trialN;
var doHowHappy;
function CueRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Cue' ---
    for (const thisComponent of CueComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(Keys.corr, level);
    }
    psychoJS.experiment.addData('Keys.keys', Keys.keys);
    if (typeof Keys.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('Keys.rt', Keys.rt);
        routineTimer.reset();
        }
    
    Keys.stop();
    // store data for psychoJS.experiment (ExperimentHandler)
    _mouseXYs = Mouse.getPos();
    _mouseButtons = Mouse.getPressed();
    psychoJS.experiment.addData('Mouse.x', _mouseXYs[0]);
    psychoJS.experiment.addData('Mouse.y', _mouseXYs[1]);
    psychoJS.experiment.addData('Mouse.leftButton', _mouseButtons[0]);
    psychoJS.experiment.addData('Mouse.midButton', _mouseButtons[1]);
    psychoJS.experiment.addData('Mouse.rightButton', _mouseButtons[2]);
    if (Mouse.clicked_name.length > 0) {
      psychoJS.experiment.addData('Mouse.clicked_name', Mouse.clicked_name[0]);}
    // Run 'End Routine' code from countHowHappy
    if ((trialN >= 3)) {
        trialN = 1;
        doHowHappy = 1;
    } else {
        trialN += 1;
        doHowHappy = 0;
    }
    
    // the Routine "Cue" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var right;
var rightx;
var left;
var leftx;
var XY;
var Gamble;
var GambleAmt;
var OtherAmt;
var Change;
var winColor;
var winText;
var CalculateComponents;
function CalculateRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Calculate' ---
    t = 0;
    CalculateClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from DetermineColor
    //js version bug: always selects left side... 
    right = false;
    rightx = false;
    left = false;
    leftx = false;
    
    right = Boolean(psychoJS.eventManager.getKeys({keyList:['right']}).length > 0);
    left = Boolean(psychoJS.eventManager.getKeys({keyList:['left']}).length > 0);
    
    XY = Mouse.getPos();
    if( XY[0] > 0 ) {
        rightx = true;
        leftx = false;
    } else {
        rightx = false;
        leftx = true;
    }
    
    if (((RiskSide === "right") && (left||leftx)))  {
        safecolor = "yellow";
        topcolor = "black";
        bottomcolor = "black";
        Gamble = false;
    } else {
        if (((RiskSide === "right") && (right||rightx)))  {
            safecolor = "black";
            topcolor = "yellow";
            bottomcolor = "yellow";
            Gamble = true;
        } else {
            if (((RiskSide === "left") && (left||leftx)))  {
                safecolor = "black";
                topcolor = "yellow";
                bottomcolor = "yellow";
                Gamble = true;
            } else {
                if (((RiskSide === "left") && (right||rightx))) {
                    safecolor = "yellow";
                    topcolor = "black";
                    bottomcolor = "black";
                    Gamble = false;
                }
            }
        }
    }
    
    //Set Gamble outcome
    if ((Outcome === "top")) {
        GambleAmt = TopAmt;
        OtherAmt = BottomAmt;
    } else {
        GambleAmt = BottomAmt;
        OtherAmt = TopAmt;
    }
    if (Gamble) {
        Change = GambleAmt;
    } else {
        Change = CertainAmt;
        //only update total now if safebet
        total = total + Change;
        totalWin="Total\n$" + total.toFixed(2);
    }
    
    winColor = "black";
    if (Gamble) {
        winText = "";
    } else {
        if ((Change > 0)) {
            winText = "You won $" + Change.toFixed(2);
        } else {
            if ((Change === 0)) {
                winText = "You got $" + Change.toFixed(2);
            } else {
                winText = "You lost $" + Change.toFixed(2);
            }
        }
    }
    
    // keep track of which components have finished
    CalculateComponents = [];
    
    for (const thisComponent of CalculateComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function CalculateRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Calculate' ---
    // get current time
    t = CalculateClock.getTime();
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
    for (const thisComponent of CalculateComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function CalculateRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Calculate' ---
    for (const thisComponent of CalculateComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Calculate" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var SelectionShownComponents;
function SelectionShownRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'SelectionShown' ---
    t = 0;
    SelectionShownClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    Safe_2.setPos([safex, safey]);
    Safe_2.setLineColor(new util.Color(safecolor));
    Top_2.setPos([gamblex, gambletop]);
    Top_2.setLineColor(new util.Color(topcolor));
    Bottom_2.setPos([gamblex, gamblebottom]);
    Bottom_2.setLineColor(new util.Color(bottomcolor));
    SafeText_2.setPos([safex, safey]);
    SafeText_2.setText(certainAmt);
    TopText_2.setPos([gamblex, gambletop]);
    TopText_2.setText(topAmt);
    BottomText_2.setPos([gamblex, gamblebottom]);
    BottomText_2.setText(bottomAmt);
    Win_2.setText(totalWin);
    WinMsg.setColor(new util.Color(winColor));
    WinMsg.setPos([safex, winy]);
    WinMsg.setText(winText);
    // keep track of which components have finished
    SelectionShownComponents = [];
    SelectionShownComponents.push(LeftHalf_2);
    SelectionShownComponents.push(RightHalf_2);
    SelectionShownComponents.push(Safe_2);
    SelectionShownComponents.push(Top_2);
    SelectionShownComponents.push(Bottom_2);
    SelectionShownComponents.push(SafeText_2);
    SelectionShownComponents.push(TopText_2);
    SelectionShownComponents.push(BottomText_2);
    SelectionShownComponents.push(Total_2);
    SelectionShownComponents.push(Win_2);
    SelectionShownComponents.push(WinMsg);
    
    for (const thisComponent of SelectionShownComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function SelectionShownRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'SelectionShown' ---
    // get current time
    t = SelectionShownClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LeftHalf_2* updates
    if (t >= 0.0 && LeftHalf_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LeftHalf_2.tStart = t;  // (not accounting for frame time here)
      LeftHalf_2.frameNStart = frameN;  // exact frame index
      
      LeftHalf_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LeftHalf_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LeftHalf_2.setAutoDraw(false);
    }
    
    // *RightHalf_2* updates
    if (t >= 0.0 && RightHalf_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RightHalf_2.tStart = t;  // (not accounting for frame time here)
      RightHalf_2.frameNStart = frameN;  // exact frame index
      
      RightHalf_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RightHalf_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RightHalf_2.setAutoDraw(false);
    }
    
    // *Safe_2* updates
    if (t >= 0.0 && Safe_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Safe_2.tStart = t;  // (not accounting for frame time here)
      Safe_2.frameNStart = frameN;  // exact frame index
      
      Safe_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Safe_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Safe_2.setAutoDraw(false);
    }
    
    // *Top_2* updates
    if (t >= 0.0 && Top_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Top_2.tStart = t;  // (not accounting for frame time here)
      Top_2.frameNStart = frameN;  // exact frame index
      
      Top_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Top_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Top_2.setAutoDraw(false);
    }
    
    // *Bottom_2* updates
    if (t >= 0.0 && Bottom_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Bottom_2.tStart = t;  // (not accounting for frame time here)
      Bottom_2.frameNStart = frameN;  // exact frame index
      
      Bottom_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Bottom_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Bottom_2.setAutoDraw(false);
    }
    
    // *SafeText_2* updates
    if (t >= 0.0 && SafeText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SafeText_2.tStart = t;  // (not accounting for frame time here)
      SafeText_2.frameNStart = frameN;  // exact frame index
      
      SafeText_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SafeText_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SafeText_2.setAutoDraw(false);
    }
    
    // *TopText_2* updates
    if (t >= 0.0 && TopText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TopText_2.tStart = t;  // (not accounting for frame time here)
      TopText_2.frameNStart = frameN;  // exact frame index
      
      TopText_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (TopText_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      TopText_2.setAutoDraw(false);
    }
    
    // *BottomText_2* updates
    if (t >= 0.0 && BottomText_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BottomText_2.tStart = t;  // (not accounting for frame time here)
      BottomText_2.frameNStart = frameN;  // exact frame index
      
      BottomText_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BottomText_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BottomText_2.setAutoDraw(false);
    }
    
    // *Total_2* updates
    if (t >= 0.0 && Total_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Total_2.tStart = t;  // (not accounting for frame time here)
      Total_2.frameNStart = frameN;  // exact frame index
      
      Total_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Total_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Total_2.setAutoDraw(false);
    }
    
    // *Win_2* updates
    if (t >= 0.0 && Win_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Win_2.tStart = t;  // (not accounting for frame time here)
      Win_2.frameNStart = frameN;  // exact frame index
      
      Win_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Win_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Win_2.setAutoDraw(false);
    }
    
    // *WinMsg* updates
    if (t >= 0.0 && WinMsg.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WinMsg.tStart = t;  // (not accounting for frame time here)
      WinMsg.frameNStart = frameN;  // exact frame index
      
      WinMsg.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (WinMsg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      WinMsg.setAutoDraw(false);
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
    for (const thisComponent of SelectionShownComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function SelectionShownRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'SelectionShown' ---
    for (const thisComponent of SelectionShownComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Run 'End Routine' code from code
    if (Gamble) {
        if ((Change > 0)) {
            winText = `You won $${Change}`;
            winColor = "limegreen";
        } else {
            if ((Change < 0)) {
                winText = `You lost $${Change}`;
                winColor = "red";
            } else {
                if ((GambleAmt > OtherAmt)) {
                    winText = `You won $${Change}`;
                    winColor = "limegreen";
                } else {
                    if ((GambleAmt < OtherAmt)) {
                        winText = `You lost $${Change}`;
                        winColor = "red";
                    } else {
                        winText = `how did you get here? $${GambleAmt}`;
                        winColor = "magenta";
                    }
                }
            }
        }
    } else {
        if ((GambleAmt > CertainAmt)) {
            safecolor = "red";
            winText = `You would have won $${GambleAmt}`;
            winColor = "red";
        } else {
            safecolor = "limegreen";
            winText = `You would have lost $${GambleAmt}`;
            winColor = "limegreen";
        }
    }
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var GambleRevealedComponents;
function GambleRevealedRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'GambleRevealed' ---
    t = 0;
    GambleRevealedClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from RevealGamble
    // 
    if (Gamble) {
        // if chose gamble, add total to outcome
        total = total + Change;
        totalWin="Total\n$" + total.toFixed(2);
        if (((Outcome === "top") && (TopAmt > BottomAmt))) {
            topcolor = "limegreen";
            bottomcolor = "black";
        } else {
            if (((Outcome === "top") && (TopAmt < BottomAmt))) {
                topcolor = "red";
                bottomcolor = "black";
            } else {
                if (((Outcome === "bottom") && (BottomAmt > TopAmt))) {
                    topcolor = "black";
                    bottomcolor = "limegreen";
                } else {
                    if (((Outcome === "bottom") && (BottomAmt < TopAmt))) {
                        topcolor = "black";
                        bottomcolor = "red";
                    }
                }
            }
        }
    } else {
        if (Outcome === "top") {
            topcolor = "mediumorchid";
            bottomcolor = "black";
        } else {
            topcolor = "black";
            bottomcolor = "mediumorchid";
        }
    }
    
    Safe_3.setPos([safex, safey]);
    Safe_3.setLineColor(new util.Color(safecolor));
    Top_3.setPos([gamblex, gambletop]);
    Top_3.setLineColor(new util.Color(topcolor));
    Bottom_3.setPos([gamblex, gamblebottom]);
    Bottom_3.setLineColor(new util.Color(bottomcolor));
    SafeText_3.setPos([safex, safey]);
    SafeText_3.setText(certainAmt);
    TopText_3.setPos([gamblex, gambletop]);
    TopText_3.setText(topAmt);
    BottomText_3.setPos([gamblex, gamblebottom]);
    BottomText_3.setText(bottomAmt);
    Win_3.setText(totalWin);
    WinMsg_2.setColor(new util.Color(winColor));
    WinMsg_2.setPos([gamblex, 0]);
    WinMsg_2.setText(winText);
    // keep track of which components have finished
    GambleRevealedComponents = [];
    GambleRevealedComponents.push(LeftHalf_3);
    GambleRevealedComponents.push(RightHalf_3);
    GambleRevealedComponents.push(Safe_3);
    GambleRevealedComponents.push(Top_3);
    GambleRevealedComponents.push(Bottom_3);
    GambleRevealedComponents.push(SafeText_3);
    GambleRevealedComponents.push(TopText_3);
    GambleRevealedComponents.push(BottomText_3);
    GambleRevealedComponents.push(Total_3);
    GambleRevealedComponents.push(Win_3);
    GambleRevealedComponents.push(WinMsg_2);
    
    for (const thisComponent of GambleRevealedComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function GambleRevealedRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'GambleRevealed' ---
    // get current time
    t = GambleRevealedClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *LeftHalf_3* updates
    if (t >= 0.0 && LeftHalf_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      LeftHalf_3.tStart = t;  // (not accounting for frame time here)
      LeftHalf_3.frameNStart = frameN;  // exact frame index
      
      LeftHalf_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (LeftHalf_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      LeftHalf_3.setAutoDraw(false);
    }
    
    // *RightHalf_3* updates
    if (t >= 0.0 && RightHalf_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      RightHalf_3.tStart = t;  // (not accounting for frame time here)
      RightHalf_3.frameNStart = frameN;  // exact frame index
      
      RightHalf_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (RightHalf_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      RightHalf_3.setAutoDraw(false);
    }
    
    // *Safe_3* updates
    if (t >= 0.0 && Safe_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Safe_3.tStart = t;  // (not accounting for frame time here)
      Safe_3.frameNStart = frameN;  // exact frame index
      
      Safe_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Safe_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Safe_3.setAutoDraw(false);
    }
    
    // *Top_3* updates
    if (t >= 0.0 && Top_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Top_3.tStart = t;  // (not accounting for frame time here)
      Top_3.frameNStart = frameN;  // exact frame index
      
      Top_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Top_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Top_3.setAutoDraw(false);
    }
    
    // *Bottom_3* updates
    if (t >= 0.0 && Bottom_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Bottom_3.tStart = t;  // (not accounting for frame time here)
      Bottom_3.frameNStart = frameN;  // exact frame index
      
      Bottom_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Bottom_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Bottom_3.setAutoDraw(false);
    }
    
    // *SafeText_3* updates
    if (t >= 0.0 && SafeText_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SafeText_3.tStart = t;  // (not accounting for frame time here)
      SafeText_3.frameNStart = frameN;  // exact frame index
      
      SafeText_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (SafeText_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      SafeText_3.setAutoDraw(false);
    }
    
    // *TopText_3* updates
    if (t >= 0.0 && TopText_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      TopText_3.tStart = t;  // (not accounting for frame time here)
      TopText_3.frameNStart = frameN;  // exact frame index
      
      TopText_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (TopText_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      TopText_3.setAutoDraw(false);
    }
    
    // *BottomText_3* updates
    if (t >= 0.0 && BottomText_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      BottomText_3.tStart = t;  // (not accounting for frame time here)
      BottomText_3.frameNStart = frameN;  // exact frame index
      
      BottomText_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (BottomText_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      BottomText_3.setAutoDraw(false);
    }
    
    // *Total_3* updates
    if (t >= 0.0 && Total_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Total_3.tStart = t;  // (not accounting for frame time here)
      Total_3.frameNStart = frameN;  // exact frame index
      
      Total_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Total_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Total_3.setAutoDraw(false);
    }
    
    // *Win_3* updates
    if (t >= 0.0 && Win_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Win_3.tStart = t;  // (not accounting for frame time here)
      Win_3.frameNStart = frameN;  // exact frame index
      
      Win_3.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Win_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Win_3.setAutoDraw(false);
    }
    
    // *WinMsg_2* updates
    if (t >= 0.0 && WinMsg_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      WinMsg_2.tStart = t;  // (not accounting for frame time here)
      WinMsg_2.frameNStart = frameN;  // exact frame index
      
      WinMsg_2.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (WinMsg_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      WinMsg_2.setAutoDraw(false);
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
    for (const thisComponent of GambleRevealedComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function GambleRevealedRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'GambleRevealed' ---
    for (const thisComponent of GambleRevealedComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var TimeoutComponents;
function TimeoutRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Timeout' ---
    t = 0;
    TimeoutClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(8.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    TimeoutComponents = [];
    TimeoutComponents.push(timeoutText);
    
    for (const thisComponent of TimeoutComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function TimeoutRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Timeout' ---
    // get current time
    t = TimeoutClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *timeoutText* updates
    if (t >= 0.0 && timeoutText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      timeoutText.tStart = t;  // (not accounting for frame time here)
      timeoutText.frameNStart = frameN;  // exact frame index
      
      timeoutText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 8.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (timeoutText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      timeoutText.setAutoDraw(false);
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
    for (const thisComponent of TimeoutComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function TimeoutRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Timeout' ---
    for (const thisComponent of TimeoutComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _SliderKeyboard_allKeys;
var HowHappyComponents;
function HowHappyRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'HowHappy' ---
    t = 0;
    HowHappyClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from ShowSlider
    //if ((Rating === 0)) {
    //   continueRoutine = false;
    //}
    
    //HowHappySlider.marker.size = [0.05, 0.05];
    
    HowHappySlider.reset()
    SliderKeyboard.keys = undefined;
    SliderKeyboard.rt = undefined;
    _SliderKeyboard_allKeys = [];
    // keep track of which components have finished
    HowHappyComponents = [];
    HowHappyComponents.push(HowHappySlider);
    HowHappyComponents.push(UnHappy);
    HowHappyComponents.push(Happy);
    HowHappyComponents.push(SliderKeyboard);
    HowHappyComponents.push(SpacetoExit);
    
    for (const thisComponent of HowHappyComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function HowHappyRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'HowHappy' ---
    // get current time
    t = HowHappyClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *HowHappySlider* updates
    if (t >= 0.0 && HowHappySlider.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      HowHappySlider.tStart = t;  // (not accounting for frame time here)
      HowHappySlider.frameNStart = frameN;  // exact frame index
      
      HowHappySlider.setAutoDraw(true);
    }

    
    // *UnHappy* updates
    if (t >= 0.0 && UnHappy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      UnHappy.tStart = t;  // (not accounting for frame time here)
      UnHappy.frameNStart = frameN;  // exact frame index
      
      UnHappy.setAutoDraw(true);
    }

    
    // *Happy* updates
    if (t >= 0.0 && Happy.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Happy.tStart = t;  // (not accounting for frame time here)
      Happy.frameNStart = frameN;  // exact frame index
      
      Happy.setAutoDraw(true);
    }

    
    // *SliderKeyboard* updates
    if ((HowHappySlider.getRating()) && SliderKeyboard.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SliderKeyboard.tStart = t;  // (not accounting for frame time here)
      SliderKeyboard.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { SliderKeyboard.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { SliderKeyboard.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { SliderKeyboard.clearEvents(); });
    }

    if (SliderKeyboard.status === PsychoJS.Status.STARTED) {
      let theseKeys = SliderKeyboard.getKeys({keyList: ['space'], waitRelease: false});
      _SliderKeyboard_allKeys = _SliderKeyboard_allKeys.concat(theseKeys);
      if (_SliderKeyboard_allKeys.length > 0) {
        SliderKeyboard.keys = _SliderKeyboard_allKeys[_SliderKeyboard_allKeys.length - 1].name;  // just the last key pressed
        SliderKeyboard.rt = _SliderKeyboard_allKeys[_SliderKeyboard_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    
    // *SpacetoExit* updates
    if ((HowHappySlider.rating) && SpacetoExit.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      SpacetoExit.tStart = t;  // (not accounting for frame time here)
      SpacetoExit.frameNStart = frameN;  // exact frame index
      
      SpacetoExit.setAutoDraw(true);
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
    for (const thisComponent of HowHappyComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function HowHappyRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'HowHappy' ---
    for (const thisComponent of HowHappyComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    psychoJS.experiment.addData('HowHappySlider.response', HowHappySlider.getRating());
    psychoJS.experiment.addData('HowHappySlider.rt', HowHappySlider.getRT());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(SliderKeyboard.corr, level);
    }
    psychoJS.experiment.addData('SliderKeyboard.keys', SliderKeyboard.keys);
    if (typeof SliderKeyboard.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('SliderKeyboard.rt', SliderKeyboard.rt);
        routineTimer.reset();
        }
    
    SliderKeyboard.stop();
    // the Routine "HowHappy" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var FixationComponents;
function FixationRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'Fixation' ---
    t = 0;
    FixationClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // keep track of which components have finished
    FixationComponents = [];
    FixationComponents.push(Cross);
    
    for (const thisComponent of FixationComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function FixationRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'Fixation' ---
    // get current time
    t = FixationClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *Cross* updates
    if (t >= 0.0 && Cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      Cross.tStart = t;  // (not accounting for frame time here)
      Cross.frameNStart = frameN;  // exact frame index
      
      Cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + ITI - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (Cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      Cross.setAutoDraw(false);
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
    for (const thisComponent of FixationComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function FixationRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'Fixation' ---
    for (const thisComponent of FixationComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // the Routine "Fixation" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ThankYouComponents;
function ThankYouRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ThankYou' ---
    t = 0;
    ThankYouClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(5.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ThankYouComponents = [];
    ThankYouComponents.push(exitText);
    
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
    return Scheduler.Event.NEXT;
  }
}


function ThankYouRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ThankYou' ---
    // get current time
    t = ThankYouClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *exitText* updates
    if (t >= 0.0 && exitText.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      exitText.tStart = t;  // (not accounting for frame time here)
      exitText.frameNStart = frameN;  // exact frame index
      
      exitText.setAutoDraw(true);
    }

    frameRemains = 0.0 + 5.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (exitText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      exitText.setAutoDraw(false);
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
    for (const thisComponent of ThankYouComponents)
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
        break;
      }
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ThankYouRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ThankYou' ---
    for (const thisComponent of ThankYouComponents) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
