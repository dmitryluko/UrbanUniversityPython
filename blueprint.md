<p align="center">
  <img src="https://img.icons8.com/external-tal-revivo-duo-tal-revivo/100/external-markdown-a-lightweight-markup-language-with-plain-text-formatting-syntax-logo-duo-tal-revivo.png" width="100" />
</p>
<p align="center">
    <h1 align="center">URBAN UNIVERSITY PYTHON</h1>
</p>
<p align="center">
    <em>Always to be first!</em>
</p>
<p align="center">
	<img src="https://img.shields.io/github/license/dmitryluko/UrbanUniversityPython?style=flat&color=0080ff" alt="license">
	<img src="https://img.shields.io/github/last-commit/dmitryluko/UrbanUniversityPython?style=flat&logo=git&logoColor=white&color=0080ff" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/dmitryluko/UrbanUniversityPython?style=flat&color=0080ff" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/dmitryluko/UrbanUniversityPython?style=flat&color=0080ff" alt="repo-language-count">
</p>
<p align="center">
		<em>Developed with the software and tools below.</em>
</p>
<p align="center">
	<img src="https://img.shields.io/badge/Python-3776AB.svg?style=flat&logo=Python&logoColor=white" alt="Python">
	<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style=flat&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions">
</p>
<hr>
<!-- Table of Contents -->
## Quick Links
> - [Overview](#overview)
> - [Features](#features)
> - [Repository Structure](#repository-structure)
> - [Modules](#modules)
> - [Getting Started](#getting-started)
>   - [Installation](#installation)
>   - [Running UrbanUniversityPython](#running-urbanuniversitypython)
>   - [Tests](#tests)
> - [Project Roadmap](#project-roadmap)
> - [Contributing](#contributing)
> - [License](#license)
> - [Acknowledgments](#acknowledgments)
---
## Overview
Urban University Python is a comprehensive learning project aimed at teaching Python programming through practical tasks, modules, and projects. It includes various chapters, each focusing on different aspects of Python, from basics to advanced topics.
---
## Features
- **Modular Design**: Organized into chapters and modules to facilitate step-by-step learning.
- **Practical Examples**: Real-world examples and tasks to reinforce learning.
- **Automated Testing**: Includes a suite of tests to ensure code correctness.
- **CI/CD Integration**: Uses GitHub Actions for continuous integration and deployment.
---
## Repository Structure
```sh
└── UrbanUniversityPython/
    ├── .github
    │   └── workflows
    │       └── python-app.yml
    ├── Chapter_1
    │   ├── average_goal.py
    │   ├── debug_demo.py
    │   ├── module_1_3.py
    │   ├── module_1_4.py
    │   ├── module_1_5.py
    │   ├── module_1_6.py
    │   ├── task1.py
    │   ├── task2.py
    │   ├── task3.py
    │   ├── task4.py
    │   ├── task_string.py
    │   └── task_variables.py
    ├── Chapter_2
    │   ├── TicTacToe
    │   │   ├── requirements.txt
    │   │   └── tiktaс.py
    │   ├── module_2_2.py
    │   ├── module_2_3.py
    │   ├── module_2_4.py
    │   ├── module_2_5.py
    │   └── module_2_hard.py
    ├── Chapter_3
    │   ├── calc
    │   │   └── main.py
    │   ├── module_3_1.py
    │   ├── module_3_2.py
    │   ├── module_3_3.py
    │   ├── module_3_4.py
    │   ├── module_3_5.py
    │   └── module_3_hard.py
    ├── Chapter_4
    │   ├── hw_4_1
    │   │   ├── fake_math.py
    │   │   ├── module_4_1.py
    │   │   └── true_math.py
    │   └── module_4_2.py
    ├── Chapter_5
    │   ├── module_5_1.py
    │   ├── module_5_2.py
    │   ├── module_5_3.py
    │   ├── module_5_4.py
    │   └── module_5_hard.py
    ├── README.md
    ├── blueprint.md
    ├── main.py
    ├── playground
    │   ├── __init__.py
    │   └── demo.py
    ├── reqirements.txt
    └── tests
        ├── __init__.py
        ├── test_fake_math.py
        ├── test_module_2_2.py
        ├── test_module_2_3.py
        ├── test_module_2_4.py
        ├── test_module_2_5.py
        ├── test_module_2_hard.py
        ├── test_module_2_hard3.py
        ├── test_module_3_1.py
        ├── test_module_3_2.py
        ├── test_module_3_3.py
        ├── test_module_3_4.py
        ├── test_module_3_5.py
        ├── test_module_3_6.py
        ├── test_module_3_hard.py
        ├── test_module_5_4.py
        ├── test_module_5_hard.py
        ├── test_module_5_hard2.py
        ├── test_module_5_hard3.py
        ├── test_task1.py
        ├── test_task2.py
        ├── test_task3.py
        ├── test_task4.py
        ├── test_task_string.py
        ├── test_task_string2.py
        ├── test_task_string3.py
        ├── test_task_string4.py
        ├── test_task_string5.py
        ├── test_task_variables.py
        └── test_true_math.py
```
---
## Modules
<details closed><summary>.</summary>
| File                                                                                               | Summary                                     |
| ---                                                                                                | ---                                         |
| [main.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/main.py)                 | Entry point for the Urban University Python program. |
| [reqirements.txt](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/reqirements.txt) | Lists the dependencies required for the project.      |
</details>
<details closed><summary>Chapter_2</summary>
| File                                                                                                           | Summary                                                |
| ---                                                                                                            | ---                                                    |
| [module_2_4.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/module_2_4.py)       | Contains exercises and tasks related to topic 2.4.     |
| [module_2_hard.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/module_2_hard.py) | Contains advanced exercises for chapter 2.             |
| [module_2_2.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/module_2_2.py)       | Contains exercises and tasks related to topic 2.2.     |
| [module_2_5.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/module_2_5.py)       | Contains exercises and tasks related to topic 2.5.     |
| [module_2_3.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/module_2_3.py)       | Contains exercises and tasks related to topic 2.3.     |
</details>
<details closed><summary>Chapter_2.TicTacToe</summary>
| File                                                                                                                     | Summary                                                          |
| ---                                                                                                                      | ---                                                              |
| [tiktaс.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/TicTacToe/tiktaс.py)               | Implementation of the Tic-Tac-Toe game.                          |
| [requirements.txt](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_2/TicTacToe/requirements.txt) | Dependencies required to run the Tic-Tac-Toe game.               |
</details>
<details closed><summary>playground</summary>
| File                                                                                          | Summary                                        |
| ---                                                                                           | ---                                            |
| [demo.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/playground/demo.py) | Playground for demo scripts and prototypes.    |
</details>
<details closed><summary>Chapter_5</summary>
| File                                                                                                           | Summary                                                |
| ---                                                                                                            | ---                                                    |
| [module_5_1.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_5/module_5_1.py)       | Contains exercises and tasks related to topic 5.1.     |
| [module_5_3.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_5/module_5_3.py)       | Contains exercises and tasks related to topic 5.3.     |
| [module_5_hard.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_5/module_5_hard.py) | Contains advanced exercises for chapter 5.             |
| [module_5_4.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_5/module_5_4.py)       | Contains exercises and tasks related to topic 5.4.     |
| [module_5_2.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_5/module_5_2.py)       | Contains exercises and tasks related to topic 5.2.     |
</details>
<details closed><summary>Chapter_4</summary>
| File                                                                                                     | Summary                                             |
| ---                                                                                                      | ---                                                 |
| [module_4_2.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_4/module_4_2.py) | Contains exercises and tasks related to topic 4.2.  |
</details>
<details closed><summary>Chapter_4.hw_4_1</summary>
| File                                                                                                            | Summary                                                    |
| ---                                                                                                             | ---                                                        |
| [true_math.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_4/hw_4_1/true_math.py)   | Module implementing true mathematical functions.           |
| [fake_math.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_4/hw_4_1/fake_math.py)   | Module for demonstrating common mathematical mistakes.     |
| [module_4_1.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_4/hw_4_1/module_4_1.py) | Contains exercises and tasks related to topic 4.1.         |
</details>
<details closed><summary>.github.workflows</summary>
| File                                                                                                               | Summary                                                      |
| ---                                                                                                                | ---                                                          |
| [python-app.yml](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/.github/workflows/python-app.yml) | Configuration file for GitHub Actions CI/CD.                 |
</details>
<details closed><summary>Chapter_3</summary>
| File                                                                                                           | Summary                                                |
| ---                                                                                                            | ---                                                    |
| [module_3_3.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/module_3_3.py)       | Contains exercises and tasks related to topic 3.3.     |
| [module_3_1.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/module_3_1.py)       | Contains exercises and tasks related to topic 3.1.     |
| [module_3_hard.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/module_3_hard.py) | Contains advanced exercises for chapter 3.             |
| [module_3_4.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/module_3_4.py)       | Contains exercises and tasks related to topic 3.4.     |
| [module_3_5.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/module_3_5.py)       | Contains exercises and tasks related to topic 3.5.     |
| [module_3_2.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/module_3_2.py)       | Contains exercises and tasks related to topic 3.2.     |
</details>
<details closed><summary>Chapter_3.calc</summary>
| File                                                                                              | Summary                                            |
| ---                                                                                               | ---                                                |
| [main.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_3/calc/main.py) | Main script for the calculator project.            |
</details>
<details closed><summary>Chapter_1</summary>
| File                                                                                                             | Summary                                                 |
| ---                                                                                                              | ---                                                     |
| [task4.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/task4.py)                   | Contains exercises and tasks related to topic 1.4.      |
| [task_variables.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/task_variables.py) | Exercises for understanding Python variables.           |
| [task1.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/task1.py)                   | Contains exercises and tasks related to topic 1.1.      |
| [module_1_4.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/module_1_4.py)         | Contains exercises and tasks related to topic 1.4.      |
| [debug_demo.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/debug_demo.py)         | Demonstrates debugging techniques in Python.            |
| [module_1_5.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/module_1_5.py)         | Contains exercises and tasks related to topic 1.5.      |
| [module_1_6.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/module_1_6.py)         | Contains exercises and tasks related to topic 1.6.      |
| [task3.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/task3.py)                   | Contains exercises and tasks related to topic 1.3.      |
| [module_1_3.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/module_1_3.py)         | Contains exercises and tasks related to topic 1.3.      |
| [task2.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/task2.py)                   | Contains exercises and tasks related to topic 1.2.      |
| [task_string.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/task_string.py)       | Exercises for working with strings in Python.           |
| [average_goal.py](https://github.com/dmitryluko/UrbanUniversityPython/blob/master/Chapter_1/average_goal.py)     | Script for calculating average goals.                   |
</details>
---
## Getting Started
***Requirements***
Ensure you have the following dependencies installed on your system:
* **Python**: `version x.y.z`
### Installation
1. Clone the UrbanUniversityPython repository:
```sh
git clone https://github.com/dmitryluko/UrbanUniversityPython
```
2. Change to the project directory:
```sh
cd UrbanUniversityPython
```
3. Install the dependencies:
```sh
pip install -r requirements.txt
```
### Running UrbanUniversityPython
Use the following command to run UrbanUniversityPython:
```sh
python main.py
```
### Tests
To execute tests, run:
```sh
pytest
```
---
## Project Roadmap
- [X] Initial setup of the repository and project structure.
- [X] Add basic Python modules and tasks.
- [ ] Develop Chapter 6 with advanced topics.
- [ ] Integrate additional automated testing.
- [ ] ...
---
## Contributing
Contributions are welcome! Here are several ways you can contribute:
- **[Submit Pull Requests](https://github.com/dmitryluko/UrbanUniversityPython/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.
- **[Join the Discussions](https://github.com/dmitryluko/UrbanUniversityPython/discussions)**: Share your insights, provide feedback, or ask questions.
- **[Report Issues](https://github.com/dmitryluko/UrbanUniversityPython/issues)**: Submit bugs found or log feature requests for Urban University Python.
<details closed>
    <summary>Contributing Guidelines</summary>
1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Loc
