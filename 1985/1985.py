# Divide: This involves dividing the problem into smaller sub-problems.
# Conquer: Solve sub-problems by calling recursively until solved.
# Combine: Combine the sub-problems to get the final solution of the whole problem.

def mergeSort(arr):
  if len(arr) > 1:
    # Finding the mid of the array
    mid = len(arr)//2

    # Dividing the array elements into 2 halves
    L = arr[:mid]
    R = arr[mid:]

    # Sorting the halves
    mergeSort(L)
    mergeSort(R)

    i = j = k = 0

    # Copy data to temp arrays L[] and R[]
    while i < len(L) and j < len(R):
        if int(L[i]) <= int(R[j]):
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


class Solution:
  def kthLargestNumber(self, nums: list[str], k: int) -> str:
    mergeSort(nums)
    return nums[len(nums) - k]

solution = Solution()

nums = ["2","21","12","1"]
k = 3

print(solution.kthLargestNumber(nums, k))

