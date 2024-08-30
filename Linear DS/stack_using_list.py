# stack of size 5
stack = [None] * 10      

# declare top of the stack
top = -1 

# push ( inserting elements in stack )
def push():
    global top
    if top == len(stack) -1:
        print("stack is full")
    else:
        top = top + 1
        push = input("Enter the element to push : ")
        stack[top] = push



# POP ( Deleting the element in a stack )
def pop():
    global top
    if top == -1:
        print(" stack is empty ")
    else:
        print("element popped from stack is : ", stack[top])
        top = top -1


# Display the stack 
def Display():
    global top
    if top == -1:
        print("the stack is empty")
    else:
        print("Stack is : ")
        for i in range(top, -1, -1):   
            print(stack[i],end=" ")
            print()
        
# main function
def main():
    while True:
        print("1. Push")
        print("2. Pop")
        print("3. Diplay")
        print("4. Exit")
        choice = int(input("Enter your choice : "))
        if choice == 1:
            push()
        elif choice == 2:
            pop()
        elif choice == 3:
            Display()
        elif choice == 4:
            break
        else:
            print("invalid choice") 
 
# call the main function 
if __name__ == "__main__":
    main()
