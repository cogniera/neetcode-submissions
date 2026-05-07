class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        streak = 0
        maximus = 0

        for i in nums :

            if i == 1 :
                streak += 1
                if streak > maximus :
                    maximus = streak
            else :
                streak = 0
        
        return maximus