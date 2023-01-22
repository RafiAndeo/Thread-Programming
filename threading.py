import threading


def prime(m, n):
    count = 0
    for i in range(m, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            count = count + 1
    print("Banyaknya bilangan prima dari rentang ",
          m, " sampai ", n, ": ", count)


t1 = threading.Thread(target=prime, args=(9999, 20000))

t1.start()

t1.join()


def factorial(x, n):
    if x == 0:
        print("Nilai faktorial dari 0 adalah 1")
    else:
        for i in range(1, x + 1):
            n = n * i
        print("Nilai faktorial dari ", x, " adalah ", n)


t2 = threading.Thread(target=factorial, args=(15, 1))

t2.start()

t2.join()

t3 = threading.Thread(target=factorial, args=(20, 1))

t3.start()

t3.join()
