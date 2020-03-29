import random
from enum import Enum
Trees = Enum('TreeType', 'Evergreen Spruce ')
class Tree:
    tree = {}
    def __new__(cls, treetype):
        objectt = cls.tree.get(treetype, None)
        if not objectt:
            objectt = object.__new__(cls)
            cls.tree[treetype] = objectt
            objectt.treetype = treetype
        return objectt

    def trees_data(self,  x, y,age):
        print(' {}  x cordinates {} , y cordinates {}, age {} )'.format(self.treetype,  x , y,age))

def main():
    #take input from user for the number of trees ten convert them to int
    in1 = input("How many evergreens?")
    in2 = input("How many Spruces? ")
    NoOfEvergreens = int(in1)
    NoOfSpruces = int(in2)

    #random range for x within 50,y within 50 ,age of trees within 300 .
    randomValues = random.Random()
    for i in range(NoOfEvergreens):
        evergreen = Tree(Trees.Evergreen)
        evergreen.trees_data(randomValues.randrange(50),
                  randomValues.randrange(50),
                  randomValues.randrange(300))


    for i in range(NoOfSpruces):
        spruce = Tree(Trees.Spruce)
        spruce.trees_data(randomValues.randrange(50),
                  randomValues.randrange(50),
                  randomValues.randrange(300))

    print()
    print("No of the tress:  " + in1 + " Evergreen  and " + in2 + " Spruce , Total tress = " +str(NoOfEvergreens+NoOfSpruces))

if __name__ == '__main__':
    main()
