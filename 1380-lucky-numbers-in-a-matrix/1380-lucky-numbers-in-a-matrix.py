class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        r=[]
        for row in matrix:
            r.append(min(row))
        rows = len(matrix)
        c= len(matrix[0])
        l= []
        for j in range(0,c):
            o=[]
            for i in range(0,rows):
                o.append(matrix[i][j])
            if max(o) in r:
                l.append(max(o))
        return l
        