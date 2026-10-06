import random

MOVES = ['rock', 'paper', 'scissors']


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class AllRockPlayer(Player):
    """Always plays rock."""

    def move(self):
        return 'rock'


class RandomPlayer(Player):
    def move(self):
        return random.choice(MOVES)


class HumanPlayer(Player):
    def move(self):
        while True:
            move = input(
                "Enter move (rock/paper/scissors or quit): "
            ).lower()
            if move == 'quit':
                print("Thanks for playing!")
                exit()
            if move in MOVES:
                return move
            print("Invalid input. Please try again.")


class ReflectPlayer(Player):
    def __init__(self):
        self.last_move = 'rock'

    def move(self):
        return self.last_move

    def learn(self, my_move, their_move):
        self.last_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.index = 0
        self.my_move = None

    def move(self):
        move = MOVES[self.index]
        self.index = (self.index + 1) % 3
        return move

    def learn(self, my_move, their_move):
        self.my_move = my_move


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"\nPlayer 1 plays: {move1}")
        print(f"Player 2 plays: {move2}")

        if move1 == move2:
            print("It's a tie!")
        elif beats(move1, move2):
            print("Player 1 wins the round!")
            self.score1 += 1
        else:
            print("Player 2 wins the round!")
            self.score2 += 1

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

        print(
            f"Score -> Player 1: {self.score1} | "
            f"Player 2: {self.score2}"
        )

    def play_game(self):
        print("Rock Paper Scissors Game!")
        print("Type 'quit' anytime to exit.\n")

        round_number = 1
        while True:
            print(f"Round {round_number}")
            self.play_round()
            round_number += 1


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
