# Report - March 1st, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##
### Concepts:
- Lighting and debugging in Unreal
- Reading text files
- Advanced blueprint logic in Unreal



### Activities:
I first spent some time debugging what was going on with the lighting. I'll detail the issue in more detail in the section below, but the gist of it is that lighting seemed to have been built differently for each level - which it was :/. 

The solution(s):
- I went through each level and deleted any other lighting elements. The goal was to have lighting only in the main, persistent level that would affect all other levels. 
    - NOTE: sometimes the lights liked to hide. Even with object meshes on I couldn't find many of them - and that was on a mostly empty map! Remembering to use the World Outliner was a lifesaver!
- Then, I ran into the issue with weird shadows in the levels. Again, long story short, you shouldn't build all the levels at once. I paired the persistent level with each of the others, one at a time, and rebuilt that. That produced a solid image. 

![picture of newly rebuilt lighting](lighting-rebuilt.png)

Lastly, I spent a lot of time reworking the blueprints to make them readable, as well as to add the funcitonality to read in strings. It read the string in fine, but I wasn't able to correctly implement the feature. The main thing holding me back was that apparently Unreal doesn't support 2D arrays, or does but the documentation has escaped me. The advice is to wrap it in a structure, but I don't know how. For now, I think I'll continue using a flattened array and using the transforms to place them properly, but there are a host of smaller issues I need to fix first, like the fact that it only adds the first 9 numbers to the array.



## Issues/Problems
- Inconsistent lighting:
    - Cause: Hidden lights all over each of the levels, that Unreal automatically puts in to be "helpful".
    - Solution: Use the World Outliner to find and delete all of these. Worst offenders are the skylights.
- Random Shadows in levels:
    - Cause: multiple levels built on top of each other left traces of themselves all over, often inconsistently. 
    - Solution: Build each level independently, while the others are hidden. In my case, I had to have the persistent level unhidden also, since that was the one with the lighting source.
- no support for 2D arrays in Unreal
    - Cause: ?
    - Solution: you can use a flattened array detailed [here](https://answers.unrealengine.com/questions/180534/two-dimensional-array.html) or use
        - NOTE: one of the answers to this question details a 2D vector, but no supporting documentaiton, so I can't recreate it.
    - Missteps to avoid: 
        - tried out [this plugin](https://www.youtube.com/watch?v=4BI_CPYIRvs&feature=youtu.be&ab_channel=SaurabhSharma) but it no longer works




## Plans for next week
- Continue debugging
- Finish this feature
