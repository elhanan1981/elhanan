from cards import Deck


class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand

    def __repr__(self):
        return self.name


class Game:
    def __init__(self, name1, name2, deck=Deck()):
        self.player1 = Player(name1, deck.deal_hand(27))
        self.player2 = Player(name2, deck.deal_hand(27))
        self.score = {name1: 0, name2: 0}
        self.cash = []

    def check_finish(self):
        return len(self.player1.hand) == 0 or len(self.player2.hand) == 0

    def add_round_l(self, n):
        while n > 0 and not self.check_finish():
            self.cash.append(self.player1.hand.pop(0))
            self.cash.append(self.player2.hand.pop(0))
            n -= 1

    def who_won(self):
        if self.cash[-2] > self.cash[-1]:
            self.winner_round(self.player1)
        else:
            self.winner_round(self.player2)

    def winner_round(self, win):
        win.hand.extend(self.cash)
        self.score[win.name] += 1
        self.cash.clear()

    def round(self):
        self.add_round_l(1)
        while self.cash[-2] == self.cash[-1] and not self.check_finish():
            self.add_round_l(3)
        self.who_won()

    def flow_game(self, rounds=float('inf')):
        while rounds > 0 and not self.check_finish():
            self.round()
            rounds -= 1
        return self.__repr__()

    def __repr__(self):
        if not self.check_finish():
            return 'equal'
        if len(self.player1.hand) > len(self.player2.hand):
            winner, loser = self.player1, self.player2
        else:
            winner, loser = self.player2, self.player1
        return (f'the winner is :{winner},amount cards:{len(winner.hand)},scores:{self.score[winner.name]}\n'
                f'the loser is :{loser},amount cards:{len(loser.hand)},scores:{self.score[loser.name]}')


a = Game('yitschak', 'elhanan')
print(a.flow_game())
