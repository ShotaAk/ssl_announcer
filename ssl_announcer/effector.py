
from pygame import mixer
import time
from proto import referee_pb2

ref = referee_pb2.SSL_Referee


class Effector(object):

    def __init__(self):

        mixer.init()

        self._MASTER_VOLUME = 0.7
        self._TIME_SLEEP_COLOR = 0.8
        self._TIME_SLEEP_STAGE = 2.0

        self._referee_command = None
        self._referee_stage = None

        # referee commands
        self._sound_commands = {}
        self._sound_commands[ref.HALT] = mixer.Sound('./sounds/halt.wav')
        self._sound_commands[ref.STOP] = mixer.Sound('./sounds/stop.wav')
        self._sound_commands[ref.NORMAL_START] = \
            self._sound_commands[ref.FORCE_START] =\
            mixer.Sound('./sounds/start.wav')

        self._sound_commands[ref.PREPARE_KICKOFF_BLUE] = \
            self._sound_commands[ref.PREPARE_KICKOFF_YELLOW] = \
            mixer.Sound('./sounds/kickkoff.wav')
        self._sound_commands[ref.PREPARE_PENALTY_BLUE] = \
            self._sound_commands[ref.PREPARE_PENALTY_YELLOW] = \
            mixer.Sound('./sounds/penalty.wav')
        self._sound_commands[ref.DIRECT_FREE_BLUE] = \
            self._sound_commands[ref.DIRECT_FREE_YELLOW] = \
            mixer.Sound('./sounds/direct.wav')
        self._sound_commands[ref.INDIRECT_FREE_BLUE] = \
            self._sound_commands[ref.INDIRECT_FREE_YELLOW] = \
            mixer.Sound('./sounds/indirect.wav')
        self._sound_commands[ref.TIMEOUT_BLUE] = \
            self._sound_commands[ref.TIMEOUT_YELLOW] = \
            mixer.Sound('./sounds/timeout.wav')
        self._sound_commands[ref.GOAL_BLUE] = \
            self._sound_commands[ref.GOAL_YELLOW] = \
            mixer.Sound('./sounds/goal.wav')

        self._sound_commands['BLUE'] = mixer.Sound('./sounds/blue.wav')
        self._sound_commands['YELLOW'] = mixer.Sound('./sounds/yellow.wav')
        self._sound_commands['CHEER'] = mixer.Sound('./sounds/cheer.wav')

        for key in self._sound_commands:
            self._sound_commands[key].set_volume(self._MASTER_VOLUME)

        # referee stages
        self._sound_stages = {}
        self._sound_stages[ref.NORMAL_FIRST_HALF_PRE] = \
            self._sound_stages[ref.NORMAL_SECOND_HALF_PRE] = \
            self._sound_stages[ref.EXTRA_FIRST_HALF_PRE] = \
            self._sound_stages[ref.EXTRA_SECOND_HALF_PRE] = \
            mixer.Sound('./sounds/half_pre.wav')
        self._sound_stages[ref.NORMAL_HALF_TIME] = \
            self._sound_stages[ref.EXTRA_TIME_BREAK] = \
            self._sound_stages[ref.EXTRA_HALF_TIME] = \
            mixer.Sound('./sounds/halftime.wav')
        self._sound_stages[ref.POST_GAME] = mixer.Sound('./sounds/endgame.wav')

        for key in self._sound_stages:
            self._sound_stages[key].set_volume(self._MASTER_VOLUME)


    def play_command(self, referee_command):
        if self._referee_command != referee_command:
            self._referee_command = referee_command

            if referee_command in self._sound_commands:
                if referee_command == ref.PREPARE_KICKOFF_BLUE or \
                        referee_command == ref.PREPARE_PENALTY_BLUE or \
                        referee_command == ref.DIRECT_FREE_BLUE or \
                        referee_command == ref.INDIRECT_FREE_BLUE or \
                        referee_command == ref.TIMEOUT_BLUE or \
                        referee_command == ref.GOAL_BLUE:
                    self._sound_commands['BLUE'].play()
                    time.sleep(self._TIME_SLEEP_COLOR)

                elif referee_command == ref.PREPARE_KICKOFF_YELLOW or \
                        referee_command == ref.PREPARE_PENALTY_YELLOW or \
                        referee_command == ref.DIRECT_FREE_YELLOW or \
                        referee_command == ref.INDIRECT_FREE_YELLOW or \
                        referee_command == ref.TIMEOUT_YELLOW or \
                        referee_command == ref.GOAL_YELLOW:
                    self._sound_commands['YELLOW'].play()
                    time.sleep(self._TIME_SLEEP_COLOR)

                self._sound_commands[referee_command].play()

                if referee_command == ref.GOAL_BLUE or \
                        referee_command == ref.GOAL_YELLOW:
                    self._sound_commands['CHEER'].play()

                print(referee_command)


    def play_stage(self, referee_stage):
        if referee_stage != self._referee_stage:
            self._referee_stage = referee_stage

            if referee_stage in self._sound_stages:
                time.sleep(self._TIME_SLEEP_STAGE)
                self._sound_stages[referee_stage].play()


def sub_one(value)->int:
    return value - 1
