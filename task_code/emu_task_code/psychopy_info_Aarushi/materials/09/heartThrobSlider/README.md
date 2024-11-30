Slider demo: dynamic heart throb
================================

This is a demo of how to use sliders locally and online. Currently there are some subtle differences between sliders locally (in PsychoPy) and online (in PsychoJS), so this demo aims to help explain how we can make the most out of sliders locally and online. 

Useful slider attributes
-------------------------

*	`.markerPos` *or* `._markerPos` accesses the current marker position (locally and online respecitvely). Note that by default a marker is not displayed on the slider untill a response has been made, so in this demo we use a code component to only poll this attribute once it exists. Untill we have a rating, we provide a default rating of `thisRating` in the begin experiment tab. 
* `.rating` corresponds to the provided rating. This attribute is created/updated when the participant stops moving the marker (e.g. by no longer pressing the mouse key). In this demo we save that final rating using `thisExp.addData` or `psychoJS.experiment.addData` respectively.

Making things dynamic
-------------------------

<img src="/figures/heartthrob.gif" width="80%"/>

The fun thing about this demo is that stimuli are dynamic, i.e. stimulus attributes are updated on every frame to give the appearance of motion/pulsing. In the heart  image, in the `Size [w,h]` parameter we have used code to set the current size of the heart based on the formula for a sine wave. In this formula we have the start size of the hear in height units (.25) the minimum size of the heart in height units, which is half it's maximal size (.125), we then use the formula:

*sin(t x thisRating)) ^ 4*

Where *t* is the time since the start of the routine (this is actually a variable always available "under the hood" in PsychoPy, we don't have to do anything to create it), *thisRating* is the current position of the slider marker (fetched in rate code - *Note: the only reason we use code here rather than directly feeding marker position into the size parameter of the heart is because a) the marker pos doesn't exist untill the user clicks on the scale and b) the attribute names for marker position subtly differ between PsychoPy and PsychoJS*). We then change the shape of our sinusoid to the power of 4 to alter the shape of the curve and make it more "pointy" - this will make our throb seem more "pulse-like" because it will be small most of the time and then large briefly. 

We can also save the size of the heart on every frame, along with its timestamp using *t*:

```
thisExp.addData('heart_height', heart.size[1])
thisExp.addData('time_stamp', t)
thisExp.nextEntry()
```

In the each frame tab (note the different between thisExp in PsychoJS for online use), then we can plot the size of your heart to see the produced wave! You can find a custom script here called `heartthrob-plot.py` in the analysis folder.

<img src="/figures/excitement-plot.png" width="80%"/>