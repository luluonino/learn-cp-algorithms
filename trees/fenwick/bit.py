# Fenwick Tree, or Binary Indexed Tree
class BITree:
    def __init__(self, n):
        self.n = n
        self.l = [0] * (n + 1)

    def update(self, i, x):
        i = i + 1
        while i <= self.n:
            self.l[i] = max(self.l[i], x)
            i += i & -i # move up to all nodes covering point i
        
    def query(self, i):
        i += 1
        ans = 0
        while i:
            ans = max(ans, self.l[i])
            i -= i & -i # move down to all ranges before i
        return ans

    def print(self):
        print(self.l)
