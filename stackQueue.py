from collections import deque
q = deque([])

def enQueue(x):
    q.append(x)
    
def deQueue():
    if len(q) == 0:
        print("Empty Queue!! Deletion is not possible")
        return
    q.popleft()

def display():
    if len(q) == 0:
        print("Empty Queue!!")
        return
    for i in q:
        print(i,end=" ")
    print()
