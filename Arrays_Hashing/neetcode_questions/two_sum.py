# Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.


class Solution: #brute force n*2
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]



class Solution:#using hashmap 0(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        
        for index,num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff] , index]
            hashmap[num] = index
            
        return
        

        
