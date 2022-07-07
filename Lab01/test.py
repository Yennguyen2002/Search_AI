from queue import PriorityQueue
path=[]
visited={}
q = PriorityQueue()

visited[1] = 1
q.put((3, 1, [1,4,5])) 
q.put((0, 1, [1,4,5])) 
q.put((4, 1, [1,4,5])) 

print(q)
a = q.get()
print(q.qsize())