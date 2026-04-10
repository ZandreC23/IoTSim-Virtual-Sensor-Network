# Template Analysis: GitHub Project Templates

## Comparison Table of 3+ Templates

| Feature | Basic Kanban | Automated Kanban | Team Planning |
|---------|--------------|------------------|---------------|
| **Default Columns** | Todo, In Progress, Done | Todo, In Progress, Done | Backlog, In Progress, Done |
| **Workflow** | Manual drag and drop | Auto-moves issues based on triggers | Manual with sprint planning |
| **Automation Features** | None | Auto-closes issues when PR merged; auto-moves when issue closed | None |
| **Issue Linking** | Manual | Automatic when PR references issue | Manual |
| **Suitable For** | Small teams, simple projects | Teams using GitHub heavily | Teams doing sprint planning |
| **Agile Support** | Basic Kanban | Kanban with automation | Scrum + Kanban hybrid |
| **WIP Limits** | Not supported | Not supported | Not supported |
| **Custom Columns** | Yes | Yes | Yes |

## My Chosen Template: Basic Kanban

I selected the **Basic Kanban** template for the following reasons:

### Justification

1. **Simplicity**: My project is a single-person IoT simulator. I don't need complex automation that might hide what I'm working on.

2. **Full Control**: Automated Kanban moves issues automatically when PRs are merged. Since I'm working alone, I want to manually control when tasks move between columns.

3. **Customizable**: Basic Kanban allows me to add columns like "Testing" and "Blocked" which are essential for my workflow.

4. **Alignment with Assignment 6**: The Basic Kanban template matches the sprint backlog I created in Assignment 6, where I had tasks in Todo, In Progress, and Done states.

5. **No Over-engineering**: Team Planning template is designed for multiple people doing sprint planning. I am one person. Basic Kanban is perfect for my scale.

### How It Aligns with My Project Needs

| Need | How Basic Kanban Addresses It |
|------|------------------------------|
| Track 11 user stories | All issues visible in Todo column |
| Know what I'm working on | Move issues to In Progress |
| Verify work before completion | Testing column added |
| Handle unexpected problems | Blocked column added |
| Track completion | Done column shows finished work |

### Comparison to Other Tools

| Tool | Pros | Cons |
|------|------|------|
| **GitHub Projects (Basic Kanban)** | Integrated with issues, free, no setup | Limited reporting |
| **Trello** | Beautiful UI, easy to use | No GitHub integration |
| **Jira** | Powerful, detailed reporting | Overkill for solo project, expensive |

For my project, GitHub Projects is the best choice because my code is already on GitHub.