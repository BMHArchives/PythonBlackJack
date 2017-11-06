# DeckService.py - This class responsbility is the following:
# 1 - Create a card deck that has 52 cards
# 2 - Shuffle the card deck
# 3 - Get a card value.
import random
class CardDeckService:


      ShuffledCardDeck = None
      SelectedCards    = None
      MasterCardDeck   = None
      
      def __init__(self):
          self.ShuffledCardDeck = {}
          self.SelectedCards = {}
          self.MasterCardDeck = {}
      
      def BuildCardDeck(self):
          """
          BuildCardDeck() - builds a card deck of 52 cards 
          """
          cardDeck = {}
          cardTypes = "Clubs,Spades,Diamonds,Hearts".split(",")
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
                            value = "1or10"
                        elif cardNumber == "Q" or cardNumber == "K" or cardNumber == "J":
                            value = "10"
                        else:
                            value = cardNumber
                        
                        # Add to consumer MasterCardDeck dictionary
                        self.MasterCardDeck[key] = value
          except:
              print("BuildCardDeck() - Error")
          
    
      def ShuffleCardDeck(self):
          """
          ShuffleCardDeck() - Shuffles the card deck in a random order and returns the shuffle card deck back to the consumer.
          """
          try:
              self.ShuffledCardDeck = {}
          
              # Copy the keys (Cards Display Name) to a local list
              Cards = list(self.MasterCardDeck.keys())

              # Shuffle the keys using random.shuffle
              rnd = random.shuffle(Cards)

              # Set the shuffle keys into the new dictionary
              for Card in Cards:
                  self.ShuffledCardDeck[Card] = self.GetCardValue(Card)
          except:
              print("ShuffleCardDeck() - Error")
          
      def GetCardValue(self, CardKey):
          """
          GetCardValue(CardKey) - Retrieves a card's numeric value
          param CardKey: represents tehe the Card face name.
          """
          # Get the master card deck
          CardValue =self.MasterCardDeck[CardKey]

          # Return the card value back to the consumer
          return CardValue
      
      
      
      
      
      def GetCard(self):
          PlayingCard = list(self.ShuffledCardDeck.keys())[0]

          # Remove the card from the ShuffledCardDeck
          del self.ShuffledCardDeck[PlayingCard]

          # return the card back to the consumer
          return PlayingCard



