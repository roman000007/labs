from arraystack import ArrayStack
import copy


def queue_to_stack(queue):
    stack = ArrayStack()
    new_queue = copy.deepcopy(queue)
    while not new_queue.isEmpty():
        stack.add(new_queue.pop())
    return stack
