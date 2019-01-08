import os 
import urllib.request

def readFile(nameFile):
    
    quotes = open(os.getcwd() + nameFile) 
    contentes = quotes.read()
    quotes.close()
    
    return contentes

def checkProfanity(message):
    
    message = message.replace(' ', '%')
    message = message.replace('\n', '%')
    message = 'http://www.wdylike.appspot.com/?q=' + message
    
    connection = urllib.request.urlopen(message)
    result = connection.read()
    connection.close()
    
    if result == (b'true'):
        return 'There are profanity words'
    else: 
        return 'There are no words of desecration'

message = readFile('/note.txt')

print( checkProfanity(message) )
