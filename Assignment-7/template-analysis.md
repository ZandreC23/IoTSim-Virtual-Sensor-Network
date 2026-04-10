# Template Analysis: GitHub Project Templates

## Screenshot of Available Templates

![GitHub Project Templates](template-comparison.png)

*Above: The three built-in templates available when creating a new GitHub Project.*

## Comparison Table

| Feature | Team Planning | Roadmap | Basic Kanban |
|---------|---------------|---------|--------------|
| **Default View** | Table (spreadsheet layout) | Timeline (Gantt-style) | Board (Kanban cards) |
| **Primary Use** | Sprint planning, backlog management | Long-term planning, milestone tracking | Daily task workflow |
| **Columns** | Backlog, Ready, In Progress, Done | Timeline with date ranges | Todo, In Progress, Done |
| **Best For** | Scrum teams, sprint planning | Project roadmaps, stakeholder communication | Continuous flow, Kanban teams |
| **Automation** | Yes (built-in workflows) | Limited | Yes (drag-and-drop, auto-close) |
| **Dependencies** | Not visualized | Yes (task dependencies shown) | No |
| **Date Tracking** | Start/end dates per item | Timeline view with dates | No |
| **Team Capacity** | Yes (effort estimates per member) | No | No |

## My Chosen Template: Basic Kanban

I selected **Basic Kanban** for my IoT Simulator project for these reasons:

### Justification

1. **Solo Developer**: I am the only person working on this project. Team Planning is designed for multiple team members with capacity planning. I don't need that complexity.

2. **No Fixed Deadlines**: Roadmap is for projects with hard deadlines and dependencies. My IoT Simulator has no external deadlines or task dependencies.

3. **Simple Workflow**: Basic Kanban has exactly what I need: Todo, In Progress, Testing, Blocked, Done. I added "Testing" and "Blocked" as custom columns.

4. **Visual Progress**: Board view lets me see all 11 user stories at once and drag them as I make progress.

5. **GitHub Integration**: Issues link directly to code. When I close an issue, it can auto-move to Done.

### Why Not Team Planning?

Team Planning is great for Scrum teams with multiple people doing sprint planning. It has fields for effort estimates, team capacity, and sprint iterations. I am one person. I don't need to estimate capacity across a team.

### Why Not Roadmap?

Roadmap is for projects with fixed release dates, milestones, and task dependencies. My IoT Simulator has none of these. I am building features in priority order, not on a fixed timeline.

## How Basic Kanban Aligns with My Project Needs

| Need | How Basic Kanban Addresses It |
|------|------------------------------|
| Track 11 user stories | All issues visible in Todo column |
| Know what I'm working on | Move issues to In Progress |
| Verify work before completion | Added "Testing" column |
| Handle unexpected problems | Added "Blocked" column |
| Track completion | Done column shows finished work |

## Comparison to Other Tools

| Tool | Pros | Cons | Best For |
|------|------|------|----------|
| **GitHub Basic Kanban** | Integrated with code, free, simple | Limited reporting | Solo developers, small teams |
| **Trello** | Beautiful UI, easy to use | No GitHub integration | Non-technical teams |
| **Jira** | Powerful, detailed reporting | Overkill for solo project, expensive | Enterprise teams |

For my solo IoT Simulator project, GitHub Basic Kanban is the perfect choice because my code is already on GitHub and I need simple task tracking, not complex sprint planning.