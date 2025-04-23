class Message:
    def __init__(self, message_type, timestamp, site_id):
        self.message_type = message_type
        self.timestamp = timestamp
        self.site_id = site_id


class Site:
    def __init__(self, site_id):
        self.site_id = site_id
        self.requesting = False
        self.executing = False
        self.timestamp = 0
        self.deferred_queue = []
        self.replies_pending = set()

    def request_critical_section(self, sites):
        self.requesting = True
        self.timestamp += 1
        self.replies_pending = {site.site_id for site in sites if site.site_id != self.site_id}
        for site in sites:
            if site.site_id != self.site_id:
                request_message = Message("REQUEST", self.timestamp, self.site_id)
                self.send_message(request_message, site)
        self.wait_for_replies()

    def send_message(self, message, destination):
        print(f"Site {self.site_id} sends {message.message_type} message to Site {destination.site_id}")
        destination.receive_message(message, self)

    def receive_message(self, message, sender):
        print(f"Site {self.site_id} receives {message.message_type} message from Site {sender.site_id}")
        if message.message_type == "REQUEST":
            if not self.requesting and not self.executing:
                self.send_message(Message("REPLY", 0, self.site_id), sender)
            elif self.requesting and (message.timestamp < self.timestamp or
                                      (message.timestamp == self.timestamp and message.site_id < self.site_id)):
                self.deferred_queue.append((message, sender))
            else:
                self.send_message(Message("REPLY", 0, self.site_id), sender)
        elif message.message_type == "REPLY":
            self.replies_pending.discard(sender.site_id)
            if not self.replies_pending:
                self.executing = True
                print(f"Site {self.site_id} enters critical section.")

    def wait_for_replies(self):
        # This is a simulation; in a real system, you'd wait for messages asynchronously
        while self.replies_pending:
            pass  # Simulated blocking wait

    def release_critical_section(self, sites):
        self.requesting = False
        self.executing = False
        for message, sender in self.deferred_queue:
            self.send_message(Message("REPLY", 0, self.site_id), sender)
        self.deferred_queue.clear()
        print(f"Site {self.site_id} releases critical section.")


def main():
    number_of_sites = int(input("Enter the number of sites: "))
    sites = [Site(i + 1) for i in range(number_of_sites)]
    for site in sites:
        site.request_critical_section(sites)
        site.release_critical_section(sites)


if __name__ == "__main__":
    main()
