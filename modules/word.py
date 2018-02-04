#This Word class is responsible for manipulating the words in the profanitylist.txt file and the username.txt file.
#there needs to be functions to READ, INSERT, and, UPDATE the fields in the files. The files are piped delimited between columns
#and space delimited between rows
import sys
from string import *
import errno
import fileinput, optparse

#a Word class that will contain function for manipulating word records from in input files
class Word():
    #constructor. Takes the file name and the chat message as the arguments. They are initially set to blank
    def __init__ (self, fileName):
        self.fileName = fileName
        print self.fileName
    #a function to search for a word in input file and compares it to the input word
    def searchWord(self,keyWord):
        errorMsg = "No match found"
        #open the file for read and iterate through each line until a match is found
        lines = open(self.fileName).read().splitlines()
        print("file was opened")
        print lines
        if keyWord in lines:
            print(str(keyWord) + " is in the file")
        else:
            print(str(keyWord) + " is not in the file")

    #a function to append a unquie new word to a file
    def insertNewWord(newWord):
        #first open the file to append a new value
        try:
            f = open(self.fileName, "a")
        except:
            print("Error! Unable to open the input file.")
        #check if the word already exists. If does not, then insert into file and notify user
        if searchWord(newWord) == FALSE:
            f.append(self.fileName)
            print("insert successful")
            f.close()
        else:
            print("insert fail")
            f.close()
