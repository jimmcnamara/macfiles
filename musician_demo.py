import random
def main():
    Band1=Band()
    Band1.add_member("john")
    Band1.add_member('shaun')
    Band1.add_member('jill')
    Band1.roster()
    Band1.fired('jill')
    Band1.roster()
    Band1.play(3)



class Band(object):
    def __init__(self):
        self.musicians=[Guitarist(),Bassist(),Drummer()]
        self.ourBand=[]
        self.n=0
        
    def add_member(self,name):
        if self.n<3:
            new_mem=self.musicians[self.n]
            new_mem.setname(name)
            self.ourBand.append(new_mem)
            self.n+=1
        else:
            print('sorry, band is full')

    def fired(self,name):
        for i in self.ourBand:
            if i.name==name:
                self.ourBand.remove(i)
                print(i.name," was removed from the band")

    def roster(self):
        for i in self.ourBand:
            print(i.name)
        

    def play(self,length):
        for i in self.ourBand:
            i.solo(length)

class Musician(object):
    def __init__(self,sounds):
        self.sounds=sounds
        self.name=""

    def solo(self,length):
        for i in range(length):
            print(self.sounds[i%len(self.sounds)], end=" ")
            print()

    def setname(self,name):
        self.name=name

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
        countdown=['one','two','three','four']
        for i in countdown:
            print(i, end="\n")
#        while True:
#            try:
#                high=int(input("what number should he count to? "))
#                break
#            except ValueError:
#                print("please enter an integer")
#        for i in range():
#            print(i,end=" ")
    def combust(self):
        print("BAAAAAANG")
        print("... the drummer has mysteriously vanished")



##    def fired(self,name):
##        self.name=name
##        try:
##            self.ourBand.pop(name)
##        except:
            
        
        
        
        
        
            
