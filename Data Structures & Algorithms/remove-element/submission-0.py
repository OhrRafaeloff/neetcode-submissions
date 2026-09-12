class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)): # Check each number
            if nums[i] != val:
                # Is this a number we want to keep?
                nums[k] = nums[i]
                k += 1 
        return k