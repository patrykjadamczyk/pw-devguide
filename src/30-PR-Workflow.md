## 3.0 - PR Workflow
So you want to make some functionality. Now how to do it properly?

We will skip parts of clean Git Workflow because it was covered in previous chapter. But we will reference to it.

So let's say you want to make new powerful Watcher Mode for <abbr title="PAiP Web Build System">PWBS</abbr>. Now what you should do to start doing it properly?

Firstly make fork of repository if you haven't done it. (People accepted to PAiP Web Open Team or PAiP Web Core Team may skip it because they might be able to work on original repository if they ask for it)
After that clone repository to some folder. (The best just clone development branch because there you will be working [`git clone -b <development_branch> <repository_url>`]).
When you have done it make new feature branch in way specified in previous chapter.
Make your awesome Watcher Mode functionality.

So you done your functionality? Ok let's slowly get into this chapter real topic.

Firstly push all your changes to your branch. (For sure commit from time to time the best is to commit every working part of functionality)
Now make PR from your branch back to development branch.
In Title one short sentence what functionality you have done. In Description write more in details what you have done and if you had problem with something then with what and how next time we would have helped you.
On GitLab if you want you can add how much time you spent on this task (with all elements where you was stuck and etc.) simply by putting `/est <time>` in comment.
Ok, so you made your PR. For sure if project have CHANGELOG and things in that kind of thing make sure you added what you have done to it.
Next what you need to do is wait or just ask for Code Review of PR. In PAiP Web for that part are PAiP Web Admins which have to approve PRs.
After Code Review if there was need for fixes then fix elements specified and move back to waiting or asking for next Code Review. If your code went through Code Review fine then it will be merged.
