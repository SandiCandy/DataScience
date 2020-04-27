def intro():
    print("Welcome to Tic-Tac-Toe!")

def read_field():
    field = int(input("Choose a field: ")) 
    print(field)
    if is_field_free(field):
        gamefield[field]="X"
        print_game(gamefield)
        return won_game(gamefield, 'X')
    else: 
        print("Not possible. Choose another field!")
        read_field()

def is_field_free(pos):
    if pos<=8 and not gamefield[pos]:
        return True
    return False

def computer_choose():
    print("Computer...")
    for pos, val in enumerate(gamefield):
        if is_field_free(pos):
            gamefield[pos]="O"
            print("...choose field", pos)
            return won_game(gamefield, 'O')

def won_game(gamefield, player):
    if ((gamefield[0]==player and gamefield[1]==player and gamefield[2]==player) or 
    (gamefield[3]==player and gamefield[4]==player and gamefield[5]==player) or
    (gamefield[6]==player and gamefield[7]==player and gamefield[8]==player) or
    (gamefield[0]==player and gamefield[3]==player and gamefield[6]==player) or
    (gamefield[1]==player and gamefield[4]==player and gamefield[7]==player) or
    (gamefield[2]==player and gamefield[5]==player and gamefield[8]==player) or
    (gamefield[0]==player and gamefield[4]==player and gamefield[8]==player) or
    (gamefield[2]==player and gamefield[4]==player and gamefield[6]==player)):
        print(player, "won!")
        return True
    return False

def print_game(gamefield):
    print(print_singlefield(gamefield[0]),"|",print_singlefield(gamefield[1]),"|",print_singlefield(gamefield[2]))
    print("_______________")
    print(print_singlefield(gamefield[3]),"|",print_singlefield(gamefield[4]),"|",print_singlefield(gamefield[5]))
    print("_______________")
    print(print_singlefield(gamefield[6]),"|",print_singlefield(gamefield[7]),"|",print_singlefield(gamefield[8]))


def print_singlefield(singlefield):
    if not singlefield:
        return " "
    else:
        return singlefield

gamefield = [None] * 9

def game_loop():
    while True:
        if read_field() or computer_choose():
            return True
        print_game(gamefield)
    print("Bye.")

intro()
print_game(gamefield)
game_loop()