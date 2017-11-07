# Dealer.py - This class has the following responsiblity
# 1 - Deal the intial 2 cards to the user.
# 3 - Deal cards to the user when its their turn
# 4 - Declare winners and how much they won.
# 5 - Create players 
import User
import CardDeckService
class Dealer:
      UserBetsAmount = 0
      PlayingCards = []
      UserCards = []      
      Players = []
      CardDeckSvc = None

      Players = []
      def __init__(self):
          self.CardDeckSvc = CardDeckService.CardDeckService()
          self.CardDeckSvc.BuildCardDeck()
          self.CardDeckSvc.ShuffleCardDeck()

      # Deals initlal cards to users
      def DealStarterCards(self):

          playingCards = []
          
          playingCards = []
          svc = self.CardDeckSvc
          playingCards.append(svc.GetCard())
          playingCards.append(svc.GetCard())

          return playingCards
      
      def DealCard(self):
          svc = self.CardDeckSvc
          return svc.GetCard()
      def CreatePlayers(self, NumberOfPlayers):
          """
          CreatePlayers(NumberOfPlayers) - Creates x number of players based on the NumerOfPlayers variable value.
          param: NumberOfPlayers - represents the number of players to create.
          """
          
          for value in range(NumberOfPlayers):
              # Create the User object
              player = None
              player = User.User()
              player.IsDealer = False
              self.Players.append(player)
        
          # Add the dealer user
          #player = None
          #player = User.User()
          #player.IsDealer = True
          #self.Players.append(player)
    
      def GetCardHandValue(self, PlayingCard):
          CardValue = None
          cds = self.CardDeckSvc

          #Look up the card value and return back to the consumer 
          CardValue = cds.GetCardValue(PlayingCard)
          
          return CardValue
   



