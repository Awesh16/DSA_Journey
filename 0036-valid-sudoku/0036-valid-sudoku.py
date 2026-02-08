from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # We use sets to store digits we've seen
        # Key will be the index (0-8), value will be a set of digits
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set) # Key will be a tuple (row//3, col//3)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                
                # Skip empty cells
                if val == ".":
                    continue
                
                # 1. Check Row
                if val in rows[r]:
                    return False
                rows[r].add(val)
                
                # 2. Check Column
                if val in cols[c]:
                    return False
                cols[c].add(val)
                
                # 3. Check 3x3 Box
                # (r//3, c//3) gives us a unique coordinate for each sub-box
                box_idx = (r // 3, c // 3)
                if val in boxes[box_idx]:
                    return False
                boxes[box_idx].add(val)
                
        return True