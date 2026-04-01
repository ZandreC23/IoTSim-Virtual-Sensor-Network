# Reflection: Assignment 6 - Agile Planning

## The Challenge of Being the Only Stakeholder

This assignment required me to step into the role of a product owner and create an Agile plan for my IoT simulator project. The hardest part was that I am the only stakeholder. There was no product manager to ask, no real users to interview, and no team to debate priorities with. I had to imagine what different stakeholders would want and then make difficult decisions about what to build first.

## Prioritization Struggles

**What I Learned About MoSCoW**

Using MoSCoW (Must-have, Should-have, Could-have, Won't-have) forced me to make hard choices. I had 11 user stories but only 2 weeks for the sprint. I had to decide what absolutely had to be in the first release.

The hardest decision was ranking US-010 (offline operation) as Must-have. My instinct was to put it in Should-have because it's "just" a security requirement. But when I thought about the IT Department stakeholder from Assignment 4, I realized the system would never get deployed if it needed internet or external services. So it became Must-have.

**What I Would Do Differently**

If I had real stakeholders, I would have asked them directly what they needed most. I think my estimates might be off because I'm guessing what's complex versus simple. For example, US-007 (dashboard with charts) I estimated as 5 story points, but it might be easier with Streamlit. Or it might be harder if I run into bugs.

## Estimation Challenges

**Story Points vs Hours**

I used story points to estimate relative complexity, but then I also estimated hours for sprint tasks. This was confusing at first. I learned that story points help with long-term planning, but hours are needed for sprint planning.

Some tasks I underestimated. T-008 (TemperatureSensor with daily cycle) I estimated 4 hours. But thinking about it, I need to figure out sine wave math and time-of-day calculations. That could take longer.

**The "Unknown Unknowns"**

The hardest part of estimation is what I don't know I don't know. For example, T-020 (integration) I estimated 4 hours. But if the simulator writes to CSV and the dashboard reads at the same time, there might be file locking issues. I won't know until I actually build it.

## Sprint Planning Decisions

**Why I Chose These 6 Stories**

I selected all 7 Must-have stories for the sprint. This was ambitious. The total story points were 21, which might be too much for 2 weeks. But I felt the system wouldn't be useful without all of them:

- Without US-001, US-002, US-003: no data
- Without US-004: no configurability
- Without US-006: no data to verify
- Without US-007: no visualization
- Without US-010: IT would reject it

**Breaking Stories into Tasks**

Breaking user stories into tasks was useful because it exposed gaps. For example, US-007 (dashboard) required 5 tasks. I realized I needed to learn Streamlit specifically for charts and auto-refresh. That's something I can research before coding.

## Aligning Agile with Previous Work

| Previous Assignment | How It Informed This Assignment |
|---------------------|--------------------------------|
| Assignment 4 (Stakeholders) | Told me who the users are and what they need |
| Assignment 4 (Requirements) | Gave me the "what" to build |
| Assignment 5 (Use Cases) | Showed me how users interact with the system |
| Assignment 6 (User Stories) | Turned requirements into user-focused stories |

The traceability table in USER-STORIES.md shows how each user story connects back to requirements from Assignment 4. This was important because without that traceability, I might have built features nobody asked for.

## What I Would Do Differently Next Time

1. **Involve real users earlier.** Even if it's just asking classmates, real feedback is better than imagining needs.

2. **Smaller first sprint.** 6 stories might be too many. Maybe 4 stories with a clear working demo would be better.

3. **More time for integration.** The hardest bugs always happen when components connect. I should add buffer time.

4. **Better estimation.** I need to build a few things first to calibrate what 1 story point really means for me.

## Summary

This assignment taught me that Agile planning is about making trade-offs. You can't build everything at once. You have to decide what matters most to users (or stakeholders) and deliver that first. Being the only stakeholder made this harder because I had to argue with myself about priorities. But it also forced me to think carefully about what "value" really means for this project.

The sprint plan I created is ambitious but realistic. If I follow the tasks and timeline, I should have a working MVP at the end of 2 weeks. And that MVP will actually solve the problem from Assignment 4: giving developers realistic sensor data without physical hardware.

