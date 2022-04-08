# Command-line interface (CLI) for Canasta

### Synopsis
##### Abstract

A command-line interface (CLI) is a text-based user interface (UI) used to run programs, manage computer files and interact with the computer. Command-line interfaces are also called command-line user interfaces, console user interfaces and character user interfaces. 
**Canasta CLI** will be proven very helpful as it will offer users a concise and efficient mode of interacting with the OS, without requiring the overhead of GUI or set of instructions need to be followed.

There are multiple ways to design **Canasta CLI** using Node, Bash, Python and many more. But, I propose to create a **CLI using Python**, and we can also integrate Bash scripts in it. 

======Detailed Proposal
**Canasta CLI** can be created using Python.
Steps to follow:

- Create a Virtual env
```
python -m venv canasta
``` 
- Install libraries if not present (setuptools, argparse)

```
pip install -r requirements.txt
```
- *create a setup.py file*: using this file, we can easily download, build, install upgrade, and uninstall Python packages

*Sample code snippet:*
```
from setuptools import find_packages, setup

setup(
    name="canasta",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    ## Entry point for command line and function to be executed
    entry_points={
        'console_scripts': ['canasta=main:main'],
    }
)
```

- *create a src/ main.py file*: this file will contain all the code needed to create a CLI. 

*Sample code snippet:*
```
import os
import sys
import argparse

def main():
    # create a cli argument parser for dispaying date with optional argument
    parser = argparse.ArgumentParser(description='Welcome to Canasta CLI')

    # create a argument to Move into root directory
    parser.add_argument('-m', '--move', help='move into root directory', action='store_true')

    # create an argument to update docker container by stopping and reinstalling it
    parser.add_argument('-u', '--update', help='update docker container', action='store_true')

    args = parser.parse_args()

    if args.move:
        os.chdir('/')

    if args.update:
        os.system('docker rm -f $(docker ps -a -q)')
        os.system('docker rmi $(docker images -q)')
        os.system('docker build -t node:10.15.3-alpine .')
        os.system('docker run -it --rm -p 8080:8080 -v $(pwd):/usr/src/app/src/main.py -w /usr/src/app/src/main.py node:10.15.3-alpine node src/main.js')
    
    # if no argument is passed, display help
    if len(sys.argv) == 1:
        parser.print_help()

if __name__ == '__main__':
    main()

```
*In the above code we created a **CLI** with two arguments*
*To use the CLI:*
*1. **canasta -h or --help**: To see the manual*
*2. **canasta -m or --move**: To go back to root of the directory*
*3. **canasta -u or --update**: To update the docker image by deleting and reinstalling it*

- Deploying as Micro-Service
If time allows create a kubernetes deployment for Canasta

### Mentors
@Jeffry @Yaron

Have you contacted your mentors already?
We had a conversation over GitHub and the Phabricator regarding what's next and how should we proceed

### Deliverables

- A well mantained GitHub Repository with feature branches.
- Use-cases and detailed study report.
- Well elaborative `README` file with How-To use instruction set
- Documentation on **Canasta CLI** other than `README` in `.pdf` or `.docx`
- Weekly report on progress made
- Blog post

### Participation

- Weekly Report: I will be presenting weekly report on progress made on the project.
- Blog Post: Research and the knowledge will be shared and published on Canasta. 
Describe how you plan to communicate progress and ask for help, where you plan to publish your source code, etc.
- Email: I will be active and respond ASAP to the emails.
- IRC: I will be available on the IRC at my proposed time, that is, 12 PM to 1 AM (UTC+05:30)
- Phabricator: I will be actively commenting over the threads and tasks on Phabricator.

### About Me
Tell us about a few:
- **Your education (completed or in progress):** 
Currently in Pre-final year of Bachelors in Technology, Computer Science field from Jaipur Engineering College and Research Centre. `Graduation Year: 2023`
- **How did you hear about this program?**
I heared about Google Summer of Code (GSoC) from various social platforms like, LinkedIn, Twitter. GSoC informations are also circulated on various tech communities on Discord, Telegram, and WhatsApp. I also interacted with previous GSoC participants and was fascinated from their experience. It is the primary reason I am eager to participate.
- **Will you have any other time commitments, such as school work, another job, planned vacation, etc, during the duration of the program?**
I have college starts in the first week of June. But, I am confident that I can commit enough time for the project as there are no examinations.
- **We advise all candidates eligible for Google Summer of Code and Outreachy to apply for both programs. Are you planning to apply to both programs and, if so, with what organization(s)?**
I am eligible for Google Summer of Code and Outreachy to apply for both programs. I want to apply with our organization **Wikimedia** in both. As it is first time I am applying and I researched well about the Canasta, so I am confident on this project very much.
- **What does making this project happen mean to you?**
This project is full of learning and polishing my tech stack. I have been learning and working in field of Python, Kubernetes and Dockerization from a year. Creating a complete CLI and a Microservice deployment of Canasta will brush up my knowledge and gives me an opportunity to prove my skills globally. Creating something which will be used globally gives a sense of proud and belongingness. If I got selected, this project will be my dream project as I will work on what I have learnt past . Hence, making this project happen means a lot to me and I will ensure that it will happen definitely, whether or not I get selected.

===Past Experience
- **Please add links to any feature or bug fix you have written for a Wikimedia project during the application phase.**
I cannot deny the fact that the GSoC had a very competitive environment. Contributors here are very amazing and had contributed a much before. I walked through all the issues, but one or other had either fixed it or on it. I got a chance to fix one issue, mentioned here:
https://github.com/CanastaWiki/Canasta/pull/65
I had also suggested a change in one issue, once approved and acknowledged by mantainers, I can move ahead:
https://github.com/CanastaWiki/Canasta/issues/55

- **Describe any relevant projects that you've worked on previously and what knowledge you gained from working on them.**
I had a good working experience with various DevOps related organizations. 
 1.I had set up a completely automated Blockchain based Microservice architecture using helm and GitLab CI for **Zeeve**. My work is preserved as an intellectual property of the organization.
 2.I had also worked with **Sirpi**, which is a DataScience company where I dockerrized the application and created kuberneted deployment of various projects. 
 *Sample: https://github.com/abhi-bhatra/React-Kubernetes-Server/tree/main/Kubernetes-Scripts* 
 3.Currently, I am working on setting up Rancher as a Microservice to the existing cluster.
 *Sample: https://github.com/abhi-bhatra/Rancher-Demo*
 4.I also worked with **Windowscope**, and created many automation scripts for automated backups of complete Repository along with every branch (active or stale), zip it and upload it to AWS s3 bucket.
 *Sample: https://github.com/abhi-bhatra/automating_backup_to_s3*
 5.I had also demonstrated a quality documentation on various projects.

- **Describe any open source projects you have contributed to as a user and contributor (include links).**
 https://github.com/microsoft/ML-For-Beginners/commits?author=abhi-bhatra
 https://github.com/CanastaWiki/Canasta/pull/65
 https://github.com/crenspact02/AI-Banking-Suite_Microsoft-Azure-Developer-League/graphs/contributors
 https://github.com/symblai/Github-Externship-Assignment/pull/24
 https://github.com/cncf/contribute/issues/64#event-5882248878
 Member of: https://github.com/orgs/campus-experts/teams/campus-experts/members?query=abhi-bhatra

===Any Other Info
Add any other relevant information such as UI mockups, references to related projects, a link to your proof of concept code, etc
Although, I might be beginner in Open-Source, but I carry a good amount of knowledge and technologies needed for this project.
