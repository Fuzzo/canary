# File: commands.py
#
# Contains the commands that the shell can call.

from googlevoice import Voice
from googlevoice.util import input

"""This default command is called when the command does not exist."""
def not_found(phonebook, voice, args):
    print "Command not found: " + args[0]

"""This command sends a text message to a subset of the students as defined by
the arguments. The last argument is the message, so you should enclose the
message in quotes.

Arguments before the message constitute subsets of the phonebook."""
def send(phonebook, voice, args):
    if len(args) == 0:
        help()

def help():
    print "Help logic goes here."
