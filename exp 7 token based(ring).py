import time 
 
class Node: 
    def __init__(self, node_id): 
        self.node_id = node_id 
        self.has_token = False 
        self.request_CS = False  # Wants to enter critical section 
 
    def __str__(self): 
        status = "has token" if self.has_token else "no token" 
        return f"Node {self.node_id} [{status}]" 
 
    def enter_critical_section(self): 
        print(f"    Node {self.node_id} is entering the critical section...") 
        time.sleep(1)  # Simulate time spent in critical section 
        print(f"    Node {self.node_id} has exited the critical section.") 
 
class TokenRing: 
    def __init__(self, total_nodes): 
        self.nodes = [Node(i) for i in range(total_nodes)] 
        self.token_index = 0 
        self.nodes[self.token_index].has_token = True  # Token starts with node 0 
 
    def request_critical_section(self, node_id): 
        self.nodes[node_id].request_CS = True 
 
    def pass_token(self): 
        current_node = self.nodes[self.token_index] 
        if current_node.request_CS: 
            current_node.enter_critical_section() 
            current_node.request_CS = False 
 
        # Pass token to next node 
        current_node.has_token = False 
        self.token_index = (self.token_index + 1) % len(self.nodes) 
        next_node = self.nodes[self.token_index] 
        next_node.has_token = True 
        print(f"    Token passed to Node {next_node.node_id}") 
 
    def show_status(self): 
        for node in self.nodes: 
            print(node) 
        print() 
 
# Example Usage 
if __name__ == "__main__": 
    ring = TokenRing(5) 
    ring.show_status() 
 
    # Request CS from Node 2 and Node 4 
    ring.request_critical_section(2) 
    ring.request_critical_section(4) 
 
    # Run the ring for a few rounds 
    for _ in range(10): 
        ring.pass_token() 
        time.sleep(0.5)