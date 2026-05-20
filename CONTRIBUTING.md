# Contributing to IoTSim: Virtual Sensor Network Simulator

Thank you for your interest in contributing! Follow these steps to get started.

## Prerequisites
- Python 3.11+
- Git

## Setup Instructions
1. **Fork this repository** by clicking the Fork button at the top right of this page
2. **Clone your fork** to your local machine:
```bash
   git clone https://github.com/YOUR-USERNAME/IoTSim-Virtual-Sensor-Network.git
   cd IoTSim-Virtual-Sensor-Network
```
3. **Install dependencies:**
```bash
   cd Assignment-12
   pip install fastapi uvicorn pytest httpx pydantic anyio
```
4. **Run the tests** to confirm everything works:
```bash
   python -m pytest tests/ -v
```
   You should see 21/21 tests passing.

## How to Contribute
1. Go to the **Issues** tab and pick one labeled `good-first-issue`
2. Comment on the issue saying "I'd like to work on this"
3. Create a new branch:
```bash
   git checkout -b fix/issue-name
```
4. Make your changes and write tests
5. Run tests to make sure nothing is broken:
```bash
   python -m pytest tests/ -v
```
6. Commit and push:
```bash
   git add .
   git commit -m "Fix #ISSUE_NUMBER: description of change"
   git push origin fix/issue-name
```
7. Open a **Pull Request** targeting `master` and describe what you changed

## Coding Standards
- Follow PEP8 Python style guidelines
- All new features must include unit tests
- All tests must pass before submitting a PR
- Use descriptive commit messages linked to issues (e.g. `Fix #12: add validation`)

## Peer Review
To star or fork this repository:
- **Star** — click the ⭐ Star button at the top right if you find this project useful or well documented
- **Fork** — click the Fork button to create your own copy and contribute