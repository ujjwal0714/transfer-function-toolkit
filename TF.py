from __future__ import annotations
from typing import List
from pydantic import BaseModel
from polynomial import Polynomial


    


class TF(BaseModel):
    nr: Polynomial
    dr: Polynomial

    model_config = {
        "frozen": True
        }

    def __repr__(self) -> str:
        return super().__repr__()
    
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