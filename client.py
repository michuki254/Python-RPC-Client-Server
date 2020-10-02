import xmlrpclib
import time

client = xmlrpclib.ServerProxy('http://'+str(raw_input('Provide ip and port (0.0.0.0:0000) of server to connnect to: ')))
print(client.connEstablished())
print('\n')

try:
    user_response = raw_input("Start Game (Yes/No)")
    while (user_response == 'y') or (user_response == 'Y') or (user_response == 'yes') or (user_response == 'Yes'):
        user_input = raw_input("Enter Rock(1) Paper (2) Scissor (3): \n")
        print(client.RockPaperScissors(user_input))
        user_response = raw_input('Play again? (Yes/No)')
    print ("\n")
    print ("Thanks for playing!")
    time.sleep(1)  # OPTIONAL
    exit()
except:
     print ("Program terminated")