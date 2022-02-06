# Report - April 6, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##

### Concepts:
- Airsim, Scripted movement
- Custom Airsim environment
- Migrating actors



### Accomplishments:
- Built Airsim on my own machine
- Downloaded and explored the Landscape Mountains airsim base project
- Installed Visual Studio (without breaking VS Code this time!!)


## Activities:
- Spoke with Michael on P-ai about his own work with computer vision
    - his team is using Airsim, which can be configured to run with either a drone or a car (like, big SUV)
        * Michael thinks he remembers seeing an option to change the skins of the vehicles, so perhaps you can make it smaller and look more like a rover also
    - you can set a spawnpoint in airsim and control the movement (by setting locations for it to go to)
    - they're still trying to figure out how to feed it data from the convolutional model
    - most of the work is done through API calls. You have to pass airsim the actor and let is assume control.
    
- Did some research on Airsim and Ardupilot
    + Ardupilot has support for rovers, which is going to be great for us!
    + Tried to read through as much documentation as possible. I'd done this before, last semester, but the notes are crispy so it was helpful to go through it again.

- Set up Airsim on their testing environment and followed some tutorials to learn more about it. 
    + https://microsoft.github.io/AirSim/unreal_custenv/
        * important steps here are including Airsim in AdditionalDependencies and in Plugins

- Had to install Visual Studio on the way. That took forever.





## Issues/Problems
- Found it hard to port over the rover vehicle in Unreal
    + Solution(ish): some research revealed that ArduPilot has support for rovers in collaboration with AirSim. Maybe we'll just end up using those anyway, so I'm going to stop attempting for now
- Everything about Visual Studio is slow. I'm not sure why, but even opening up the solutions file was much slower there than in VS Code. It was parsing way more files than VS Code ever did. 
- When putting in the Airsims plugin, I had to do a complete rebuild for both projects I tried it on. Also for both, it couldn't do an automatic build when it loaded, and recommended a manual build.
- Pretty serious issue: I somehow corrupted my freshProcedural file. I think because I didn't add a blank class in there, Unreal refuses to generate a solution file, which means it can't load airsim and won't open the editor, further preventing me from adding that empty class.



## Plans for next week
- Try to salvage the freshProcedural file and get a new environment working.
- Continue going through Airsim. Try to set it up on the environment I've built, with the maze. 