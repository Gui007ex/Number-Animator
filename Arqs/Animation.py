from time import sleep
from os import system as sys

class Animation:
    def __init__(self, frames, name) -> None:
        self.__name = name if len(name) >= 1 else 'Sem nome'
        self.__frames = frames
        self.__speed = 0.6

    def SetSpeed(self, speed):
        self.__speed = speed

    def Play(self):
        for frame in self.__frames:
            sys('cls')
            print(frame)
            sleep(self.__speed)

    def Name(self):
        return self.__name