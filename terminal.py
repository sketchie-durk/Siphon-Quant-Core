
import asyncio
from core.engine.event_bus import EventBus, Event
from core.engine.logic import SiphonLogicEngine, Signal, SignalType
from core.telemetry.monitor import SiphonTelemetry

class SiphonTerminal:
    def __init__(self):
        self.bus = EventBus()
        self.engine = SiphonLogicEngine(self.bus)
        self.telemetry = SiphonTelemetry()
        self.bus.subscribe("SIGNAL", self.on_signal)

    async def on_signal(self, event: Event):
        print(f"\n🔔 SIGNAL ALERT: {event.data.asset} | {event.data.type} | Confidence: {event.data.confidence:.2f}")
        print(f"Reasoning: {event.data.reasoning}")
        print("--------------------------------------------------")

    async def run(self):
        print("==================================================")
        print("   SIPHON QUANT CORE | TERMINAL v1.0   ")
        print("==================================================")
        print("System Online. Listening for market events...")
        await self.bus.emit(Event("SIGNAL", Signal(asset="BTC", type=SignalType.LONG, confidence=0.85, reasoning="Z-Score Convergence")))
        while True:
            await asyncio.sleep(1)

if __name__ == "__main__":
    term = SiphonTerminal()
    asyncio.run(term.run())
