'''
Send a specific SMS to several phones using Twilio.

Twilio needs to be installed and the creation of a register in the official website of the brand.

Note: SMS sending services generate expenses in dollars.

'''

from twilio.rest import Client

def sendMultipleMessages(message, listPhones):

    for i in list: 
        
        message = client.messages.create(to=i, from_="your_number", body=message)
        
    print(message.sid)    

list = ['+PPDD9XXXXXXXX']

account_sid = 'AC83aae6a685fcabb2fd5eb724215e1ac6'
auth_token = 'your_auth_token'

client = Client(account_sid, auth_token)

sendMultipleMessages('message', list)
