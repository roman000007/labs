from Queue.stack_to_queue import stack_to_queue
from Stack.queue_to_stack import queue_to_stack
from arraystack import ArrayStack
from arrayqueue import ArrayQueue

s = ArrayStack()
s.push(1)
s.push(2)
s.push(3)
q = stack_to_queue(s)
print(s)
print(q)


q = ArrayQueue()
q.add(1)
q.add(2)
q.add(3)
s = queue_to_stack(q)
print(s)
print(q)
print(s.pop())