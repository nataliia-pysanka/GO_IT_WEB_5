from time import time


def factorize(*number):
    res_num = []
    for num in number:
        res = []
        counter = 1
        while counter <= num:
            if num % counter == 0:
                res.append(counter)
            counter += 1
        print(res)
        res_num.append(res)
    return res_num


if __name__ == '__main__':
    timer = time()

    factorize(128, 255, 99999, 10651060)
    time_delta = time() - timer
    print(f'Program worked for {round(time_delta, 4)} sec')

# Program worked for 1.6261 sec
# Program worked for 1.2516 sec
# Program worked for 2.3706 sec