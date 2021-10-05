# Report - Week of Oct 8, 2021#

## Agenda, Activities/Accomplishments,  and Concepts/Lessons Learned ##
### Agenda
1. Install Unreal Engine and set up maps as detailed in the [Creating Maze Project section on the repo](https://github.com/anthonyjclark/raycasting-simulation/tree/master/Unreal)
2. Check out the [Gait repository](https://github.com/anthonyjclark/gaitpt/blob/main/gait_pt.py) and start learning about it

### Activites & Accomplishments

#### Unreal Setup
Installation required an account, so I used my personal. I've set it to not require any extra sign-up, but would potentially like to see if we have a lab account so we can link it there directly. I just went ahead and did it with my personal so I wouldn't slow our progress any more. 

I initialized the project with name = "Maze Project". The notes on enabling Plugins were a little confusing but I found that going to Edit > Plugins I could enable individual plugins. I didn't have the plugin for unrealcv made yet so I had to stop and make that.  
- Note:  I got a permission denied error when trying to build using powershell. Worked fine on regular command terminal in Windows



#### Gait
I'm going through the python file and taking notes as I understand it. 



## Issues/Problems
- Python not installed on lab machine.
    - Solution: installed Anaconda and created environment for unreal
- UnrealCV build failed... I think it had to do with needing a version of .NET framework SDK at 4.6.0 or higher, based on error logs
    - Solution: Installed .NET framework 4.8.0 from Microsoft
- UnrealCV build failed again: this time the error is C2248 "UActorComponent::bIsActive cannot acess private member declared in class UActorComponent


## Plans for next week

