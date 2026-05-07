class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        k = len(arr) 

        current_max = -1

        for i in range(k - 1, -1, -1) : 

            num = arr[i]

            arr[i] = current_max 

            if num > current_max :
                current_max = num

        return arr