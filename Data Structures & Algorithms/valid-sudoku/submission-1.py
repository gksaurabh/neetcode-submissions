class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we can use a hashset for each of the following: rows, columns, and boxes
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)

        # note that the boxes can be identified as the row and column integerdivided by 3. so it will be a 3x3 matrix instead of a 9x9
        boxes = collections.defaultdict(set) 

        # traverse through the matrix
        for r in range(len(board)):
            for c in range(len(board)):

                # if we encounter "." just continue, 
                if board[r][c] == ".":
                    continue

                # if we encounter the same value in any of the following: rows, columns, or boxes then return false. We found a duplicate
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r // 3, c // 3)]):                  
                    return False

                # update our rows, columns and boxes with the curent value. 
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r // 3, c // 3)].add(board[r][c])
        
        return True