# крестики-нолики
from random import *
X = 'X'
O = 'O'
TIE = 'Ничья'

def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        try:
            response = int(input(question))
        except:
            print('Введи число')    
    return response            


def lot(): 
    go_first = ['y', 'n']
    choice(go_first)                
    if choice(go_first) == 'y':
        print('\nСлепой жребий показал, что ты первый! Играй крестиками. ')
        human = X
        computer = O
    else:
        print('\n Слепой жребий показал, что буду начинать я. ')
        human = O
        computer = X  
    return computer, human


def new_board():
    board = [' ' for i in range(9)]
    return board


def print_board(board):
    print('\n\t', board[0], '|', board[1], '|', board[2])
    print('\t', '---------') 
    print('\t', board[3], '|', board[4], '|', board[5])
    print('\t', '---------')
    print('\t', board[6], '|', board[7], '|', board[8], '\n')


def legal_moves(board):
    '''Создает список доступных ходов'''
    moves = [i for i in range(9)if board[i] == ' ']
    return moves


def winner(board):
    win_in_game = ((0, 1, 2),
                  (3, 4, 5),
                  (6, 7, 8),
                  (0, 3, 6),
                  (1, 4, 7),
                  (2, 5, 8),
                  (0, 4, 8),
                  (2, 4, 6))
    for row in win_in_game :
        if board[row[0]] == board[row[1]] == board[row[2]] != ' ':
            winner = board[row[0]]
            return winner       # Х или О если один из игроков побеждает 
        if ' ' not in board:    # если все поля заняты но победы никто не достиг
            return TIE 
    return None                 # если хотя бы одно из полей пусто, но победителя нет  


def human_move(board, human):
    move = None
    while move not in legal_moves(board):
        move = ask_number(f'Твой ход. Выбери одно из полей {legal_moves(board)}: ', 0, 9)
        if move not in legal_moves(board):
            print('\nЭто поле уже занято. Выбери другое.\n')
    return move


def computer_move(board, computer, human):                 # функция с такой стратегией компьютера:
    board = board[:]                                       # если существует выигрышный ход - делает
    print('Я выберу поле номер: ' , end = '')              # если существует у человека ход, после которого он выйграет - нужно предупредить и сделать этот ход
    moves = legal_moves(board)                             # в ином случает выбирается из "лучших"(более центрально расположенных) полей
    for move in legal_moves(board):
       board[move] = computer
       if winner(board) == computer:
            print (move)
            return move
    board[move] = ' '
    for move in legal_moves(board) :
        board[move] = human
        if winner(board) == human:
            print (move)
        return move
    board[move] = ' '
    for move in (4, 0, 2, 6, 8, 1, 3, 5, 7):
        if move in legal_moves(board):
            print(move)
        return move   


def next_turn(turn):
    return (O if turn == X else X)


def tick_tack_toe():
    print(''' Добро пожаловать в игру "Крестики - нолики". Чтобы сделать ход, введи число от 0 до 8. Числа соответствуют полям доски - так, как показано ниже:
    0 | 1 | 2
    ---------
    3 | 4 | 5 
    ----------
    6 | 7 | 8 
    ''') 
    computer, human = lot() 
    turn = X
    board = new_board()                  # пустую доску для игры в "Крестики-нолики"
    print_board(board)                  
    while not winner(board):               
        if turn == human: 
            move = human_move(board, human)  
            board[move] = human          # изменить вид доски
        else: 
            move = computer_move(board, computer, human) 
            board[move] = computer
        print_board(board)               # вывести на экран обновленный вид доски
        turn = next_turn(turn)           # переход хода   
    the_winner = winner(board)
    print('Три', the_winner, 'в ряд!\n' if the_winner != TIE else 'Ничья!\n')
    if the_winner == computer:
        print('Победа за компьютером ')
    elif the_winner == human:
        print('Поздравляю!!! Ты победитель!')
    elif the_winner == TIE:
        print('Игра вничью')


tick_tack_toe()                   