# AiAutomatedClaims Crew

Welcome to the AiAutomatedClaims Crew project, powered by [crewAI]

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV] for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `GEMINI_API_KEY`(or preferred AI model) into the `.env` file**

- Modify `src/ai_automated_claims/config/agents.yaml` to define your agents
- Modify `src/ai_automated_claims/config/tasks.yaml` to define your tasks
- Modify `src/ai_automated_claims/crew.py` to add your own logic, tools and specific args
- Modify `src/ai_automated_claims/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

## Understanding The Project 

The ai-automated-claims Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

