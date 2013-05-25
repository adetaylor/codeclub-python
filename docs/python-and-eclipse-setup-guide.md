Setup guide
=================================

General
-------

You need to install:

* Python 2.7
* PyGame 1.9
* Pyro 4 (not needed for the first few exercises)
* Eclipse
  * Within Eclipse, egit and PyDev

All of these things are available for Windows PCs, Macs, and also Linux (for example on Raspberry Pis). However, on Raspberry Pis they are _very slow indeed_!!

Specific instructions for Windows installations
--------------------

Things to install if you're using Windows:

1. Python 2.7 32-bit.

   From: http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi
   This normally installs itself to c:\Python27 which is fine for us; anywhere else is also fine.

2. PyGame 1.9

   From: http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi

3. Eclipse

   From: http://download.eclipse.org/eclipse/downloads/drops4/R-4.2.2-201302041200/download.php?dropFile=eclipse-platform-4.2.2-win32.zip

   This should normally be unzipped to c:\eclipse but you can put it wherever you like.

   You should create a start menu item (or desktop shortcut) for eclipse.exe within it.

4. egit and PyDev

   Within Eclipse you should do this:
   1. Choose Help
   2. Choose Software Updates (or 'Install new software')
   3. In the update site box, type http://pydev.org/updates
   4. Follow the wizard through until you have installed PyDev (you don't need the Mylyn integration)
   4. Do 1 and 2 again
   5. From the drop down list of update sites, select Juno
   6. Under the Team category, choose egit

For some of the later exercises we also need Pyro4. To install that, you first need to install distribute/pip.

*Do not do these bits unless you're doing the Chat Room or Airport exercises.* It's too painful.

1. Python 'distribute'

   From: http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute - choose the version for win32 py2.7

2. Python 'pip'

   From: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip - again, the win32 py2.7 version

3. Pyro4

   After installing all of the above you should be able to type 'pip install Pyro4' to install one final Python library we need.

Automating all of this for school installations
----------------------

This is all rather complicated. I believe that steps 1-5 put things in c:\Python27 and nowhere else. So, you should be able to do this on one machine then copy that folder to all the others. I haven't tested this, but I believe there are no registry entries involved or anything anywhere else on the PC.

Also, steps 6 and 7 only put things in c:\eclipse and nowhere else. So again you should be able simply to copy that from machine to machine (and create a suitable start menu/desktop icon).

You could even put both c:\Python27 and c:\eclipse into a single c:\CodeClub directory and copy it around.

Network access
--------------

   We need access to:
   https://github.com
   (note the https).
