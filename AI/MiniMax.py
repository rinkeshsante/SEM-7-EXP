import random

value = {
    'X': 1,
    "O": -1,
    0: 0
}


def CheckWin(game):
    count = 0
    for sym in ['X', 'O']:
        for i in range(3):
            if game[i][0] == sym and game[i][1] == sym and game[i][2] == sym:
                return sym
            if game[0][i] == sym and game[1][i] == sym and game[2][i] == sym:
                return sym
            if game[0][0] == sym and game[1][1] == sym and game[2][2] == sym:
                return sym
            if game[0][2] == sym and game[1][1] == sym and game[2][0] == sym:
                return sym
    for i in range(3):
        for j in range(3):
            if game[i][j] == '.':
                count += 1
    # finised but no win
    if count == 0:
        return 0
    # unfinished
    else:
        return None


def printMatrix(graph):
    for i in graph:
        for j in i:
            print(j, end=' ')
        print('')


def miniMax(game, isMax):
    score = CheckWin(game)
    if score == 0:
        return 0

    if isMax:
        max_val = -10000

        for i in range(3):
            for j in range(3):
                if game[i][j] == '.':
                    game[i][j] = 'X' if isMax else 'Y'
                    max_val = max(max_val, miniMax(game, False))
        return max_val

    else:
        min_val = 10000

        for i in range(3):
            for j in range(3):
                if game[i][j] == '.':
                    game[i][j] = 'X' if isMax else 'Y'
                    min_val = min(min_val, miniMax(game, True))
        return min_val


def PlayTikTack():
    # start = random.choice([0, 1])
    game = [["." for i in range(3)] for j in range(3)]

    for i in range(9):
        printMatrix(game)
        bestMove = None
        bestScore = 0

        if i % 2 == 1:
            x, y = map(int, input('enter the next coordinate : ').split(' '))
            game[x][y] = 'O'

        val = CheckWin(game)
        if val == 'X':
            print('AI win')
        elif val == 'O':
            print('Human Win')


if __name__ == '__main__':
    PlayTikTack()
