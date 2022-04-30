class Solution:
    def candy(self, ratings: List[int]) -> int:
        def recursive(ratings, candies, list_offset):
            print(ratings)
            if len(ratings) == 1:
                if list_offset not in candies.keys():
                    candies[list_offset] = 1
                return ratings
            mid = len(ratings) // 2
            left = recursive(ratings[:mid], candies, list_offset)
            right = recursive(ratings[mid:], candies, list_offset + mid)
            if left[-1] > right[0]:
                if candies[list_offset + mid - 1] <= candies[list_offset + mid]:
                    candies[list_offset + mid - 1] = candies[list_offset + mid] + 1
                    for i in range(len(left) - 1, 0, -1):
                        if left[i - 1] > left[i]:
                            candies[list_offset + i - 1] = candies[list_offset + i] + 1
                return ratings
            elif left[-1] < right[0]:
                print("numbers:", left[-1], right[0])
                print("candies:", candies[list_offset + mid - 1], candies[list_offset + mid])
                if candies[list_offset + mid - 1] >= candies[list_offset + mid]:
                    candies[list_offset + mid] = candies[list_offset + mid - 1] + 1
                    print("candies after change:", candies[list_offset + mid - 1], candies[list_offset + mid])
                    for i in range(0, len(right) - 1):
                        if right[i + 1] > right[i]:
                            candies[list_offset + mid + i + 1] = candies[list_offset + mid + i] + 1
                            print("HELLO,", candies[list_offset + mid + i], candies[list_offset + i + 1])
                            print("again, ", right[i], right[i + 1])
                print(candies[list_offset + mid - 1], candies[list_offset + mid])
                return ratings
            else:
                return ratings
        
        candies = {}
        
        recursive(ratings, candies, 0)
        result = 0
        print()
        for i in candies.keys():
            print(candies[i], end=", ")
            result += candies[i]
            
        return result