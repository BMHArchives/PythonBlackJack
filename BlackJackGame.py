# BlackJacGame.py - This file represents the execution of the game BlackJack
# Author: Brandon M. Hunter
# Created Date: 11.05.2017
import CardDeckService
import Dealer
import User
import time
import locale
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
    PlayerName = input("Hi player, what can I call you? ")
    Player.SetUserName(PlayerName)

#-----------------------
# Display player's name
#-----------------------
print("Welcome, ")
for Player in DealerUser.Players:
    if(Player.IsDealer == False):    
       print(Player.DisplayName)

#--------------------------
# Get their starting cards
#--------------------------
print("")
print("Alight players!!!! Let's get your starting cards")
for Player in DealerUser.Players:    
       Player.GetPlayingCard(DealerUser.DealCard())
       Player.GetPlayingCard(DealerUser.DealCard())

#-----------------------------------------------------------------------------------------------------------------------
# GetCardValue (CardSuit, Player) - Sets the user CardSuit numeric value. In case the user gets an 'Ace' card, the user 
# would have to decide if they want their Ace to have a value of 1 or 10.
#-----------------------------------------------------------------------------------------------------------------------       
def GetCardValue(CardSuit, Player):
    CardValue = CDS.GetCardValue(CardSuit)
    if CardValue == "1or10" :
       AcceptedCardValue = False
       print("")
       print("{}, here is your current hand {} ".format(Player.DisplayName, Player.PlayingCards))
       print("Hey {}, you have a card {}, that has a value of either 1 or 10. ".format(Player.DisplayName, CardSuit))

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
                    print("-------------------------------------------------------")
                    print("Error: You must enter a 1 or a 10 in order to continue.")
                    print("-------------------------------------------------------")
                    print("")
             else:
                  return SelectedCardValue
                  break
    else:
         return int(CardValue)

#--------------------------------------------
# MakeBets() - Allows the user to make a bet
#--------------------------------------------
def MakeBets():
    AcceptedAnswer = False
    while AcceptedAnswer == False:
          Answer = input("Do you want to make a bet ('y' for yes or 'n' for no)? 'y' for yes and 'n' for no")
          if Answer == 'y':
             AcceptedBet = False
             PlayerBetAmount = 0
             while AcceptedBet == False:
                   try:
                       BetAmount = int(input("Please enter your bet: "))
                       if(BetAmount <= 0):
                          raise
                       else:
                            print("You've enter in a bet of ${:0,.0f} dollars".format(BetAmount))
                            print("")
                            PlayerBetAmount = BetAmount
                            AcceptedBet = True
                            break
                   except:
                          print("")
                          print("----------------------------------------------------")
                          print("Please enter an numeric value that is greater than 0")
                          print("----------------------------------------------------")
                          print("")

             AcceptedAnswer = True             
             return PlayerBetAmount
          elif Answer == 'n':
               AcceptedAnswer = True
               return 0
          else:
               print("You must type in 'y' to make a bet or 'n' to not make a bet in order to continue")
       
    
#----------------------------------------------------------------------------------------
# HitOrStay(Player): A UI piece that will walk through players the hit and stay workflow
#----------------------------------------------------------------------------------------
def HitOrStay(Player):
    ContinuePlay = True
    PlayerBust = False
    while ContinuePlay == True:
          try:
            HitOrStay = None
            HitOrStay = input("Do you want a hit or do you want to stay? To 'Hit', type in 'h' or to stay type in 's'? ")
            
            if HitOrStay == 'h':
               NewCard = DealerUser.DealCard()
               Player.GetPlayingCard(NewCard)
               Player.SetCurrentHandValue(GetCardValue(NewCard, Player))                    
               print("")
               print("Here is your playing hand and playing hand value: ")
               print("{}".format(Player.PlayingCards))
               print("{}".format(Player.CurrentCardValues))
               print("")
               # Check see if the user has busted.
               if Player.CurrentCardValues > 21:
                  PlayerBust = True
                  print("**** Sorry {}, you have bust ****".format(Player.DisplayName))
                  print("")
                  ContinuePlay = False
                  break
               else:
                    
                    Player.SetBet(MakeBets())
            elif HitOrStay == 's':
                 ContinuePlay = False
                 break
            else:
                 raise
          except:
                 print("")
                 print("--------------------------------------------------------------------------------------")
                 print("In order to continue, type in a 'h' to get another card or type in a 's' to stop play.")
                 print("--------------------------------------------------------------------------------------")
                 print("")
    
    return PlayerBust
    #return Player 

#-------------------------------------------------------------------------------------------------------------------------------------
# Add a check to see if the user has an Ace of an suit. If they does, then ask them if they want play this card as a 1 or a 10 value.
#-------------------------------------------------------------------------------------------------------------------------------------
for Player in DealerUser.Players:
    # Evaluate the player cards.
    for Card in Player.PlayingCards:
        Player.SetCurrentHandValue(GetCardValue(Card, Player))
       
    print("Hey {}, here are your cards and your current hand value:".format(Player.DisplayName))
    print("Playing Cards: {}".format(Player.PlayingCards))
    print("Current Hand Value: {}".format(Player.CurrentCardValues))
    print("")
                   
#-----------------------------                 
# Get the players initial bets
#-----------------------------
print("Let's make our initial bets. All bets must be a whole number and greater than $0 dollars")
for Player in DealerUser.Players:
    AcceptedBet = False
    print("")
    print("You're up {}".format(Player.DisplayName))
    while AcceptedBet == False:
          try:
              BetAmount = int(input("Please enter your bet: "))
              if(BetAmount <= 0):
                 raise
              else:
                   
                   print("You've enter in a bet of ${:0,.0f} dollars".format(BetAmount))
                   print("")
                   Player.SetBet(BetAmount)
                   AcceptedBet = True
                   break
          except:
                 print("")
                 print("----------------------------------------------------")
                 print("Please enter an numeric value that is greater than 0")
                 print("----------------------------------------------------")
                 print("")

#--------------------------------------------------------------
# Check if the user wants another card of if they want to stay
#--------------------------------------------------------------
for Player in DealerUser.Players:
    print("")
    print("Hey {}, here are your current playing hand and your current hand value".format(Player.DisplayName))
    print("- Playing Hand: {}".format(Player.PlayingCards))
    print("- Playing Hand Value: {}".format(Player.CurrentCardValues))
    Player.Busted = HitOrStay(Player) # Check to see if the user has busted or not.
    print("Player: {} - Busted? {}".format(Player.DisplayName, Player.Busted))

# Check to see if all users were busted
def AllPlayersBusted(Players):
    NumberOfPlayersBusted = 0
    for Player in Players:
        if Player.Busted == True:
           NumberOfPlayersBusted += 1

    if NumberOfPlayersBusted == NumberOfPlayers:
       return True
    else:
        return False    
        
DealerWon = AllPlayersBusted(DealerUser.Players) 

if DealerWon == True:
   print("Dealer won")
else:
    IsDealerWinner = False
    #---------------
    # Dealer's turn
    #---------------
    print("")
    print("Dealer's turn")
    # Create Dealer user
    Dealer = User.User()
    Dealer.SetUserName("Dealer")

    # get started cards
    for value in range(2):
        NewCard = DealerUser.DealCard()
        Dealer.GetPlayingCard(NewCard)
        CardValue = CDS.GetCardValue(NewCard)
        if CardValue == "1or10" :
           # Personal choice - always set this eone.  
           Dealer.SetCurrentHandValue(1)
        else:
            Dealer.SetCurrentHandValue(int(CardValue))

    # if the dealer has 21, then the game is over. The dealer has won.
    if Dealer.CurrentCardValues == 21:
       print ("{} has 21, the house won !!!!".format(Dealer.DisplayName))
    else: 
        # Loop until the dealer busts, stays or get's 21.
        StopPlay = False
        while StopPlay == False:
              # Get starter cards
              print("{} hits".format(Dealer.DisplayName))
              HitCard = DealerUser.DealCard()
              Dealer.GetPlayingCard(HitCard)
              CardValue = CDS.GetCardValue(HitCard)
              if CardValue == "1or10" :
                 # Personal choice - always set this one.  
                 Dealer.SetCurrentHandValue(1) 
                 print("The {} has {}".format(Dealer.DisplayName, Dealer.PlayingCards))
                 print("The dealers current hand value is {}".format(Dealer.CurrentCardValues))
              else:
                   Dealer.SetCurrentHandValue(int(CardValue)) 
            
              # Show dealer hand
              
              print("Current cards {}".format(Dealer.PlayingCards))
              print("Current card hand value {}".format(Dealer.CurrentCardValues))
              print("")
              # Check if see if user has busted or not.
              if Dealer.CurrentCardValues > 21: # Dealer has busted.
                 print("{} busted !!!".format(Dealer.DisplayName))
                 Dealer.Busted = True
                 StopPlay = True
              elif Dealer.CurrentCardValues >= 19 and Dealer.CurrentCardValues < 21: # Personal choice to stop getting new cards.
                   # Stay, do not ask for any more cards.
                   StopPlay = True
                   Dealer.Busted = False
              elif Dealer.CurrentCardValues == 21: # Dealer has won.
                   print ("{} has 21, the house won !!!!".format(Dealer.DisplayName))
                   IsDealerWinner = True
                   Dealer.Busted = False
                   StopPlay = True
              else:
                   StopPlay = False # Continue to get more cards
                   #time.sleep(5) # Pause the screen for the user to clearly what is happening on the screen.
        
    # Check if the dealer won
    if IsDealerWinner != True:
       # Determine winner
       for Player in DealerUser.Players:
           if Player.Busted == True: # Call out the loosers
              print("{} you lost")
              print("")
           elif Dealer.Busted == True and Player.CurrentCardValues <= 21: # If the dealer has already busted, then any users that has not busted is a winner.
                WiningAmount = Player.GetBets() * 2
                print("{} you won !!!".format(Player.DisplayName))
                print("- Here are your wining hand: {}".format(Player.PlayingCards))
                print("- Here are your winings: ${:0,.0f}".format(WiningAmount))
           elif Dealer.Busted == False and Player.CurrentCardValues > Dealer.CurrentCardValues: # If the player has a higher card value than the dealer, then the player won.
                WiningAmount = Player.GetBets() * 2
                print("{} you won !!!".format(Player.DisplayName))
                print("- Here are your wining hand: {}".format(Player.PlayingCards))
                print("- Here are your winings: ${:0,.0f}".format(WiningAmount))
           elif Player.Busted == False and Player.CurrentCardValues <= Dealer.CurrentCardValues: # If the player has a lower card value than the dealer, then the dealer won.
                print("Sorry, the house one :(")
            