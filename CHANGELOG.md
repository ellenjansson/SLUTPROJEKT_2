## Changelog

### Version 1.0: Function to open random word from list

#### Tillagt eller ändrat

- Added filemanagement inside a constructor
- Added two classes, Word and Game
- Added a main function

***

### Version 2.0: Function that compares if word is correct

#### Added or changed

- Added a compare function with a guess variable
- Added an input linked to the Word class asking for a word
- Added a guessing counter

***

### Version 3.0: Guessing system

#### Added or changed

- Changed language to english
- Added a while loop checking if the max guesses have been guessed

***

### Version 4.0: Compare loops and colorencoding

#### Added or changed

- Added if-statement with colorencoded boxes using ansi-chars

***

### Version 4.1: Colorencoding system fixed

#### Added or changed

- Fixed colorencoding problem with the yellow and white color
- Imported Counter from collections

#### Removed

- Removed colorencoding if-statement from previous version and replaced it with a for loop and another improved if-statement

***

### Version 5.0: Added constants for ansi-chars

#### Added or changed

- Added constants for all the colors aswell as an ascii box.
- Replaced all ansi-chars in code with constants.

***

### Version 6.0: Fixed too long/short answers and restart option

#### Added or changed

- Added an if-statement with an interval correcting if a too long/short guess is guessed
- Moved guess counter inside the if-statement correcting the word lengths
- Added a restart option that clears the consol
- Imported os
- Imported sleep from time
- Imported colorama

***

### Version 6.1: Fixed restart option and color problem

#### Added or changed

- Added spacings inbetween the prints
- Fixed else from the if-statement from the restart option. When it asked the person to repeat the answer nothing happened
- Added line constant and put them inbetween the answers

***

### Version 6.2: Fixed small problem with restart option

#### Added or changed


- Changed y to a n in the restart if-statment for no answer.

***

### Version 7.0: Completed versionwith docstrings and comments

#### Added or changed

- Added docstrings and comments throughtout the code. 
