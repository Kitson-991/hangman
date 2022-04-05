class Card:
    suits = ["spades", "hearts", "diamonds", "clubs"]
    # spade < heart < diamond < club

    values = [None, None,
              "2", "3", "4", "5", "6", "7", "8", "9",
              "10", "Jack", "Queen", "King", "Ace",]
    # 冒頭のNoneはインデックス値と数字を一致させるため

    def __init__(self, v, s):
        """スートも整数値"""
        self.value = v
        self.suit = s

    def __lt__(self, c2):
    # __lt__ は比較演算子の特殊メソッド
    # testcode
        if self.value < c2.value:
            return True
        if self.value == c2.value:
            if self.suit < c2.suit:
                return True
            else:
                return False
        # if self.value > c2.value:
        return False

    def __gt__(self, c2):
    # __gt__ は比較演算子の特殊メソッド
        if self.value > c2.value:
            return True
        if self.value == c2.value:
            if self.suit > c2.suit:
                return True
            else:
                return False
        # if self.value < c2.suit:
        return False

    def __repr__(self):
        v = self.values[self.value] + " of " \
            +self.suits[self.suit]
        return v


card1 = Card(10, 2)
card2 = Card(11, 3)
print(card1 < card2)
print(card1 > card2)

card = Card(3, 2)
print(card)


from random import shuffle


class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2, 15):
            for j in range(4):
                self.cards.append(Card(i, j))
            # shuffleはrandomモジュール内のメソッド
            shuffle(self.cards)

        def rm_card(self):
            if len(self.cards) == 0:
                return
            return self.cards.pop()

deck = Deck()
for card in deck.cards:
    print(card)


class Player:
    def __init__(self, name):
        self.wins = 0
        self.card = None
        self.name = name

class Game:
    def __init__(self):
        name1 = input("プレイヤー1の名前 ")
        name2 = input("プレイヤー2の名前 ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)

    def wins(self, winner):
        w = "このラウンドは {} が勝ちました"
        w = w.format(winner)
        print(w)

    def draw(self, pln, plc, p2n, p2c):
        d = "{} は {}、 {} は {} を引きました"
        d = d.format(pln, plc, p2n, p2c)
        print(d)

    def play_game(self):
        cards = self.deck.cards
        print("戦争を始めます！")
        while len(cards) >= 2:
            m = "q で終了、それ以外のキーでPlay:"
            response = input(m)
            if response == 'q':
                break
            p1c = self.deck.rm_card()
            p1c = self.deck.rm_card()
            p1n = self.p1.neme
            p2n = self.p2.name
            self.draw(p1n, plc, p2n, p2c)
            if plc > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            else:
                self.p2.wins += 1
                self.wins(self.p2.name)
        # if len(cards) < 2
        win = self.winner(self.p1, self.p2)
        print("ゲーム終了、{} の勝利です！".format(win))

    def winner(self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins < p2.wins:
            return p2.name
        # if p1.wins == p2.wins
        return "引き分け！"

game = Game()
# オブジェクトの作成時に名前入力を受け付ける
game.play_game()
