import random
import asyncio

class MockDataFeeder:
    def __init__(self, asset: str, bus):
        self.asset = asset
        self.bus = bus

    async def stream(self):
        while True:
            data = {
                'asset': self.asset,
                'price': random.uniform(30000, 60000),
                'rsi': random.uniform(20, 80),
                'sentiment': random.uniform(0, 1)
            }
            await self.bus.emit(Event("MARKET_DATA", data))
            await asyncio.sleep(1)
