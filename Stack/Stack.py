max_size = 5
stack = [0]*max_size
top_value = -1

def is_full():
    if top_value == max_size -1:
        return True
    else:
        return False

def is_empty():
    if top_value == -1:
        return True
    else:
        return False

def pop():
    global top_value
    data = 0
    if is_empty() != 1:
        data = stack[top_value]
        top_value = top_value - 1
        return data
    else:
        print("Stack is full")
    return data

def push(data):
    global top_value
    if is_full() != 1:
        top_value = top_value + 1
        stack[top_value] = data
    else:
        print("Stack is full")
    return data

def peek():
    return stack[top_value]


push(1)
push(2)
push(3)
push(4)
push(5)
print("Stack's elements")
for i in range(max_size):
    print(stack[i], end= " ")
print("\n Element at top: ", peek())
print("Stack full", is_full())
print("Stack empty", is_empty())
# print("\n Elements are popped from stack")
# while is_empty() != 1:
#     data = pop()
#     print(data, end= " ")
