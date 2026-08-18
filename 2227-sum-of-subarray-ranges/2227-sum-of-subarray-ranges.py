class Solution:
    # Function to find the sum of 
    # subarray ranges in each subarray
    def subArrayRanges(self, arr):
        
        # Size of array
        n = len(arr)
        
        # To store the sum
        total_sum = 0
        
        # Traverse on the array
        for i in range(n):
            
            # To store the smallest value of subarray
            smallest = arr[i]
            
            # To store the largest value of subarray
            largest = arr[i]
            
            # Nested loop to get all 
            # subarrays starting from index i
            for j in range(i, n):
                
                # Update the smallest value
                smallest = min(smallest, arr[j])
                
                # Update the largest value
                largest = max(largest, arr[j])
                
                # Update the sum
                total_sum += (largest - smallest)
        
        # Return the computed sum
        return total_sum

