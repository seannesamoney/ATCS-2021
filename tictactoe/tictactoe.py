import random
import time

class TicTacToe:
    def __init__(self):
        # TODO: Set up the board to be '-'
        # self.board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]
        self.board = [['-', '-', '-'],['-', '-', '-'],['-', '-', '-']]

        ##self.print_board()

    def print_instructions(self):
        # TODO: Print the instructions to the game
        instructions = "Welcome to TicTacToe!\nPlayer 1 is X and Player 2 is O.\nTake turns placing your pieces - the first to 3 wins!"
        print(instructions)

    def print_board(self):
        # TODO: Print the board
        counter = 0
        print("\t0\t1\t2")
        for i in self.board :
            print(counter, "\t", end="")
            counter = counter + 1
            for y in i :
                print(y,"\t", end = "")
            print("")


    def is_valid_move(self, row, col):
        # TODO: Check if the move is valid

            if row <= 2 and row >= 0 and col <= 2 and col >=0:
                if self.board[row][col] == "-":
                    return True

            return False

    def place_player(self, player, row, col):
        # TODO: Place the player on the board
        self.board[row][col] = player


    def take_manual_turn(self, player):
        # TODO: Ask the user for a row, col until a valid response
        #  is given them place the player's icon in the right spot
        row1 = int(input("Enter a row: "))
        col1 = int(input("Enter a column: "))

        while self.is_valid_move(row1, col1) == False :
            print("Invalid input. Try Again")
            row1 = int(input("Enter a row: "))
            col1 = int(input("Enter a column: "))

        self.place_player(player, row1, col1)

    def take_turn(self, player):
        # TODO: Simply call the take_manual_turn function
        depth = 2
        alpha = -100
        beta = 100
        if player == "X":
            self.take_manual_turn("X")
        if player == "O":
            self.take_minimax_alpha_beta_turn("O", depth, alpha, beta)

    #Chooses a random spot on the TicTacToe board
    def take_random_turn(self, player):
        rand_row = random.randint(0, 2)
        rand_col = random.randint(0, 2)
        while self.is_valid_move(rand_row, rand_col) == False:
            rand_row = random.randint(0, 2)
            rand_col = random.randint(0, 2)
        self.place_player(player, rand_row, rand_col)



    def check_col_win(self, player):
        # TODO: Check col win
        # counter = 0
        # for i in self.board[0]:
        #     for n in range(3):
        #         if n == player:
        #             counter = counter + 1
        #         if counter == 3:
        #             return True
        #         counter = 0
        # return False

        for i in range(0,3):
            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True

        return False


    def check_row_win(self, player):
        # TODO: Check row win
        for i in self.board:
            if i == [player, player, player]:
                return True
        return False



    def check_diag_win(self, player):
        # TODO: Check diagonal win
        if (self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player):
            return True
        elif (self.board[2][0] == player and self.board[1][1] == player and self.board[0][2] == player):
            return True

        return False

        
        return False

    def check_win(self, player):
        # TODO: Check win
        if self.check_row_win(player) == True:
            return True
        if self.check_col_win(player) == True:
            return True
        if self.check_diag_win(player) == True:
            return True
        
        return False

    def check_tie(self):
        # TODO: Check tie
        isTie = False
        for i in self.board:
            for a in i:
                if a == "-":
                    return False
        if self.check_win("X") == True :
            return False

        if self.check_win("O") == True :
            return False
            
        return True
                        
    #Minimax function uses recursion to find best move to always win or tie
    def minimax(self, player, depth):
        opt_row = -1
        opt_col = -1
        #Base Case
        # if self.check_win(player) == True or self.check_tie() == True:
        if self.check_win("O") == True:
            return (10, None, None)
        if self.check_win("X") == True:
            return (-10, None, None)
        if self.check_tie() == True:
            return (0, None, None)
        if depth == 0:
            return (0,None,None)

        #Recursive Case
        if player == "O":
            best = -100
            for i in range(3):
                for a in range(3):
                    if self.is_valid_move(a,i) == True:
                        self.place_player("O", a, i)
                        score = self.minimax("X", depth-1)[0]
                        self.place_player("-", a, i)
                        if best < score:
                            best = score
                            # self.place_player("-", a, i)
                            opt_row = a
                            opt_col = i
            return (best, opt_row, opt_col)

        if player == "X":
            worst = 100
            for i in range(3):
                for a in range(3):
                    if self.is_valid_move(a,i) == True:
                        self.place_player("X", a, i)
                        score,r,c = self.minimax("O", depth-1)
                        self.place_player("-", a, i)
                        if worst > score:
                            worst = score
                            self.place_player("-", a, i)
                            opt_row = a
                            opt_col = i
            return (worst, opt_row, opt_col)


    def take_minimax_turn(self, player, depth):
        start = time.time()
        score, row, col = self.minimax(player, depth)
        end = time.time()
        self.place_player(player, row, col)
        print("This turn took:", end - start, "seconds")

    def take_minimax_alpha_beta_turn(self, player, depth, alpha, beta):
            start = time.time()
            score, row, col = self.minimax_alpha_beta(player, depth, alpha, beta)
            end = time.time()
            self.place_player(player, row, col)
            print("This turn took:", end - start, "seconds")

    def  minimax_alpha_beta(self, player, depth, alpha, beta):
        opt_row = -1
        opt_col = -1
        # Base Case
        #if self.check_win(player) == True or self.check_tie() == True:
        if self.check_win("O") == True:
            return (10, None, None)
        if self.check_win("X") == True:
            return (-10, None, None)
        if self.check_tie() == True:
            return (0, None, None)
        if depth == 0:
            return (0, None, None)

        # Recursive Case
        if player == "O":
            best = -100
            for i in range(3):
                for a in range(3):
                    if self.is_valid_move(a,i) == True:
                        self.place_player("O", a, i)
                        score = self.minimax_alpha_beta("X", depth - 1, alpha, beta)[0]
                        alpha = max(alpha,score)

                        self.place_player("-", a, i)
                        if best < score:
                            best = score
                            opt_row = a
                            opt_col = i
                        if alpha >= beta:
                            return (best, opt_row, opt_col)

            return (best, opt_row, opt_col)

        if player == "X":
            worst = 100
            for i in range(3):
                for a in range(3):
                    if self.is_valid_move(a,i) == True:
                        self.place_player("X", a, i)
                        score, r, c = self.minimax_alpha_beta("O", depth - 1,alpha,beta)
                        beta = min(beta,score)

                        self.place_player("-", a, i)
                        if worst > score:
                            worst = score
                            opt_row = a
                            opt_col = i
                        if beta <= alpha:
                            return(worst, opt_row, opt_col)

            return (worst, opt_row, opt_col)
    

    def play_game(self):
        # TODO: Play game
        self.print_instructions()
        self.print_board()
        while self.check_tie()==False and self.check_win('X')==False and self.check_win('O')==False:
            self.take_turn('X')

            self.print_board()
            if self.check_win('X')==False and self.check_tie()==False:
                self.take_turn('O')
                self.print_board()
            if self.check_tie() == True:
                print("Tie!")
            if self.check_win("X") == True:
                print("X wins!")
            if self.check_win("O") == True:
                print("O wins!")
        #print("Game over!")





