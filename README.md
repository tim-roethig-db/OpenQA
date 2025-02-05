# OpenQA
The idea is to create a Quality Assurance suite for git repositories (python only initially).

## Features
1. AI Agent that automatically sets up the environment and installs dependencies
**Approach**: Use CrewAI to define a devops agent, having acces to a shell execution and a read directory tool.
Crew needs to run in a docker container, where a venv is created vor the tested repo.
Backend for now is OpenAI's 4o mini.
2. Code Format check using black
3. Linting using pyling
4. LLM based linting fixes
5. LLM generated tests using hypothesis to spot errors
