from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatBot import genResponse

chatbot = ChatBot('Ron Obvious')

userIn = ""

print("Start Speaking to Bot: ")

while(userIn != "exit"):
    userIn = input()
    if(userIn != "exit"):
        print(genResponse(userIn))

