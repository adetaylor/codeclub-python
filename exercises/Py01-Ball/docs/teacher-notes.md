Py01-Ball
=========

The aim of this exercise is to talk the kids through some basic Python syntax,
especially in relation to PyGame which is what subsequent exercises will use.

It's really the absolute simplest thing I can come up with in Pygame.

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

Explain what a comment is. They start with #. The pupils can put whatever they
want into comments.

```python
#######################################################################################
# CodeClub Ball exercise
#######################################################################################
```

Explain that, in Scratch, their programs actually triggered other programs.
For example, 'Say "Hello"' knew how to draw a speech bubble. You relied on those.
The problem with Scratch is that there were a fixed number of those things and
you couldn't do things like multi-player network games, nor bouncing balls,
nor robots, etc.

In Python there are loads of other programs we can rely on, to do all sorts of things.
But we need to say what other programs we want to use. That's called "importing"
their programs into ours.

```python
import pygame
import codeclub_pygame_handy_functions
from pygame.locals import *
```

The main other program we're using is called pygame, which shows a window on
the computer screen where we can draw a game into it. Now that we've imported it
we can tell the pygame program to do everything it needs to do at the beginning.
It's a bit like telling pygame that the green flag was clicked.

The '.' means we're asking pygame to do something. This is a bit like sending
a broadcast, except that we're sending it specifically to pygame instead of to
everything. This is called 'calling a method'.

```python
pygame.init()
```

Now we set up some variables we need. In Scratch, variables are usually
just numbers but they can be words. In Python, they can be more complicated
things such as rectangles.

Let's say how big we want the screen to be:

```python
screen_rect = Rect(0, 0, 640, 480)
```

The next variable is even more complicated. It represents the whole
computer screen. Pygame knows how to make this, so we'll call a method
on pygame and it will reply with the result.

Also, we're telling pygame the size of our screen. So this is kind of
like sending a broadcast to pygame, which includes a bit of information
- the screen size - and then pygame replies to the broadcast with
a bit more information - the screen.

```python
screen = pygame.display.set_mode(screen_rect.size)
```

Now a variable containing an image. Here we're sending a message
to our own module of code.

```python
ball_image = codeclub_pygame_handy_functions.load_image_from_data_directory('ball.png')
```

And now let's shrink it!

```python
small_ball_image = pygame.transform.scale(ball_image, (50, 50))
```

Now finally we can create a Sprite. This is where we see the first
proper advantage over Scratch. In Scratch there is exactly one of each
sprite. In Python, you say you've got a _class_ of sprites, and there can
be several of them.

So here we're going to say we have a ball. We say how a ball is supposed
to work. But there might be several ball.

```python
class Ball(pygame.sprite.Sprite):

    def __init__(self):
        super(Ball, self).__init__()
        self.image = small_ball_image
        self.rect = self.image.get_rect(midbottom=screen_rect.midbottom)
```

TBC...

```python

    def move(self, direction):
        self.rect.move_ip(direction*5, 0)
        self.rect = self.rect.clamp(screen_rect)

background = pygame.Surface(screen_rect.size)
ball = Ball()
all = pygame.sprite.RenderUpdates()
all.add(ball)

running = True

while running:

    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            running = False
    keys_pressed = pygame.key.get_pressed()
    direction = keys_pressed[K_RIGHT] - keys_pressed[K_LEFT]
    ball.move(direction)

    all.clear(screen, background)

    dirty = all.draw(screen)
    pygame.display.update(dirty)
`