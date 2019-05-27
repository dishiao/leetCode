class Solution:
    def judgeCircle(self, moves: str) -> bool:
        r = 0
        l = 0
        u = 0
        d = 0
        for m in moves:
            if m == 'R':
                r += 1
            elif m == 'L':
                l += 1
            elif m == 'U':
                u += 1
            elif m == 'D':
                d += 1
        if r == l and u == d:
            return True
        else:
            return False
