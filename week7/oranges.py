from collections import deque
class Solution:
    def findInfo(self, oranges):
        cnt = 0
        rotten = deque()
        for row in range(len(oranges)):
            for col in range(len(oranges[row])):
                if oranges[row][col] == 2:
                    rotten.append((row, col))
                if oranges[row][col] == 1:
                    cnt += 1
        return cnt, rotten

    def neighbors(self, pos):
        res = []
        if pos[0] > 0:
            res.append((pos[0] - 1, pos[1]))
        if pos[0] < len(self.grid) - 1:
            res.append((pos[0] + 1, pos[1]))
        if pos[1] < len(self.grid[0]) - 1:
            res.append((pos[0], pos[1] + 1))
        if pos[1] > 0:
            res.append((pos[0], pos[1] - 1))
        return list(filter(lambda n: n not in self.visited and self.grid[n[0]][n[1]] != 0, res))
    def orangesRotting(self, grid: list[list[int]]) -> int:
        self.grid = grid
        fresh, rotten = self.findInfo(grid)
        if not start or not fresh: return 0
        queue = rotten
        self.visited = set(queue)
        minutes = 0
        while queue:
            length = len(queue)
            while length:
                if length == 1:
                    minutes += 1
                cell = queue.popleft()
                neighbors = self.neighbors(cell)
                for n in neighbors:
                    self.grid[n[0]][n[1]] = 2
                    if self.neighbors(n):
                        queue.append(n)
                    self.visited.add(n)
                    fresh -= 1
                length -= 1
            if not fresh: return minutes
        if fresh: return -1