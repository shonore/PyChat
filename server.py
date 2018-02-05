#This is the server script for the multithreaded python chat applicaiton
import pdb
import sys
from string import *
from socket import *
import select
import thread
import errno
from modules.word import Word #importing the custom word class to read, input, and, update data

PORT=8888
s = socket(AF_INET, SOCK_STREAM)
# checks whether sufficient arguments have been provided
if len(sys.argv) != 2:
     print "Must enter the following: script, IP address of server"
     exit()
# takes the first argument from command prompt as IP address
HOST= str(sys.argv[1])
try:
 s.bind((HOST,PORT))
 s.listen(100)
except:
 raw_input("Error: Server cannot start on IP address "+ str(sys.argv[1]))
 exit()

print "Server is ready!"
print "Listening at: ",s.getsockname()

def listening(conn,addr,username):
 global clients, joinMessage, leaveMessage, status, userStatus
 while 1:
   try:
     temp=conn.recv(1024)
   except:
     return
   #the word filter logic would go here
   profanityFile = "profanityList.txt" #passing in the profanity list string, but it will not be processed with Sudha's logic. She uses a dictionary to store the profanity list
   msgFilter = Word(profanityFile)
   dirtyTemp = temp
   temp = msgFilter.profanityFilter(dirtyTemp)
   
   #when the message is displayed in the chat window we want to include the associated username
   messageClient=username+": "+temp+" "
   messageServer=username+": "+temp+" "
   leaveMessage=username+" left the chat"
   #print the username and message to the server for logging purposes
   if temp != "":
     print messageServer.decode()
   else:
     print leaveMessage.decode()
     try:
       for i in range(0,(len(clients)/4)):
         try:
           clients[i*4].send(leaveMessage.encode())
         except error as e:
            #remote peer disconnect
            print "No clients connected"
            break

     except IndexError:
       print "no clients connected"
       break
     break
   flag = 0
   for client in clients:
     #to view user list
     if username == client:
       if str(client)+": -userlist" in messageClient:
         try:
           #send error list
           usrListAddr = clients.index(client)-1
           usrListConn = clients.index(client)-2
           clients[usrListConn].sendall(str(userStatus), usrListAddr)
          #display error message if the username cannot be retieved
         except:
           errorMsg="Error. Cannot retieve user list"
           clients[usrListConn].sendall(str(errorMsg), usrListAddr)
     #for direct message
     if "@"+str(client) in messageClient:
       flag = 1
       mentionAddr = clients.index(client)-1
       mentionConn = clients.index(client)-2
       clients[mentionConn].sendall(messageClient, mentionAddr)
       break
     #if the client doesn't specify a particular client with the @ symbol send to all
   if flag == 0:
     for i in range(0,(len(clients))/4):
       try:
         #send the message to all connected clients
         clients[i*4].send(messageClient)
       except:
         pass
 return

def manager():
 global s,clients,joinMessage

 while 1:
   conn,addr=s.accept()
   username=strip(conn.recv(1024))
   thread.start_new_thread(listening,(conn,addr,username))
   old=0
   for i in range(0,len(clients)/4):
     if clients[i*4]==conn:
       old=1
       break
   if old==0:
     status = "online"
     #validate to see if the username already exists. If it does, assign another username **
     #Here is the logic for read/insert of username.txt files with the given username
     userNameFile = 'test-username.txt' #this is a hardcoded value
     #1. Create a new instance of the word class
     wordValue = Word(userNameFile)
     #2.get input username from the users
     #3.check to see if the user name already exists in the username.txt files
     wordValue.searchWord(username)
     #4. If the username does exisit in the file, check to see if it is in the blacklist.txt files
     #5. If the username is not in the blacklist.txt file and not in the username.txt file, insert the username into the username.txt files
     #for i in range (0,(len(clients)/4)):
         #if username == clients[i*4+2]:
           #username="User"+str(randint(1000,9000))
     clients.append(conn)
     clients.append(addr)
     clients.append(username)
     clients.append(status)
     userInfo = "username: "+username+"status: "+status+" "
     userStatus.append(userInfo) #print current users to the console
     joinMessage = username+" joined the chat. Type @[username] for direct messages and -userlist to view other users"

     #notify all clients that a new user has joined and print to the server that the user joined
     print username+" joined the chat"
     #send the username to the userlist in the client chat windows as well as the welcome message
     for i in range(0,(len(clients)/4)):
       try:
         #clients[i*4].send(str(clients[i*4+2]).encode()+": "+clients[i*4+3].encode())
         clients[i*4].send(joinMessage.encode())  #need to encode the data before server can send it
       except error as e:
         print "Error"
         break
 return

clients=[]
userStatus=[]
thread.start_new_thread(manager,())
while 1:
   #set a variable with the user's status. Have it default to offline
   menu="\nCommands:\n\n"
   menu=menu+"! - shutdown\n"
   menu=menu+"? - current users online\n"
   menu=menu+"\n>"
   result=raw_input(menu)
   if strip(result)=="!":
     s.close()                             #shut down the server
     sys.exit()
   if strip(result)=="?":
     #check to see if the client is online or not
     for client in clients:
       if client == 0:  #if the connection is false
         print "test"
         i = client.index(client)+3
         clients[i] = "offline"#the the user is offline
     for i in range(0,(len(clients)/4)):
       try:
         userStatus = "username: "+clients[i*4+2],"status: "+clients[i*4+3]+" " #print current users to the console
         print "username: ",clients[i*4+2],"status: ",clients[i*4+3] #print current users to the console
       except:
        pass
