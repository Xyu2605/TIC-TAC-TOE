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
        
class AIComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            square = random.choice(game.available_moves()) #Chon 1 nuoc di random
        else:
            square = self.minimax(game, self.letter)['position']
        return square    
    
    def minimax(self, state, player):
        # state đại diện cho trạng thái hiện tại của trò chơi (game state).
        max_player = self.letter
        other_player = 'O' if player == 'X' else 'X'
        #Check xem ai la nguoi win truoc
        if state.current_winner == other_player:
            return {'position' : None,
                    'score' : 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)
            }
        
        elif not state.empty_squares():
            return {'position': None, 'score' : 0}
        
        if player == max_player:
            best = {'position': None, 'score' : -math.inf}
        else:
            best = {'position': None, 'score' : math.inf}

        for possible_move in state.available_moves():
            # Buoc 1: Thuc hien di chuyen, thu buoc di
            state.make_move(possible_move, player)
            # Buoc 2: lặp lại bằng cách sử dụng minimax để mô phỏng trò chơi sau khi thực hiện bước đi đó
            sim_score = self.minimax(state, other_player) 
            # Buoc 3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move
            # Buoc 4: cap nhat tu dien neu can thiet
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score   
        return best