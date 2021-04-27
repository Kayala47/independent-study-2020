# Report - April 13, 2021

## Activities/Accomplishments and Concepts/Lessons Learned ##


### Concepts:
- Conference decisions
- Related works
- Moving an actor in Unreal

### Accomplishments:
- Found three potential conferences to submit to
- Created a graph of related works and added a few of the closest to the doc


## Activities:
I looked at some conferences we could submit to. It looks like Jared beat me to the closest, but I was able to find a few that we can submit this summer and then present by the end of the year. Hopefully that's not too bad! There were a couple disappointing ones that looked really cool but had already passed. 

I wasn't sure what to say for the quality of each of these conferences - i'm not sure where those metrics would come from. I tried to stick to the ones that explicitly said "international" when they were not in the US as much as possible. Also read through a couple and decided not to include because they weren't our research area specifically. Hope that's ok! I recognize I don't have much experience here so let me know if I should just include available conferences indiscriminately.

For the papers, I tried to just read the abstract and summarize that in our google doc. I provided a link so hopefully we can check out the most relevant ones in greater detail. I also left the link to the graph so we can keep exploring that. It's a really cool site!

Afterwards, I moved back to Unreal. As of Sunday night I still cannot get the vehicle actor to be possessed at spawn. I can do it manually from the editor and have done some testing to make sure the vehicle itself works, and it does. It seems I don't have the correct grasp of the player controller. 

Monday night, after a lot more reading, actor possession is working! There were several things to get through:
- Possession through blueprints only works on a "server". This tripped me up for a long time because I wasn't creating a server (I thought). But I should've realized that the client itself is a type of host. You just have to check that the player has authority in that server. Since I set no permissions, by default we do. That's what the Switch Has Authority block is doing.
- Next, we have to check that the actor spawned in correctly and is valid to be possessed. Simple enough. I was doing that with a Delay block before, but it's not enough, apparently. Before adding it, I was getting debug messages saying that I had successfuly possessed when that really wasn't the case.
- Finally, we have to create a player controller! Unreal Documentation doesn't list this, for some reason! But, if you're running this on a computer, there's no "controller" by default. You have to create a new one, linking it to the new actor we created. Then (and only then) you can actually posses the actor, using the newly created controller. 

Here's what that all looked like:
![Final Blueprint](final-blueprint.png)

And here's how it looks when you're playing:
![](success-posses.png)

NOTE: it straight up will not auto-possess when you're looking through the viewport editor. I spent a lot of time trying to debug it after it was already working fine, so don't get caught up there. Instead, you'll want to run it as a Standalone Game. That's an option in the Play menu. I usually just do Play for normal stuff, but that keeps the editor open, which puts you outside of the game (doesn't assign you to the player controller we created).


## Issues/Problems
- Don't know much about conference / paper submission. Tried my best to filter for the "best" conferences.
- I could get this rover to be possessed automatically for the longest time.
    + Read through this forum to no avail: https://answers.unrealengine.com/questions/398737/client-pawn-possession-not-working.html. Actually, read through several forums. 
    + Solution: [this answer](https://answers.unrealengine.com/questions/221336/spawning-actor-server-side-possessing-it-from-clie.html) finally had the magic sauce. More above



## Plans for next week
