letters = {}
letters[2] = ('a', 'b', 'c')
letters[3] = ('d', 'e', 'f')
letters[4] = ('g', 'h', 'i')
letters[5] = ('j', 'k', 'l')
letters[6] = ('m', 'n', 'o')
letters[7] = ('p', 'q', 'r', 's')
letters[8] = ('t', 'u', 'v')
letters[9] = ('w', 'x', 'y', 'z')

def mySearch(digits):
    print(digits)
    if len(digits) ==  0:
        return ()
    elif len(digits) == 1:
        return letters[int(digits[0])]
    else:
        results = mySearch(digits[1:])
        result = set()
        print(int(digits[1]))
        print(letters[int(digits[0])])
        for letter in letters[int(digits[0])]:
            for item in results:
                result.add(letter + item)

    return result

print(mySearch("234"))

# letters = {}
# letters['2'] = ('a', 'b', 'c')
# letters['3'] = ('d', 'e', 'f')
# letters['4'] = ('g', 'h', 'i')
# letters['5'] = ('j', 'k', 'l')
# letters['6'] = ('m', 'n', 'o')
# letters['7'] = ('p', 'q', 'r', 's')
# letters['8'] = ('t', 'u', 'v')
# letters['9'] = ('w', 'x', 'y', 'z')


# def mySearch(digits):
#     if len(digits) ==  0:
#         return []
#     elif len(digits) == 1:
#         return letters[digits[0]]
#     else:
#         results = mySearch(digits[1:])
#         result = []
#         for letter in letters[digits[0]]:
#             for item in results:
#                 result.append(letter + item)
#     return result

# class Solution(object):
    
#     def letterCombinations(self, digits):
        

#         """
#         :type digits: str
#         :rtype: List[str]
#         """
#         return mySearch(digits)