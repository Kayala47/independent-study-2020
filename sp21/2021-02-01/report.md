# Report - Feb 2, 2021#

## Activities/Accomplishments and Concepts/Lessons Learned ##
Concepts:

- C++
- Procedural generation of terrain
- Levels in Unreal Engine 


Activities:

- installed g++ compiler for c++
- crash course on C++
- Watched Youtube video on procedural generation
- Read through forums, including one with links to paid procedural generation libraries
- Found the best youtube tutorial on how to do procedural generation

I started just by taking a crash course on C++. The course was C++ essentials on Lynda (LinkedIn Learning now, I believe). I watched at 2x speed, just trying to get the basics down. Pointers and references are still tripping me up a little, but actually it probably shouldn't be a big problem for this project. I also had to research a little and install a compiler. I ended up going with the [mingw-64 compiler](http://mingw-w64.org/doku.php). 

Anyway, after a couple hours of that, I moved on to learning how to actually procedurally generate some terrain. The first tutorial I stumbled on was a [21-part series](https://www.youtube.com/watch?v=WP-Bm65Q-1Y&list=PLFt_AvWsXl0eBW2EiBtl_sxmDtSgZBxB3&index=2&ab_channel=SebastianLague) using Perlin noise to generate the maps. It wasn't exactly what I wanted, but actually was a little useful. I didn't want to watch the whole thing because it didn't seem super relevant, so I went on some forums. [This](https://answers.unrealengine.com/questions/110369/how-to-create-a-simple-object-in-c-with-ue4.html) was the best advice I found. Trying to do it with a C++ class actually landed me in Issues #1 and 2 mentioned below, so I went looking again.

Luckily, I stumbled upon a [much better video](https://www.youtube.com/watch?v=VmRggTwhiew&t=337s&ab_channel=PubGames) soon afterwards. This one focused on using levels to generate the content. I don't know if its the recommended way or a hack, but it seems clever: essentially, you set up distinct levels, each with one object oriented in a specific way. To generate the whole environment, you actually just create a new instance of a level and place it where you want. Best of all, it can generally be done in blueprints (although I will still probably have to use C++ to do all the reading in and processing of the files). Since all we need to do is place walls of varying colors and orientations, this seemed perfect. 

I followed the tutorial and didn't quite get it right. In the picture below, you can see I made a new wall using a cube material. That was the level that was supposed to be copied and made into a wall on the opposite side of the rover, but it failed pretty miserably. I think one of the main issues is that the tutorial went really fast and I messed up the Persistent level so my x and y positions are off. I think to fix it I'll just have to start over and be more careful which things I delete. 
![](level-walls.png)
*The red arrow points to the wall that should have been copied*

As an added bonus, if I start over, I can make the walls appear on the existing racetrack, which has pre-built terrain, cameras, and lighting. That should save us a lot of time moving forward. 



## Issues/Problems

- When creating a new C++ class to generate an actor, I got an error that said to rebuild the project. I exited and re-opened the project, then got an error saying that the project couldn't be built. This was confusing, but luckily I hadn't put too much work into the first one, so I decided to make another, this time as a C++ instead of Blueprint project.
- When I went to build the new project, I got this error message:

![Error building project](build-error.png)

I could've sworn I had already installed a new version of .NET, but I went ahead and installed it again anyway. That didn't work at first, but after a restart I was able to create the new project.



## Plans for next week

- Despite the hiccups, I'm feeling relatively confident that I can finish this part by next week. They'll probably be bare walls at that point, so I'll have to work on making materials and making it look right afterwards. 
- Obviously, the above tutorial was for randomly generating the walls. Since we need them in specific locations for our maze, I'll have to do some research to combine reading in the files with getting the locations for the walls, probably by trying to read the text file positions proportionally to the map. 