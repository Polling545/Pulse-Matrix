import asyncio
import json
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] Test-Client: %(message)s")

async def send_stream(host: str, port: int, client_id: int, payload: bytes, interval: float, count: int):
    try:
        reader, writer = await asyncio.open_connection(host, port)
        logging.info(f"Client {client_id} connected to server.")

        for i in range(count):
            writer.write(payload)
            await writer.drain()
            
            data = await reader.read(8192)
            logging.info(f"Client {client_id} sent/received packet {i+1}/{count} (Size: {len(payload)} bytes)")
            
            await asyncio.sleep(interval)

        writer.close()
        await writer.wait_closed()
        logging.info(f"Client {client_id} disconnected gracefully.")
    except Exception as e:
        logging.error(f"Client {client_id} connection error: {e}")

async def main():
    # 读取同级目录的 config.json 获取端口，或默认连接本地 9090
    host = "127.0.0.1"
    port = 9090
    try:
        with open("config.json", "r") as f:
            config = json.load(f)
            host = config["server"]["host"]
            if host == "0.0.0.0":
                host = "127.0.0.1"
            port = config["server"]["port"]
    except Exception:
        pass

    test_payload = b"X" * 1024  # 1KB 测试封包
    concurrency = 3           # 模拟 3 个并发客户端
    interval = 1.0            # 发送间隔 1 秒
    count = 10                # 每个客户端发送 10 次

    tasks = [
        send_stream(host, port, i + 1, test_payload, interval, count)
        for i in range(concurrency)
    ]
    
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Test client stopped.")
