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
