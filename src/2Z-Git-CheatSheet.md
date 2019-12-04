## 2.Z Git Cheatsheet

### Git
* `git init` - Initialization of Local Repository
* `git add <File>` - Add file to changes staged for commiting
* `git add -A` - Add all changed files to changes stage for commiting
* `git commit -m "<message>"` - Commit staged changes to your Local Repository
* `git remote` - Managing Remote Repositories connected with current Local Repository
    
    * `git remote add <name> <repository-url>` - Connect Remote Repository with current Local Repository
    * `git remote rm <name>` - Disconnects Remote Repository with current Local Repository
    * `git remote show <name>` - Shows information about Connection with Remote Repository

* `git push` - Push Local Repository to Remote Repository
* `git push <remote> <branch>` - Push Branch of Local Repository to Remote Repository
* `git push -u <remote> <branch>` - Set Remote Repository Branch to default to this one on this branch and push Local Repository to Remote Repository
* `git pull` - Pull Changes from Remote Repository to Local Repository
* `git checkout <file>` - Restore specified file to state before current changes
* `git checkout <branch>` - Restore state of current branch changes of specified branch
* `git tag <name>` - Tags current changes (commit) with specified name
