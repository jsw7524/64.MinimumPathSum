class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m=len(grid)
        n=len(grid[0])
        dp=[[0 for x in range(n)] for y in range(m)]
        dp[0][0]=grid[0][0]
        for x in range(1,n):
            dp[0][x]=grid[0][x]+dp[0][x-1]

        for y in range(1,m):
            dp[y][0] = grid[y][0]+dp[y-1][0]

        for y in range(1, m):
            for x in range(1, n):
                if dp[y-1][x] > dp[y][x-1]:
                    dp[y][x]=dp[y][x-1]+grid[y][x]
                else:
                    dp[y][x]=dp[y-1][x]+grid[y][x]
        return dp[m-1][n-1]


sln=Solution()
assert 7==sln.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
])

assert 1==sln.minPathSum([[1]])