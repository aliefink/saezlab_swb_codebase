Exercise 9.2 use a slider to change the volume of a sound
=============================================================

In this exercise we will dynamically change the properties of a sound using a slider. 

Solution
------------------------

1. First of all we need  sound component - in this case let's just use a tone internally generated from PsychoPy and make it last 10 seconds.
2. In the volume field of the sound we will use a variable, let's call it `thisVolume` and set that field to `set every frame`.
3. In a code component we use the begin routine tab to say what we want the start volume of the tone to be, then inthe eachframe tab we check a) has the participant clicked on the slider and if yes use that marker position to set thisVolume::

	if slider.markerPos:
	    thisVolume = slider.markerPos

References
------------------------

Peirce, J.W., Hirst, R.J., and MacAskill, M. (2022). "Building experiments in PsychoPy." Sage Publishing.
