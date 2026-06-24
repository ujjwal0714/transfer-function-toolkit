from __future__ import annotations
from typing import List
from pydantic import BaseModel

def convolve(a: List[int], b: List[int]) -> List[int]:
    """
    [1,1] * [1,1] = [1,2,1]
    """
    res = [0] * (len(a)+len(b)-1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            res[i + j] += ai * bj
    return res
    
def add(a: List[int], b: List[int]) -> List[int]:
    """
    [1,1] + [1,1,1] = [1,2,2]
    """
    max_len = max(len(a), len(b))
    a = [0] * (max_len - len(a)) + a
    b = [0] * (max_len - len(b)) + b
    return [x + y for x, y in zip(a, b)]

def subtract(a:List[int], b:List[int]):
    """
    [1,1,1] - [1,1] = [1,0,0]
    """
    max_len = max(len(a), len(b))
    a = [0]*(max_len-len(a)) + a
    b = [0]*(max_len-len(b)) + b
    return [x-y for x,y in zip(a,b)]
    
class TF(BaseModel):
    nr: List[int]
    dr: List[int]

    model_config = {
        "frozen": True
        }

    def __mul__(self, other:TF) -> TF:
        """
        (tf1, tf2) => tf1 * tf2
        tf1 = {nr:[1],dr[1,0]}
        tf2 = {nr:[1],dr[1,0]}
        res = tf1 * tf2 = {nr:[1],dr[1 0 0]}
        """
        nr = convolve(self.nr, other.nr)
        dr = convolve(self.dr, other.dr)

        return TF(nr=nr,dr=dr)

    def __add__(self, other:TF) -> TF:
        """
        (tf1, tf2) => tf1 + tf2 => res = (nr1*dr2+nr2*dr1)/(dr1*dr2)
        tf1 = {nr:[1],dr[1,0]}
        tf2 = {nr:[1],dr[1,0]}x
        """
        nr = add(
            convolve(self.nr, other.dr),
            convolve(other.nr, self.dr)
        )
        dr = convolve(self.dr, other.dr)

        return TF(nr=nr,dr=dr)
    
    def __sub__(self, other:TF) -> TF:
        nr = subtract(
            convolve(self.nr, other.dr),
            convolve(other.nr, self.dr)
        )
        dr = convolve(self.dr, other.dr)

        return TF(nr=nr,dr=dr)
    
    def  __invert__(self) -> TF:
        """
        (tf) => 1 / tf
        """
        return TF(nr=self.dr,dr=self.nr)

    def __truediv__(self, other:TF) -> TF:
        nr = convolve(self.nr, other.dr)
        dr = convolve(self.dr, other.nr)

        return TF(nr=nr, dr=dr)

one = TF(nr=[1],dr=[1])
neg_one = TF(nr=[-1],dr=[1])

if __name__=="__main__":
    p1 = TF(nr=[1,2,3],dr=[4,5,6])
    p2 = TF(nr=[1,2,3],dr=[4,5,6])
    print(p1*p2+p1*p2)
    print(p1*p2)
    print(~p1)