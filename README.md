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

Why on earth are these using PyCharm, github, markdown etc.?
---------------------------------------
Good questions and I'm not wedded to any of these decisions, but [I have documented my reasoning here](setup/rationale.md)


Evolution of the course of exercises
---------------------------------------

* [Py01-Ball](exercises/Py01-Ball/docs/README.md):

  The first exercise is for the kids to be talked through Python to pick up some basic syntax. There is a single challenge for them to do.

* [Py03-Alien](exercises/Py03-Alien/docs/README.md):

  It's been proposed that the Python exercises start off by shadowing one or more of the Scratch exercises the kids will already have done.

  I think that's a great idea but I don't personally have time, so I've made a stab at a first exercise or two by starting with one of the PyGame examples. At least this saves the step of writing and debugging a game.

	The intention of the first Python session is to get the kids used to looking through actual textual code, and identifying clues. If we can end the session with an idea that a 'class' relates to a sprite on the screen, we're doing well.

* [PyNotSureYet-Guess](exercises/PyNotSureYet-Guess/README.md):

  This exercise has been produced by Peter Lewin and is probably similar in scope to the initial Ball exercise. I am inclined to make this more difficult and ask the kids to do more with this one by themselves, thus making it appropriate as a third exercise perhaps? But we could do it the other way round.

* [Py04-Felix](exercises/Py04-Felix/README.md):

  This exercise has been produced by Peter Lewin and I think it slots pretty well after the ball and alien, as they actually have to do stuff here (instead of, mostly, just looking through the code as with the Alien exercise). We might want to adjust it so that they have to do slightly more. Perhaps.

* Additional unwritten Scratch project conversion, or two.

* [Py06-Chatroom](exercises/Py06-Chatroom/docs/README.md):

  A networked chat room.

* Subsequently:

  We should build up to a network game, possibly in teams somehow. I also think use of a simple physics library, for example [this one](http://www.petercollingridge.co.uk/pygame-physics-simulation) could make for fun games that just wouldn't be possible in Scratch.

To do
------

* Create Scratch-Python conversion guide. (Not just the blocks, but also sprites, sounds, variables and broadcasts. There's a [start at this here, but it's incomplete](docs/scratch-python-cheatsheet/README.md).
* Work out the best way to check out a certain branch within PyCharm.
* Think about whether PyCharm is truly the best IDE for the job. An open-source one would be better...
* Work out tabs versus spaces
* Merge in Peter Lewin's exercises which are [here](exercises/PyNotSureYet-Guess/README.md) and [here](exercises/PyNotSureYet-Felix_Tutorial/README.md).
  * Figure out where they go relative to the other exercises
	* Come up with a single ```codeclub.py``` library for use in all exercises which emulates Scratch sprites and does whatever else we need to hide from the kids for simplicity's sake.
	* Work out whether we're nervous about getting the kids to declare classes. Ade's exercises do this. Peter's avoid it. Ade's rationale: the kids now have a good concept of attaching scripts to Sprites in Scratch, so I think it will make logical sense for them to do the same in Python.
	* In general make Peter and Ade's stuff more consistent.
