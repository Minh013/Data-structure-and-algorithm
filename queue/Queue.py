max_size = 10
queue = [0]*max_size
front_value = 0
rear_value = -1
item_count = 0


def isEmpty():
    return item_count == 0


def isFully():
    return item_count == max_size

def enqueue(data):
    global rear_value, item_count
    if not isFully():
        if rear_value == max_size - 1:
            rear_value = - 1
        rear_value = rear_value + 1
        queue[rear_value] = data
        item_count + 1
    else:
        print("Queue is full")

def dequeue():
    global front_value, item_count
    if not isEmpty():
        date = queue[front_value]
        front_value = (front_value + 1) % max_size
        item_count -= 1
        return date

enqueue(4)
enqueue(5)
enqueue(6)
enqueue(8)
enqueue(10)
enqueue(11)
enqueue(12)
enqueue(13)
enqueue(14)
enqueue(15)
# enqueue(16)
print("Queue: ")
for i in range(max_size):
    print(queue[i], end=" ")

print("\nDequeue")
while not isEmpty():
    removed = dequeue()
    print(removed, end=" ")