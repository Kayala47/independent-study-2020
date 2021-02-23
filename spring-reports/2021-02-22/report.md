# Report - Feb 16, 2021#

## Activities/Accomplishments and Concepts/Lessons Learned ##
Concepts:

- Procedural generation of terrain
- Layers (Unreal Engine)
- I/O on Unreal Engine


Activities:

I spent some time re-installing Rama's extension (issue detailed below). After a little fiddling, I got it installed and working.

I spent quite a bit of time designing new levels and getting it to work with the previous logic. I did have an issue with the lighting: although the colors show up faintly, they're not quite perfect. Also, floor generation was weird - I'm getting a bunch of weird issues where blank levels that I didn't make are showing up. Lastly, the orientations of the levels sometimes show up differently, even though I've set them statically. I'll go into a little more detail in Issues, but suffice it to say, I moved on and worked on reading input for a bit. 

I fiddled with the different types of blueprints now available because of the plugins, and then settled on the ones I wanted. There is a "Load string array from file" blueprint that is really useful - it takes an array of strings, where each line of the file is one element in the array. Since each individual number corresponds to a type of level and the length of the string on each line is the size of our maze, it is exactly what we need.

Notably, that blueprint doesn't have a "start" input. I figured out that the way to make it run is to connect it to something else which does have a start, and experimented with the ticker functionality. That overwrote the file a ton but at least I figured out how it worked!

I connected that blueprint to a "save string array to file" to test it and it seemed to work fine. I've done some preliminary fiddling and can see how it'll work now: I'll read the array, then go through each line in a loop, chaining with some if statements to connect the correct number into the "load level instance" blueprint. From there, its business as usual, and I shouldn't have to change much more of the blueprint. I'll definitely need to remove some of the extra logic now that I'm not operating on random integers. 


Achievements:
- Pretty Levels! I made them as Prof. Clark described, so there are horizontal hallways, vertical hallways, a green beginning, a blue ending mark, a wall with a left signal arrow, and a wall with a right signal arrow. 
- File I/O successful!

## Issues/Problems
- Unreal officially terminated its official Wiki, home of the current Rama's download link. I spent too much time going down the rabbithole, but suffice it to say, I don't think their legacy database includes Rama's plugin. Here's a [link to an older version](http://www.mediafire.com/file/0q10k9...gin26.zip/file). 
    - Once you've downloaded it from there, you can unzip the contents and transfer that resulting file into a new folder in the same directory as your project's main directory (the one with the .uproject file). Make sure that the folder name is "Plugins" exactly. 
- Lighting issues. I think these stem from having different lighting sources in my levels, but I'm not sure where the came from. I haven't added them, and when I was following the tutorial, they didn't appear in the new levels I generated. 
    - For example, I'm seeing sky on lots of the procedural levels when there seems to be no object creating it. That throws off the overall lighting when the level is displayed, since the persistent level and even other procedurally generated levels don't have the same lighting. 
    - Also, the colors in the custom textures I put in aren't showing through. I did some investigating on the generated maps and it seems like it may also be a lighting issue, since at certain points its pretty obvious that light is drowning out the colors. Again, that's weird mostly because even when I delete the lighting sources it doesn't get better. I usually put the lighting sources back only because the maze is super dark without them, so I'll have to actually figure out what the root of the issue is soon. I wasted too much time investigating the lighting, so I finally decided to move on to I/O. 


## Plans for next week
- Speak w Prof. Clark and Jared to see what types of inputs I'll be getting, and if I'll need to adjust any levels.
- Implement the new file I/O generation. 
- Fix the lighting :(
- If time, make some nicer materials
