l = []

def push(x):
    l.append(x)

def pop():
    if len(l) == 0:
        print("List is empty!! Deletion is not possible")
        return
    l.pop()

def display():
    if len(l) == 0:
        print("List is empty")
        return

    for i in list(reversed(l)):
        print(i)
