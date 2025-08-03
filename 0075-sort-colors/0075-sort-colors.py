class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low, i, high = 0, 0, len(nums) - 1

        while i <= high:
            if nums[i] == 0:
                nums[low], nums[i] = nums[i], nums[low]
                low += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            else:                         
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
