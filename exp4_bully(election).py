class Process: 
    def __init__(self, pid): 
        self.pid = pid 
        self.active = True 
 
    def __str__(self): 
        return f"Process {self.pid} [{'Active' if self.active else 'Down'}]" 
 
class BullyElection: 
    def __init__(self, process_ids): 
        self.processes = [Process(pid) for pid in process_ids] 
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
                    print("       Coordinator is down! Election needed.") 
                break 
 
    def hold_election(self, initiator_pid): 
        initiator = next((p for p in self.processes if p.pid == initiator_pid), None) 
        if not initiator or not initiator.active: 
            print("  Initiator process not active.") 
            return 
 
        print(f"\\n       Election initiated by Process {initiator_pid}") 
        higher_processes = [p for p in self.processes if p.pid > initiator_pid and p.active] 
 
        if not higher_processes: 
            self.coordinator = initiator 
            print(f"   Process {initiator_pid} becomes the new coordinator!") 
        else: 
            for p in higher_processes: 
                print(f"         Process {initiator_pid} sends election message to Process {p.pid}") 
            max_proc = max(higher_processes, key=lambda p: p.pid) 
            self.coordinator = max_proc 
            print(f"      Process {max_proc.pid} becomes the new coordinator!") 
 
    def activate_process(self, pid): 
        for p in self.processes: 
            if p.pid == pid: 
                p.active = True 
                print(f"    Process {pid} is now active.") 
                break 
 
# Example usage 
if __name__ == "__main__": 
    system = BullyElection([1, 2, 3, 4, 5]) 
    system.display_status() 
 
    system.deactivate_process(5)  # Simulate coordinator crash 
    system.hold_election(2)       # Process 2 initiates election 
    system.display_status()