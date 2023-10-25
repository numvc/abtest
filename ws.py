import time
import pickle
import asyncio
from aio_binance.futures.usdt import WsClient

SYMBOL = 'BTCUSDT'
CONNECTION_AMOUNT = 5
DURATION_SEC = 60
PICKLE_FILENAME = 'pickle_data.pkl'
ws_data = []


async def callback_handler(message: dict):
    receive_time = time.time() * 1000
    current_connection = asyncio.current_task().get_name().replace("Task", "connection")
    ws_data.append({
        "receive_time": receive_time,
        "connection_name": current_connection,
        "raw_data": message,
    })
    print(current_connection + ' end')


async def main():
    tasks = []
    for i in range(CONNECTION_AMOUNT):
        tasks.append(
            asyncio.create_task(
                WsClient().stream_book_ticker(SYMBOL, callback_handler)
            )
        )

    await asyncio.sleep(DURATION_SEC)

    for task in tasks:
        task.cancel()

    with open(PICKLE_FILENAME, 'wb') as pick:
        pickle.dump(ws_data, pick)


asyncio.run(main())
