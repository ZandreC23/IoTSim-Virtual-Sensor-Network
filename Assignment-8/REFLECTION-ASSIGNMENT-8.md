
---

## Step 4: Create `reflection-assignment-8.md`

```markdown
# Reflection: Assignment 8 - State and Activity Modeling

## Challenges in Choosing Granularity for States and Actions

The hardest part of this assignment was deciding how detailed to make my diagrams. If I made them too detailed, they became hard to read. If I made them too simple, they didn't capture important behavior.

For the state transition diagrams, I had to decide which states were meaningful. For example, the Sensor object could have had more states like "Initializing" or "Calibrating." But those don't exist in my simple simulator. I kept only the states that actually happen: Created, Enabled, Disabled, Generating, Error.

For the activity diagrams, I struggled with the Generate Humidity Data workflow. The condition "change from previous reading ≤5%" required a decision node and a loop back to regenerate. I almost made it a simple linear flow, but that would have been incorrect because the system must keep trying until the change is acceptable.

## Aligning Diagrams with Agile User Stories

The traceability tables helped me ensure every diagram mapped to functional requirements from Assignment 4 and user stories from Assignment 6. This was time-consuming but valuable.

For example, the Save Data to CSV activity diagram maps to FR-07, FR-08, FR-09, and US-006. When I build this feature in my sprint, I can look at the activity diagram and know exactly what steps to implement.

One challenge was that some user stories (like US-011: Add new sensor type) are "Could-have" priority. I almost skipped creating a diagram for it. But I decided to include it because it helps show the extensibility of the system.

## Comparing State Diagrams vs Activity Diagrams

| Aspect | State Diagrams | Activity Diagrams |
|--------|----------------|-------------------|
| **Focus** | Object lifecycle (how an object changes over time) | Process flow (how work gets done) |
| **Key Elements** | States, transitions, events, guard conditions | Actions, decisions, parallel flows, swimlanes |
| **Best For** | Understanding object behavior over time | Understanding workflow and who does what |
| **Example** | How a Sensor goes from Created to Enabled to Generating | The steps to generate temperature data |
| **Question Answered** | "What are the possible states of this object?" | "How does this process work step by step?" |

Both diagram types are complementary. State diagrams help me understand object behavior. Activity diagrams help me understand process flow.

## What I Learned

This assignment taught me that dynamic modeling is different from static modeling. In Assignment 3, I created C4 diagrams (static structure). In Assignment 8, I created state and activity diagrams (dynamic behavior).

The state diagrams showed me the lifecycle of my objects. For example, the CSVFile object can be in NotExists, Created, Writing, Corrupted, or Full states. This helped me think about error conditions I hadn't considered before (like disk full).

The activity diagrams showed me the workflow of my processes. The Dashboard Display diagram has a continuous loop: load data, update charts, wait 2 seconds, repeat. This matches the auto-refresh requirement from Assignment 4.

## What I Would Do Differently

1. **Start with traceability earlier**. I created the diagrams first, then mapped them to requirements. Next time, I would start with the requirements and design diagrams to meet them.

2. **Use swimlanes more consistently**. Some of my activity diagrams have swimlanes (User vs System), but some don't. I should add swimlanes to all of them.

3. **Add more guard conditions**. Some state transitions could have guard conditions (e.g., "Transition to Generating only if sensor is enabled"). I included some but could add more.

## Summary

This assignment helped me understand how to model the dynamic behavior of my IoT Simulator. The state diagrams show object lifecycles. The activity diagrams show process flows. Together, they prepare me for implementation because I know exactly what each object should do and how each process should work.