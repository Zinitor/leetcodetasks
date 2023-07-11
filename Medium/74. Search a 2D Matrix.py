class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])-1
        for i in range(m):
            if matrix[i][0] <= target <= matrix[i][n]:
                l, r = 0, n
                while l <= r:
                    halfpoint = (l+r)//2
                    if target == matrix[i][halfpoint]:
                        return True
                    if target > matrix[i][halfpoint]:
                        l = halfpoint+1
                    if target < matrix[i][halfpoint]:
                        r = halfpoint-1
        return False


a = Solution()
print(a.searchMatrix(matrix=[[1, 3, 5, 7], [
      10, 11, 16, 20], [23, 30, 34, 60]], target=3))
