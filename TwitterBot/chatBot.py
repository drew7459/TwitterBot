from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.comparisons import levenshtein_distance

chatbot = ChatBot('Ron Obvious',
                  statement_comparison_function=levenshtein_distance
                  )

def genResponse(message):
    return chatbot.get_response(message)


