class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s=set()
        for r in range(9):
            for c in range(9):
                n=board[r][c]
                if n==".":
                    continue
                if ((n,r) in s or (c,n) in s or (r//3,c//3,n) in s):
                    return False
                s.add((n,r))
                s.add((c,n))
                s.add((r//3,c//3,n))
        return True