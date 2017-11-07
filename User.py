# User.py - This class has the following responsiblity:
# 1 - Define the player's name
# 2 - Make a bet(s)
# 3 - Get playing cards

import CardDeckService

class User:
    IsDealer = False # Identifies if the current user is the dealer or not
    UserBets = None # Stores a total the user's current bets
    DisplayName = None # Stores the user's display name
    PlayingCards = [] # Stores the user's playing cards
    CardDeckSvc = None # Represents an instance of the CardDeckService
    CurrentCardValues = None # Stores the user playing cards values
    Busted = False # Determines if the user busted or not.
    # def __new__(cls, *p, **k):
    #      inst = object.__new__(cls)
    #      return inst
    
    def __init__(self):
        self.CardDeckSvc = CardDeckService.CardDeckService()
        self.UserBets = 0.00
        self.DisplayName = None
        self.PlayingCards = []
        self.CurrentCardValues = 0
        

    
    
    # Get the player's display name that they want to use
    def SetUserName(self, DisplayName):
        self.DisplayName = DisplayName

    def GetUserName(self):
        return self.DisplayName
        # if DisplayName == None:
        #     validDisplayName = False
        #     while validDisplayName == False :
        #         userInput = input("Hi user, what is your name?")
        #         if(userInput == "" or userInput == None):
        #             validDisplayName = False
        #             print("Error: Please enter in a valid display name")
        #         else:
        #             self.DisplayName = userInput
        #             validDisplayName = True
        # else:
        #     self.DisplayName = DisplayName
        
        # # Return the username back to the consumer
        # return self.DisplayName

    
    def GetPlayingCard(self, PlayingCard):
        """
        GetPlayingCard(PlayingCard) - accepts a playing card from the producer
        params: PlayingCard - represents a playing card
        """
        # Save teh playing card to the local list.
        self.PlayingCards.append(PlayingCard)
        
    
    def SetBet(self, Amount):
        """
        SetBet(Amount) - Sets the bet made by the user.
        params: Amount - represents a bet dollar amount
        """
        # Save the bet to the local list
        self.UserBets += Amount
    
    def GetBets(self):
        """
        GetBets() - retrieves the total bets made by the user.
        """
        return self.UserBets
    
    def SetCurrentHandValue(self, CardValue):
        """
        SetCurrentHandValue(CardValue) - sets the current playing card value hand.
        param: CardValue - represents the playing card value.
        """
        # Set the user's list card value
        self.CurrentCardValues += CardValue

    def GetCurrentHandValue(self):
        """
        GetCurrentHandValue() - gets the current playing card value.
        param: None
        """
        return self.CurrentCardValues



    

    


 


