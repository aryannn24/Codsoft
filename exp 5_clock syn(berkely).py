import random 
 
class Node: 
    def __init__(self, node_id, clock_time): 
        self.node_id = node_id 
        self.clock_time = clock_time  # In seconds 
        self.offset = 0 
 
    def __str__(self): 
        return f"Node {self.node_id}: Clock = {self.clock_time + self.offset:.2f} sec" 
 
class BerkeleyClockSync: 
    def __init__(self, nodes): 
        self.nodes = nodes 
        self.master = nodes[0]  # First node is the master 
 
    def synchronize(self): 
        print("       Clock Times Before Synchronization:") 
        for node in self.nodes: 
            print(node) 
 
        total_time = 0 
        active_nodes = 0 
        offsets = [] 
 
        # Master collects time differences 
        for node in self.nodes: 
            if node != self.master: 
                delay = random.uniform(0.1, 0.5)  # Simulate network delay 
                difference = node.clock_time - self.master.clock_time - delay 
                offsets.append((node, difference)) 
                total_time += node.clock_time 
                active_nodes += 1 
 
        # Include master's time too 
        total_time += self.master.clock_time 
        active_nodes += 1 
        average_time = total_time / active_nodes 
 
        # Set master offset 
        self.master.offset = average_time - self.master.clock_time 
 
        # Adjust other nodes 
        for node, diff in offsets: 
            node.offset = average_time - node.clock_time 
 
        print("\\n   Clock Times After Synchronization:") 
        for node in self.nodes: 
            print(node) 
 
# Example Usage 
if __name__ == "__main__": 
    nodes = [ 
        Node(1, 10.5), 
        Node(2, 12.8), 
        Node(3, 9.6), 
        Node(4, 11.0) 
    ] 
 
    sync = BerkeleyClockSync(nodes) 
    sync.synchronize()