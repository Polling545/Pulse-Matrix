# Pulse-Matrix

[![Pulse-Matrix CI Test](https://github.com/Polling545/Pulse-Matrix/actions/workflows/ci_test.yml/badge.svg)](https://github.com/Polling545/Pulse-Matrix/actions/workflows/ci_test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

High-concurrency async streaming gateway and core engine built with Python's standard `asyncio` library.

---

## 🚀 Features

- **High Concurrency**: Built on non-blocking TCP packet routing powered by Python's native `asyncio`.
- **Configurable Architecture**: Easily customize buffer sizes, timeouts, connection limits, and operational modes via JSON config.
- **Real-time Telemetry**: Built-in metric tracking for throughput, active packets, and latency.
- **Lifecycle Management**: Clean startup and graceful shutdown routines for enterprise-grade reliability.

---

## 📦 Quick Start

### 1. Configure
Ensure your `config.json` is set up in the root directory. You can copy the provided template to get started:
```bash
cp config.example.json config.json
```
2. Run the Server
Launch the core gateway engine:
```bash
python pulse_matrix_core.py
```
3. Run the Test Client (Demo Mode)
Simulate multi-client concurrent traffic and test packet round-trips:
```bash
python client_test.py
```

