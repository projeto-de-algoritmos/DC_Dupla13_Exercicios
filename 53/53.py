# Divide: This involves dividing the problem into smaller sub-problems.
# Conquer: Solve sub-problems by calling recursively until solved.
# Combine: Combine the sub-problems to get the final solution of the whole problem.

import math

def findMaxSubArray(nums: list[int], left: int, right: int):
    # caso o left for maior que o right
    if left > right:
      return -math.inf     

    mid = (left + right) // 2
    left_sum, right_sum, cur_sum = 0, 0, 0

    # Percorre os elementos da esquerda procurando o maior valor deles
    for i in range(mid - 1, left - 1, - 1): # A partir do meio para as bordas
      left_sum = max(left_sum, cur_sum := cur_sum + nums[i]) # Checa o maior valor que conseguiu assumir desde o meio

    cur_sum = 0
    # Percorre os elementos da direita procurando o maior valor deles
    for i in range(mid + 1, right + 1): # A partir do meio para as bordas
      right_sum = max(right_sum, cur_sum := cur_sum + nums[i]) # Checa o maior valor que conseguiu assumir desde o meio
    
    # Retorna o maior valor que as bordas ou a substring atual conseguem assumir com a soma de todos os elementos
    return max(findMaxSubArray(nums, left, mid - 1), findMaxSubArray(nums, mid + 1, right), left_sum + right_sum + nums[mid])

class Solution:
  def maxSubArray(self, nums: list[int]) -> int:
    return findMaxSubArray(nums, 0, len(nums) - 1)

solution = Solution()
nums = [5,4,-1,7,8]

print(solution.maxSubArray(nums))