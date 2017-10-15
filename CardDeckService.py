# DeckService.py - This is a class that will provide functionality to serve as a Card Deck Service to the consumer
import random
class CardDeckService:

      _cardDeck = {}
      ShuffledCardDeck = {}
      SelectedCards = {}
      _masterCardDeck = {}
      def __init__(self):
          self._masterCardDeck = self.BuildCardDeck()
          self.ShuffleCardDeck()
      
      def BuildCardDeck(self):
          cardTypes = "Clubs,Spads,Diamons,Hearts".split(",")
          cardNumbers= "A,2,3,4,5,6,7,8,9,10,J,Q,K".split(",")
          try:
              # Loop through the cardTypes array
                for cardType in cardTypes:

                    # Loop through the cardNumbers array
                    for cardNumber in cardNumbers:

                        # Create the key
                        key = "{} - {}".format(cardNumber,cardType)
                        
                        value = ""
                        # Determine value
                        if cardNumber == "A":
                            value = "1or21"
                        elif cardNumber == "Q" or cardNumber == "K" or cardNumber == "J":
                            value = "10"
                        else:
                            value = cardNumber
                        
                        # Add to consumer cardDeck dictionary
                        self._cardDeck[key] = value
                
                return self._cardDeck
          except:
              return None
          
    
      def ShuffleCardDeck(self):
          self.ShuffledCardDeck = {}
          
          # Copy the _cardDeck keys to a list
          listOfKeys = list(self._cardDeck.keys())
          
          # Shuffle the keys using random.shuffle
          rnd = random.shuffle(listOfKeys)

          # Set the shuffle keys into the new dictionary
          for key in listOfKeys:
              self.ShuffledCardDeck[key] = self._cardDeck[key]
          
          
          return self.ShuffledCardDeck
      
      # Documentation
      def DealCard(self):
          """ Returns the Card Type only to the consumer
          :param Empty:.
          """
          # Get the next card in the shuffle deck
          SelectedCard = list(self.ShuffledCardDeck.keys())[0]

          # Keep track the card that was dealt
          self.SelectedCards[SelectedCard] = self.ShuffledCardDeck[SelectedCard]

          # Removed the selected card from the shuffled card deck
          del self.ShuffledCardDeck[SelectedCard]

          # Retrun the card back to the consumer
          return SelectedCard
    
      def GetCardValue(self, CardKey):
          
          # Get the master card deck
          CardValue =self._cardDeck[CardKey]

          # Return the card value back to the consumer
          return CardValue

cds = CardDeckService()
cds.ShuffleCardDeck()
CardValue = cds.DealCard()
