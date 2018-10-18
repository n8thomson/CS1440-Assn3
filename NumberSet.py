import random

class NumberSet():
    def __init__(self, size):
        """NumberSet constructor"""
        self.__m_size = size
        self.__m_numberList = []
        for i in range(1, size + 1):
            self.__m_numberList.append(i)
        self.__m_counter = 0

        pass

    def getSize(self):
        """Return an integer: the size of the NumberSet"""
        return self.__m_size


    def get(self, index):
        """Return an integer: get the number from this NumberSet at an index"""
        return self.__m_numberList[index]


    def randomize(self):
        """void function: Shuffle this NumberSet"""
        random.shuffle(self.__m_numberList)
        pass


    def getNext(self):
        """Return an integer: when called repeatedly return successive values
        from the NumberSet until the end is reached, at which time 'None' is returned"""
        n = self.__m_counter

        x = self.__m_numberList[n]
        self.__m_counter += 1
        return x
