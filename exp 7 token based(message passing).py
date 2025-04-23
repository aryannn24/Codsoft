import time

class Node:
    def __init__(self, node_id, ring):
        self.node_id = node_id
        self.ring = ring  # This should be the list of nodes
        self.token = False
        self.request_CS = False
        self.in_critical_section = False

    def __str__(self):
        return f"Node {self.node_id} [{'Token' if self.token else 'No Token'}]"

    def request_critical_section(self):
        print(f"Node {self.node_id} is requesting the critical section.")
        self.request_CS = True

    def enter_critical_section(self):
        if self.token and self.request_CS:
            self.in_critical_section = True
            print(f"Node {self.node_id} is entering the critical section.")
            time.sleep(1)
            print(f"Node {self.node_id} has exited the critical section.")
            self.in_critical_section = False
            self.request_CS = False

    def receive_token(self):
        if self.request_CS and not self.in_critical_section:
            print(f"Node {self.node_id} has received the token.")
            self.enter_critical_section()

    def pass_token(self):
        if self.token and not self.in_critical_section:
            print(f"Node {self.node_id} has the token and will pass it.")
            self.token = False
            next_node = self.ring[(self.node_id + 1) % len(self.ring)]
            next_node.token = True
            print(f"Token passed to Node {next_node.node_id}")
            return next_node
        return self


class TokenRing:
    def __init__(self, total_nodes):
        self.nodes = [Node(i, None) for i in range(total_nodes)]
        for node in self.nodes:
            node.ring = self.nodes
        self.token_index = 0
        self.nodes[self.token_index].token = True

    def show_status(self):
        print("\nCurrent Ring Status:")
        for node in self.nodes:
            print(node)
        print()

    def start_token_pass(self):
        for _ in range(20):
            current_node = self.nodes[self.token_index]
            if current_node.token:
                current_node.receive_token()
            next_node = current_node.pass_token()
            self.token_index = next_node.node_id
            self.show_status()
            time.sleep(1)


if __name__ == "__main__":
    ring = TokenRing(5)
    ring.show_status()

    # Request CS for nodes
    ring.nodes[1].request_critical_section()
    ring.nodes[4].request_critical_section()

    ring.start_token_pass()
