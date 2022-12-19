#Imports
from datetime import datetime
from time import sleep
import os 
import random

# Variables
path = '/home/dracul/programing/python/poemary/poems/'
poems_list = [i.name for i in os.scandir(path)]

# Funtions
def select_poem():
    '''Search in the poems dir, select a poem and returns a dict with name of file and title'''
    choice = random.choice(poems_list)
    # To make the dir use choice as name_file and split the name file by the . and use the first item tu the tittle 
    choice_info = {
            'file_name': choice,
            'title': choice.split('.')[0]
            }
    return choice_info

def load_poem(file_name):
    '''Load de poem file'''
    with open(path + file_name, 'r', encoding='utf-8') as f:
        poem = f.readlines()
    return poem

def continue_poem(func):
    '''Clean the window and continue de poem after a pause'''
    def wrapper(*args, **kwargs):
        os.system('clear')
        print(f'                      {poem_info["title"]}              {datetime.now().strftime("%H:%M")}')
        func(*args, **kwargs)
        input('...')
    return wrapper

@continue_poem
def declaim(poem):
    '''Declaim the choseen poem making a pause in each verse'''
    global counter
    for line in poem:
        if line != poem[counter]:
            continue
        elif line == '\n':
            break
        else:
            print(line)
            sleep(1)
            counter += 1
        

def run():
    '''Principal function that runs the script'''
    global counter
    global poem_info
    counter = 0
    poem_info = select_poem()
    poem = load_poem(poem_info['file_name'])
    while counter < len(poem):
        declaim(poem)
        counter += 1
# Main

if __name__ == '__main__':
    run()
