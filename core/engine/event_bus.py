
import asyncio
from typing import Callable, Dict, List, Any
from dataclasses import dataclass

@dataclass
class Event:
    type: str
    data: Any

class EventBus:
    """
    Asynchronous event bus for low-latency signal propagation.
    Wall Street standard: Decouples data ingestion from signal execution.
    """
    def __init__(self):
        self.subscribers: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, callback: Callable):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    async def emit(self, event: Event):
        if event.type in self.subscribers:
            tasks = [callback(event) for callback in self.subscribers[event.type]]
            await asyncio.gather(*tasks)

# Example of an async engine using the bus
class AsyncLogicEngine:
    def __init__(self, bus: EventBus):
        self.bus = bus
        self.bus.subscribe("MARKET_DATA", self.on_market_data)

    async def on_market_data(self, event: Event):
        # Logic for processing high-frequency data
        print(f"[LOGIC] Processing data for {event.data['asset']}... ")
        # If signal detected -> self.bus.emit(Event("SIGNAL", ...))
