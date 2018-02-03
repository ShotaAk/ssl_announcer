#!/usr/bin/env python3

from listener import Listener
from effector import Effector


def add_one(value)->int:
    return value + 1

if __name__ == "__main__":
    my_listener = Listener('224.5.23.1',10003)
    my_effector = Effector()


    while 1:
        my_listener.receive()

        command = my_listener.get_command()
        my_effector.play_command(command)



