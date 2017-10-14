# DeckService.py - This is a class that will provide functionality to serve as a Card Deck Service to the consumer
class CardDeckService:

      _cardDeck = {}
      _masterCardDeck = {}
      def __init__(self):
          self._masterCardDeck = self.BuildCardDeck()
      
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
          
    
      def ShuffleCardDeck(self, CardDeck):
          pass
    
      def DealCard(self):
          pass
    
      def GetCardValue(self, CardKey):
          pass

svc = CardDeckService()
CardDeck = svc.BuildCardDeck()
print(CardDeck)