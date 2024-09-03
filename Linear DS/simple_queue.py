queue = []

def enqueue():      # insert 
    element = input("Enter the element to be inserted: ")
    queue.append(element)
    print(element, "is inserted into the queue")


def dequeue():  # delete
    if not queue:
        print("Queue is empty.")
    else:
        e = queue.pop(0)    
        print("Removed element:", e)


def display():    # display
    if not queue:
        print("Queue is empty.")
    else:
        print("Queue:", queue)


while True:
    print("Select the operation: 1. ADD 2. REMOVE 3. DISPLAY 4. EXIT")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
