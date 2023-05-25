from time import sleep
from os import system as sys
from random import randint

class Animation:
    def __init__(self, _Animation__frames, _Animation__name, _Animation__speed, _Animation__identifier) -> None:
        self.__frames = _Animation__frames
        self.__name = _Animation__name if len(_Animation__name) >= 1 else 'Sem nome'
        self.__speed = _Animation__speed
        self.__identifier = _Animation__identifier

    def SetSpeed(self, speed):
        self.__speed = speed
    
    def Speed(self):
        return self.__speed

    def Play(self):
        for frame in self.__frames:
            sys('cls')
            print(frame)
            sleep(self.__speed)

    def Name(self):
        return self.__name
    
    def SetName(self, name):
        self.__name = name

    def AllFrames(self):
        return self.__frames
    
    def CreateId(self, dict):
        if self.__identifier == None:
            id = str(randint(0, 100000))
            if id not in dict:
                self.__identifier = id
            else:
                self.SetId(dict)
    
    def SetId(self, id):
        self.__identifier = id

    def Id(self):
        return self.__identifier