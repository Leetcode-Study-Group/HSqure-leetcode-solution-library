class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n=0
        i=0
        result = nums[0]
        while n < len(nums) - 2:
            n = 2 * i + 1
            # 比对
            if nums[n-1] != nums[n]:
                result = nums[n-1]
                break
            i+=1
            result = nums[n+1]

        return result
