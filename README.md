
# Greed
Greed is the game where players recollect points by grabing artifacts that are falling. The more artifacts the user collects the more points he gets. 
## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 Greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Greed               (source code for game)
  +-- game              (specific game classes)
    +--casting          (Module with classes)
      --actor
      -- cast
    +--directing        (Module with classes)
      --director
    +-- services        (Module with classes)
      --keyboard_services
      --video_service
    +-- shared          (Module with classes)
      --color
      --point
+-- __main__.py       (entry point for program)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
Gabriel Guerrero gguerero@gmail.com