######################################################
###  Machine Learning Decal, Fall 2018, NLP Track  ###
######################################################

######################################################
#
# This main file can be used to create a conversation
# loop. Please DO NOT modify this file, as we will
# use it for grading your submissions. You should be
# modifying 'conversation.py' instead.
#
######################################################

import argparse
import os

from conversation import Conversation


def create_loop():

    conversation = Conversation()

    while True:
        inp = input('>>> ')
        if len(inp) > 0:
            print('<<< ' + str(conversation.respond(inp)))

def evaluate_all(indir):

    for fname in os.listdir(indir):
        print(fname)

        with open(indir + '/' + fname, 'r') as f:

            conversation = Conversation()
            print('>' * 30)

            for line in f:
                line = line.strip()
                print('>>> ' + line)
                print('<<< ' + conversation.respond(line))
            
            print('<' * 30)

        print()

def main():
    
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str)
    args = parser.parse_args()

    if args.dir:
        evaluate_all(args.dir)
    else:
        create_loop()


if __name__ == '__main__':
    main()

