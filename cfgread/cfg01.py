#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())


######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()

## Iterate thrhough configlist
for x in configlist:
    print((x.rstrip("\n").lstrip()))

## Always close your file
configfile.close()

