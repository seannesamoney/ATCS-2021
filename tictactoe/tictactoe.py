import random


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
        if player == "X":
            self.take_manual_turn("X")
        if player == "O":
            self.take_random_turn("O")

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





