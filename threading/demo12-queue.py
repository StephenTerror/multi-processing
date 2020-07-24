import queue

q = queue.PriorityQueue()
# put进入一个元组,元组的第一个元素是优先级(通常是数字,也可以是非数字之间的比较),数字越小优先级越高
q.put((2, 'a'))
q.put((1, 'b'))
q.put((3, 'c'))

print(q.get())
print(q.get())
print(q.get())

# 如果是字符，按照ASCII表来排序
q.put(('a', "sfsja"))
q.put(('b', "sdfsdf"))
q.put(('A', "sdfsdf"))
q.put(('ae', "sdfsdf"))
q.put(('ab', "sdfsdf"))
print(q.get())
print(q.get())
print(q.get())
print(q.get())
print(q.get())
