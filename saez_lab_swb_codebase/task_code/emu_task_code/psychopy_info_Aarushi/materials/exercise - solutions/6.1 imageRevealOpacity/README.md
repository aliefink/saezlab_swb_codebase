Image reveal opacity
===============================================

This is a basic demo of changing stimulus parameters dynamically, here we dynamically reveal an image by increasing its opacity from 0 to 1. If we are changing something dynamically, we make sure to set that field to "set every frame" because want our image to be fully opaque at 5 seconds, we can utilise the variable `t` that exists "under the hood" of all PsychoPy experiments and set the opacity field of the image to be `t/5`. Remember *t represents the time in seconds since the start of the routine*. 

References
--------------

face01.jpg image obtained from: 
 Creative Commons Attribution 3.0 Unported (CC BY 3.0)
 https://commons.wikimedia.org/wiki/File:Obama_portrait_crop.jpg
 Pete Souza/Notwist

Posner, M.I. (1980). "Orienting of attention". Quarterly Journal of Experimental Psychology. 32 (1): 3–25.
Peirce, J.W., Hirst, R.J., and MacAskill, M. (2022). "Building experiments in PsychoPy." Sage Publishing.
