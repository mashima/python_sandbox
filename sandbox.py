from collections import namedtuple
import copy

#intelli-sense is enabled for named tuple 
Item = namedtuple('Item', ('title', 'url', 'user', 'body'))
item = Item('hoge', 'https://' , 'massy', 'bobobobo')
print(item)

import dataclasses

@dataclasses.dataclass(frozen=False) # frozen ~= immutable
class User:
    name: str
    age: int = 0
    def print_id(self):
        """check IDs of self and members"""
        print(f"self:{id(self)}, name:{id(self.name)}, age:{id(self.age)}")

hoge=User('name', 12)
fuga=copy.copy(hoge) #shallow copy

hoge.print_id()
fuga.print_id()

#data classes are compaired by its values
print(f"1. hoge == fuga : {hoge==fuga}") 

fuga.name="fuga"
fuga.age=2
print(f"1. hoge == fuga(modified)) : {hoge==fuga}")

fuga2=copy.deepcopy(fuga) #deep copy
fuga2.print_id()

#List-comprehensions create a list
def createEvenList(r1 : int, r2 : int) -> list[int] :
    return [item for item in filter(lambda x: x % 2 == 0, range(r1, r2+1))]

foo = createEvenList(1,20)
# print([i+2 for i in range(10) if i%2])
# print([i for i in filter(lambda x: x%2==0, range(10))])

# generator create iterator (replace LC "[]" to "()" "])
iter = (i for i in filter(lambda x: x%2==0, range(10)))
print (iter) # iterator (lazy)
print (list(iter)) # list with actual values (not lazy)