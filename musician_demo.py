class Musician(object):
    def __init__(self,sounds):
        self.sounds=sounds

    def solo(self,length):
        for i in range(length):
            print(self.sounds[i%len(self.sounds)], end=" ")
            print()

class Bassist(Musician):
    def __init__(self):
        super().__init__(["twang", "thrumb", "bling"])

class Guitarist(Musician):
    def __init__(self):
        super().__init__(["Boink","Bow","Boom"])

    def tune(self):
        print("be with you in a moment")
        print("Twoing, sproing, splang")

class Drummer(Musician):
    def __init__(self):
        super().__init__(["Bang","Dong","Clang"])

    def count(self):
        while True:
            try:
                high=int(input("what number should he count to? "))
                break
            except ValueError:
                print("please enter an integer")
        for i in range():
            print(i,end=" ")
    def combust(self):
        print("BAAAAAANG")
        print("... the drummer has mysteriously vanished")
        
            
