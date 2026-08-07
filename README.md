# Pulse-Matrix

High-concurrency async streaming gateway and core engine built with Python's standard asyncio library.

## Features

Pulse-Matrix features high-concurrency non-blocking TCP packet routing, configurable buffer sizes, timeouts, and connection limits, built-in real-time telemetry and metric tracking for throughput and latency, alongside clean startup and graceful shutdown lifecycle management.

## Quick Start

### 1. Configure
Ensure your config.json is properly set up in the root directory (you can copy config.example.json as a reference):

{
  "server": {
    "host": "0.0.0.0",
    "port": 9090,
    "max_concurrency": 10000
  },
  "routing": {
    "mode": "async_stream",
    "buffer_size": 8192,
    "timeout_seconds": 30
  },
  "telemetry": {
    "enabled": true,
    "log_level": "INFO"
  }
}

### 2. Run the Server
python pulse_matrix_core.py

### 3. Run the Test Client (Demo Mode)
python client_test.py

## License
This project is licensed under the MIT License.
