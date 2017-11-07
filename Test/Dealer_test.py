import unittest
import Dealer
import User
class TestDealerInstance(unittest.TestCase):

      Dealer = None
      User_Bet_Amount = 0
      Player = None
      CardDeckSvc = None
      def setUp(self):
          self.Dealer = Dealer.Dealer()
          
      # 1 - Deal the intial 2 cards to the user.
      # 2 - Take bets from the user
      # 3 - Deal cards to the user when its their turn
      # 4 - Declare winners and how much they won.
      
      
      # test_DealStarterCards() - confirm that two cards are dealt to the caller
      def test_DealStarterCards_Confirm_Player_Gets_Two_Cards(self):

          # Call the Dealer.DealStartCards() method
          StarterCards = self.Dealer.DealStarterCards()

          # Confirm that the list has two cards.
          self.assertEqual(len(StarterCards), 2)
          
      # Confirms the deal card method works.
      def test_DealCard_GetACard_Confirm_Player_Gets_One_Card(self):
          svc = self.Dealer
          PlayingCards = []
          PlayingCards.append(svc.DealCard())

          # Confirm that the player receives one card
          ExpectedNumberOfCards = 1
          ActualNumberOfCards = len(PlayingCards)
          self.assertEqual(ExpectedNumberOfCards, ActualNumberOfCards)
          
      def test_CreatePlayers_Confirm_2_Players_Are_Created(self):
          # Create 2 players
          svc = self.Dealer
          svc.CreatePlayers(2)
          Expected_Number_Of_Players_Created = 2
          Actual_Number_Of__Players_Created = len(svc.Players)

          # Confirm that two players were created
          self.assertEqual(Expected_Number_Of_Players_Created, Actual_Number_Of__Players_Created)
      
      def test_GetWinner_Confirm_Winner_And_Losers(self):
          svc = self.Dealer
          # TODO - 
          # - Create players
          svc.CreatePlayers(1)
           
          # - Get Intial Cards
          Player = svc.Players[0]
          Player.GetPlayingCard("K - Hearts")
          Player.SetCurrentHandValue(10)
          Player.GetPlayingCard("9 - Hearts")
          Player.SetCurrentHandValue(9)
          
          # - Get players inital bets
          Player.SetBet(30.00)

          # - Have players make their bets
          Player.SetBet(100.00)

          Dealer = None
          Dealer = User.User()
          

          # - Plays gets one additional hand
          Dealer.GetPlayingCard("8 - Hearts")
          Dealer.SetCurrentHandValue(8)
          Dealer.GetPlayingCard("10 - Clubs")
          Dealer.SetCurrentHandValue(10)


          #print(PlayerCardHandValue)
          PlayerIsWinner = False
          if Player.CurrentCardValues > Dealer.CurrentCardValues:
             PlayerIsWinner = True
          else:
             PlayerIsWinner = False

          self.assertTrue(PlayerIsWinner)
      # DisplayPlayersCards(Player) - dealer displays players cards
      # DisplayDealerCards() - dealer displays cards
      # HitOrStay() - dealer decides if they want another card or not
      # PlayerHitOrStay() - dealer ask if the user wants to another card or not.
      # ShowCardsValue() - Displays dealers his\her hand
      # DeclareWinner(Player) - Dealer decalres the winner, looser or busy

if __name__ == '__main__':
    unittest.main()