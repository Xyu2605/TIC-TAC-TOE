import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter
    def get_move(self, game):
         pass      
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Random vi tri danh dau cua may
        square = random.choice(game.available_moves())  
        return square
class HumanPlayer(Player):
        def __init__(self, letter):
            super().__init__(letter)
        def get_move(self, game):
            valid_square = False
            val = None
            while not valid_square:
                square = input(self.letter + '\'s turn. Let move (0-8):')
                # Thu xem gia tri truyen vao co chinh xac hay khong
                # neu la dang int thi duoc
                # neu vi tri khong hop le tren ban co thi phan hoi gia tri truyen vao khong hop li
                try:
                    val = int(square)
                    if val not in game.available_moves():
                        raise ValueError #(["Vi tri di khong hop le"])
                    valid_square = True
                except ValueError:
                    print("Nuoc di khong hop le. Hay thu lai !")
            return val       
def AIComputerPlayer(player):
    def __init__(self, letter):
        super().__innit__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #Chon 1 nuoc di hop le de chien thang
        else:
            square = self.minimax(game, self.letter)
        return square    
    def minimax(self, state, player):
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        #Check xem ai la nguoi win truoc
        if state.currennt_winner == other_player:
            return {'position' : None,
                    'score' : 1 * (state.num_emty_squares() + 1) if other_player == max_player else -1 * (
                    state.num_empty_squares() + 1)
            }