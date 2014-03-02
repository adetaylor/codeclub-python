Setup for CodeClub Python Exercises
======================================

Is more complicated than Scratch.

Dependencies
---------------

You need to install several things:

* [Python 3.3](http://www.python.org/getit/) - I use the [32-bit version on Windows](http://www.python.org/ftp/python/3.3.4/python-3.3.4.msi)
* [PyGame 1.9.1](http://www.pygame.org/download.shtml) - specifically use [this version](https://bitbucket.org/pygame/pygame/downloads/pygame-1.9.2a0.win32-py3.3.msi) if you're on Windows, with 32-bit Python 3.3 as suggested above
* [Pyro4](http://pythonhosted.org/Pyro4/install.html#obtaining-and-installing-pyro) - to install this, I first had to install [the unofficial Windows version of distribute](http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute) and [of pip](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip) then just ```pip install Pyro4```.
* Later there may be a physics library.
* [Sublime Text 3](http://www.sublimetext.com/3) - see [the explanation of why this was chosen](rationale.md).

Check that you can access http://www.github.com _and_ https://www.github.com/

Check that exercise 3, the network one, actually works.

Installing Pygame on Mac Python3
--------------------------------

Surprisingly awkward but this worked:

  curl -O http://python-distribute.org/distribute_setup.py
  sudo python3 distribute_setup.py
  python3 /usr/local/bin/easy_install pip
  export CPPFLAGS=-I/opt/X11/include
  python3 /usr/local/bin/pip install hg+http://bitbucket.org/pygame/pygame

Things to print
---------------

* [Python quick reference sheet](http://sleet.aos.wisc.edu/~gpetty/wp/wp-content/uploads/2011/10/Python_qr.pdf)
* [Longer Python quick reference](http://www.cogsci.rpi.edu/~destem/gamedev/python.pdf)
* [Pygame quick reference](http://www.cogsci.rpi.edu/~destem/gamedev/pygame.pdf)

Teachers/guides: see [the rationale behind these decisions](rationale.md).
