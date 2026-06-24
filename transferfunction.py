from __future__ import annotations
from pydantic import BaseModel
from polynomial import Polynomial

class TF(BaseModel):
    nr: Polynomial
    dr: Polynomial

    model_config = {
        "frozen": True
        }

    def __str__(self) -> str:
        return f"{self.nr}/{self.dr}"
    
    def __mul__(self, other:TF) -> TF:
        """
        (tf1, tf2) => tf1 * tf2
        tf1 = {nr:[1],dr:[1,0]}
        tf2 = {nr:[1],dr:[1,0]}
        res = tf1 * tf2 = {nr:[1],dr[1 0 0]}
        """
        nr = self.nr * other.nr
        dr = self.dr * other.dr

        return TF(nr=nr,dr=dr)

    def __add__(self, other:TF) -> TF:
        """
        (tf1, tf2) => tf1 + tf2 => res = (nr1*dr2+nr2*dr1)/(dr1*dr2)
        tf1 = {nr:[1],dr[1,0]}
        tf2 = {nr:[1],dr[1,0]}x
        """
        nr = (self.nr * other.dr) + (other.nr * self.dr)
        dr = self.dr * other.dr

        return TF(nr=nr,dr=dr)
    
    def __sub__(self, other:TF) -> TF:
        nr = (self.nr * other.dr) - (other.nr * self.dr)
        dr = (self.dr * other.dr)

        return TF(nr=nr,dr=dr)
    
    def  __invert__(self) -> TF:
        """
        (tf) => 1 / tf
        """
        return TF(nr=self.dr,dr=self.nr)

    def __truediv__(self, other:TF) -> TF:
        nr = (self.nr * other.dr)
        dr = (self.dr * other.nr)

        return TF(nr=nr, dr=dr)

one = TF(
    nr=Polynomial(coffs=[1]),
    dr=Polynomial(coffs=[1])
    )

neg_one = TF(
    nr=Polynomial(coffs=[-1]),
    dr=Polynomial(coffs=[1])
    )
