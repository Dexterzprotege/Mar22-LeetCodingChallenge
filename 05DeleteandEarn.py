# Question: https://leetcode.com/problems/delete-and-earn/submissions/

# Solution:
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        numset = sorted(list(set(nums)))
        curr1, curr2 = 0, 0
        for i in range(len(numset)):
            currVal = numset[i]*dic[numset[i]]
            if i > 0 and numset[i] - 1 == numset[i-1]:
                curr1, curr2 = curr2, max(currVal + curr1, curr2)
            else:
                curr1, curr2 = curr2, currVal + curr2
        return curr2
      
# Verdict:
# Runtime: 98 ms, faster than 36.69% of Python3 online submissions for Delete and Earn.
# Memory Usage: 14.2 MB, less than 66.35% of Python3 online submissions for Delete and Earn.
