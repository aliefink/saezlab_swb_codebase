Exercise 5.1: Take the Glasgow Face Matching Task online
========================================================

In this chapter we learned how to push experiments online, to pavlovia.org, from PsychoPy. Now we are going to try "pushing" another experiment online - the GFMT we made in chapter 3. To start with, you can just copy and paste the experiment files you made in that chapter to a new folder - let's call it "GFMT_online". Remember, when we are pushing experiments online it is important to make sure that the location we have our experiment files saved in is not already under version control (e.g. google drive), otherwise git will become confused which version history to utilise. It is also good practice to make sure that each time you start a new experiment, you create a unique folder for that experiment (don't just keep your experiment files on your desktop or PsychoPy might try to sync your entire desktop to pavlovia!)

Solution
-------------
1. Push the experiment online - we start by making sure that we are signed into pavlovia.org (in our browser) as well as "locally" in PsychoPy, we log in locally by selecting the fourth globe icon along the top taskbar. After that we can select the globe with the sync icon and we should be prompted to create a new project. Once your experimet has synced you can take a look in your dashboard on pavlovia.org - the experiment should be ready and waiting for you in your experiments panel! - click on it, set your experiment to "piloting" mode and select "pilot" to give it a go!

2. Making things touch screen compatible: The second part of this exercise is to make things touch screen compatible. We could do that either by adding 2 clickable images OR we could use the button component! Replace all of your keyboard components with buttons. Add one button to replace the "ready" keyboard" component in the instructions routine ad add 2 buttons, one that says SAME and one that says DIFFERENT to your trial routine.

3. Change the instructions - don't forget to change the instructions to tell participants to click on the buttons instead of use their keyboards! 



References
--------------

Burton, A. Mike, David White, and Allan McNeill (2010). “The Glasgow Face Matching Test.” Behavior Research Methods 42 (1): 286–91. doi:10.3758/BRM.42.1.286.
Peirce, J.W., Hirst, R.J., and MacAskill, M. (2022). "Building experiments in PsychoPy", Sage Publishing.
