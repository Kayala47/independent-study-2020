# Report - April 13, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##
### Accomplishments:
- installed UnrealCV (with help :) )
- wrote script to send commands to Unreal... successfully!!
- relocated rover camera to remove obstructions in field of view. Also removed sound!
- added Project to Git

### Concepts:
- scripting with UnrealCV
- Unreal commands


## Activities:
After I met with Prof Clark and we managed to install the correct version of UnrealCV, the program loaded fine.

Note for future readers: you'll have to compile the project to a binary yourself. All the projects listed under UnrealCV's project zoo cost ~$60. You can download the latest version [here](https://github.com/unrealcv/unrealcv). Currently, you'll need to look at the branches of the repo for the version updated for 4.26.

Thereafter, I started working on coding up a python file to send these commands. For the sake of being able to make changes and send commands on the fly, I made a jupyter notebook. To summarize the procedure: the UnrealCV library has a command called "request" that lets you send commands to Unreal. Some of these are built in Unreal commands, and some are made by the UnrealCV team. A full list is detailed [here](http://docs.unrealcv.org/en/master/reference/commands.html).

- NOTE: blueprint commands aren't well-detailed there. I had to look them up separately, and [this forum](https://forums.unrealengine.com/t/call-blueprint-event-from-console/9245/6) had the information I needed. 


I played around with a lot of the commands, and now I'm able to take and save screenshots and change some settings about the game. I haven't been as successful with blueprint commands, which I think will be the most useful for taking pictures. I think I'll actually move away from physically moving the rover and move towards teleporting it a couple feet ahead. This way, we don't have to worry about it shaking or continuing its momentum. That'll require blueprint commands, so I really need to get those working ASAP. 

## Issues/Problems
- In the [instructions on generating a binary file](http://docs.unrealcv.org/en/master/plugin/package.html), it says to adjust one of the settings files ("Engine\Config\ConsoleVariables.ini") by adding the following line to the end:
> r.ForceDebugViewModes = 1

I couldn't find the file, nor change the setting elsewhere. They made it seem like it was crucial to UnrealCv working properly... which, is maybe not true since I got it to work, but it does concern me. I'm going to spend some time this week continuing to look for it. So far, my Google Fu has not been enough to find it.




## Plans for next week
- Updates to Unreal Project
    + Change the textures in the following ways: 
        - Add a texture for turns, which consists of a cube wrapped in arrows
        - Change floor texture to the one used in raycasting
        - Change the wall texture similarly
        - Update the lighting (it's too bright!)
    + Fix the leveling of the floor. Some of them are higher than others, which causes wobbliness. This may be fixed naturally when I switch to teleportation anyway. 
    + Anything I missed?
- Create tutorial for setup from scratch
