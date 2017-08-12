<h3>Git Transfer</h3>
This is a python script that will transfer all the branches and tags of your git project to a new remote repository.
#### Purpose
When we start working on a existing project, we may not **checkout** to all the **branches** while working on the project. So when we try to transfer the full repository we cannot push all the branches. This project is meant to solve the problem.
#### Prerequisites
- Have to have **python2.7** installed in your local machine.
- Have to have **git** installed
- It is better if you setup ```ssh``` with your [bitbucket][69e33d05] or github account
- A freshly created repository

  [69e33d05]: https://bitbucket.org/ "bitbucket"

#### Installation
- ```git clone git@github.com:rhasan33/git-transfer.git```. I am using ssh here. You can use https as well
- ```cd git-transfer```
- ```cp transfer.py /path/to/your/local/project/repository```

#### Usage
- ```cd /path/to/your/local/project/repository```
- Run ```python transfer.py```
- It will ask for your new git repository's ssh address.
- Then it will ask for your old repositories remote alias (normally origin)
- If it is not origin then the prompt will ask for y/n to be authenticated.
- It will ask for the new remote's alias.
- If the new remote alias cannot be similar to old remote alias.

That's it. Now you need to wait for the repository to be transferred.

**Thanks**
