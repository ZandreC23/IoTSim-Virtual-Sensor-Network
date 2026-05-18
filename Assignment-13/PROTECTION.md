# Branch Protection Rules

## Rules Applied to `master` Branch

1. **Require pull request reviews** — At least 1 approval is required before merging. This ensures a second pair of eyes reviews every change, catching bugs and maintaining code quality.

2. **Require status checks to pass** — The CI workflow (all 21 tests) must pass before a PR can be merged. This prevents broken code from ever reaching master.

3. **No direct pushes** — All changes must go through a pull request. This enforces the review process and keeps a clean audit trail of all changes.

## Why These Rules Matter

- **Quality Control**: Buggy code cannot reach the master branch because tests act as an automatic gate.
- **Collaboration**: PR reviews ensure knowledge sharing and catch issues that automated tests might miss.
- **Audit Trail**: Every change to master is documented through a PR with description, review comments, and linked issues.
- **Industry Standard**: These rules mirror real-world professional development workflows used at companies like Google, Microsoft, and Amazon.