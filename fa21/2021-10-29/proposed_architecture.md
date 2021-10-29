# Proposed Architecture for Gaitpt
It's my understanding that we're mostly focused on simulating different gaits as shown in the [Animator Notebook article](https://www.animatornotebook.com/learn/quadrupeds-gaits). 

That means we're looking at how to model a: trot, pace, canter, and gallop. Therefore, I thought to start by modeling those gaits and work my way up to the rest of the animal, using much of Professor Clark's code found in [his repo](https://github.com/anthonyjclark/gaitpt/blob/main/gait-pre-training.md).

## Gaits
As I brainstormed, I thought the best way to represent a gait was as an animation of sorts: if we have a sense of how each foot changes during each phase of movement, we can represent it more or less easily. 

I thought the best way to represent this would be to have a list of deltas for each leg. I think for typing I'll probably make this an Enum of sorts.

The challenge would be representing gaits where movement is symmetric. It would be simpler to have a system where you have to input the deltas for each leg, even if they're all the same. Also, we could probably put it on the user to provide the correct number of foot deltas. In the future, we might like to modify our architecture to do things like, for example, take in 3 foot deltas for a 6-legged creature and simply assign the delta to a pair at a time. But I think we'll start with more of the onus on the user, and refine it later.

For now, I think I'll start testing using constant values. I think later it might be nice to explore strides being relative to the size of the leg or the size of the angle between legs or the size of the angle between the legs and the y axis to the ground.

Once we have a way to represent gaits, we'll have to figure out a way to pass that information to our animat. 

## Animat
The whole animal will be composed of some number of hips and some number of legs. We might also want to draw a body between but that seems less essential. 

To think about it, I tried to start from bottom up and see which of the classes we needed to keep and what we needed to modify it.

### Point
We'll keep this class as written to represent any type of point we need. It won't have any responsibilities to other classes, but will be used often for coordinate movement.

### HingedSegments
Since feet don't really work any differently than other parts of the leg, this is the smallest component of any leg. We'll keep this basically as written.

Each HingedSegment will be responsible for knowing who it's child and parent are, and for continuing the propagation chain that allows inverse kinematics to move the leg into position. It should also store information about where its tip is, since that's what we're pointing in the direction of our goal.

It should also be responsible communicating its position to be stored by Leg.

### Leg
We need some object to represent the leg, and we had two in the previous code: Leg and SegmentChain. I think we'll combine those here. 

The Leg's responsibility will be mainly to keep track of its component HingedSegments. It will hold a list of states for each segment, and lists for lengths and angles of each segment. It is also responsible for starting the chain of propagation when we want to move a leg.

Leg receives its foot delta and causes the movement required, then returns the information recorded. 

### Hip
This is a section that I'm not sure about. It might be an unnecessary level of abstraction that we don't need. Here is my pros and cons list:

#### Pros:
- If we move to having strides based on angles between the leg and the ground, that could be based on the hip's position.
- If we change our architecture to allow a user to pass in a gait where pairs of legs move in the same way, the hip holding each section of legs could be in charge of assigning those foot deltas correctly.

#### Cons:
- This might be currently unecessary. We could represent this with a point and retain the current functionality for HingedSegments. That would reduce complexity.
- We would have to re-work our Leg such that we could either have Hip be a parent, or otherwise let the Leg know which Hip it belongs to.
- We would similarily have to rework the Animat to keep track of its hips and which legs belong to which hips.


If implemented, the Hip would be in charge of knowing which legs are assigned to it, passing and possibly computing foot deltas for each leg it owns, and communicating information about its position and that of its component legs to the animat. 

### Animat
The class, not the overarching structure. This class will be mostly in charge of receiving the gait, processing it in whichever way we choose (for now, just assigning that directly to legs or hips) and then recording the movement information of each leg. 

The storage of positions is the most important, since the end goal will be to pass those positions to our model. 

We'll mostly keep this as written, though may need to modify it to include our use of Hip. 