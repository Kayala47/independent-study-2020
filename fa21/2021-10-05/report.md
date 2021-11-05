# Report - Week of Nov 5, 2021#

## Activities/Accomplishments,  and Concepts/Lessons Learned ##

### Activites & Accomplishments
- Finished gaits.py file
- Finished adjustment of leg.py
- Finished proposed architecture document

I spent a lot of time looking at the gait website and tried to think of how I could represent them. I stuck with an Enum that was basically a list of foot states for each leg.

My first attempt was to represent gaits as either moving or not, and then have different sizes of steps, to represent speed. After talking with Prof Clark, I decided to instead not worry about encoding speed, but rather focus more on the different positions the leg would have. I settled on a hybrid of the FootState model he already had, with the new FootState representing the foot either being on the ground, moving, or suspended in air (useful for some of the gaits at the end of the website). 

That took a while to settle, but at that point I was able to more easily encode each of the 5 gaits represented in the website. I left out some in favor of just going ahead with the rest of the coding, but I'll go back and add them soon. 

Then, I moved on to the Leg class. Leg in my implementation actually looks a lot like SegmentChain in Prof. Clark's. The difference is: I've decided that it should only be responsible for making one small adjustment at a time. The job of assigning its goal positions and continuing to run steps will be given to animat class. I'm hoping that this choice will help better account for gaits where only some of the legs are moving at certain times, and especially to account for those gaits where suspension is used and thus momentum is needed. 

As currently defined, Leg will still keep track of all the states it took to reach a goal, and will return those states once it has reached the goal animat set for it. Then, animat will assign a new goal based off cycling through the given gait.

To control things like making an animat and choosing a gait, I'll have a Controller class. That might not be super necessary, as I can just have that be top-level code. But my goal is to make all of this as clean and especially modifiable as possible, so I thought it would be a worthwhile step. 


## Issues/Problems
- Unsure how to account for backwards movement of the leg (thrust from prof Clark's FootState?)
- need to include joint limits
- 

## Plans for next week
- Work on Animat, which will be responsible for most of the operations we need, from assigning goals and cycling through foot patterns in a gait, to plotting those steps. 
- Work on Controller, which should be easy enough after Animat: it will provide a plot, decide the number of legs and hips of the animat, and decide the speed at which it is traveling (since some gaits are identical except for the speed). 