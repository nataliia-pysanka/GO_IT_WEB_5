from time import time
from multiprocessing import Pool, Process, cpu_count


def calcul(num):
    res = []
    counter = 1
    while counter <= num:
        if num % counter == 0:
            res.append(counter)
        counter += 1
    return res


def callback(result):
    print(f'Result in callback: {result}')


def factorize(*number):
    with Pool(cpu_count()) as p:
        p.map_async(calcul,
                    number, callback=callback)
        p.close()
        p.join()


if __name__ == '__main__':
    print(f'Count CPU: {cpu_count()}')
    timer = time()
    factorize(128, 255, 99999, 10651060)
    time_delta = time() - timer
    print(f'Program worked for {round(time_delta, 4)} sec')

# Program worked for 1.9605 sec
# Program worked for 1.5383 sec
# Program worked for 1.822 sec