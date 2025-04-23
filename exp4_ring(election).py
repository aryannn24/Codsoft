class RingProcess: 
    def __init__(self, pid): 
        self.pid = pid 
        self.active = True 
 
    def __str__(self): 
        return f"Process {self.pid} [{'Active' if self.active else 'Down'}]" 
 
class RingElection: 
    def __init__(self, process_ids): 
        self.processes = [RingProcess(pid) for pid in process_ids] 
        self.n = len(self.processes) 
        self.coordinator = max(self.processes, key=lambda p: p.pid) 
 
    def display_status(self): 
        for p in self.processes: 
            print(p) 
        print(f"\\n      Current Coordinator: Process {self.coordinator.pid}\\n") 
 
    def deactivate_process(self, pid): 
        for p in self.processes: 
            if p.pid == pid: 
                p.active = False 
                print(f"    Process {pid} is now down.") 
                if self.coordinator.pid == pid: 
                    print("       Coordinator is down! Election required.") 
                break 
 
    def activate_process(self, pid): 
        for p in self.processes: 
            if p.pid == pid: 
                p.active = True 
                print(f"    Process {pid} is now active.") 
                break 
 
    def hold_election(self, initiator_pid): 
        print(f"\\n       Ring Election initiated by Process {initiator_pid}") 
 
        if not any(p.pid == initiator_pid and p.active for p in self.processes): 
            print("  Initiator is not active.") 
            return 
 
        index = next(i for i, p in enumerate(self.processes) if p.pid == initiator_pid) 
        msg = [] 
 
        for i in range(self.n): 
            curr_index = (index + i) % self.n 
            curr_proc = self.processes[curr_index] 
            if curr_proc.active: 
                msg.append(curr_proc.pid) 
                print(f"    Passing through Process {curr_proc.pid}") 
 
        new_coordinator_pid = max(msg) 
        self.coordinator = next(p for p in self.processes if p.pid == new_coordinator_pid) 
        print(f"      New Coordinator is Process {self.coordinator.pid}") 
 
# Example Usage 
if __name__ == "__main__": 
    system = RingElection([1, 2, 3, 4, 5]) 
    system.display_status() 
 
    system.deactivate_process(5) 
    system.hold_election(2)  # Process 2 initiates the election 
    system.display_status()