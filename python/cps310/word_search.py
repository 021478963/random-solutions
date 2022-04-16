def starter(board, word):
    def searcher(board, word, searched, x, y):
        if len(word) == 0:
            return True
        elif (x, y) in searched:
            return False
        elif x < 0 or x > boardX or y < 0 or y > boardY:
            return False
        elif board[x][y] == word[0]:
            searched.append((x, y))
            if searcher(board, word[1:], searched[:], x, y + 1):
                return True
            elif searcher(board, word[1:], searched[:], x, y - 1):
                return True
            elif searcher(board, word[1:], searched[:], x - 1, y):
                return True
            elif searcher(board, word[1:], searched[:], x + 1, y):
                return True
            else:
                return False
        else:
            return False

    boardX = len(board) - 1
    boardY = len(board[0]) - 1
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == word[0]:
                if searcher(board, word, [], i, j):
                    return True
    return False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
print(starter(board, word))