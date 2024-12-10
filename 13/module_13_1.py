import asyncio
from time import sleep


async def start_strongman(name, power):
    num = 1
    print(f'Силач {name} начал соревнования.')
    while num <= 5:
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {num}')
        num += 1
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vadim', 10))
    task2 = asyncio.create_task(start_strongman('Dima', 8))
    task3 = asyncio.create_task(start_strongman('Asya', 6))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
