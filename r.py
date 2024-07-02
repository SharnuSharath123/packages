# approach 1
import p
import q

p.fly()
p.color()
p.behaviour()

q.fly()
q.color()
q.behaviour()

# approach 2
from p import *
fly()
color()
behaviour()

from q import *
fly()
color()
behaviour()