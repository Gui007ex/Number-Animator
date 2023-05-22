from time import sleep
from os import system as sys

class Animation:
    def __init__(self, frames, name) -> None:
        self.__name = name if len(name) >= 1 else 'Sem nome'
        self.__frames = frames
        self.__speed = 0.5

    def SetSpeed(self, speed):
        self.__speed = speed
    
    def Speed(self):
        return self.__speed

    def Play(self):
        for i in range(3):
            for frame in self.__frames:
                sys('cls')
                print(frame)
                sleep(self.__speed)

    def Name(self):
        return self.__name
    
    def SetName(self, name):
        self.__name = name