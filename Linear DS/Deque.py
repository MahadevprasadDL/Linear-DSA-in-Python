from collections import deque

deque_queue = deque()

def enqueue_front():
    element = input("Enter the element to be inserted at front: ")
    deque_queue.appendleft(element)
    print(element, "is inserted at the front of the deque.")

def enqueue_rear():
    element = input("Enter the element to be inserted at rear: ")
    deque_queue.append(element)
    print(element, "is inserted at the rear of the deque.")

def dequeue_front():
    if not deque_queue:
        print("Deque is empty.")
    else:
        e = deque_queue.popleft()
        print("Removed element from front:", e)

def dequeue_rear():
    if not deque_queue:
        print("Deque is empty.")
    else:
        e = deque_queue.pop()
        print("Removed element from rear:", e)

def display_deque():
    if not deque_queue:
        print("Deque is empty.")
    else:
        print("Deque:", list(deque_queue))

# Example usage (integrate this with your loop)
while True:
    print("Select the operation: 1. ADD FRONT 2. ADD REAR 3. REMOVE FRONT 4. REMOVE REAR 5. DISPLAY 6. EXIT")
    choice = int(input())
    if choice == 1:
        enqueue_front()
    elif choice == 2:
        enqueue_rear()
    elif choice == 3:
        dequeue_front()
    elif choice == 4:
        dequeue_rear()
    elif choice == 5:
        display_deque()
    elif choice == 6:
        break
    else:
        print("Invalid choice.")
