# DeckServices.Test.py - This is a unit test to test to confirm that the functions implemented within the
# DeckServices.py file work as expected.
import unittest
import CardDeckService
class TestDeckService(unittest.TestCase):
      
      cds = None
      def setUp(self):
          self.cds = CardDeckService.CardDeckService()
    
      # Test to make sure the service can build a card deck    
      def test_BuildCardDeck(self):
          # Get an instance of the card deck
          cardDeck = {}
          cardDeck = self.cds.BuildCardDeck()
          self.assertIsNotNone(cardDeck)

      
      # Test the behavior that the service can shuffle a deck of cards
      def test_CardShuffling(self):
          ShuffleCardDeck = self.cds.ShuffleCardDeck()
          self.assertEqual(len(ShuffleCardDeck), 52)
     
      # Test to confirm that the card deck service shuffle a card by comparing the card before it was 
      # shuffled and then after the card deck was shuffle.  
      def test_CardShufflingIsDifferentFromAnUnShuffledCardDeck(self):
          # Get a unshuffled card deck
          cardDeck = {}
          cardDeck = self.cds.BuildCardDeck()
          firstPlayingCard = list(cardDeck.keys())[0]

          # Get a shuffled card deck
          shuffleCardDeck = {}
          shuffleCardDeck = self.cds.ShuffleCardDeck()
          secondPlayingCard = list(shuffleCardDeck.keys())[0]
          
          # Make sure the first cards from each deck are not equal
          self.assertNotEqual(firstPlayingCard, secondPlayingCard)


      # Test to ensure that a card can be dealt from the card deck service
      def test_DealCard(self):
          # Shuffle the card deck
          self.cds.ShuffleCardDeck()

          # Request a card from the CardDeckService
          selectedCard = self.cds.DealCard()
          
          # Check to see if a card was dealt
          self.assertIsNotNone(selectedCard)
      
      # Confirm that the service returns a different card when you call it more than once.
      def test_DealCard_ReturnsDifferentCards(self):
         # Shuffle the card deck
         self.cds.ShuffleCardDeck()

         #Request a playing card
         firstPlayingCard = self.cds.DealCard()

         # Request another playing card
         secondPlayingCard = self.cds.DealCard()
        
         self.assertNotEqual(firstPlayingCard, secondPlayingCard)
    
      # Confirm that the service can return a value for the card you've submitted
      def test_GetCardValue(self):
          svc = self.cds
          # Shuffle the card deck
          svc.ShuffleCardDeck()
          # Get a playing card
          PlayingCard = svc.DealCard()
          # Get the Playing card value
          PlayingCardValue = svc.GetCardValue(PlayingCard)
          # Check make sure the value is not empty
          self.assertIsNotNone(PlayingCardValue)
          

if __name__ == '__main__':
    unittest.main()