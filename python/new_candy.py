class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = {}
        for i in range(len(ratings)):
            candies[i] = 1
            
        for i in range(0, len(ratings) - 1):
            if ratings[i + 1] > ratings[i]:
                candies[i + 1] = candies[i] + 1
                
        for i in range(len(ratings) - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:

                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
            
        result = 0
        for i in candies.keys():
            print(candies[i], end=", ")
            result += candies[i]

        return result