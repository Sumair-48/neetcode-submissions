class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash = {}
        for i in nums:
            hash[i] = hash.get(i,0) + 1

        max_num = max(hash,key=hash.get)
        return max_num
            