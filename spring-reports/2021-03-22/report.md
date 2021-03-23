# Report - March 22, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##

### Concepts:
- File I/O
- Python/Unreal Engine pipeline


### Accomplishments:
- Created python program to process and separate file
- Installed Python plugin for Unreal
- Successfully generated from file

## Activities:

I created a python file to process the initial maze.txt file given and turn it into a bunch of useful files, all of which will be much easier to read into Unreal this way. I also commented it thouroughly, trying to get it to where anyone could pick it up and understand it. It's under the python directory in this repo :). 

Once I had that done, I had to do some editing of the Unreal blueprints until they accepted all the new files. I removed the old, hardcoded values and made sure the new variables updated according to the files I fed in. 

I also did some research and found that you can run Python scripts from Unreal! I was able to get my setup file to run automatically on loading of the project, which saves some time and opens the door for potentially loading many different files/mazes into one project simultaneously. 

To do that, I:
- Enabled Python Plugin in Edit > Plugins
- Created a new startup script in Edit > Project Settings. I provided the Content file as the folder to run the scripts from, and put my script there for now. 

Once all that was done, here's what the generation looked like:
![](images/gen-from-file.png)
I thought it looked really weird - the files supplied should've produced a nice maze. Turns out, I had messed myself up by providing a random Yaw rotation as a placeholder. Once I dealt with that, it looked much better:


![](images/finally-looks-like-maze.png)

As you can see, it still looks a little unfinished. Mostly, its the fact that all the corridors are only vertical. I do have horizontal walls, but the maze file just doesn't account for that. So I think I'll have to make some modifications to my script to put in different values for places where it should go horizontally or vertically. That'll help me place the correct textures there.





## Issues/Problems
- Initially, the maze was unrecognizable from the text file
    - Solution: Removed Yaw rotation from the level transform. Honestly, I'm not sure why I had that in there. I think I thought it would give more variety
    - Note: I'll still need the rotation later, otherwise the walls won't be right. OR I could reformat the whole maze file with different values for horizontal and vertical walls...


## Plans for next week
- modify script to make changes to file such that I can have different vertical and horizontal sections of the maze
- start using UnrealCV to pilot an agent through the course. I think good progress next week will be just having an agent move through according to the solution file.

