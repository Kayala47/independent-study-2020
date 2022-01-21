# Report - Week of Jan 21st, 2022 #

## Agenda ##
- Finish Trot
- Debug sub-ground movement and maybe prepare for a meeting to fix it

## Activities/Accomplishments and Concepts/Lessons Learned ##
1. Designed and implemented trot.

This one took a couple of attempts because I wasn't sure how to account for that one phase where all the legs are supposed to be up. I first tried a system where I would add a large number (10) to all the stages, which puts them in a situation where they need to discontinue their current action in order to curl up. Because I added 10 to all of them, I could then subtract it for all of them and put them right back to their original position, without a bunch of checks. 

That didn't quite work, and really was adding more messiness than necessary. The next attempt was just to use the stages system. I was wary of changing it before, but then I just started to think that I could handle mini-steps like "curl forward" and "curl backwards". The problem was, it ended up being like 6-8 mini-steps, and I thought it was going to be unnecessarily complex. I didn't really know what a better option was until I looked at the [animations](https://mymodernmet.com/animal-gaits-animation-stephen-cunnane/) again. I noticed that this page highlighted the legs on the same side, as opposed to the paper, which focused on the movements of diagonal legs. They do the same thing of course, but it gave me the insight that the front and back leg on each side are moving towards and then away from each other simultaneously. I realized that the "suspend" step was already being handled by the leg's natural movement, if only I could get the current system to skip the times when no legs were supposed to be stepping. Now, I just `continue` when there are no feet in the current foot order, and that means that the back step of the front leg and the forward step of the back leg line up nicely to give us the suspend state. 

2. Debug sub-ground movement

This one has been a doozy. Just from print statements and such, I can tell that clipping the points at the ground *does* work, sort of. No points are assigned as goals where the point has a y value lower than the ground. Unfortunately, that still doesn't solve our issue. 

I think I've narrowed it down to this: when the start position is on the ground and the ending position is also on the ground but backwards, move_tip doesn't lift up and go backwards, it pushes down. That causes it to swing like a pendulum to reach the backward step stage, and that's what causes it to dip below the floor. 

I've poured through the difference between the first working commit (which doesn't *seem* to have the same issue), and my current version. There don't seem to be any changes to move_tip, and of the changes to taking a step, nothing I can find that would cause it to skip below the ground. In my head, mine should be less likely to dip below, since it actively clips the y value to never go below the ground. But I can't be sure.

3. Change return files to just angles

Fairly easy, I just filtered out the actual position of each segment, since we don't care about that. We also want to return a config file for the animat, but since that's included in sample_json, we've already got it!

## Issues/Problems
The issue with touching the ground is hard for me to debug. I worry that I might have to re-write some of move_point, in a way that I'm not sure I understand. I think I might have to meet with Prof. Clark on this one, because I'm not really sure where to start.


## Plans for next session
Meet with Prof. Clark about the sub-ground steps, and then start to think about next steps for getting this into the model. 