Py03 – Chat Room
============

Introduction
------------
This isn't a game! You're going to create a chat room to talk to your classmates across the computer network.

Step 1: Create classes for the chat room, messages, and participants
-------------------------------------

1. Create a new project in PyCharm.
2. Create three new files - called `message.py`, `room.py` and `participant.py`.
3. `room.py` contains a class representing a chat room:

```python
class Room:
	def __init__(self):
		self.participants = []
	
	def add_participant(self, participant):
		self.participants.append(participant)
	
	def say(self, message_text):
		for p in self.participants:
			p.heard(message_text)
```

   Notice how it's a class, but _not_ a sprite. Classes can be any sort of 'object' or 'thing' in your program - not necessarily something you can visibly see on the screen. In this case, it's a room in which people can chat.

   The room starts with an empty list of participants - but they can be added using `add_participant`. Each time somebody `say`s something, it gets sent to each of the participants. That's what a chat room is!

4. `participant.py` represents somebody who is in a chat room:

```python
class Participant:
	def __init__(self, room):
		self.room = room
	
	def say(self, message):
		self.room.say(message)
	
	def heard(self, message):
		print message.get_message_text() + "\n"
```

   What happens when a participant `say`s something? What happens to the message? Does it end up within `heard`? How?

	 ----------------------
	 ----------------------
	 ----------------------
	 ----------------------
	 ----------------------

5. Finally `message.py` is the message. You should:
   * Add a class called `Message`.
	 * Add an `__init__` method which is given `self` as normal, but also takes an extra variable called `message_text`. It should store the message text in `self.message_text`.
	 * Add a method called `get_message_text` which does this:
	   ```python
		 return self.message_text
     ```

	 Can you see what calls `get_message_text`?

	 -----------------
	 -----------------
	 -----------------
	 -----------------

Step 2: Try it out on your own computer
-----------------------------------------

1. Add another file called `simple.py` which looks like this:

   ```python
from room import Room
from message import Message
from participant import Participant

room = Room()
janet = Participant(room)
room.add_participant(janet)
john = Participant(room)
room.add_participant(john)
fred = Participant(room)
room.add_participant(fred)

first_message = Message("Hello everyone!")

janet.say(first_message)
```

   Before you run it - what do you expect? How many times do you expect to see "Hello everyone!" appear on the screen?
   
   -------------------
   -------------------
   -------------------
   -------------------
   
2. Run it. Does it do what you expect?

3. Why do you think we have tried it out on just one computer? It's not very useful.
   
Step 3: Make it work between several computers
--------------------------------------------------------

We want it to work like this:


