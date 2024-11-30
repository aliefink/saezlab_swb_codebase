Exercise 9.3 make a "temperature" slider
=============================================================

In this exercise we are entering a slider matrix... using a slider to update itself. All we need are 2 components, the slider and a code component!

Solution
------------------------

First thing about what attribute is changing dynamically in time, in this case it will be the marker color itself. so open up your slider component, shuffle over to the Appearance tab and use a variable in the Marker Color field `$thisCol` - remember to set this to update "every frame".

The next step is to define our variable "thisCol". In the colde component start by providing a baseline value in the begin routine tab. Let's start with a black marker by using the RGB values `thisCol = [-1, -1, -1]`. Then in the eachframe tab we can use the marker positions to update the red and blue fields of our RGB color::

	if slider.markerPos: 
	    thisCol = [slider.markerPos, 0, 1-slider.markerPos]
	    print(thisCol)

Here we aer just printing the value to our Std window of runner so that we can check this is working how we expect "under the hood"

References
------------------------

Peirce, J.W., Hirst, R.J., and MacAskill, M. (2022). "Building experiments in PsychoPy." Sage Publishing.
