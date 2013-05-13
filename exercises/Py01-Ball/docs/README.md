Py01-Ball
=========

[Student handout](py01-ball.md)

The aim of this exercise is to talk the kids through some basic Python syntax,
especially in relation to PyGame which is what subsequent exercises will use.

It's the simplest possible thing using PyGame.

You should get them to type it up following along, whilst you explain
everything.

Finally, there's one challenge to make sure they understood everything.
Or at least, some of it.

Setup:

* You should start with a version of ball.py with lots of carriage returns
  everywhere that you can then delete, to reveal a bit of the program
  a bit at a time.

Before starting you should set expectations:

* This exercise is boring and terrifying.
* They won't understand everything.
* But from next week, we will be back to real games.

Things to explain then reveal.
------------------------------

Perhaps tick each item off to make sure you don't miss some...

* What's a comment.

```python
#######################################################################################
# CodeClub Ball exercise
#######################################################################################
```

* In Scratch programs triggered other programs. e.g. "Say 'Hello'" knew how to draw
  speech bubble.
* But options limited. In Python there are many options but we have to choose what we want.
* That's what `import` does.

```python
import pygame
import codeclub
from pygame.locals import *
```

* What `pygame` does.
* We have to tell it to set up (equivalent of 'when green flag clicked')
* What `something.somethingelse()` means - like a broadcast, but sent to something specific. In this
  case pygame. _Emphasise that the brackets are important._
* It's called "calling a method".

```python
pygame.init()
```

* Variables now. Easier than Scratch - no need to say "create" variables - we just put something into them.
* In Scratch variables can be numbers or writing. In Python they can be lots
  of things. This one will be the size and shape of a rectangle

```python
screen_rect = Rect(0, 0, 640, 480)
```

* The next variable represents the whole window where the game occurs.
* Only pygame knows how to make the value we want to store in this variable.
* We call a method on pygame and it replies with the value.
* We also have to pass the screen size into it. So this is kind of like
  a broadcast where:
  * It's sent only to pygame
  * We send some information with the message
  * It sends some information back
* But we don't send this just to pygame. We send it to the `display` variable which belongs to
  pygame.

```python
screen = pygame.display.set_mode(screen_rect.size)
```

* Warn that this is the most complicated bit.
* In Scratch there is just one of each sprite. In Python there are multiple
  instances of each sprite, so we call each type of sprite a "class".
* Also, they're not necessarily created at the start of the game. They
  can be created or destroyed later.
* We're going to call our sprite `Ball` and say that it's a type of CodeClub
  sprite. This second bit means it knows how to do lots of the typical
  things which CodeClub sprites need to do.

```python
class Ball(codeclub.CodeClubSprite):
```

* Each script on a class is called a 'method' and starts with `def`.
* The first method, `__init__` is special and runs when a new Ball is created.
* It stands for "initialise"

```python
	def __init__(self):
		super(Ball, self).__init__() # ignore this line, it's complicated.
```

* When our `__init__` method is called, we want to ask ourselves to set a costume.
* This is possible only because we've said we're a CodeClub sprites, and all
  CodeClub sprites know how to do this.
* We need to tell ourself just what sort of costume we need - the name of an image
  file and how big we want to be.

```python
		self.set_costume('ball.png', 50)
```

* Now we set up some more variables.
* Talk through the lines.

```python
background = pygame.Surface(screen_rect.size)
ball = Ball()
all = pygame.sprite.RenderUpdates()
```

* The `all` variable contains a list of all the different sprites.
  pygame will draw these. So we need t make sure that the ball we've
  made is within that list.
* So we send a message ("call a method") to the 'all' list,
  asking it to add the ball to itself.

```python
all.add(ball)
```

* Now we actually run the game.
* We keep running as long as the variable `running` is 'yes'.
* 'yes' is `True`

```python
running = True

while running:
```

* We stop the game running when someone presses escape or the close
  box on the window is pressed.
* Talk through the lines.

```python
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			running = False
```

* We want to move the ball whenever left or right is pressed.
* We set up a new variable containing the state of all the keys, which pygame tells us.

```python
	keys_pressed = pygame.key.get_pressed()
```

* `keys_pressed[name of key]` is 0 if the key is not pressed, or 1 if it is pressed
* We tell our ball to point in a certain direction and move. Again, all CodeClubSprites
  know how to do this - not just our Ball.

```python
	if keys_pressed[K_RIGHT]:
		ball.point_in_direction(180)
		ball.move(5)
	if keys_pressed[K_LEFT]:
		ball.point_in_direction(0)
		ball.move(5)
```

* Finally we do some things to draw the ball on a blank background.

```python
	all.clear(screen, background)

	dirty = all.draw(screen)
	pygame.display.update(dirty)
```

Challenge
---------

This is all going to be very terrifying for them so it's something simple where
they copy existing code.

TODO
----

* Add another sprite (e.g. a goal, a football background) in the data directory so kids who want to push it further can have more possibilities.
