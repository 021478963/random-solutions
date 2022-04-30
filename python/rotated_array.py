class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        mid = (high + low) // 2
        
        while 1:
            # print(low, high)
            if nums[mid] == target:
                return mid
            elif high - low <= 2:
                if nums[high] == target:
                    return high
                if nums[low] == target:
                    return low
                return -1
            if nums[mid] < nums[low]:
                if target >= nums[mid] and target < nums[0]:
                    low = mid
                else:
                    high = mid
            else:
                if nums[low] <= target and target < nums[mid]:
                    high = mid
                else:
                    low = mid
            mid = (high + low) // 2