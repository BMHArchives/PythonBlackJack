# Dealer.py - represents an instance of a Black Jack Dealer
import User
class Dealer:
      UserBetsAmount = 0
      UserCards = []      
      def __int__(self):
          pass
      # DealCardsToPlayer(Player) - dealer deals cards to user
      def DealCardsToPlayer(self, Player):
          pass
      def GetInitialPlayingCards(self):
          pass

      def CalculatePlayerCardsValue(self, Player):
          pass
      
      def RequestBet(self, Amount, Player):
          pass
      # RequestBet(Amount, User) - dealer request the user to make a bet
      # _CalculateUsersCardsCount(Player) - dealer counts current value of the player's card
      # _CalculateDealerCardsCount() - dealer counts their own hands
      # DisplayPlayersCards(Player) - dealer displays players cards
      # DisplayDealerCards() - dealer displays cards
      # HitOrStay() - dealer decides if they want another card or not
      # PlayerHitOrStay() - dealer ask if the user wants to another card or not.
      # ShowCardsValue() - Displays dealers his\her hand
      # DeclareWinner(Player) - Dealer decalres the winner, looser or busy