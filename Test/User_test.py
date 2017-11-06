# User_test.py - This is a unit test file to test the functionality of the User class

import unittest
import User
import CardDeckService
class TestDeckService(unittest.TestCase):
      
      UserSvc = None
      CardDeckSvc = None
      def setUp(self):
          self.UserSvc = User.User()
          self.CardDeckSvc = CardDeckService.CardDeckService()
        #   CardDeckSvc = CardDeckService.CardDeckService()
        #   CardDeckSvc.BuildCardDeck()
        #   CardDeckSvc.ShuffleCardDeck()
      
      def test_SettingTheUserName(self):
          svc = self.UserSvc
          svc.SetUserName("Brandon")
          ActualUserName = svc.GetUserName()
          ExpectedUserName = "Brandon"
          self.assertEqual(ExpectedUserName, ActualUserName)  

      # Make sure that we can get the total bets that the user made on the current game.
      def test_GetUserBets(self):
          svc = self.UserSvc
          svc.SetBet(200.00)
          svc.SetBet(300.00)
          What_Did_The_User_Bet = svc.GetBets()
          self.assertEqual(What_Did_The_User_Bet, 500.00)
      
      def test_SetCardValue_Confirm_A_Card_Value_Was_Set(self):
          UserSvc = self.UserSvc
          CardDeckSvc = self.CardDeckSvc

          CardValue = 10
          UserSvc.SetCurrentHandValue(CardValue)
          ExpectedValue = 10
          ActualValue = UserSvc.GetCurrentHandValue()
          self.assertEqual(ExpectedValue, ActualValue)

if __name__ == '__main__':
    unittest.main()