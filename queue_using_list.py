class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise IndexError ("queue underflow")
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError ("queue underflow")
    def get_rear(self):
        if not self.is_empty():
            return self.item[-1]
        else:
            raise IndexError ("queue underflow")
    def size(self):
        return len(self.items)
q1=Queue()
try:
    print(q1.get_front())
except IndexError as e:
    print(e.args[0])
 
q1.enqueue(10)
q1.enqueue(20)
print("front is",q1.get_front())

    
 

        



        
