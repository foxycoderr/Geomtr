# Reference
This section will briefly explain each of the program's modules' functionalities, giving you an insight into the program; recommended to read before looking at the code.

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