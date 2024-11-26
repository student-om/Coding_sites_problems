class Solution:
    def judgeCircle(self, moves: str) -> bool:
        # (x, y)
        coordinates = [0, 0]
        for i in range(len(moves)):
            if moves[i] == 'U':
                coordinates[1] = coordinates[1] + 1
            elif moves[i] == 'D':
                coordinates[1] = coordinates[1] - 1
            elif moves[i] == 'R':
                coordinates[0] = coordinates[0] + 1
            else:
                coordinates[0] = coordinates[0] - 1

        return coordinates == [0, 0]    
