
from pygame import mixer
import time
from proto import referee_pb2

ref = referee_pb2.SSL_Referee

class Effector(object):

    def __init__(self):

        mixer.init()

        self._sound_dict = {}
        self._sound_dict[ref.HALT] = mixer.Sound('./sounds/halt.wav')
        self._sound_dict[ref.STOP] = mixer.Sound('./sounds/stop.wav')
        self._sound_dict[ref.NORMAL_START] = \
            self._sound_dict[ref.FORCE_START] =\
            mixer.Sound('./sounds/start.wav')

        self._sound_dict[ref.PREPARE_KICKOFF_BLUE] = \
            self._sound_dict[ref.PREPARE_KICKOFF_YELLOW] = \
            mixer.Sound('./sounds/kickkoff.wav')
        self._sound_dict[ref.PREPARE_PENALTY_BLUE] = \
            self._sound_dict[ref.PREPARE_PENALTY_YELLOW] = \
            mixer.Sound('./sounds/penalty.wav')
        self._sound_dict[ref.DIRECT_FREE_BLUE] = \
            self._sound_dict[ref.DIRECT_FREE_YELLOW] = \
            mixer.Sound('./sounds/direct.wav')
        self._sound_dict[ref.INDIRECT_FREE_BLUE] = \
            self._sound_dict[ref.INDIRECT_FREE_YELLOW] = \
            mixer.Sound('./sounds/indirect.wav')
        self._sound_dict[ref.TIMEOUT_BLUE] = \
            self._sound_dict[ref.TIMEOUT_YELLOW] = \
            mixer.Sound('./sounds/timeout.wav')
        self._sound_dict[ref.GOAL_BLUE] = \
            self._sound_dict[ref.GOAL_YELLOW] = \
            mixer.Sound('./sounds/goal.wav')

        self._sound_dict['BLUE'] = mixer.Sound('./sounds/blue.wav')
        self._sound_dict['YELLOW'] = mixer.Sound('./sounds/yellow.wav')

        for key in self._sound_dict:
            self._sound_dict[key].set_volume(0.7)

        self._referee_command = None

        self._TIME_SLEEP = 0.8


    def play_command(self, referee_command):
        if referee_command != self._referee_command:
            self._referee_command = referee_command

            if referee_command in self._sound_dict:
                if referee_command == ref.PREPARE_KICKOFF_BLUE or \
                        referee_command == ref.PREPARE_PENALTY_BLUE or \
                        referee_command == ref.DIRECT_FREE_BLUE or \
                        referee_command == ref.INDIRECT_FREE_BLUE or \
                        referee_command == ref.TIMEOUT_BLUE or \
                        referee_command == ref.GOAL_BLUE:
                    self._sound_dict['BLUE'].play()
                    time.sleep(self._TIME_SLEEP)

                elif referee_command == ref.PREPARE_KICKOFF_YELLOW or \
                        referee_command == ref.PREPARE_PENALTY_YELLOW or \
                        referee_command == ref.DIRECT_FREE_YELLOW or \
                        referee_command == ref.INDIRECT_FREE_YELLOW or \
                        referee_command == ref.TIMEOUT_YELLOW or \
                        referee_command == ref.GOAL_YELLOW:
                    self._sound_dict['YELLOW'].play()
                    time.sleep(self._TIME_SLEEP)

                self._sound_dict[referee_command].play()


def sub_one(value)->int:
    return value - 1
