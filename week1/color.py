class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s_0 = 0
        s_2 = len(nums) - 1
        pointer = 0
        while pointer <= s_2:
            if nums[pointer] == 0:
                nums[s_0], nums[pointer] = nums[pointer], nums[s_0]
                s_0 += 1
                pointer += 1
            elif nums[pointer] == 2:
                nums[pointer], nums[s_2] = nums[s_2], nums[pointer]
                s_2 -= 1
            else:
                pointer += 1
