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

