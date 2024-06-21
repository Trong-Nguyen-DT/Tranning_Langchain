from queue import Queue

q = Queue(-1)

# for i in range(6):
#     print("----- Put -----")
#     print("Put: {}".format(i))
#     q.put(i)
#     print("----- Get -----")
#     while not q.empty():
#         print("===========")
#         gt = q.get()
#         print("Get: {}".format(gt))

print("----- Put -----")
for i in range(6):
    print("Put: {}".format(i))
    q.put(i)
    
print("----- Get -----")
while not q.empty():
    if q.qsize() == 3:
        print("===========")
        q.put(10)
        print("Size Top: {}".format(q.qsize()))
        gt = q.get()
        print("Size Bottom: {}".format(q.qsize()))
        print("Get: {}".format(gt))
        break
    gt = q.get()
    print("Get: {}".format(gt))