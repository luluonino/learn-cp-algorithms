class UnionFind:
    def __init__(self, n: int):
        self.representative = [i for i in range(n + 1)]
        self.size = [1] * (n + 1)

    # size prioritized union 
    def union(self, i: int, j: int):
        i = self.find(i)
        j = self.find(j)
        
        if i == j:
            return
        else:
            if self.size[i] >= self.size[j]:
                self.representative[j] = i
                self.size[i] += self.size[j]
            else:
                self.representative[i] = j
                self.size[j] += self.size[i]

    # with path compression
    def find(self, i: int) -> int:
        if i == self.representative[i]:
            return i
        else:
            self.representative[i] = self.find(self.representative[i])
            return self.representative[i]
 
    def getSize(self, i: int) -> int:
        return self.size[self.find(i)]
