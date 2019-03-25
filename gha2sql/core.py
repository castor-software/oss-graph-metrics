import os
import threading
from tqdm import tqdm

def create_dir(dir):
    """Create the dir if the dir does not exists
    """
    if not os.path.exists(dir):
        os.makedirs(dir)
    return dir


def multi_threading(queue, number_of_threads, task):
    pbar = tqdm(total=len(queue))
    def pop_queue():
        if len(queue) > 0:
            return queue.pop()
        return False
    result = {}
    def process():
        data = pop_queue()
        while data:
            result[data] = task(*data)
            pbar.update(1)
            data = pop_queue()
    threads = []
    for i in range(number_of_threads):
        threads.append(threading.Thread(target=process))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return result
