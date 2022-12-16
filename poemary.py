# Imports
from datetime import datetime
from time import sleep
import os 
import random

# Variables
path = '/home/dracul/programing/python/poemary/poems/'
poems_list = [i.name for i in os.scandir(path)] 
# Funtions

def select_poem():
    '''Search in the poems dir, select a poem and charge it'''
    pass

def continue_poem():
    '''Clean the window and continue de poem after a pause'''
    pass

def declaim():
    '''Declaim the choseen poem makinga pause in all the dots'''
    pass

def run():
    '''Principal function that runs the script'''
    print(poems_list)

# Main

if __name__ == '__main__':
    run()
