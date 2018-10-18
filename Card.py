import sys
import math

import NumberSet

class Card():
    def __init__(self, idnum, size, numberSet):
        """Card constructor"""
        self.__m_id = idnum
        self.__m_size = size
        self.__m_numberSet = numberSet

        pass


    def getId(self):
        """Return an integer: the ID number of the card"""
        return self.__m_id

    def getSize(self):
        """Return an integer: the size of one dimension of the card.
        A 3x3 card will return 3, a 5x5 card will return 5, etc.
        """
        return self.__m_size

    def print(self, file=sys.stdout):
        """void function:
        Prints a card to the screen or to an open file object"""
        numCounter = 0

        # Get amount of characters in the largest number
        numberSet = self.__m_numberSet
        largestNumber = 0
        freeSpace = None
        for i in range(0, self.__m_size**2):
            if (numberSet.get(i) > largestNumber):
                largestNumber = numberSet.get(i)

        #does card need free space
        if self.__m_size % 2 == 1:
            freeSpace = True
        else:
            freeSpace = False



        columnSize = len(str(largestNumber)) + 2

        if freeSpace == True:
            if columnSize < 5:
                columnSize = 5




        #initial corner
        file.write('+')
        #loop for initial top border
        for i in range(self.__m_size):
            for num in range(columnSize):
                file.write('-')
            file.write('+')

        #loop for each row
        for i in range(self.__m_size):


            print("")
            #initial side
            file.write("|")
            #loop for each number
            for j in range(self.__m_size):
                if freeSpace and numCounter == math.floor((self.__m_size ** 2)/2):
                    file.write("FREE!")

                else:
                    num = numberSet.get(numCounter)
                    numberLength = len(str(num))
                    #if number length is odd, equal amount of spaces before and after the number. If even, put the extra number on the left side
                    spaces = columnSize - numberLength
                    spacesBeforeNum = 0
                    SpacesAfterNum = 0

                    if spaces % 2 == 0:
                        spaceBeforeNum = spaces // 2
                        spacesAfterNum = spaces // 2

                    else:
                        spaceBeforeNum = spaces // 2
                        spacesAfterNum = spaces // 2 + 1
                        pass


                    for k in range(spaceBeforeNum):
                        file.write(" ")

                    file.write(str(num))

                    for k in range(spacesAfterNum):
                        file.write(" ")

                numCounter += 1

                file.write("|")

            print("")
            file.write('+')

            for j in range(self.__m_size):
                for num in range(columnSize):
                    file.write('-')
                file.write('+')
        print("")
        pass
