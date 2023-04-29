import T_ARRAY

class Cir_Que():
    def __init__(self, size):
        self._cir_que = T_ARRAY.T_Array(size)
        self._front = self._back = 0
    
    def __call__(self):
        print("Front = ", self._front)
        print("Rear = ", self._back)
        self._cir_que()


    def getNumElement(self):
        return self._cir_que.getNumElement()

    # Q가 비었는지 확인하는 함수
    def isEmpty(self):
        if self._cir_que.empty():
            return True
        else:
            return False
        
    # Q가 가득 찼는지 확인하는 함수
    def isFull(self):
        if(self._back) == self._front:
            return True
        else:
            return False
        
    def sort(self, arg):
        self._cir_que.sort(arg)
    
    #Q에 하나를 추가하는 함수   
    def enqueue(self, element):
        if not self.isEmpty():
            if self.isFull():
                print("ERROR, Queue is Now Full")
                exit()
        
        self._cir_que.insert(self._back, element)
        self._back = (self._back + 1)%self._cir_que.getSize()

    # Q에서 하나를 빼오는 함수
    def dequeue(self):
        if self.isEmpty():
            print("ERROR, Que is Now Empty")
            return
        
        element = self._cir_que.remove(self._front)
        self._front = (self._front+1)%self._cir_que.getSize()
        return element
    
    def glance_output(self):
        output = self._cir_que.get_element(self._front)
        return output
    

class Queue():
    def __init__(self, size):
        self._queue= T_ARRAY.T_Array(size)
        self._output = 0
        self._back = 0
    
    def __call__(self):
        print("Rear = ", self._back)
        self._queue()

    def getNumElement(self):
        return self._queue.getNumElement()

    # Q가 비었는지 확인하는 함수
    def isEmpty(self):
        if self._queue.empty():
            return True
        else:
            return False
        
    # Q가 가득 찼는지 확인하는 함수
    def isFull(self):
        if(self._back) == self._queue.getSize():
            return True
        else:
            return False
        
    def sort(self, arg):
        self._queue.sort(arg)

    def glance_output(self):
        output = self._queue.get_element(self._output)
        return output
    
    #Q에 하나를 추가하는 함수   
    def enqueue(self, element):
        if not self.isEmpty():
            if self.isFull():
                print("ERROR, Queue is Now Full")
                exit()
        
        self._queue.insert(self._back, element)
        self._back = self._queue.getNumElement()

    # Q에서 하나를 빼오는 함수
    def dequeue(self):
        if self.isEmpty():
            print("ERROR, Que is Now Empty")
            return
    
        element = self._queue.remove(self._output)
        self._queue.rebalance()
        return element