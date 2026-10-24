from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class OrderRequest:
    asset: str
    amount: float
    side: str 
    order_type: str 
    price: float = None

class BaseExecutionAdapter(ABC):
    @abstractmethod
    async def execute_order(self, request: OrderRequest) -> bool:
        pass

class BinanceAdapter(BaseExecutionAdapter):
    async def execute_order(self, request: OrderRequest) -> bool:
        print(f"[BINANCE] Sending {request.order_type} {request.side} order for {request.amount} {request.asset}...")
        return True

class UniswapAdapter(BaseExecutionAdapter):
    async def execute_order(self, request: OrderRequest) -> bool:
        print(f"[UNISWAP] Routing {request.amount} {request.asset} through V3 pools...")
        return True
