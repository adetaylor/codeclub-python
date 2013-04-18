Setup for CodeClub Python Exercises
======================================

Is more complicated than Scratch.

Dependencies
---------------

You need to install several things:

* [Python 2.7](http://www.python.org/getit/) - I use the [32-bit version on Windows](http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi)
* [PyGame 1.9.1](http://www.pygame.org/download.shtml) - specifically use [this version](http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi) if you're on Windows, with 32-bit Python 2.7 as suggested above
* [Pyro4](http://pythonhosted.org/Pyro4/install.html#obtaining-and-installing-pyro) - to install this, I first had to install [the unofficial Windows version of distribute](http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute) and [of pip](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip) then just ```pip install Pyro4```.
* Later there may be a physics library.

And either PyCharm or Eclipse or something else depending on what on earth we use for an IDE. (See [the explanation of why I'm unhappy with both options](rationale.md)).

If we use PyCharm.
* [git](http://git-scm.com/downloads)
* [PyCharm IDE](http://www.jetbrains.com/pycharm/download/) which is free for use in schools, but you'll need to fill in a form.
* And you will need to squeeze a license out of them.

If we use Eclipse:
* [Eclipse Platform Runtime Binary](http://download.eclipse.org/eclipse/downloads/drops4/R-4.2.2-201302041200/) - specifically I am using the [Windows 32-bit version](http://download.eclipse.org/eclipse/downloads/drops4/R-4.2.2-201302041200/download.php?dropFile=eclipse-platform-4.2.2-win32.zip)
* Within that you will need to install PyDev from the update site http://pydev.org/updates, and egit from the main Juno update site. If we continue to use Eclipse then more precise instructions will be forthcoming, but otherwise you can muddle through.
* Later all this Eclipse stuff can be a self-contained zip file which you can just extract to anywhere on the PC and therefore in some senses it's easier to install than PyCharm
* The PCs will also need to have Java.

Check that you can access http://www.github.com _and_ https://www.github.com/

Check that exercise 3, the network one, actually works.

Things to print
---------------

* [Python quick reference sheet](http://sleet.aos.wisc.edu/~gpetty/wp/wp-content/uploads/2011/10/Python_qr.pdf)
* [Longer Python quick reference](http://www.cogsci.rpi.edu/~destem/gamedev/python.pdf)
* [Pygame quick reference](http://www.cogsci.rpi.edu/~destem/gamedev/pygame.pdf)

Teachers/guides: see [the rationale behind these decisions](rationale.md).
