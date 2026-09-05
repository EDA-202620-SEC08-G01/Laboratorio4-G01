from DataStructures.Stack import stack as st

def new_stack():
    stack = st.new_stack()
    return stack
    
    
def push(my_stack,element):    
    my_stack = st.push(my_stack, element)
    return my_stack


def pop(my_stack):
    elemento = st.pop(my_stack)
    return elemento
    

def is_empty(my_stack):
    return(st.is_empty(my_stack))
    

# peek() = top()
def peek(my_list):
    elemento = st.top(my_list)
    return elemento

