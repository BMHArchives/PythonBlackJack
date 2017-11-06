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
          svc = self.cds
          # Initiate the build of the card deck()
          svc.BuildCardDeck()
          # Check to see if the master copy of the card deck exists.
          self.assertIsNotNone(svc.MasterCardDeck)

      def test_BuildCardDeck_Check_If_We_Have_52_Cards(self):
          svc = self.cds
          # Initiate the build of the card deck()
          svc.BuildCardDeck()
          # Check to see if the deck has 52 cards
          self.assertEqual(len(svc.MasterCardDeck), 52)
          

      # Test the behavior that the service can shuffle a deck of cards
      def test_ShuffleCards_Check_If_We_Still_Have_52_Cards(self):
          svc = self.cds
          svc.BuildCardDeck()
          svc.ShuffleCardDeck()
          self.assertEqual(len(svc.ShuffledCardDeck), 52)
     
      # Confirm that the MasterCardDeck and teh ShuffleCardDeck top cards are different after we call the BuildCardDeck and ShuffCardDeck methos.
      def test_CardShufflingIsDifferentFromAnUnShuffledCardDeck(self):
          svc = self.cds

          # Get a unshuffled card deck
          svc.BuildCardDeck()
          firstPlayingCard = list(svc.MasterCardDeck.keys())[0]

          # Get a shuffled card deck
          svc.ShuffleCardDeck()
          secondPlayingCard = list(svc.ShuffledCardDeck.keys())[0]
          
          # Make sure the first cards from each deck are not equal
          self.assertNotEqual(firstPlayingCard, secondPlayingCard)


      
      # Confirm that the service can return a value for the card you've submitted
      def test_GetCardValue(self):
          svc = self.cds
          
          # Build the card deck
          svc.BuildCardDeck()

          # Shuffle the card deck
          svc.ShuffleCardDeck()

          # Pick the first card from the the shuffle card deck
          PlayingCard = list(svc.ShuffledCardDeck.keys())[0]

          # Get the Playing card value
          PlayingCardValue = svc.GetCardValue(PlayingCard)

          # Check make sure the value is not empty
          self.assertIsNotNone(PlayingCardValue)
          
      def test_GetCard_Get_A_Playing_Card(self):
          svc = self.cds
          svc.BuildCardDeck()
          svc.ShuffleCardDeck()
          PlayingCard = svc.GetCard()

          self.assertIsNotNone(PlayingCard)

      def test_GetCard_Make_Sure_We_Have_51_Cards(self):
          svc = self.cds
          svc.BuildCardDeck()
          svc.ShuffleCardDeck()
          PlayingCard = svc.GetCard()
          ExepctedValue = 51
          ActualValue = len(svc.ShuffledCardDeck)

          self.assertEqual(ExepctedValue, ActualValue)

          
if __name__ == '__main__':
    unittest.main()