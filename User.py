# User.py - this is a class that represents a user.
import CardDeckService

class User:

    UserBets = None # Stores a total the user's current bets
    DisplayName = None # Stores the user's display name
    playingCards = [] # Stores the user's playing cards
    CardDeckSvc = None # Represents an instance of the CardDeckService
    def __new__(cls, *p, **k):
         inst = object.__new__(cls)
         return inst
    def __init__(self):
        self.CardDeckSvc = CardDeckService.CardDeckService()
        self.UserBets = 0.00
        self.DisplayName = None
        self.playingCards = []
        

    # Get the player's display name that they want to use
    def GetUserName(self, DisplayName):
        if DisplayName == None:
            validDisplayName = False
            while validDisplayName == False :
                userInput = input("Hi user, what is your name?")
                if(userInput == "" or userInput == None):
                    validDisplayName = False
                    print("Error: Please enter in a valid display name")
                else:
                    self.DisplayName = userInput
                    validDisplayName = True
        else:
            self.DisplayName = DisplayName
        
        # Return the username back to the consumer
        return self.DisplayName

    # Get the initial cards for the current user.
    def GetInitalPlayingCards(self):
        for value in range(0,2):
            self.playingCards.append(self.CardDeckSvc.DealCard())
        
        # Return the cards back to the consumer
        return self.playingCards
    
    # Allows a user to make a bet
    def MakeBet(self, BetAmount):
        self.UserBets += BetAmount
        return self.UserBets
    
    def GetUserBets(self):
        return self.UserBets

    def HitOrStay(self, RequestCard):

        # check if the user is requetsing for a card or not.
        if(RequestCard == True):
            self.playingCards.append(self.CardDeckSvc.DealCard())

