# Tutorials
This section of the documentation features simple guides on how to use the program, and on how to modify it.

## For users

### How to make the program draw a diagram
1. Run the main.py file.
2. Once the prompt (>>>) appears, enter 'start'.
3. Once prompted to, enter or paste the diagram description. 
4. Your diagram will appear in a new window shortly.

All further tutorials assume you have the program's command prompt (>>>) open.
### How to view diagram history and full versions of descriptions
1. Run 'history'.
2. Locate the description you want to see fully and check its ID.
3. Run 'history <ID>', such as 'history 3'.

### How to get program info, toggle debug mode, and exit the program
1. To view program info such as version, author and release date, run 'info'
2. To toggle debug mode, simply run 'debug'. YOu will  be informed of hwo the setting changed after you ran the command.
3. To exit the program, run 'exit', or close the window in which it is running. THe program will be closed after 3 seconds.

## For developers

### How to see logs and operate with them
1. Check the 'log' file in this directory (it is autocreated after first program run).
2. You may operate with the file using the Logger module; you can check its capabilities in the logger.py file.

More tutorials are to follow. If you have ideas for tutorials or you're unsure of how to do something, please create an issue on the GitHub page.