from math import sin


def f(x):
    return -(x ** 0.5) * sin(x) + 2

def optpass(func, a, b, N):
    print("\n\nОптимальный пассивный поиск:")
    print(27 * '_')
    print("|{0:^10}|{1:^14}|".format('Количество', 'Значение x'))
    print("|{0:^10}|{1:^14}|".format('точек (N)', 'в минимуме'))
    print(27 * '-')
    for n in range(1, N+1):
        x = []
        x.append(a)
        x.extend([k * (b - a) / (n + 1.0) + a for k in range(1, n+1)])
        x.append(b)
        for i in range(1, n+2):
            if func(x[i]) > func(x[i-1]):
                #print("Минимум функции достигается при x = {0} ± {1} (N = {2})".format(x[i-1], (b-a) / (N + 1), N))
                print("|{0:^10}|{1:^14}|".format(n, "{0:.3} ± {1:.3}".format(x[i-1], (b-a) / (n + 1.0))))
                break
    print(27 * "¯")

def dihotomia(func, a, b, epsilon):
    print("\n\nПоследовательный поиск (дихотомия):")
    ak = a + 0.0
    bk = b + 0.0
    delta = epsilon / 10
    l = bk - ak
    print(61 * '_')
    print("|{0:^11}|{1:^11}|{2:^11}|{3:^11}|{4:^11}|".format('Начало', 'Конец', 'Длина', ' ', ' '))
    print("|{0:^11}|{1:^11}|{2:^11}|{3:^11}|{4:^11}|".format('интервала', 'интервала', 'интервала', 'f(ak)', 'f(bk)'))
    print("|{0:^11}|{1:^11}|{2:^11}|{3:^11}|{4:^11}|".format('(ak)', '(bk)', '(l)', ' ', ' '))
    print(61 * '-')
    while l > epsilon:
        xk1 = (bk + ak) / 2 - delta
        xk2 = (bk + ak) / 2 + delta
        f_xk1 = func(xk1)
        f_xk2 = func(xk2)
        print("|{0:^11.4}|{1:^11.4}|{2:^11.4}|{3:^11.4}|{4:^11.4}|".format(ak, bk, l, f_xk1, f_xk2))
        if f_xk1 < f_xk2:
            bk = xk1
        else:
            ak = xk2
        l = bk - ak
    print(61 * "¯")
    print("Минимальное значение функции достигается при x = {0:.4} ± {1}".format((bk + ak) / 2, epsilon))

dihotomia(f, 1, 4, 0.1)

optpass(f, 1, 4, 29)