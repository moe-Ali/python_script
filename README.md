# python_script

Used libraries: os, sys, shutil, json

This script is coded to:
- copy directories from the SOURCE directory with a specific pattern in them to the TARGET directory 
- striping off some words from copied directory names in the new directory (inside the TARGET directory)
- make a JSON file inside the target directory that contains some data about this copied directories

To run this code:
- python script.py {source directory} {target directory}
- as default use "python script.py test-source test-target"

Notes:
- source directory must be in the same directory as script.py
- target directory will be in the same directory as script.py
- to change the pattern which is "test" by default change the pattern variable in line 7
- to change the word you want to stripp off when making a copy which is "_test" by default 
     change the word_to_stripoff variable in line 8
