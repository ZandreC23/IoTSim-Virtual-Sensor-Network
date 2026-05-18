# Reflection: Assignment 13 — CI/CD with GitHub Actions

## What I Built
I implemented a full CI/CD pipeline using GitHub Actions for the IoTSim Virtual Sensor Network project. The pipeline automatically runs all 21 tests on every push and pull request, blocks merges if tests fail, and generates a release artifact when code is merged to master.

## What CI/CD Means
- **CI (Continuous Integration)**: Every code change is automatically tested. If tests fail, the developer is notified immediately before bad code spreads.
- **CD (Continuous Deployment)**: When code passes all tests and is merged to master, a release artifact is automatically built and uploaded.

## Challenges Faced
The main challenge was ensuring the GitHub Actions workflow correctly found the Assignment-12 test files and had all the required Python dependencies installed. The `conftest.py` path configuration from Assignment-12 needed to work in the Ubuntu CI environment as well as locally on Windows.

## Decisions Made
- I used `ubuntu-latest` as the runner because it is the most common CI environment and avoids Windows path issues.
- I separated the `test` and `build` jobs so that artifact generation only happens after all tests pass.
- The artifact is a ZIP of the Assignment-12 folder, which represents the deployable API package.

## What I Learned
- How GitHub Actions workflows are structured with jobs and steps.
- How branch protection rules enforce code quality gates.
- How CI/CD pipelines save time by automating repetitive testing and build tasks.
- Why the industry uses these tools — catching bugs early is far cheaper than fixing them in production.