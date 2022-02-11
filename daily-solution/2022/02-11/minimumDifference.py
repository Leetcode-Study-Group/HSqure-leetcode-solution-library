class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        minimun_list=[]
        for i in range(0,(len(nums)-k+1)):
            minimun_list.append(nums[i+k-1] - nums[i])

        minimun_list.sort()
        print(minimun_list)
        return minimun_list[0]
