import time
import logging

class SiphonTelemetry:
    def __init__(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
        self.logger = logging.getLogger("SiphonQuant")

    def log_latency(self, start_time: float, stage: str):
        latency = (time.time() - start_time) * 1000
        self.logger.info(f"[LATENCY] {stage}: {latency:.3f}ms")

    def log_signal(self, asset: str, signal_type: str, confidence: float):
        self.logger.info(f"[SIGNAL] {asset} -> {signal_type} (Conf: {confidence:.2f})")

    def log_error(self, error: Exception):
        self.logger.error(f"[CRITICAL] System Error: {str(error)}")
