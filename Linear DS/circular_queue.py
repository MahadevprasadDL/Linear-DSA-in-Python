class CircularQueue:
    def __init__(self, size):
        self.queue = [None] * size
        self.size = size
        self.front = self.rear = -1

    def enqueue(self):
        if (self.rear + 1) % self.size == self.front:
            print("Circular Queue is full")
        else:
            element = input("Enter the element to be inserted: ")
            if self.front == -1:
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
            print(element, "is inserted into the circular queue")

    def dequeue(self):
        if self.front == -1:
            print("Circular Queue is empty.")
        else:
            print("Removed element:", self.queue[self.front])
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.size

    def display(self):
        if self.front == -1:
            print("Circular Queue is empty.")
        elif self.rear >= self.front:
            print("Circular Queue:", self.queue[self.front : self.rear + 1])
        else:
            print("Circular Queue:", self.queue[self.front:] + self.queue[:self.rear + 1])

cq = CircularQueue(5)

# Example usage (integrate this with your loop)
while True:
    print("Select the operation: 1. ADD 2. REMOVE 3. DISPLAY 4. EXIT")
    choice = int(input())
    if choice == 1:
        cq.enqueue()
    elif choice == 2:
        cq.dequeue()
    elif choice == 3:
        cq.display()
    elif choice == 4:
        break
    else:
        print("Invalid choice.")
