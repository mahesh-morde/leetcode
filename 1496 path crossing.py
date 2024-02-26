
# 1496. Path Crossing
# Easy
# 1.3K
# 37
# Companies
# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

 

# Example 1:


# Input: path = "NES"
# Output: false 
# Explanation: Notice that the path doesn't cross any point more than once.
# Example 2:


# Input: path = "NESWW"
# Output: true
# Explanation: Notice that the path visits the origin twice.
 

# Constraints:

# 1 <= path.length <= 104
# path[i] is either 'N', 'S', 'E', or 'W'.



class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        visited = set()
        visited.add((0, 0))

        for direction in path:
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            else:
                x -= 1

            current_pos = (x, y)
            if current_pos in visited:
                return True  # Path crosses itself
            else:
                visited.add(current_pos)

        return False  # Path does not cross itself
