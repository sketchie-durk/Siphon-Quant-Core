
import time
from typing import Dict

class HealthMonitor:
    """
    Institutional Heartbeat Monitor.
    Tracks the liveness of all data feeders and strategies.
    """
    def __init__(self, heartbeat_threshold: float = 5.0):
        self.heartbeat_threshold = heartbeat_threshold
        self.last_heartbeats: Dict[str, float] = {}

    def record_heartbeat(self, component_id: str):
        self.last_heartbeats[component_id] = time.time()

    def check_health(self) -> List[str]:
        """
        Returns a list of components that have stopped emitting heartbeats.
        """
        now = time.time()
        dead_components = []
        for cid, last_time in self.last_heartbeats.items():
            if now - last_time > self.heartbeat_threshold:
                dead_components.append(cid)
        return dead_components

    def monitor_loop(self):
        # In a real system, this would be an async task
        while True:
            dead = self.check_health()
            if dead:
                print(f"[CRITICAL] Heartbeat lost for: {dead}")
            time.sleep(1)
