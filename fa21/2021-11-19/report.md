# Report - Week of Nov 5, 2021#

## Activities/Accomplishments,  and Concepts/Lessons Learned ##

### Activites & Accomplishments
- completed coding of:
    - animat.py
    - controller.py
    - modifications to leg.py, hingedsegment.py

I continued the rest of the architecture this week, based off the proposed architecture document plus plenty of ad-hoc additions as I got the ball rolling. 

One of the main changes is that animat now only handles the movement of the legs and the collection of data. Choosing a gait (and later a speed), designing the animat, and plotting the info will all belong to the controller class, which is heavily influenced by command line arguments. 

The basic structure is like so:
- controller takes in command line arguments for how far the animat travels, what it looks like (num of legs and segments) and builds the animat and the plot that it moves on.
- animat is then called to move. it propagates the move instruction and the appropriate gate to each of its legs, assigning goals based on the stage of the gait it is in (each leg gets a FootState that determines where and how it'll move). 
- The legs each perform their move, propagating backwards (bottom to top) through their segments. They store the position of each segment in the form of (startx, starty), (endx, endy) and return a list of those positions once they've completed their move. 
- the animat receives those states once all the moves are finished, and compiles them into a data structure mimicking its leg array. it sends that information to controller as the final part of its move function
- controller recieves all the state information. It then has to create actors on the graph it wants to plot on. The data structure for the actors looks like one row of the step states array, so it is easy to update the actors to look like any one of the given positions when called to update. 
- controller then displays the animation it creates. 




## Issues/Problems
- matplotlib was installed as a library but not accessible when I tried to run the program. I'm on a borrowed computer, so I chose to simply install anaconda and make a new environment. Took some time, but no big deal.
- I ran into the issue of where to define the animat's position. After talking through it with Prof Clark, we decided it should be the midpoint between hips. that introduced the need for updating that midpoint and therefore the hips. It wasn't a huge deal to implement, but most of the code operated on the assumption that the front left leg was defined as the position, so a little bit of finaggling was necessary.
- various small bugs, which I'm working through. Some notable ones were:
    - i couldn't have functions inside of Pt return type Pt. Those were optional type annotations so I removed them and fixed the issue easily enough that way, but I was confused as to why that would happen. I think something similar happened with HingedSegment earlier and unfortunately I forgot the fix I used then.
    - gait isn't being passed in correctly. I made it an enum such that WALK might equal a long array of footstate tuples, but when I try to call it based on a command-line arguments, my asserts trip because len(gait) is 1: ["WALK"]. A weird interaction, since I've never used Enums before. But shouldn't take long to fix. I had already googled a solution but didn't have time to implement it this week. 
    - the regular `if __name__ == "__main__"` call didn't work. I looked it up and it might be because I ran some of the other files first? I'm not really sure but the issue was easily solvable just by calling main in the top-level part of the file.

## Plans for next week
- modify controller so that it can read in a file of configurations. maybe need to talk to Prof Clark about this to see what would be more useful, but I imagine going one by one wouldn't be desirable if we're trying to build a large dataset
- create a GUI system (maybe interchangeable with the previous point). I spent some time researching and think it can be done with a tool called tkinter, which is available through the python standard library. I thought this would be good so that we can see the inputs 
- implement the various todos. the most important would be enforcing hinge angles. I think we would need to make modificaitions to HingedSegment such that it accepts a hinge range. We could then modify animat's leg builder to pass in appropriate ranges (where do we find those?) and enforce those ranges in the move function for the leg, where we update the individual segments. 