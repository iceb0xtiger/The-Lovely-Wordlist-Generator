*README FILE FOR THE LOVELY WORDLIST GENERATOR*

Thank you for your interest in The Lovely Wordlist Generator.

A long time ago I moved into a large apartment complex and didn't have internet. I discovered that the password to one of my neighbors Wifi was the word "lovely71". I don't know why, but I couldn't get this out of my head. Why would someone choose such a simple password for their Wifi? I assumed 71 must have been their birth year. I searched the ROCKYOU database and discovered the word lovely appeared quite often in the list. 

So I had the idea to create a wordlist generator that would generate variations on a root word. The code cycles through concatenating numbers 1 - 999 and then years 1900 - 2023. 

Then it cycles through what is supported as a list of names. The name Sophia is used as an example but code supports adding more names here:  

# List of common female names
female_names = ['Sophia']  # Replace with the actual list of names

While this code is gender specific in it's implementation it supports whatever names you want to enter.

Once your modified code is run it saves the wordlist in the file "variations.txt" That will be your word list.

The plan for this project is to implement a GUI version with checkboxes so you can more easily taylor the generation in an over-all better user experience.

The special version of the code iterates the same way as the first version however it also includes special characters and takes about 20 times longer to run. The resulting list using only 1 name for iteration will generate over a gigabyte of variations. 

Thank you for checking out my project!

-iceb0xtiger