import asyncio
import time
import json
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] Pulse-Matrix: %(message)s")

class PulseMatrixEngine:
    def __init__(self, config_path: str = "config.json"):
        self.config = self._load_config(config_path)
        self.host = self.config["server"]["host"]
        self.port = self.config["server"]["port"]
        self.buffer_size = self.config["routing"]["buffer_size"]
        self.metrics: Dict[str, Any] = {
            "packets_routed": 0,
            "total_bytes": 0,
            "avg_latency_ms": 0.0
        }

    def _load_config(self, path: str) -> Dict[str, Any]:
        try:
            with open(path, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            logging.warning("Config file not found. Falling back to default parameters.")
            return {
                "server": {"host": "0.0.0.0", "port": 9090},
                "routing": {"buffer_size": 8192}
            }

    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter) -> None:
        start_time = time.perf_counter()
        
        try:
            while True:
                data = await reader.read(self.buffer_size)
                if not data:
                    break
                
                processed_data = self._optimize_stream_packet(data)
                
                writer.write(processed_data)
                await writer.drain()
                
                elapsed = (time.perf_counter() - start_time) * 1000
                self._update_metrics(len(data), elapsed)
                
        except asyncio.CancelledError:
            pass
        finally:
            writer.close()
            await writer.wait_closed()

    def _optimize_stream_packet(self, packet: bytes) -> bytes:
        return packet

    def _update_metrics(self, size: int, latency: float) -> None:
        self.metrics["packets_routed"] += 1
        self.metrics["total_bytes"] += size
        self.metrics["avg_latency_ms"] = (self.metrics["avg_latency_ms"] + latency) / 2

    async def launch(self) -> None:
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        logging.info(f"Pulse-Matrix core active on {self.host}:{self.port} with buffer size {self.buffer_size}.")
        async with server:
            await server.serve_forever()

if __name__ == "__main__":
    engine = PulseMatrixEngine()
    try:
        asyncio.run(engine.launch())
    except KeyboardInterrupt:
        logging.info("Pulse-Matrix core safely suspended by Director.")
