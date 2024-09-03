import heapq

priority_queue = []

def enqueue_priority():
    element = int(input("Enter the element to be inserted: "))
    priority = int(input("Enter the priority (lower number means higher priority): "))
    heapq.heappush(priority_queue, (priority, element))
    print(f"Element {element} with priority {priority} is inserted into the priority queue.")

def dequeue_priority():
    if not priority_queue:
        print("Priority Queue is empty.")
    else:
        priority, element = heapq.heappop(priority_queue)
        print(f"Removed element: {element} with priority {priority}")

def display_priority():
    if not priority_queue:
        print("Priority Queue is empty.")
    else:
        print("Priority Queue:", sorted(priority_queue))

# Example usage (integrate this with your loop)
while True:
    print("Select the operation: 1. ADD 2. REMOVE 3. DISPLAY 4. EXIT")
    choice = int(input())
    if choice == 1:
        enqueue_priority()
    elif choice == 2:
        dequeue_priority()
    elif choice == 3:
        display_priority()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
