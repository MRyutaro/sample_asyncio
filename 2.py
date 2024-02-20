import asyncio
import time


async def hello_after(delay, name):
    await asyncio.sleep(delay)
    print(f"Hello, {name} at {time.strftime('%X')}")
    return name


async def main():
    print(f"started at {time.strftime('%X')}")
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(hello_after(1, "Taro"))
        task2 = tg.create_task(hello_after(2, "Jiro"))
        task3 = tg.create_task(hello_after(3, "Saburo"))
    print(task1)
    print(task1.result())
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())

# started at 11:02:25
# Hello, Taro at 11:02:26
# Hello, Jiro at 11:02:27
# Hello, Saburo at 11:02:28
# <Task finished name='Task-2' coro=<hello_after() done, defined at C:\Users\RECODE\Programs\sample_asyncio\2.py:5> result='Taro'>
# Taro
# finished at 11:02:28

# 3秒しかかかっていない。
