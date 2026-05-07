class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        k = len(arr) 

        current_max = -1

        for i in range(k - 1, -1, -1) : 

            original_value = arr[i]

            arr[i] = current_max 

            if original_value > current_max :
                current_max = original_value

        return arr