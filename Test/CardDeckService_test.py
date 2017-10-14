# DeckServices.Test.py - This is a unit test to test to confirm that the functions implemented within the
# DeckServices.py file work as expected.
import unittest
import CardDeckService
class TestDeckService(unittest.TestCase):
      
      cds = None
      def setUp(self):
          self.cds = CardDeckService.CardDeckService()
          
      def test_BuildCardDeck(self):
          # Get an instance of the card deck
          cardDeck = {}
          cardDeck = self.cds.BuildCardDeck()
          self.assertIsNotNone(cardDeck)

      
      # Test - Ensure card shuffling works
      def test_CardShuffling(self):
          pass

      # Test - make sure that service can deal a card to the consumer
      def test_DealCard(self):
          pass
    
      # Test - Make sure we can look up a card value and return it back to the consumer
      def test_GetCardValue(self):
          pass

if __name__ == '__main__':
    unittest.main()