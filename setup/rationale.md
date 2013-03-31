Rationale for setup decisions
===============================

PyCharm
-------

I know nothing much about Python IDEs. PyCharm was recommended and seems to be quite good.

github for storing source code
--------------------------------

git and github are obviously very complicated and to be avoided when teaching kids.
But they were the best idea I could come up with:

* With the Scratch exercises the kids are used to uploading their projects so that they can
  work on them from home and/or show their parents. This achieves the same.
* github is unlikely to have been blocked by different schools (I hope). It uses https so school
  proxies probably won't interfere too much?? (These statements may be entirely wrong.)
* At a simple level it works well with PyCharm (for checking code out).

Submodules
----------

You'll notice that the source code for the problems (and their solutions) is stored in submodules
within the main git project.

I have a love/hate relationship with submodules but I think it works OK in this case. It means
that the code projects themselves can be stored independently on github, and further, that different
revisions of the same project can be used for problem/solution code.

Kids can therefore check out the problem code as an individual repository during an exercise,
whilst for a teacher/guide to check out the whole thing it's a matter of checking out the parent
project and then just running `git submodule update --init`.
