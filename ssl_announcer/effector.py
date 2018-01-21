
import pygame
import time
from proto import referee_pb2


class Effector(object):
    def __init__(self):

        pygame.mixer.init()

        self._sound_dict = {}
        self._sound_dict[referee_pb2.SSL_Referee.HALT] = pygame.mixer.Sound('./sounds/halt.wav')
        self._sound_dict[referee_pb2.SSL_Referee.STOP] = pygame.mixer.Sound('./sounds/stop.wav')
        self._sound_dict[referee_pb2.SSL_Referee.NORMAL_START] = pygame.mixer.Sound('./sounds/start.wav')
        self._sound_dict[referee_pb2.SSL_Referee.PREPARE_KICKOFF_BLUE] = pygame.mixer.Sound('./sounds/kickkoff.wav')

        self._sound_dict['BLUE'] = pygame.mixer.Sound('./sounds/blue.wav')
        self._sound_dict['YELLOW'] = pygame.mixer.Sound('./sounds/yellow.wav')

        for key in self._sound_dict:
            self._sound_dict[key].set_volume(0.7)

        self._referee_command = None


    def play_command(self, referee_command):
        if referee_command != self._referee_command:
            self._referee_command = referee_command

            if referee_command in self._sound_dict:
                if referee_command == referee_pb2.SSL_Referee.PREPARE_KICKOFF_BLUE:
                    self._sound_dict['BLUE'].play()
                    time.sleep(0.8)

                self._sound_dict[referee_command].play()


def sub_one(value)->int:
    return value - 1
