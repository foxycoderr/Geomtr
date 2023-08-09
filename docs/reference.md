# Reference
This section will give you an overview of how the program works and then briefly explain each of the program's modules' functionalities, giving you an insight into the program; recommended to read before looking at the code.

Note that this information is not the full documentation, and is only designed to give you a rough understanding of how the program is split into modules and what each one does. You will find explanations for the code within the code itself, in the inline comments.
## Overview
Geomtr uses multiple modules in the form of classes, whose functions are run in the required order by functions of the main runner class. Each file in this folder contains a module. If you run the program, you will also see two new files "log" and "user_data.json", appear automatically. They store run logs (useful for developers to see what the program does), and custom user data, such as username, history, debug mode etc.

## Modules
### Main
This file contains the main Runner class, which is responsible for running other modules and working with the UI. When the user runs a command, it is read by one of this class' functions, which then runs the code needed to complete what the user demanded.

### Input
This class' functions just input the problem text and validate it (check it has no invalid symbols).

### Tokenizer
This is a simple class which contains two functions, one to split the problem text into sentences, the other to split sentences into words, and get the text ready for parsing.

### Parser
This class contains functions which read through the problem and pick out the data; for example, if the parser stumbles upon the word 'rectangle', it will assume the next word (say 'ABCD') is the letters that define the rectangle.

### Converter
This class uses the data found by the parser to create Point, Angle and Line objects, even from rectangles and triangles.

### Coordinator
This class uses the objects and properties created by the converter to calculate coordinates of points, which can then be used to draw the diagram.

### Drawer
This class uses the coordinates of points and the data given about lines to draw them in a graphic window. Operated by PyGame.

### Logger
This is a simple logger that logs events into the logfile. 