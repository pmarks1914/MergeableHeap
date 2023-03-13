import heapq

class MergeableHeap:
    def __init__(self):
        self.heap = []
        
    def insert(self, val):
        heapq.heappush(self.heap, val)
        
    def merge(self, other):
        self.heap = list(heapq.merge(self.heap, other.heap))
        
    def find_min(self):
        if len(self.heap) > 0:
            return self.heap[0]
        else:
            return None
        
    def replace_root(self, new_val):
        if len(self.heap) > 0:
            heapq.heapreplace(self.heap, new_val)
        else:
            self.insert(new_val)
        
    def visualize(self):
        def print_tree(heap, i):
            if i < len(heap):
                print_tree(heap, 2 * i + 2)
                print(' ' * 4 * i + f'{heap[i]}')
                print_tree(heap, 2 * i + 1)
        
        print_tree(self.heap, 0)

    # Delete min 
    def deleteMin(self):
        for i in range(len(self.heap)):
            if i > 0:
                newList.insert(self.heap[i])
        print("After delete min")
        newList.visualize()

heap1 = MergeableHeap()
heap2 = MergeableHeap()
newList = MergeableHeap()

# Insert elements into the first heap
num_elements = int(input('Enter the number of elements to insert to heap 1: '))
for i in range(num_elements):
    val = int(input(f'Enter element {i+1}: '))
    heap1.insert(val)

# Insert elements into the second heap
num_elements2 = int(input('Enter the number of elements to insert to heap 2: '))
for i in range(num_elements2):
    val = int(input(f'Enter element {i+1}: '))
    heap2.insert(val)

# Merge the two heaps
heap1.merge(heap2)

# Find the minimum element
min_val = heap1.find_min()
print(f"The minimum element is: {min_val}")


# Visualize the heap
print("The heap looks like this:")
# print(self.heap)
heap1.visualize()
heap1.deleteMin()
