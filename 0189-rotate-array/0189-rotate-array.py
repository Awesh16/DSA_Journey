class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        while(k>len(nums)):
            k=k-len(nums)
        nums[:]=nums[len(nums)-k:]+nums[0:len(nums)-k]
        