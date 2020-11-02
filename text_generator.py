from os import environ
from random import seed
from random import randint
import utils

seed(1)

class TextGenerator:
    def __init__(self):
        text_source = utils.getenv('TEXT_SOURCE','resources/edgy.txt')
        textfile = open(text_source,"r")
        texts = textfile.readlines()
        textfile.close()
        self.texts = utils.clean_carriage_return(texts)
    
    def get_random_text(self):
        random_position = randint(0,len(self.texts)-1)
        return self.texts[random_position]


