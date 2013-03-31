Python CodeClub experiments
============================

This repository contains some experiments in producing a Python CodeClub curriculum
using PyGame and, I hope eventually, networked games.

Motivation: why Python?
---------

Actually, none. Scratch is great and just right for kids of this age. However, existing CodeClub wisdom seems to be that two terms of Scratch is enough, and we should move to more 'advanced' languages.

HTML/JavaScript is not my _personal_ idea of awesome, hence I'm joining in with subversive efforts to come up with a Python alternative.

Will the kids want to do Python?
------------------------

General view of Python has been quite negative in comments in the class: terms like 'boring'. But I asked at my CodeClub session today whether the kids wanted to move to Python, because "it can do much more stuff" but "is much more difficult". The response was categorically a yes.

However, I do think many of the kids will struggle. It is _much_ more difficult no matter which way you cut it.

Hence we need to provide some real solid motivation for the kids to move to Python. I think we therefore need to do one of three things which can't be done in Scratch:

* Robotics.
* Physics.
* Networked games.

Initially I'm aiming for the latter as it's much easier.

The 'Desert Race' Scratch example was very popular because it was two-player, albeit on the same PC. If we can come up with a genuine way to get the kids producing networked multi-player games I'm sure they will definitely feel the move to Python was worth it.

That said, I also happen to have a Parrot AR.Drone which has a Python SDK so I haven't totally given up on the robotics angle :-)

Setup
------

I've added some notes in [a separate document](setup/setup.md). But it's certainly much more complex than Scratch. We need:

* Python and various libraries.
* Network connectivity.
* An IDE.

The code is being kept on github which enables reasonably efficient easy checkouts.

Evolution of the course of exercises
---------------------------------------

* [Py01-Ball](exercises/Py01-Ball/docs/README.md):

  The first exercise is for the kids to be talked through Python to pick up some basic syntax. There is a single challenge for them to do.

* [Py02-Alien](exercises/Py02-Alien/docs/README.md):

  It's been proposed that the Python exercises start off by shadowing one or more of the Scratch exercises the kids will already have done.

  I think that's a great idea but I don't personally have time, so I've made a stab at a first exercise or two by starting with one of the PyGame examples. At least this saves the step of writing and debugging a game.

	The intention of the first Python session is to get the kids used to looking through actual textual code, and identifying clues. If we can end the session with an idea that a 'class' relates to a sprite on the screen, we're doing well.

	If anyone thinks that is pessimistic, you may wish to remember that some of these kids are actually dyslexic and struggle to read normal English very easily! Python is a massive step up from coloured Scratch blobs.

* Py03-Aliens:

  We should guide them through making a more substantive change to the same game.

* Py04-Aliens 3:

  At this point we do something to introduce networking. Maybe we can simply have two players. Or maybe one person controls the 'player' whilst all the other people on the network control the aliens.

	Before we can get this far, we need to write a trivial module which integrates PyBonjour into PyGame, especially into its event loop. I am convinced we need to use PyBonjour for discovery to avoid faffing with IP addresses (I know it sounds appealing to teach kids about IP addresses, and I agree, but honestly that complexity will wipe out 50% of the code club session just through mistyping). For the subsequent communication, perhaps we need some form of Python RPC protocol. Security is not important for 10 year-olds.

* Subsequently:

  We should build up to a more complex network game, possibly in teams somehow.

To do
------

* Create Scratch-Python conversion guide. (Not just the blocks, but also sprites, sounds, variables and broadcasts)
* Figure out networking and/or physics.
* Work out the best way to check out a certain branch within PyCharm.
* Think about whether PyCharm is truly the best IDE for the job. An open-source one would be better...
