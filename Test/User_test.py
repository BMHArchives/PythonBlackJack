# User_test.py - This is a unit test file to test the functionality of the User class

import unittest
import User
class TestDeckService(unittest.TestCase):
      
      svc = None
      def setUp(self):
          self.svc = User.User()
    
      # Make sure we can capture the username that the consumer submits
      def test_GetUserName(self):
          UserName = self.svc.GetUserName("Brandon")
          self.assertIsNotNone(UserName)
      
      # Make sure the user gets two playing cards
      def test_GetInitalPlayingCards(self):
          playingCards = self.svc.GetInitalPlayingCards()
          self.assertEqual(len(playingCards), 2)
      
      # Make sure that we can get the total bets that the user made on the current game.
      def test_GetUserBets(self):
          UserBet = 200.00
          self.svc.MakeBet(UserBet)
          UserBet = 300.00
          self.svc.MakeBet(UserBet)
          What_Did_The_User_Bet = self.svc.GetUserBets()
          self.assertEqual(What_Did_The_User_Bet, 500.00)
      
      # Confirm that a user can make a bet.
      def test_MakeBet(self):
          UserBet = 200
          self.svc.MakeBet(UserBet)
          User_Current_Bet = self.svc.UserBets
          self.assertEqual(User_Current_Bet, UserBet)
      
      # Confirm that a user can get a card
      def test_Hit_GetACard(self):
          self.svc.GetInitalPlayingCards()
          self.svc.HitOrStay(True)
          self.assertEqual(len(self.svc.playingCards),3)
        
      # Confirm that a user can stay and not get a new card
      def test_Stay_DoNotGetACard(self):
          self.svc.GetInitalPlayingCards()
          self.svc.HitOrStay(False)
          self.assertEqual(len(self.svc.playingCards),2)

if __name__ == '__main__':
    unittest.main()