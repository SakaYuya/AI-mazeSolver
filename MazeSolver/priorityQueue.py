# Priority queue - preferences https://www.geeksforgeeks.org/priority-queue-in-python/
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
 
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
 
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
 
    # for inserting an element in the queue
    def push(self, data):
        self.queue.append(data)
 
    # for popping an element based on Priority
    def pop(self):
        try:
            min_val = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min_val]:
                    min_val = i
            item = self.queue[min_val]
            del self.queue[min_val]
            return item
        except IndexError:
            print()
            exit()

    def __len__(self):
        return len(self.queue)

    def get(self, i):
        return self.queue[i]