from __future__ import annotations
from typing import List
from pydantic import BaseModel

class Polynomial(BaseModel):
    coffs: List[float|int]

    def __str__(self) -> str:
        return str(self.coffs)
    
    def __repr__(self) -> str:
        return f"Polynomial(coffs={self.coffs})"

    def convolve(self, other:Polynomial) -> Polynomial:
        """
        [1,1] * [1,1] = [1,2,1]
        """
        res = [0] * (len(self.coffs)+len(other.coffs)-1)
        for i, ai in enumerate(self.coffs):
            for j, bj in enumerate(other.coffs):
                res[i + j] += ai * bj
        return Polynomial(coffs=res)

    def __mul__(self, other:Polynomial|int|float) -> Polynomial:
        if isinstance(other, Polynomial):
            return self.convolve(other)
        elif isinstance(other, (int,float)):
            res = [i*other for i in self.coffs]
            return Polynomial(coffs=res)
        return NotImplemented

    def __rmul__(self, other: int | float) -> Polynomial:
        return self * other
    
    def __sub__(self, other:Polynomial) -> Polynomial:
        """
        [1,1,1] - [1,1] = [1,0,0]
        """
        max_len = max(len(self.coffs), len(other.coffs))
        a = [0]*(max_len-len(self.coffs)) + self.coffs
        b = [0]*(max_len-len(other.coffs)) + other.coffs
        res = [x-y for x,y in zip(a,b)]
        return Polynomial(coffs=res)
    
    def __add__(self, other:Polynomial) -> Polynomial:
        """
        [1,1] + [1,1,1] = [1,2,2]
        """
        max_len = max(len(self.coffs), len(other.coffs))
        a = [0] * (max_len - len(self.coffs)) + self.coffs
        b = [0] * (max_len - len(other.coffs)) + other.coffs
        res = [x + y for x, y in zip(a, b)]
        return Polynomial(coffs = res)


