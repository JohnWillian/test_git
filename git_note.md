# GIT Command
[Reference](https://www.ruanyifeng.com/blog/2015/12/git-cheat-sheet.html)

- Create a new repository 

  `git init`


- Set userinfo 

  `git config [--global] user.name "<name>"`

  `git config [--global] user.email "<email address>"`


- Check the status

  `git status`


- Add a file to the index

  `git add <file name>`


- Add all the files that under the current dir to the index

  `git add .`


- Create a new commit

  `git commit -m "message"`


- Create a new branch

  `git branch -b <branch name>`


- Merge the current branch with other one

  `git merge <branch name>`


- Switch branch

  `git checkout <branch name>`


- Add a new remote repository

  `git remote add <shortname> <url>`


- Push the local branch to the remote repository

  `git push -u <shortname> <branch>`


- Pull the change from the remote repository

  `git pull <shortname> <branch>`


