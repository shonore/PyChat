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
        #self.fileName.close() #close the file when you are done processing it
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
    def profanityFilter(self,message):
            dict={"warning":("(ock|","[ock|","a.rse|","ar5h0le|","ar5h0les|","ars3|","arse hole|","basterd|","basyard|","basyards|","battyboy|","bum bandit|",
                            "bum hole|","bumbandit|","bum-bandit|","cvnt|","ities|","k@ffir|","k@ffirs|","jungle bunny|","twatt|","twattish|","twunt|",
                            "nig nog|","p00f|","pp@kis|","00fs|","p00fter|","po0f|","poff|","towel head|","cvnts|","darkie|""darky|","dick&nbsp;head|"
                          ),"illegal":("fuck|","a$$hole|","shit|","a$$holes|","a+*hole|","ar$ehole|","ar$hole|","ar$holes|","bastard|","bastards|","c-u-n-t|","k**t|",
                            "cunting|","cunts|","cunt's|","d**khead|","d1ck|","d1ck!|","d1ckh@ed|","dickhead|","dumbfuck|","dumbfucker|","f^^k|","f^^ked|",
                            "fucker|","fucking|","mohterfuckers|","mohterfukcer|","mohterfuccer|","niga|","nigga|","niggaz|","nigger|","niggers|","mohterfuccers|",
                            "mohterfuck|","mohterfucker|","mohterfuckers|","mohterfucking|","mohterfucks|","mohterfuk|","mohterfukcer|","mohterfukcers|",
                            "mohterfuking|","mohterfuks|","muthafuckers|","muthafucking|","muthafucks|","muthafukas|","nig nog|","f^ck|","f^cker|",
                            "f^cking|","asshole|","asswipe|","blowjob|","blow-job|","titties|","whore|","dick|")}

            val2=message.split()
            for word in val2:
              for key,values in dict.items():
                  for words in values:
                      val2=word+"|"
                  if(val2 in values and "warning" == key):
                     message = "warning!watch your language"
                     return message
                  if(val2 in values and key=="illegal"):
                     message = "you are using illegal so,you are out"
                     return message
                     #remove(conn)
            return message
