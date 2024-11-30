Exercise 9.1 use multiple sliders at once
=============================================================

In this exercise we are extending the Müller-Lyer illusion thar we made using slider stimuli in PsychoPy. This is really just a bit of "practice makes perfect" for what we already learnt in the Chapter! Adding a slider and then using it's marker position to set a property of a component.

Solution
------------------------

Add a second slider and call is possSlider, we then use that slider in the position field of our adjustable line::

	(posSlider.markerPos, .2)

and remember to set that position field to update every frame. 

References
------------------------

Peirce, J.W., Hirst, R.J., and MacAskill, M. (2022). "Building experiments in PsychoPy." Sage Publishing.
