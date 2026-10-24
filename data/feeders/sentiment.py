
import asyncio
import random

class SentimentFeeder:
    """
    Ingests social media and news sentiment using an LLM-based processor.
    """
    def __init__(self, assets: list, bus):
        self.assets = assets
        self.bus = bus

    async def stream(self):
        while True:
            for asset in self.assets:
                # Mocking LLM sentiment analysis result (-1.0 to 1.0)
                sentiment_score = random.uniform(-1, 1)
                data = {
                    'asset': asset,
                    'sentiment': sentiment_score,
                    'source': 'LLM_Aggregator',
                    'timestamp': asyncio.get_event_loop().time()
                }
                await self.bus.emit(Event("SENTIMENT_DATA", data))
            await asyncio.sleep(60) # Sentiment updates slower than price
