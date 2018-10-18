import Deck
import Menu

class UserInterface():
    def __init__(self):

        self.__m_CurrentDeck = None

        pass


    def run(self):
        """Present the main menu to the user and repeatedly prompt for a valid command"""
        print("Welcome to the Bingo! Deck Generator\n")
        menu = Menu.Menu("Main")
        menu.addOption("C", "Create a new deck")
        
        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "C":
                self.__createDeck()
            elif command == "X":
                keepGoing = False


    def __createDeck(self):
        """Command to create a new Deck"""
        # TODO: Get the user to specify the card size, max number, and number of cards
        size = None
        maxVal = None
        deckSize = None


        #Get the card size
        keepGoing = True
        while (keepGoing):
            size = int(input("Input card size (between 3 and 15): "))
            if (size >= 3) and (size <= 15):
                keepGoing = False
            else:
                print("Please input a number between 3 and 15")

        #Get the max number
        keepGoing = True
        while (keepGoing):
            maxVal = int(input("Input max number (between " + str(2 * (size ** 2)) + " and " + str(4 * (size ** 2)) + "): "))
            if (maxVal >= (2 * (size ** 2)) and maxVal <= (4 * (size ** 2))):
                keepGoing = False
            else:
                 print("Please input a number between " + str(2 * (size ** 2)) + " and " + str(4 * (size ** 2)))

        # Get the card size
        keepGoing = True
        while (keepGoing):
            deckSize = int(input("Input the number of cards in the deck (between 3 and 10000): "))
            if (deckSize >= 3 and size <= 10000):
                keepGoing = False
            else:
                print("Please input a number between 3 and 10000")

        # TODO: Create a new deck
        self.__m_currentDeck = Deck.Deck(size, deckSize, maxVal)

        # TODO: Display a deck menu and allow use to do things with the deck
        self.__deckMenu()
        pass


    def __deckMenu(self):
        """Present the deck menu to user until a valid selection is chosen"""
        menu = Menu.Menu("Deck")
        menu.addOption("P", "Print a card to the screen")
        menu.addOption("D", "Display the whole deck to the screen")
        menu.addOption("S", "Save the whole deck to a file")

        keepGoing = True
        while keepGoing:
            command = menu.show()
            if command == "P":
                self.__printCard()
            elif command == "D":
                print()
                self.__m_currentDeck.print()
            elif command == "S":
                self.__saveDeck()
            elif command == "X":
                keepGoing = False


    def __printCard(self):
        """Command to print a single card"""
        cardToPrint = self.__getNumberInput("Id of card to print", 1, self.__m_currentDeck.getCardCount())
        if cardToPrint > 0:
            print()
            self.__m_currentDeck.print(idx=cardToPrint)


    def __saveDeck(self):
        """Command to save a deck to a file"""
        fileName = self.__getStringInput("Enter output file name")
        if fileName != "":
            # TODO: open a file and pass to currentDeck.print()
            outputStream = open(fileName, 'w')
            self.__m_currentDeck.print(outputStream)
            outputStream.close()
            print("Done!")

    def __getNumberInput(self, prompt, minVal, maxVal):
        n = int(input(prompt))
        keepGoing = True
        while keepGoing:
            if n < minVal or n > maxVal:
                print("Please input a number within " + str(minVal) + " and " + str(maxVal))
            else:
                keepGoing = False

        return n

    def __getStringInput(self, prompt):

        return input(prompt)
