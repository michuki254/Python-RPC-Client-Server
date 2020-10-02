import xmlrpclib
import time
import random
from click._compat import raw_input
from SimpleXMLRPCServer import SimpleXMLRPCServer


def RockPaperScissors(user_input):
    CPU = 0
    YOU = 0
    try:
        a = random.randint(1, 3)
        b = int(user_input)

        if (a == 1 and b == 1) or (a == 2 and b == 2) or (a == 3 and b == 3):
            result = ("IT IS A TIE! \nCPU's Score: " + CPU + " Your Score: " + YOU)
        elif (a == 1 and b == 2):
            YOU = YOU + 1  # score
            result = ("CPU: Rock \nYou: Paper \nYOU WIN!!\nCPU's Score: " + CPU + " Your Score: " + YOU)
        elif (a == 1 and b == 3):
            CPU = CPU + 1  # score
            result = ("CPU: Rock \nYou: Scissor \nCPU WINS!!\nCPU's Score: " + CPU + " Your Score: " + YOU)
        elif (a == 2 and b == 1):
            CPU = CPU + 1  # score
            result = ("CPU: Paper \nYou: Rock \nCPU WINS!!\nCPU's Score: " + CPU + " Your Score: " + YOU)
        elif (a == 2 and b == 3):
            YOU = YOU + 1  # score
            result = ("CPU: Paper \nYou: Scissor \nYOU WIN!!\nCPU's Score: " + CPU + " Your Score: " + YOU)
        elif (a == 3 and b == 1):
            YOU = YOU + 1  # score
            result = ("CPU: Scissor \nYou: Rock \nYOU WIN!!\nCPU's Score: " + CPU + " Your Score: " + YOU)
        elif (a == 3 and b == 2):
            CPU = CPU + 1  # score
            result = ("CPU: Scissor \nYou: Paper \nCPU WINS!!\nCPU's Score: " + CPU + " Your Score: " + YOU)
        #"CPU's Score: " + CPU + " Your Score: " + YOU
        return (result)
    except Exception as ex:
        return "error"
def connEstablished():
    return 'Connection was successful'

server = SimpleXMLRPCServer(('127.0.0.1', 7001))
print('Server started successfully')
server.register_function(RockPaperScissors)
server.register_function(connEstablished)
server.serve_forever()