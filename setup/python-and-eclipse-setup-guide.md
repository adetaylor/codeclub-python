Provisional setup guide for Python assuming we use Eclipse
=================================

Things to install if you're using Windows:

1. Python 2.7 32-bit.

   From: http://www.python.org/ftp/python/2.7.3/python-2.7.3.msi
   This normally installs itself to c:\Python27 which is fine for us; anywhere else is also fine.

2. PyGame 1.9

   From: http://pygame.org/ftp/pygame-1.9.1.win32-py2.7.msi

3. Python 'distribute'

   From: http://www.lfd.uci.edu/~gohlke/pythonlibs/#distribute - choose the version for win32 py2.7

4. Python 'pip'

   From: http://www.lfd.uci.edu/~gohlke/pythonlibs/#pip - again, the win32 py2.7 version

5. Pyro4

   After installing all of the above you should be able to type 'pip install Pyro4' to install one final Python library we need.

6. Eclipse

   From: http://download.eclipse.org/eclipse/downloads/drops4/R-4.2.2-201302041200/download.php?dropFile=eclipse-platform-4.2.2-win32.zip

   This should normally be unzipped to c:\eclipse but you can put it wherever you like.

   You should create a start menu item (or desktop shortcut) for eclipse.exe within it.

7. egit and PyDev

   Within Eclipse you should do this:
   1. Choose Help
   2. Choose Software Updates
   3. In the update site box, type http://pydev.org/updates
   4. Follow the wizard through until you have installed PyDev (you don't need the Mylyn integration)
   4. Do 1 and 2 again
   5. From the drop down list of update sites, select Juno
   6. Under the Team category, choose edit

8. Automating all of this

   I'm aware that this is ridiculously complicated. I believe that steps 1-5 put things in c:\Python27 and nowhere else. So, you should be able to do this on one machine then copy that folder to all the others. I haven't tested this, but I believe there are no registry entries involved or anything anywhere else on the PC.

   Also, steps 6 and 7 only put things in c:\eclipse and nowhere else. So again you should be able simply to copy that from machine to machine (and create a suitable start menu/desktop icon).

   You could even put both c:\Python27 and c:\eclipse into a single c:\CodeClub directory and copy it around.

9. Network access

   Believe it or not, we also need access to a website which has the word "git" in its title, which currently doesn't work on the school network. If you haven't come across it, "git" is currently probably the most widely-used system for managing and distributing source code for programs. That's how we're going to distribute and store the source code for these Python exercises. Obviously the name is unfortunate when it comes to schools, but there we go.

   We need access to:
   https://github.com
   (note the https).
