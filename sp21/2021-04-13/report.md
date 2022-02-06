# Report - April 13, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##
Unfortunately more issues than solutions this time around. Mainly, I couldn't get plugins to work and spent a lot of time following tutorials and solutions to fix it. Haven't had any luck setting up UnrealCV...

### Concepts:
- Airsim
- Unreal CV
- Python Scripting in Unreal


### Accomplishments:



## Activities:
- installed Unreal version 4.16.3 (for use with Unreal CV)
- investigated UnrealCV and Airsim libraries further

I spent a lot of time trying to get either of Airsim and Unreal to work. For whatever, reason, I just can't install new plugins. I'm actually not sure what's wrong anymore. Installing Rama's on my procedural generation project was totally fine, but no other plugins are working, even though I'm following the exact same procedures as I did that time.

For the project on a previous version of Unreal, i'm pretty sure the problem is that it's not generating an sln file. Normally I'd do this by creating a new C++ class in the project, but it won't let me do that for some reason. I shows a C compilation error. The option to generate an sln file in File Explorer therefore does nothing (there needs to be at least one C++ file for that to work). Building with Visual Studio also isn't working. I'm trying to work through the bugs there. 





## Issues/Problems
- UnrealCV won't work with the current version we have running
    + which really sucks because we were hoping to use an even more advanced version later. The developers just haven't updated it in a bit, I guess.

- Couldn't install any plugins. Whether it was the Python scripting plugin, UnrealCV, or Airsim, nothing seemed to work. I went through several youtube videos and forum posts, but nothing seemed to fix the issue. Here are the things I tried:
    + https://community.gamedev.tv/t/unreal-not-creating-sln-file/69997
    + https://answers.unrealengine.com/questions/541257/how-to-generate-sln-file-from-launcher-downloaded.html
    + https://forums.unrealengine.com/t/how-to-generate-unreal-visual-studio-solution-files-into-specific-folders/86913
    + https://stackoverflow.com/questions/42591342/how-to-generate-unreal-visual-studio-solution-files-into-specific-folders
    + https://www.reddit.com/r/unrealengine/comments/5t0hm5/creating_c_class_breaks_project/

- UnrealCV training binary not present anymore. They want you to use the RealisticRendering model but the site they link to doesn't have it. The marketplace also doesn't have it, and most of the others in the model zoo are paid :/.



## Plans for next week
- Set up a meeting with Prof Clark to try to fix the issues with Unreal CV and get started on that. Either UnrealCV or Airsim look promising. 