class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rowmin = [min(i) for i in matrix]
        colmin = [max(i) for i in zip(*matrix)]
        return [i for i in rowmin if i in colmin]
