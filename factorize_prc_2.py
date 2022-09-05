from time import time, sleep
from multiprocessing import Pool, cpu_count


def calcul(slice_range):
    num, start, finish = slice_range
    res = []
    for counter in range(start, finish):
        if num % counter == 0:
            res.append(counter)
    return res


def callback(result):
    new_res = []
    for part in result:
        new_res += part
    print(f'Result in callback: {new_res}')


def factorize(*number):
    res_num = []
    for num in number:
        part_len = int(num / cpu_count())
        parts = []
        start, finish = 1, part_len
        for count in range(cpu_count() - 1):
            parts.append((num, start, finish))
            start = finish
            finish += part_len
        parts.append((num, start, num + 1))

        with Pool(cpu_count()) as p:
            p.map_async(calcul,
                        parts, callback=callback)
            p.close()
            p.join()
    return res_num


if __name__ == '__main__':
    time_array = []
    # print(f'Count CPU: {cpu_count()}')
    for _ in range(1000):
        timer = time()
        factorize(128, 255, 99999, 10651060)
        time_delta = time() - timer
        time_array.append(time_delta)
    # print(f'Program worked for {round(time_delta, 4)} sec')
    print(sum(time_array) / 1000)

# Program worked for 1.8216 sec
# Program worked for 1.5766 sec
# Program worked for 2.3242 sec