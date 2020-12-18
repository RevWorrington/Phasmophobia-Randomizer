# Phasmophobia Randomizer

A quick Python randomizer that can handle any number of available players. Can allow duplicates or not.

## How to Use

Run the program either in a Python IDE (IDLE, etc.) or straight on the command line, and input the following information when prompted:
1. Enter the number of players (1-4): The number of players. Type the number of players you have from 1 to 4. Other numbers will result in the program showing an error and requesting the input again.
2. Do you want to allow item duplicates between players? (Y/N): Whether you want players to be able to recieve the same items as each other or not. Type "Y" to allow them to get the same items or "N" to keep each item unique (not case-sensitive)
3. The program will run, displaying the items for each player.
4. The message "Good Hunting! Press any key to close." will display. Pressing any key will close the program.

## Rules for Program

The program functions off 3 major assumptions, aside from the constraints placed in the game:

1. The quantity of an item does not effect the chance of recieving it. This means that you are no more likely to recieve a Lighter (2 in game) than a Video Camera (6 in game). This is not true if there are none of the item available left, at which point it can no longer be rolled.
2. Each player may only recieve an item once, i.e. they cannot roll 2 Candles.
3. The following is allowed: Video Cameras each come with an optional free Tripod, and each player is allowed a Head-Mounted Camera.

Additional rules can be added for the group based on preference. Examples include: Allowing candles to be lit in the van if the group lacks a Lighter. Allowing separate use of Sanity Pills. Allowing a Lighter with a Smudge Stick. Allowing everyone to have a flashlight. Your choice.
Feel free to download and use this in any video, streaming service, coding project, web project, or other activity covered by the Creative Commons license. Attribution as required.

Happy Hunting!
