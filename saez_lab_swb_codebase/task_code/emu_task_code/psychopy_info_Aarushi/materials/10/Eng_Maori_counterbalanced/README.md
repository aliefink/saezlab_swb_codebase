The Stroop task with counterbalancing
===============================================

The experiment English_Maori_blocked extended the Stroop task to run blocks of 
trials in each language.

Here we extend that a little further to provide a way of counterbalancing the
order. The idea is that the experimenter gets to choose the order in which the
blocks are encountered for each participant by assigning them to Group A or
Group B. We create separate files for each group to set the order of the
blocks and we create an entry in the initial dialog box to allow us to choose
the group.

Implementation
-------------------

Note that this version of the experiment differs a little from the one described
in Chapter 10. In particular, it includes some analysis code so that the
participant gets some immediate feedback on the magnitude of the Stroop
interference effect in each language at the end of the experiment.

Extensions
-------------------

In Chapter 10, a number of ways of controlling the order of blocks via the outer
loop are discussed. Try changing this experiment to accomplish one of them
e.g. specifying the block order by entering a value in a field in the
experiment information dialog box that is displayed at the start of the task.

Reference
-------------------

Peirce, J.W., R.J. Hirst and MacAskill, M. 2022. "Building experiments in PsychoPy"
  Sage Publishing.
