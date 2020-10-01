# Report - October 1st #

## Activities/Accomplishments and Concepts/Lessons Learned ##
- Started working with Blender to create meshes
- Learned how to import mesh and make it a character
- Created sedan character from mesh (provided by Unreal)


### Concepts:
- Working with blender
- Importing meshes as actors from scratch
- Cameras!


### Activities:
- I spent several hours trying to finish up the Udemy course. I went through the Blender portions, but it took a while simply because there was so much complexity. I was struggling to follow along because the instructor insisted on using keyboard commands to navigate
- Then, I followed [this tutorial on importing vehicles](https://docs.unrealengine.com/en-US/Engine/Physics/Vehicles/VehicleUserGuide/index.html). It was very helpful, although it assumed you have a mesh, which I didn't. I spent some time looking online for one, but couldn't find a free model. I did come across [this very cool customizable Rover](https://unrealengine.com/marketplace/en-US/product/rover), but it's too expensive. I finally had a facepalm moment when I realized one of the Unreal tutorials had a vehicle mesh. So I borrowed that.
- I finished putting the mesh in and made a new gamemode so that it would be the default player, but it doesn't seem to be able to accept input. I'm unsure as to why that is. Still, it's basically set up. As you can see, I added a camera to the front of it, since that's the sort of view our rover will take. (Incidentally, I don't know what the rover is going to look like. If you think having an accurate model in game would really help, I would love to see a blueprint).

![](vehicle-cam.png)

- I believe the camera itself will be able to record, which is why I added it to the character model. My hope is that it'll be able to pass inputs directly to the camera portion to create our database. 


## Issues/Problems
- Blender is super user unfriendly - it took me an hour or so just playing around to start to understand how to do things
- I'm having issues with my vehicle movement. I'm able to auto-possess now, but it seems it won't accept input. I've tried the following forum posts:
    - [Accepting Inputs Correctly](https://forums.unrealengine.com/development-discussion/blueprint-visual-scripting/1504764-simple-keyboard-input-blueprint-not-working)
    - [Setting actor to default](https://forums.unrealengine.com/development-discussion/blueprint-visual-scripting/1428-change-default-pawn)
    - [Correctly setting up pawn](https://answers.unrealengine.com/questions/594917/default-pawn-1.html)


## Plans
- Fix the issue with the vehicle. It may just be that, since I've been using this world to play around with, I've got the settings in a mess. A clean build for next time should help me prioritize the character
- Figure out how to record input. I've done some research with Sequencer and it seems like that's the move. I'll have to figure out how to get it to record for every keypress though, and storage will definitely be an issue, because this computer doesn't have much.
- I really want to start a course on machine learning, so I'll know what's going on on that side. 

