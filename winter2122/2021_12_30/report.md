# Report - Dec 28, 2021#

## Agenda ##
- Finish test cases for Animat
- Start / finish coding Animat


## Activities/Accomplishments and Concepts/Lessons Learned ##
I started out by just diving into coding Animat. Yet, at every step there seemed to be other stuff that needed adjusting in other files. Things like different ways of creating legs kept popping up.

Re the legs: I decided to go with two classes for them: one that could create legs based on a more detailed specification (ie, given all the segment lenghts for each leg) and one that made equal length legs based on other factors like height of the animal. Those are routed to by the main "create legs" function, depending on which arguments are passed in. I came up with test cases to make sure that was happening correctly (and learned about the very helpful 'Mock' wrapper from unittest along the way!). 

I had to change a lot of the tests in Animat to make sure that they would fit the new architecture, but I'm happy with the new structure. 

Then, I started working on other little details that were necessary. First, I realized that HingedSegment class currently had no way of adding a new child. Since it wasn't a parameter in the init function either, that meant none of our segments were being attached to each other! So I went ahead and added a quick function for that, then modified Leg so that it would automatically add children to segments as it went along building itself in the init function. 

There are still a couple of things on my mind:
- I'm worried about how location is handled in HingedSegment. I think I have it set up to correctly track its parent's tip location as a starting point, but I'm not sure how well it will hold up to updates. This will propagate to Leg and I want to make sure it works correctly.
- the move function of leg needs to be re-written entirely.
    - related note: i've added a 'max_angle' parameter in HingedSegment so we can implement movement restrictions down the line



## Issues/Problems
- I feel a little overwhelmed with the scope of planning everything. Some good tools / advice for architecture would be much appreciated.
- At every step, I feel like I want to start from scratch. I'm wondering whether to keep fighting that urge. I think I will cave at least far enough to add test cases to leg and hinged segment and try to un-confuse myself there

## Plans for next session
As above