# Reflection: Assignment 7 - GitHub Project Templates and Kanban Board

## Challenges in Selecting and Customizing the Template

The hardest part of this assignment was choosing between the three templates. At first, I wanted to use Automated Kanban because the automation sounded helpful. But when I thought about my actual workflow, I realized automation would hide what I am doing. For example, if a PR automatically closes an issue, I might forget to test it first. Since I am the only person working on this project, I need full control over when tasks move between columns.

Another challenge was adding the Testing column. I initially thought about adding a "Code Review" column, but I am the only developer. A code review column would be empty forever. So I chose Testing because that is something I actually do: run the test cases I wrote in Assignment 5.

The Blocked column was also a difficult decision. I was not sure if I would ever use it since I am working alone. But I realized problems can still happen. For example, if a library does not install correctly, that blocks my progress. Having a Blocked column forces me to document the problem instead of ignoring it.

## Comparison of GitHub Templates to Other Tools

I have used Trello before for a group project. Trello is very similar to GitHub's Basic Kanban. Both have columns and cards. The main difference is that GitHub Projects is built into my repository. I do not need to copy issue titles from GitHub to Trello. Everything is already connected.

Jira is too powerful for my needs. Jira has epics, stories, tasks, subtasks, sprints, releases, and many other features. For a solo IoT simulator project, Jira would be like using a fire hose to water a small plant. GitHub Projects is simple enough for one person but powerful enough to scale to a team if needed.

Here is my comparison:

| Feature | GitHub Projects | Trello | Jira |
|---------|-----------------|--------|------|
| GitHub integration | Perfect (built-in) | None (manual) | Partial (plugin) |
| Learning curve | Low | Very low | High |
| Setup time | 1 minute | 5 minutes | 30+ minutes |
| Cost | Free | Free (limited) | Paid for teams |
| Reporting | Basic | Basic | Advanced |
| Best for | GitHub users | Small teams | Enterprise teams |

## What I Learned

This assignment taught me that project management tools are not one-size-fits-all. The "best" tool depends on the project, the team size, and the workflow. For my solo IoT simulator project, Basic Kanban with custom Testing and Blocked columns is perfect. It is simple enough to use without thinking but powerful enough to track all 11 user stories.

I also learned that WIP limits are important even for one person. Before this assignment, I would start five tasks at once and finish none of them. Now I force myself to focus on only two tasks at a time. This should help me actually complete the project.

## Lessons for Future Projects

1. **Start simple, add complexity later.** Basic Kanban was the right choice. I can always add automation later if I need it.

2. **Custom columns should reflect actual workflow.** I added Testing because I actually test. I did not add Code Review because I do not review my own code.

3. **WIP limits are not restrictions; they are focus tools.** Limiting myself to 2 tasks in progress helps me finish faster.

4. **GitHub Projects is good enough.** I do not need Trello or Jira when my code is already on GitHub.