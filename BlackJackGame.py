# BlackJacGame.py - This file represents the execution of the game BlackJack
# Author: Brandon M. Hunter
# Created Date: 11.05.2017
import CardDeckService
import Dealer
import User

CDS = CardDeckService.CardDeckService()
# Build the card deck and shuffle the cards.
CDS.BuildCardDeck()
CDS.ShuffleCardDeck()

DealerUser = Dealer.Dealer()
# Intro
print("----------------------------------------------------------")
print(" Welcome to BlackJack - written in Python - Version 1.0.0")
print(" Developed By: Brandon M. Hunter                         ")
print("----------------------------------------------------------")
print("")


ValidNumberOfPlayersInput = False
NumberOfPlayers = 0
ContinuePlay = True
while ValidNumberOfPlayersInput == False:
      try:
          NumberOfPlayers = int(input("Hi, my name is Dealer. How many people do we have playing today? "))
      except:
          print("Please provid a valid interger number. Like 1,2,3,4,5,etc....")
      else:
          break
      

# Create the users
DealerUser.CreatePlayers(NumberOfPlayers)
print("Great, we have {} players playing today. Let's get their names.".format(NumberOfPlayers)) 
# Set the players names
for Player in DealerUser.Players:
    if Player.IsDealer == False:
       PlayerName = input("Hi player, what can I call you? ")
       Player.SetUserName(PlayerName)
    else:
        Player.SetUserName("Dealer")

print("Welcome, ")
for Player in DealerUser.Players:
    if(Player.IsDealer == False):
       print(Player.GetUserName())

# Get their initial bets
print("Alight players!!!! Let's get your started cards")
for Player in DealerUser.Players:    
       Player.GetPlayingCard(DealerUser.DealCard())
       Player.GetPlayingCard(DealerUser.DealCard())
       
def GetCardValue(CardSuit, DisplayName):
    CardValue = CDS.GetCardValue(CardSuit)
    if CardValue == "1or10" :
       AcceptedCardValue = False
       print("Hey {}, your card {} has a value of 1 or 10. ".format(DisplayName, CardSuit))
    
       while AcceptedCardValue == False:
             SelectedCardValue = None
             try:
                 SelectedCardValue = int(input("Please choose a value of 1 or 10 to continue. "))
                 if SelectedCardValue == 1 or SelectedCardValue == 10:
                    return int(SelectedCardValue)
                    break
                 else:
                      AcceptedCardValue = False
                      raise
             except Exception as error:
                    print("You must enter a 1 or a 10 in order to continue.")
             else:
                  return SelectedCardValue
                  break
    else:
         return int(CardValue)
    
# Add a check to see if the user has an Ace of an suit. If they does, then ask them if they want play this card as a 1 or a 10 value.
for Player in DealerUser.Players:
    if Player.IsDealer == False:
       # Evaluate the player cards.
       for Card in Player.PlayingCards:
           Player.SetCurrentHandValue(GetCardValue(Card, Player.DisplayName))
       
       print("Hey {}, here are your cards and the current value {}".format(Player.GetUserName(), Player.CurrentCardValues))
       print(Player.PlayingCards)
                   
                    
# Get the players initial bets
print("Let's make our initial bets. All bets must be a whole number and greater than $0 dollars")
for Player in DealerUser.Players:
    if Player.IsDealer == False:
       AcceptedBet = False
       while AcceptedBet == False:
             try:
                 BetAmount = int(input("Alight {}, please please your bet: ".format(Player.GetUserName())))
                 if(BetAmount <= 0):
                    raise
                 else:
                      print("You've enter in a bet of ${} dollars".format(BetAmount))
                      Player.SetBet(BetAmount)
                      AcceptedBet = True
                      break
             except:
                    print("Please enter an numeric value that is greater than 0")


# Check if the user wants another card of if they want to stay
for Player in DealerUser.Players:
    if Player.IsDealer == False:
       print("Hey {}, here are your cards {} and your hand value {}".format(Player.DisplayName, Player.PlayingCards,Player.CurrentCardValues))

       AcceptedAnswer = False
       ContinuePlay = True
       while ContinuePlay == True:
             try:
                 HitOrStay = None
                 HitOrStay = input("Do you want a hit or do you want to stay? To 'Hit', type in 'h' or to stay type in 's'? ")
                 
                 if HitOrStay == 'h':
                    NewCard = DealerUser.DealCard()
                    Player.GetPlayingCard(NewCard)
                    Player.SetCurrentHandValue(GetCardValue(NewCard, Player.DisplayName))                    
                    print("")
                    print("Here is your hand {} and hand value {}".format(Player.PlayingCards, Player.CurrentCardValues))
                    print("")
                    # Check see if the user has busted.
                    if Player.CurrentCardValues > 21:
                       Player.IsWinner = False
                       print("Sorry {}, you have bust".format(Player.DisplayName))
                       ContinuePlay = False
                       break
                 elif HitOrStay == 's':
                      ContinuePlay = False
                      break
                 else:
                      raise
             except:
                    print("In order to continue, type in a 'h' to get another card or type in a 's' to stop play.")

             