# Report - Week of Oct 8, 2021#

## Agenda, Activities/Accomplishments,  and Concepts/Lessons Learned ##
### Agenda
1. Install Unreal Engine and set up maps as detailed in the [Creating Maze Project section on the repo](https://github.com/anthonyjclark/raycasting-simulation/tree/master/Unreal)
2. Check out the [Gait repository](https://github.com/anthonyjclark/gaitpt/blob/main/gait_pt.py) and start learning about it

### Activites & Accomplishments

#### Unreal Setup
Installation required an account, so I used my personal. I've set it to not require any extra sign-up, but would potentially like to see if we have a lab account so we can link it there directly. I just went ahead and did it with my personal so I wouldn't slow our progress any more. 

I initialized the project with name = "Maze". The notes on enabling Plugins were a little confusing but I found that going to Edit > Plugins I could enable individual plugins. I didn't have the plugin for unrealcv made yet so I had to stop and make that.  
- Note:  I got a permission denied error when trying to build using powershell. Worked fine on regular command terminal in Windows

Installation didn't work on 4.27. I remembered that last time we ran into issues because the unrealcv package had to be changed slightly to deal with the correct version. Knowing that 4.26 worked before, I uninstalled Unreal and installed version 4.26.2. 

While that installed, I worked on a new branch of the gait repository, wherein I tried to add a docstring to each function, based on my understanding of them. I can't guarantee their accuracy, but I think during the pull request process I'll learn a lot about how it works and the accuracy of those docstrings will improve. 

Back to Unreal: I got all the textures added and made into materials for use in the cubes. I've uploaded the mazes also. Now, I'm struggling with running the SetupMaze file. 



#### Gait
I'm going through the python file and taking notes as I understand it. Those notes should be pushed to the repo as of this writing. 

The intent is to submit a pull request once those have been checked off and add docstrings for each function, both helping me understand it and still accomplishing some work by commenting our code. 

I've submitted the initial pull request, although not all functions are tagged. Most of the ones that need documentation are because I don't fully understand what's going on, so might be good to talk about those.



## Issues/Problems
- Python not installed on lab machine.
    - Solution: installed Anaconda and created environment for unreal
- UnrealCV build failed... I think it had to do with needing a version of .NET framework SDK at 4.6.0 or higher, based on error logs
    - Solution: Installed .NET framework 4.8.0 from Microsoft
- UnrealCV build failed again: this time the error is C2248 "UActorComponent::bIsActive cannot acess private member declared in class UActorComponent
- Epic Games Launcher could not be uninstalled
    - Solution: Epic leaves a lot of processes running when you close. I hunted them all down with task manager and was able to uninstall when I got them all.
- Unrealcv build failed because Visual Studio 2017 was not installed. 2019 was installed.
    - Solution: installed 2017 version. Made sure to install .NET framework of 4.6 or higher. Build successful
- SetupMaze.py failed: cannot import name Vector from 'unreal'.



## Plans for next week
- Continue working with gait.py
- Talk about next steps with Prof Clark
