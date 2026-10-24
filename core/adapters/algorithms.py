
import asyncio
import time

class ExecutionAlgo:
    @staticmethod
    async def twap_execute(adapter, asset: str, total_amount: float, duration_seconds: int, chunks: int):
        chunk_size = total_amount / chunks
        interval = duration_seconds / chunks
        for i in range(chunks):
            print(f"[TWAP] Executing chunk {i+1}/{chunks}: {chunk_size} {asset}")
            await asyncio.sleep(interval)
