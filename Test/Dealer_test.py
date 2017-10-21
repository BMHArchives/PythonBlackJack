import unittest
import CardDeckService
import Dealer
import User
class TestDealerInstance(unittest.TestCase):

      svc = None
      User_Bet_Amount = 0
      Player = None
      CardDeckSvc = None
      def setUp(self):
          self.CardDeckSvc = CardDeckService.CardDeckService()
          self.svc = Dealer.Dealer()
          self.Player = User.User()

      # Confrim that user's bet was recorded by the user
      def test_RequestBet(self):
          self.User_Bet_Amount = 7800
          self.svc.RequestBet(self.User_Bet_Amount, self.Player)
          self.assertEqual(self.Player.UserBets, self.User_Bet_Amount)

      # _CalculateUsersCardsCount(Player) - dealer counts current value of the player's card
      # Conrim that the dealer correctly counts the card values
      def test_CalculatePlayerCardCount(self):
          # Create a player
          self.Player.GetUserName("Brandon")
          PlayingCards = self.Player.GetInitalPlayingCards()
          self.Player.HitOrStay(True)
          UserPlayingCards = self.Player.playingCards
          ExpectedCardValue = 0
          
          for PlayingCard in UserPlayingCards:
              CardValue = self.CardDeckSvc.GetCardValue(PlayingCard)
              if(CardValue == "1or10"):
                 ExpectedCardValue += 10
              else:
                 ExpectedCardValue += int(CardValue)
                  
          # Calculate the Player's card value
          ActualCardValue = self.svc.CalculatePlayerCardsValue(self.Player)

          self.assertEqual(ExpectedCardValue, ActualCardValue)
    
      # _CalculateDealerCardsCount() - dealer counts their own hands
      # Confirm that the dealer correctly count his/her own card values
      def test_CalculateDealerCardCount(self):
          

      # DisplayPlayersCards(Player) - dealer displays players cards
      # DisplayDealerCards() - dealer displays cards
      # HitOrStay() - dealer decides if they want another card or not
      # PlayerHitOrStay() - dealer ask if the user wants to another card or not.
      # ShowCardsValue() - Displays dealers his\her hand
      # DeclareWinner(Player) - Dealer decalres the winner, looser or busy


if __name__ == '__main__':
    unittest.main()