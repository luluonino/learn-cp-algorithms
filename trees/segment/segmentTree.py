from typing import List

class SegmentTree():
    """ Segment tree for finding the sum of an interval in an int array"""
    def __init__(self, a: List[int]):
        self.n = len(a)
        self.v = [0] * (self.n * 4) # 1-indexed array to save the values 
        self._build(a, 1, 0, len(a) - 1)

    def _build(self, a: List[int], i: int, tl: int, tr: int) -> None:
        if (tl == tr): # leaf node
            self.v[i] = a[tl]
        else:
            tm = (tl + tr) // 2
            self._build(a, i * 2, tl, tm)
            self._build(a, i * 2 + 1, tm + 1, tr)
            self.v[i] = self.v[i * 2] + self.v[i * 2 + 1]

    def query(self, l: int, r: int) -> int:
        return self._query(1, 0, self.n - 1, l, r) # start with root node 1 and the whole range

    def _query(self, i: int, tl: int, tr: int, l: int, r: int) -> int:
        # i: node index, tl: node interval left boundary, tr: node interval right boundary
        # l: query left boundary, r: query right boundary 
        if l > r:
            return 0
        if l == tl and r == tr:
            return self.v[i]
        tm = (tl + tr) // 2
        return self._query(i * 2, tl, tm, l, min(r, tm)) + \
            self._query(i * 2 + 1, tm + 1, tr, max(l, tm + 1), r)
        
    def update(self, pos: int, new_val: int) -> None:
        if pos < 0 or pos > self.n - 1: # nothing to do 
            return None
        else:
            self._update(1, 0, self.n - 1, pos, new_val) # recursively update nodes, starting with the root

    def _update(self, i: int, tl: int, tr: int, pos: int, new_val: int) -> None:
        if tl == tr:
            self.v[i] = new_val
        else:
            tm = (tl + tr) // 2
            if pos <= tm:
                self._update(i * 2, tl, tm, pos, new_val)
            else:
                self._update(I * 2 + 1, tm + 1, tr, pos, new_val)

            self.v[i] = self.v[i * 2] + self.v[i * 2 + 1]

