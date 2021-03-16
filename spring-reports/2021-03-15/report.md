# Report - March 16, 2021#

## Activities/Accomplishments and Concepts/Lessons Learned ##
Concepts:

- Procedural generation of terrain
- Levels in Unreal Engine 
- Compressed Arrays
- String functions Unreal


## Activities:

I implemented a new file reader, changing some of the files around in order to be supported by the tools I had available. Some of the changes I had to make include:
- flattening the file into one line, so that it could all be read as one string. Otherwise, the blueprints I'm using would only read the first line in.
- replace the spaces with x's, since the *Parse Into Array* blueprint wouldn't accept a space. I could think about potentially making a new variable for the delimiter, which would be a string. 

Here's what that looks like now:
![Blueprint for reading in new file to array](new-file-reader.png)


I implemented the procedural generation blueprints with the new array, and was successful. Here's what the blueprints look like:

![Finished blueprint](gen-blueprint.png)
You'll notice that I added an extra transform: yaw rotation. That means it can turn in any of 4 directions, which makes for more diverse maps. We can, of course, turn this off if we want a specific orientation. 


Testing it out, it seems to work ok. There are some small issues with the generation. I think I might have my compressed array slightly wrong, since it looks like the columns are too wide. I may have mixed up rows and columns. But as a proof of concept, it works!




## Issues/Problems
- Parsing a string into array didn't work with space as a delimiter. 
    - Solution: replaced spaces with X
    - Idea: write a script to do this for you. I'll need a script to break down the given file into a bunch of smaller, more specific ones anyway 

## Plans for next week
- write a script to turn the given file into a couple different ones:
    - one file for # rows and # cols. I'll read this separately
    - one file for textures, which I'll have to research how to put in here. Right now, I think if I add them manually I can just call them by reading their names from the file, but it would be interesting to see if I can load them programmatically.
    - one file for the map, which needs to be flattened into one long line, separated by x's instead of spaces. 
