import asyncio
import time


async def say_after(delay, what):
    print(f"prepare {what} at {time.strftime('%X')}")
    await asyncio.sleep(delay)
    print(f"{what} at {time.strftime('%X')}")
    return what


async def main():
    task1 = asyncio.create_task(say_after(1, 'hello'))
    task2 = asyncio.create_task(say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    await task1

    print(f"returned from await task1 at {time.strftime('%X')}")
    print(task1.result())

    await task2

    print(f"finished at {time.strftime('%X')}")
    print(task2.result())

asyncio.run(main())

# started at 11:03:39
# prepare hello at 11:03:39
# prepare world at 11:03:39
# hello at 11:03:40
# returned from await task1 at 11:03:40
# hello
# world at 11:03:41
# finished at 11:03:41
# world
# 2秒しかかかっていない。
