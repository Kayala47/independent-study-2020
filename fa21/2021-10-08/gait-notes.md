# Notes on Gait Python Program

## FootState
= an enum that translates ints 1-4 into different states.

My current understanding is that:
- Swing = leg currently moving
- Lift = leg going up from ground
- Thrust = ? (how is it different from swing?)
- Support = probably on the ground, waiting for otehr leg



## Leg Object
- initiated with: stride: float, state: FootState, foot_x: float, swing_y: floa
    - of these, I only understand FootState so far, and barely that
- swing and not swing functions ask for the FootState
- motion step: it seems the purpose is to return data about position, but it also sets the state of the leg
    - if the foot isn't swinging and is >1 half stride behind hip, start swinging.
    - if it isn't swinging but doesn't meet previous condition, don't do anything
    - if foot is swinging but more than a half stride past the hip, set footstate to ground (I'm guessing that means it's not moving, but stable on the ground). But also: this option is commented to be removed, so what does it mean?
    
    questions:
    - no check for other legs? can all legs be swinging?

- create actors: what is the ax variable? it's a set of Axes as far as I can tell, but what is it for?
    - TODO: find out what .plot returns

## Animat Object
- typo for Animal? or maybe "thing to be animated"?
- initialized with only two legs
- motion_step: 
    - new_x input makes me think this causes movement, which seems to be the case, as hip_x is updated. Unsure what "change to body" comment means
    - returns pose of every leg, but comment makes me think it's not quite accounted for yet
- generate_poses:
    - for every position from curr to finalx (input), generate a pose
- create_actors:
    - hinges on leg.create_actors, which I don't understand yet
- update_actors:
    - unsure. frame_index? It seems we're adding data in for each leg, based on foot_poses that we get from the poses array
- animate:
    - not sure I understand what's going on here


Simplify_angle:
- get all anges within pi? or at least one pi closer

## Pt Object
- initialized as x,y coord
- sub: subtract two points with both x and y (overwrite)
- classmethod: allows for calling this. normally this is used for creation in other methods. any reason this couldn't be a regular function?

## HingedSegment object
- init: given the angle and length of a segment, maybe originating from a parent
    - else statement is simple. if parent is hingedSegment, runs update_from_parent, but where does self.chi come from?
- update_from_parent: unsure where self.chi updated, or what it means

## SegmentChain Object
- init: given a list of angles and lengths, appends them together to make the chain
    - last segment is the "effector"