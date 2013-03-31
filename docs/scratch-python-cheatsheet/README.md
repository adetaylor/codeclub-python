Scratch-Python cheat sheet
==========================

Here's a conversion from Scratch to Python and PyGame

Scratch                                                         | Python
---------------------------------------------------------------:|--------
![New sprite icons](new-sprite-icons.png)                       | ```python```
                                                                | surface = pygame.image.load("c:\SomeFolder\SomeImage.png")
																														  	|	```
																																| but this requires a complete file location so you might prefer
																																| to do this:
																																| ```python
																																| main_dir = os.path.split(os.path.abspath(__file__))[0]
																																| file = os.path.join(main_dir, 'data', 'SomeImage.png')
																																| ```
																																| to use an image in a folder called 'data' in the same place
																																| as your script.
![Sprite title and motion types](sprite-title-motion-types.png) | Testing...
