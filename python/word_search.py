def findWords(board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        def searcher(board, word, x, y):
            if len(word) == 0:
                return True
            elif (x, y) in searched:
                return False
            elif x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
                return False
            elif board[x][y] == word[-1]:
                searched.add((x, y))
                word = word[:len(word) - 1]
                if searcher(board, word, x + 1, y):
                    return True
                if searcher(board, word, x, y - 1):
                    return True
                if searcher(board, word, x - 1, y):
                    return True
                if searcher(board, word, x, y + 1):
                    return True
                searched.remove((x, y))
                return False
            else:
                return False

        found_words = []
        letters = set()
        
        for i in board:
            for j in i:
                letters.add(j)
                
        for z in words:
            for letter in z:
                if letter not in letters:
                    break
            else:
                searched = set()
                for i in range(len(board)):
                    for j in range(len(board[i])):
                        if board[i][j] == z[-1]:
                            if searcher(board, z, i, j):
                                if z not in found_words:
                                    found_words.append(z)

        return found_words

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]
print(findWords(board, words))