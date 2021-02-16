# Report - Feb 2, 2021#

## Activities/Accomplishments and Concepts/Lessons Learned ##
Concepts:

- C++
- Procedural generation of terrain
- Levels in Unreal Engine 


Activities:

- updated to new version (4.26.1)
- watched more of the crash course
- created clean project
- successfully implemented procedural generation

I started out just wanting a clean build of the environment I'd be working in. However, Unreal wanted an update. So I worked on the crash course for a little bit, working on things like structs, pointers, and operations on strings. 

It soon updated, and then the fun began. I followed this [this amazing tutorial](https://www.youtube.com/watch?v=VmRggTwhiew&t=337s&ab_channel=PubGames) to get them procedurally generated. It took surprisingly long just because he often went really fast and didn't explain certain bits, but I think I understood how to do it well. 

The gist is: I started off with some simple levels, which I created by hand just by putting different sized blocks in different positions. Then, there was some fancy work done in the level blueprints to randomly load those levels in to a coordinate on our one persistent level. Since each of the procedural levels only had a couple objects, we are able to get a lot of variety out of just a small amount of layers. 

Here's what the blueprint looked like:

![Bluepring](proc-blueprint.png)

It is a mess, because following the tutorial took some research. But you can see that it is mostly two nested for loops, which go through the length and width of the persistent map and add a small procedural general to each piece randomly, making sure it loads and is visible. 

Then we do some math to get the pieces where we want them. Since 0, 0, 0 is actually the middlepoint and not top left as we're used to in CS, we subtract half the size of the map, which is what all those light and dark green lines you see going into the transform are. 

The pink represents the array of procedural levels, which fills in the instance on the blue box in the corner, beginning the loading process. I also added unique names to each generated square so that we can debug or possibly add more later. 

The end result was pretty spectacular. I started with just 4 levels, which you can see here: 

![All Levels](all-levels.png)

In the image, they're all layered on top of each other. You can see that they're each just small cube parts in different patterns. In the blueprint, I created a 10x10 grid to fit these into, so the procedurally generated levels will look something like this: 

![Generated](fully-generated.png)

In the above image, none of the individual levels are visible. Rather, you're seeing these randomly generated bits overlayed on the one persistent layer. Note that the light sources are not generated along side it, which I think is more realistic. Those stay on the persistent level. However, we can change that up as needed for our maze.


## Issues/Problems
- Had some trouble tracking the video at times. He uses lots of keyboard shortcuts which can leave the watcher hanging. For future readers of this report, I watched at 0.75 and still had to rewing, pause, and look stuff up. 


## Plans for next week
- Definitely work on cleaning up the blueprint first and foremost
- Add the rover vehicle to these maps and see how placing that works on blueprints. This might take some research, but I'm assuming it'll be important to control where the rover starts. 
- Pretty some of these levels up. I'm fairly certain it should be easy to match the colors and textures that I saw in Prof Clark's raycasted version. I need to recreate those asap. 
- Finally, figure out how to read in text and use a textfile to generate the maps. I'm thinking I'll have levels for: clear, wall (with different colors), and exits. Then, we can add the first two based on the text file and add in exits as well. This should be doable with Rama's extension. 
