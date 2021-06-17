import logging
import threading
import time

GLOBAL_VALUE = 0

def thread_function(name):
    print("Thread %s: starting", name)
    time.sleep(2)
    global GLOBAL_VALUE
    GLOBAL_VALUE = name
    print("Thread %s: finishing", name)

# if __name__ == "__main__":
#     x = threading.Thread(target=thread_function, args=(1,))
#     print('START Thread')
#     x.start()
#     print('CALCULATIONS')
#     x.join()
#     print('END Thread')

# if __name__ == "__main__":
#     start = time.time()
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     threads = list()
#     for index in range(3):
#         logging.info("Main    : create and start thread %d.", index)
#         x = threading.Thread(target=thread_function, args=(index,))
#         threads.append(x)
#         x.start()
#     index = 0
#     for thread in threads:
#         logging.info("Main    : before joining thread %d.", index)
#         thread.join()
#         logging.info("Main    : thread %d done", index)
#         index += 1
#     print(time.time() - start)
#     logging.info("Main    : threads Done")

# import concurrent.futures

# if __name__ == "__main__":
#     format = "%(asctime)s: %(message)s"
#     logging.basicConfig(format=format, level=logging.INFO,
#                         datefmt="%H:%M:%S")
#     with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
#         executor.map(thread_function, range(10))
#     print(GLOBAL_VALUE)

# class CustomThread(threading.Thread):
#     def __init__(self, limit):
#         threading.Thread.__init__(self)
#         self._limit = limit

#     def run(self):
#         for i in range(self._limit):
#             print(f"from CustomThread: {i}")
#             time.sleep(0.5)

# cth = CustomThread(3)
# cth.start()

# from threading import Thread, Lock
# from time import sleep
# lock = Lock()
# stop_thread = False
# def infinit_worker():
#     print("Start infinit_worker()")
#     while True:
#         print("--> thread work")
#         lock.acquire()
#         if stop_thread is True:
#            break
#         lock.release()
#         sleep(0.1)
#     print("Stop infinit_worker()")

# # Create and start thread
# th = Thread(target=infinit_worker)
# th.start()
# sleep(2)
# # Stop thread
# lock.acquire()
# stop_thread = True
# lock.release()

# import os
# from multiprocessing import Process
 

# GLOBAL_VALUE = 10


# def doubler(number):
#     """
#     Функция умножитель на два
#     """
#     global GLOBAL_VALUE
#     GLOBAL_VALUE = number
#     result = number * 2
#     proc = os.getpid()
#     print('{0} doubled to {1} by process id: {2}'.format(
#         number, result, proc))
 
 
# if __name__ == '__main__':
#     numbers = [5, 30, 15, 20, 25]
#     procs = []
    
#     for index, number in enumerate(numbers):
#         proc = Process(target=doubler, args=(number,))
#         procs.append(proc)
#         proc.start()
    
#     for proc in procs:
#         proc.join()

#     print(GLOBAL_VALUE)

# def simple_coroutine():
#   value = yield
#   print(value)
# coro = simple_coroutine()
# from_coro = next(coro)
# print(from_coro)
# coro.send(42)

# import random
# from time import sleep
# import asyncio


# def task(pid):
#     """Synchronous non-deterministic task.
#     """
#     sleep(0.05)
#     print('Task %s done' % pid)


# async def task_coro(pid):
#     """Coroutine non-deterministic task
#     """
#     await asyncio.sleep(0.05)
#     print('Task %s done' % pid)


# def synchronous():
#     for i in range(1, 100):
#         task(i)


# async def asynchronous():
#     tasks = [asyncio.ensure_future(task_coro(i)) for i in range(1, 100)]
#     await asyncio.wait(tasks)


# print('Synchronous:')
# start = time.time()
# synchronous()
# print(time.time() - start)

# print('Asynchronous:')
# start = time.time()
# ioloop = asyncio.get_event_loop()
# ioloop.run_until_complete(asynchronous())
# ioloop.close()
# print(time.time() - start)

# import aiohttp
# import asyncio
# import requests

# URL = 'https://api.github.com/events'
# MAX_CLIENTS = 3


# def parse_github():
#     response = requests.get(URL)
#     print("Status:", response.status_code)
#     print("Content-type:", response.headers['content-type'])

#     html = response.text
#     print("Body:", html[:15], "...")

# def sync_github():
#     start = time.time()
#     [parse_github() for _ in range(MAX_CLIENTS)]
#     print(time.time() - start)


# async def aparse_github():
#     async with aiohttp.ClientSession() as session:
#         async with session.get(URL) as response:

#             print("Status:", response.status)
#             print("Content-type:", response.headers['content-type'])

#             html = await response.text()
#             print("Body:", html[:15], "...")

# async def main():
#     start = time.time()
#     tasks = [asyncio.ensure_future(aparse_github()) for i in range(1, MAX_CLIENTS + 1)]
#     await asyncio.wait(tasks)
#     print(time.time() - start)


# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())

# sync_github()

from flask import Flask

app = Flask(__name__)

@app.route('/index/')
@app.route('/')
def index():
    return 'Hello Minsk'

@app.route('/check')
def check():
    print(asdlkfhas)

@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return "Profile page of user #{user}".format(user=user_id)

@app.route('/books/<genre>/')
def books(genre):
    return "All Books in {} category".format(genre)

@app.route('/homepage/')
def homepage():
    my_name = "Yan"
    location = "Minsk"
    return f"""
    <h1>Hello world</h1>
    <p>My first page</p>
    <p>My name is {my_name}</p>
    <p>I am {location}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)

# import asyncio
# import time

# loop = asyncio.get_event_loop()

# async def say_after(delay, what):
#     await asyncio.sleep(delay)
#     print(time.time(), what)
#     return what

# async def main():
#     task1 = asyncio.create_task(say_after(1, 'hello'))
#     task2 = asyncio.create_task(say_after(1, 'world'))
#     print(f"started at {time.strftime('%X')}")
#     time.sleep(3)
#     result1 = await task1
#     result2 = await task2
#     print(f"finished at {time.strftime('%X')}")

# asyncio.run(main())
