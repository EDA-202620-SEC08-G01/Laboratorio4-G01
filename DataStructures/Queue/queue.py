from DataStructures.Queue import queue as queue




def new_queue():
    queue = queue.new_queue()
    print(queue) 


    

def enqueue(my_queue, element):
    cola = queue.enqueue(my_queue, element)
    print(cola)
    


    
def dequeue(my_queue):
    elemento = queue.dequeue(my_queue)
    print(elemento) # Salida esperada: {'name': 'John', 'age': 25}
    print(my_queue)



def is_empty(my_queue):
    print(queue.is_empty(my_queue))



def peek(my_queue):
    elemento = queue.peek(my_queue)
    print(elemento) # Salida esperada: {'name': 'John', 'age': 25}
    print(my_queue)



def size(my_queue):
    print(queue.size(my_queue))
    