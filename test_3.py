import sys
import os

user_input = input("Enter the path of your file: ")

assert os.path.exists(user_input), "I did not find the file at, "+str(user_input)
f = open(user_input,'r+')
print("Hooray we found your file!")
#stuff you do with the file goes here
#f.close()
