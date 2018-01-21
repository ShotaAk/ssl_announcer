#!/usr/bin/env python3

import listener
import effector


def add_one(value)->int:
    return value + 1

if __name__ == "__main__":
    my_listener = listener.Listener('224.5.23.1',10003)
    my_effector = effector.Effector()


    while 1:
        my_listener.receive()

        command = my_listener.get_command()
        my_effector.play_command(command)



