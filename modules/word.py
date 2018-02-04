#This Word class is responsible for manipulating the words in the profanitylist.txt file and the username.txt file.
#there needs to be functions to READ, INSERT, and, UPDATE the fields in the files. The files are piped delimited between columns
#and space delimited between rows
import sys
from string import *
import errno
import fileinput, optparse

#a Word class that will contain function for manipulating word records from in input files
class Words(object):
    #constructor. Takes the file name and the chat message as the arguments. They are initially set to blank
    def __init__ (self, fileName=None, chatMsg=None):
        self.current = ""
        self.fileName = fileName
        self.chatMsg = chatMsg
    #a function to search for a word in input file and compares it to the input word
    def searchWord(keyWord, fileName):
        errorMsg = "No match found"
        #open the file for read and iterate through each line until a match is found
        with open(fileName, "r") as f:
            lines = f.readlines()
    #a function to append a unquie new word to a file
    def insertNewWord(newWord, fileName):
        #first open the file to append a new value
        try:
            f = open(fileName, "a")
            #check if the word already exists do not insert into file and notify user
            #user search function here
        except:
            print("Error! Unable to open the input file.")
