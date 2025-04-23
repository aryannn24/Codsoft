import time

class WeightedServer:
    def __init__(self, server_id, weight):
        self.server_id = server_id
        self.weight = weight
        self.load = 0

    def __str__(self):
        return f"Server {self.server_id} [Weight: {self.weight}, Load: {self.load}]"

    def process_request(self):
        self.load += 1
        print(f"Server {self.server_id} (Weight {self.weight}) is processing request. Total load: {self.load}")
        time.sleep(0.5)

class WeightedLoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.current_index = 0
        self.current_weight_count = 0

    def get_next_server(self):
        while True:
            server = self.servers[self.current_index]
            if self.current_weight_count < server.weight:
                self.current_weight_count += 1
                return server
            else:
                self.current_index = (self.current_index + 1) % len(self.servers)
                self.current_weight_count = 0

    def distribute_requests(self, num_requests):
        print(f"\nDistributing {num_requests} requests (Weighted Round Robin):")
        for _ in range(num_requests):
            server = self.get_next_server()
            server.process_request()

    def show_server_status(self):
        print("\nServer Status:")
        for server in self.servers:
            print(server)

# Example usage
if __name__ == "__main__":
    servers = [WeightedServer(i, weight) for i, weight in enumerate([2, 1, 3], start=1)]
    load_balancer = WeightedLoadBalancer(servers)

    load_balancer.show_server_status()
    load_balancer.distribute_requests(10)
    load_balancer.show_server_status()