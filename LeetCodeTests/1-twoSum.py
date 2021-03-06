class Solution:
    # interesting c solution, define simple hash by self 
    # https://leetcode.com/problems/two-sum/discuss/19/Accepted-C-solution-of-HashMap-in-4ms
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict = {}
        length = len(nums)
        for i in range(0, length):
            num_i = nums[i]
            numDict[num_i] = i
        for i in range(0, length):
            num = nums[i]
            remain = target - num
            if remain in numDict:
                remain_index = numDict[remain]
                if i != remain_index:
                    return [i, remain_index]

def test_func():
    test = Solution()
    assert test.twoSum([3,2,4], 6) == [1,2]
