from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatBot import genResponse
import time

chatbot = ChatBot('Ron Obvious')

userIn = ""

print("Start Speaking to Bot: ")

while(userIn != "exit"):
    userIn = input()
    start_time = time.time()
    if(userIn != "exit"):
        print(genResponse(userIn))
    elapsed_time = time.time() - start_time
    print(time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))
    

