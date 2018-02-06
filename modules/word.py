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
    #def __init__ (self):

    #a function to search for a word in input file and compares it to the input word
    def searchWord(self,keyWord,filename):
        flag = False
        errorMsg = "No match found"
        #open the file for read and iterate through each line until a match is found
        lines = open(filename).read().splitlines()
        print("file was opened")
        print lines
        if keyWord in lines:
            print(str(keyWord) + " is in the file")
            flag = True
            return flag
        else:
            print(str(keyWord) + " is not in the file")
            return flag
        #self.fileName.close() #close the file when you are done processing it
    #a function to append a unquie new word to a file
    def insertWord(self,newWord, filename):
        #first open thse file to append a new value
        try:
            f = open(filename, "a")
        except:
            print("Error! Unable to open the input file.")
        #check if the word already exists. If does not, then insert into file and notify user
        wordFlag = self.searchWord(newWord, filename)
        if wordFlag == False:
            f.write(newWord+"|")
            print("insert successful")
            f.close()
        else:
            print("insert fail")
            f.close()
    def profanityFilter(self,message, username, conn):
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
                        message = "You have used an illegal word. You will be banned from the chat room. Goodbye!"
                        #add logic for inserting username into the blacklist.txt files
                        self.insertWord(username, "blacklist.txt")
                        return message
                        #remove(conn)
            return message
    #def login():
        #w=Word("test-usernames.txt")
        #while(1):
            #x=raw_input("Please enter your username to login:   ")
            #if(w.searchWord(x)==True):
                #return x
            #else:
                #print("oops! we dont have that username on file, you may have mistyped it!, try again:  ")
                #continue


    #def createNewAccount():
        #username=""
        #w=Word("test-usernames.txt")
        #while(1):
            #username = str(raw_input('Please enter a username less than sixteen characters:   '))
            #if(w.searchWord(username)==True):
                #print("That username is already taken, please enter a different one:   ")
                #continue
            #if len(username)>16:
                #continue
            #break
        #w.insertNewWord(username)
        #return username

#add this code to the client.py files
#if(z)==0:
    #username=login()
#else:
    #username=createNewAccount()
#This is the remove function
#def removeWord(self,rword):
    #try:
        #f=open(self.fileName,"r")
    #except:
        #print("Error! Will not open file")
    #lines = f.readlines()
    #f.close()
    #f=open(self.fileName,'w')
    #for line in lines:
        #if line!=rword+"\n":
            #f.write(line)
