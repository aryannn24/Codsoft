import time

class Server:
    def __init__(self, server_id):
        self.server_id = server_id
        self.load = 0  # Number of requests handled by the server

    def __str__(self):
        return f"Server {self.server_id} [Load: {self.load}]"

    def process_request(self):
        """Simulate processing a request."""
        self.load += 1
        print(f"Server {self.server_id} is processing request. Total load: {self.load}")
        time.sleep(0.5)  # Simulate processing time


class LoadBalancer:
    def __init__(self, servers):
        self.servers = servers
        self.index = 0

    def get_next_server(self):
        """Select the next server in round-robin fashion."""
        server = self.servers[self.index]
        self.index = (self.index + 1) % len(self.servers)  # Ensure circular rotation
        return server

    def distribute_requests(self, num_requests):
        """Distribute incoming requests to servers using Round Robin."""
        print(f"\nDistributing {num_requests} requests:")
        for _ in range(num_requests):
            server = self.get_next_server()
            server.process_request()

    def show_server_status(self):
        """Show the current load on each server."""
        print("\nServer Status:")
        for server in self.servers:
            print(server)


# Example Usage
if __name__ == "__main__":
    servers = [Server(i) for i in range(1, 4)]  # 3 servers
    load_balancer = LoadBalancer(servers)

    load_balancer.show_server_status()

    # Simulate distributing 10 requests to the servers
    load_balancer.distribute_requests(10)

    # Show final load on each server
    load_balancer.show_server_status()
