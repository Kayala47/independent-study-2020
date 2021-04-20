# Report - April 13, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##


### Concepts:
- Custom game modes Unreal
- Asset migration
- Actor blueprints


### Accomplishments:
- Successfuly migrated vehicle blueprint to freshProcedural
- Successfully spawned vehicle actor in correct location
- Set up input controls


## Activities:
I decided to focus on importing the actor asset this week, since I didn't have time to schedule a meeting with Prof Clark. It was pretty productive. I managed to set up the blueprints such that the little rover spawned into the maze at a good position. 

I also set up movement controls so that it could move with the keyboard. However, i didn't get pawn possession to work; that is, the game doesn't start out with the player possessing the rover. That was frustrating, and I still haven't found a good fix for it, but i'm convinced I can resolve that soon. 

Lastly, I had to do some reworks on my original blueprints because I found out my tileSize variable is wrong. It seems to work fine now, but there's a deeper issue with the blueprints, because the sizes are just not matching up and i'm worried that's going to affect the positioning of the maze objects. 

Tutorials:
- https://www.youtube.com/watch?v=i59AKLodlAM&ab_channel=InfuseStudio
- https://www.youtube.com/watch?v=PpVfL2OhkmI&ab_channel=UnrealEngine
- https://forums.unrealengine.com/t/spawn-actor-from-blueprints/3495
- https://www.youtube.com/watch?v=z7WG-Vr3iCY&ab_channel=FattyBull


## Issues/Problems
- Small issue with the inputs not working correctly at first. 
![](input_errors.png)
    + Solution: I just made sure all the inputs were included, including the ones for VR support. Also made sure the names exactly matched. No big deal.
- At first, the rover was spawning before some of the cubes below it spawned, which meant that it just kind of fell for eternity. Not fun. I tried using the sequencer to fix that, but for some reason, even though it was supposed to go only after the other stuff finished loading, it would just go whenever it wanted. So I ended up adding a blueprint to explicitly make it wait, but got this error:
![](delay-error.png). Then that blueprint also threw an error
    + I did a little bit of research on the Task Owner. I'm still not exactly sure, but I tihnk you connect it to some sort of threader or something. As I was researching, I found that there was a "delay" block that did what I wanted without any fuss, so I switched to that and sidestepped this problem. Still, maybe something to keep in our back pocket; this block seems more powerful than just a straight delay. 


## Plans for next week
- Meet with Prof. Clark (for realsies).
- Watch the last of the tutorials to try and make sure the rover moves as expected and the player spawns in as the rover. 