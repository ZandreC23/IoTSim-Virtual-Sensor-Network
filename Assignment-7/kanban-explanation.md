# Kanban Board Explanation

## What is a Kanban Board?

A Kanban board is a visual project management tool that helps me track tasks as they move through different stages of completion. The word "Kanban" comes from Japanese and means "visual signal" or "card." In software development, it is a way to see what needs to be done, what is being worked on, and what is finished.

My Kanban board has 5 columns:
- **Todo** - Tasks that need to be started
- **In Progress** - Tasks I am currently working on
- **Testing** - Tasks that need to be verified before marking done
- **Blocked** - Tasks that cannot proceed due to an issue
- **Done** - Completed tasks

## How My Board Visualizes Workflow

The columns represent the journey of a task from start to finish:

1. A new task starts in **Todo**
2. When I begin working, I move it to **In Progress**
3. After coding, I move it to **Testing** to verify it works
4. If something stops me, I move it to **Blocked** with a note explaining why
5. Once tested and working, I move it to **Done**

This visual layout gives me immediate answers:
- What should I work on next? (Look at Todo column)
- What am I currently doing? (Look at In Progress column)
- What is waiting for verification? (Look at Testing column)
- What is preventing progress? (Look at Blocked column)
- What have I finished? (Look at Done column)

## Work-in-Progress (WIP) Limits

To avoid overload, I set these WIP limits:

| Column | WIP Limit | Why |
|--------|-----------|-----|
| Todo | No limit | Backlog can be any size |
| In Progress | 2 tasks | I can only focus on 2 things at once |
| Testing | 2 tasks | Verification takes time and attention |
| Blocked | No limit | Problems can accumulate |
| Done | No limit | Completed work is archived |

If I try to move a third task to In Progress, I know I am trying to do too much at once. The WIP limit forces me to finish something before starting something new.

## How Kanban Supports Agile Principles

| Agile Principle | How My Kanban Board Supports It |
|----------------|--------------------------------|
| **Individuals and interactions** | The board shows exactly what I am working on. No confusion. |
| **Working software** | The Testing column ensures I verify before marking done. |
| **Customer collaboration** | The board can be shared with stakeholders to show progress. |
| **Responding to change** | The Blocked column captures problems immediately. |
| **Continuous delivery** | Tasks flow from Todo to Done in small increments. |
| **Simplicity** | The board has only 5 columns. Nothing extra. |

## Benefits for My Project

1. **Visibility**: I can see all 11 user stories at once.
2. **Focus**: WIP limits stop me from starting too many tasks.
3. **Problem tracking**: Blocked column captures issues immediately.
4. **Quality**: Testing column ensures verification before completion.
5. **Progress tracking**: Done column shows what I have accomplished.

## Example Workflow

1. I look at Todo column. Issue #1 is there.
2. I drag Issue #1 to In Progress.
3. I write the temperature sensor code.
4. I drag Issue #1 to Testing.
5. I run my test cases from Assignment 5.
6. All tests pass. I drag Issue #1 to Done.
7. I repeat for Issue #2.

This simple workflow keeps me moving forward without getting stuck or overwhelmed.