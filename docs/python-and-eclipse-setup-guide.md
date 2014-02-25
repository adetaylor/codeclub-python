Setup guide
=================================

General
-------

You need to install:

* Python 2.7
* PyGame 1.9
* Pyro 4 (not needed for the first few exercises)

All of these things are available for Windows PCs, Macs, and also Linux (for example on Raspberry Pis). However, on Raspberry Pis they are _very slow indeed_!!

Specific instructions for Windows installations
--------------------

Things to install if you're using Windows:

1. Python 2.7 32-bit.

   From: http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi
   This normally installs itself to c:\Python27 which is fine for us; anywhere else is also fine.

2. PyGame 1.9

   From: http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi

For some of the later exercises we also need Pyro4. To install that, you first need to install distribute/pip.

*Do not do these bits unless you're doing the Chat Room or Airport exercises.* It's too painful.

1. Python 'distribute'

   From: http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute - choose the version for win32 py2.7

2. Python 'pip'

   From: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip - again, the win32 py2.7 version

3. Pyro4

   After installing all of the above you should be able to type 'pip install Pyro4' to install one final Python library we need.

Network access
--------------

   We need access to:
   https://github.com
   (note the https).
