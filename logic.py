from kanren import run, var, fact
from kanren.assoccomm import eq_assoccomm as eq
from kanren.assoccomm import commutative, associative
addition = 'add'
multiplication = 'mul'
fact(commutative, multiplication)
fact(commutative, addition)
fact(associative, multiplication)
fact(associative, addition)
x, y = var('a'), var('b')
OriginalPattern = (multiplication, (addition, 5, x), y)
ex1 = (multiplication, 2, (addition, 5, 3))
ex2 = (addition,5,(multiplication,8,1))
print(run(0, (x,y), eq(ex1,OriginalPattern)))
print(run(0, (x,y), eq(ex2, OriginalPattern)))


*output*
((3, 2), (3, 2))
()