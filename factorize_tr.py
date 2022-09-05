from time import time
from threading import Thread


def calcul(num):
    res = []
    counter = 1
    while counter <= num:
        if num % counter == 0:
            res.append(counter)
        counter += 1
    print(res)
    return res


def factorize(*number):
    res_num = []
    threads = []
    for num in number:
        th = Thread(target=calcul, args=(num,))
        th.start()
        threads.append(th)
    [el.join() for el in threads]
    return res_num


if __name__ == '__main__':
    timer = time()

    res = factorize(128, 255, 99999, 10651060)
    time_delta = time() - timer
    print(f'Program worked for {round(time_delta, 4)} sec')

# Program worked for 1.8256 sec
# Program worked for 1.768 sec
# Program worked for 2.5289 sec