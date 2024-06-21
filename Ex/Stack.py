
stack = []

for i in range(5):
    stack.append(i)
    print("Stack: {}".format(stack))
    
for i in range(5):
    print("Pop: {}".format(stack.pop()))
    print("Stack: {}".format(stack))