class Stack:
    def __init__(self, size):
        self.items = [] ;
        self.size = size
        self.indx=-1

    def is_empty(self):
        if stack.indx == -1:
            return True
        return False



    def is_full(self):
        if stack.indx== stack.size-1 :
            return True
        return False

    def push(self, data):
        if not self.is_full():
            # Write code here
            stack.items.append(data)
            stack.indx=stack.indx+1

    def pop(self):
        if not self.is_empty():
            # Write code here
            stack.items.pop()
            stack.indx=stack.indx-1

    def status(self):
        for i in range(0, len(stack.items)):
             print(stack.items[i],end="\n")
             

# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
