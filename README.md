# PAiP Web Developer Guide
## 0.1 Hello World

Hello! If you are reading this there is some possible causes why.

1. You want to contribute to work of PAiP Web. If that's the case then you really awesome and thank you. Stay motivated!
2. You want to become PAiP Web Developer. If that's the case then welcome on the board.
3. You want made Pull Request or Merge Request and you were referred to this document. If that's the case then propably the best way to find this what you are looking for is by direct link provided.
4. You just want to see PAiP Web Code Style Guide and maybe even make your own based from this. If that's the case feel free to look around and fork this repo.
## 0.2 Information About Guide

This guide is made by [Patryk Adamczyk](mailto:patrykadamczyk@patrykadamczyk.net).

This is PAiP Web Developer Guide version 1.

If you find something which doesn't make sense, it's in too complicated language even for programmer or anything just make Issue on GitHub.
## 1.0 Introduction

### So what is this guide for ?
It's for people to read how we working in PAiP Web and what rules we are trying restrict ourselves too for making better code.

### Why i created this guide ?
It's for making my CR easier process and making place rules for making better code which i find along my path of Developer.

### What this guide will cover ?
Firstly we will take a look at some Git Workflow and Git itself to make everything easy.
Afterwards we are going to take a look how to make good Pull Request and Merge Request (Same thing but diffrently named. Merge Requests are used as name in GitLab and Pull Requests are used as name in GitHub).
After that in section 4 we will take a look at how to write good documentation elements.
In section 5 we will take a look on how to write tests and think about testing.
In section 6 we look at Code Style things that are Language Agnostic pretty much. About patterns that are really good to know about.
Section 7 will be all about Python and it's Code Style Guide.
Section 8 will be about JavaScript Code Style with looking to TypeScript, Flow (Static type checker) and React.
In Section 9 We will be looking at PHP Code Style Guide.
Afterwards in section 10 we will sum things up.
And in special section FF i will leave my inspirations for this guidelines.

**Have a good lecture**
## 1.Z Dictionary
**This is special section for dictionary with definitions of more complicated elements or just short versions of some names.**

### Git Workflow
* `PR` - Pull Requests (this name will be used in place of Pull Request or Merge Requests for consistency)
## 2.0 Git Workflow

So someone one time long ago though about Git as good tool and found good solution for naming branches and complete workflow. It's called GitFlow. People liked that and made own ways of this workflow to fit them better. That's start of our workflow.

I will write about our flow only. If you will want to learn about GitFlow go to section FF maybe you will find something useful for you there.

### PAiP Web GitFlow

#### Base Branches

So everything starts from 2 base branches:
- `master` - Holding your current stable state of Project
- `develop` - Holding your current development state of Project

Note:
    If you are administrator of Project then these 2 branches you want to make as protected branches.

Master branch should hold history of releases.
Develop branch should hold history of development of releases.

#### Feature Branches

So now you would want to make some new feature.

1. Make new feature branch of `develop`
2. Make your new awesome features
3. Make your PR or just merge your branch to `develop`
4. After your all work on features make stable release so change Changelog ,merge to `master` or PR and merge to `master` afterwards add tag

Ok so that's the workflow with features let's destruct it into smaller and easier to understand parts.
1. `Make feature branch of develop`
    Feature branches have this naming scheme based on your project needs. If you don't know what naming convention project uses just ask in Issue.
    Naming Conventions for Feature Branches:

        * `feature/<name-of-feature>`
        * `feature/<source-like-trello>/<name-of-feature>`
        * `feature/<source-like-trello>/<identifier-of-task>`
        * `feature/<source-like-trello>/<identifier-of-task>/<name-of-feature>`
        * `feat/<name-of-feature>`
        * `feat/<source-like-trello>/<name-of-feature>`
        * `feat/<source-like-trello>/<identifier-of-task>`
        * `feat/<source-like-trello>/<identifier-of-task>/<name-of-feature>`
        * `issue-<number-of-issue-on-git-issue-board-like-github>`
        * `issue/<number-of-issue-on-git-issue-board-like-github>`
        * `issue-<number-of-issue-on-git-issue-board-like-github>/<name-of-feature>`

    Examples for PWBS Project in time of writing:

        * `issue-x/gitlab-ci`
        * `issue-7/command-runner-fixes`
        * `feat/trello/Jfq3zI8z/38-docker-container`

2. Just write your code. Just that what you want to change or make.
3. After your work make a PR from your branch to `develop`. If you are working alone on Project you may want to just merge your branch to `develop` manually. I don't advice that but there is possibility if you really would need to.
4. After some features, fixes and all other work make stable release.

    `change Changelog` about Changelogs we will talk about in section 4, for now just know that it exists and it is needed to be changed on release.
    After that make PR (same thing what to 2 applies everywhere) from `develop` to `master`
    After merge of this PR add tag to repository with version as name. (for example `v.0.1.0` or just `0.1.0`).

#### Release Branches

In some cases you need to use release branches to support and bugfix some versions of your project.
If you are working on something big you might just work on special branch for version you are build. Made from `develop` branch like `v.<version>.x` (for example `v.0.6.x`). 
But if you want to maintain your older versions or just make them as branches for documentation.
Then name your release branches in one of these ways:

* `release/<release-version>`
* `version/<release-version>`

This ways is not adviced but sometimes it can be the best for temporary release branch for example:

* `v.<release-version>` 
* `<release-version>`

#### HotFix Branches

If you need to fix something on stable version for temporary fix while you are working on better fix in next stable release. You should use hotfix branch.

Hotfixes are handled this way:
1. Make a new hotfix branch based on `master`
    Hotfix Branch Name Convention:

        * `hotfix/<name-of-issue-which-you-are-fixing>`
        * `hotfix/<source-like-trello-or-github>/<identifier-of-task>`
        * `hotfix/<source-like-trello-or-github>/<identifier-of-task>/<name-of-issue-which-you-are-fixing>`
2. Fix what you need to fix
3. Change changelog, Make PR
4. Merge it, Release new version of Project, add tag on repository
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
## FF - Inspirations

### 2.0 Git Workflow
#### GitFlow
https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow
https://datasift.github.io/gitflow/IntroducingGitFlow.html
https://danielkummer.github.io/git-flow-cheatsheet/
