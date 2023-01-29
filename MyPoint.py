from __future__ import annotations # needed to use self type annotation
import dataclasses as dc
import math
import unittest

@dc.dataclass(frozen=False) #make the class mutable
class MyPoint:
    x : float
    y : float
    def distance_of(self, other: MyPoint) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

def main():
    pass

if __name__ == "__main__":
    # execute only if run as a script
    main()