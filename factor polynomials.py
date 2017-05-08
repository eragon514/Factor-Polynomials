##Author: Timothy Williams
#
##Date: 5/7/17
#
##Factors polynomials of the second degree

#factors a power 2 polynomial
#l1 has the possible first terms of the factored polynomial
#l2 has the possible second terms

#4x**2 - 5x - 9
#l1 =((1, 4), (2, 2)) 
#l2 = ((-3, 3), (1, -9), (-1, 9))

while True:
    while True:
        a = input("a: ")
        try:
            a = int(a)
        except:
            pass
        else:
            break
    while True:
        b = input("b: ")
        try:
            b = int(b)
        except:
            pass
        else:
            break
    while True:
        c = input("c: ")
        try:
            c = int(c)
        except:
            pass
        else:
            break

    l1 = []
    if a > 0:
        if a == 1:
            l1 = [(1, 1)]
        for i in range(1, (a // 2) + 1):
            if a % i == 0:
                l1.append((i, a // i))
    elif a < 0:
        if a == -1:
            l1 = [(1, -1)]
        else:
            k = abs(a)
            for i in range(1, (k // 2) + 1):
                if a % i == 0:
                    l1.append((0 - i, k // i))
                    l1.append((i, 0 - (k // i)))

    l2 = []
    if c > 0:
        if c == 1:
            l2 = [(1, 1)]
        if b > 0:
            for i in range(1, (c // 2) + 1):
                if c % i == 0:
                    l2.append((i, c // i))
        else:
            for i in range(1, (c // 2) + 1):
                if c % i == 0:
                    l2.append((0 - i,  0 - (c // i)))
    elif c < 0:
        if c == -1:
            l2 = [(1, -1)]
        else:
            l = abs(c)
            for i in range(1, (l // 2) + 1):
                if c % i == 0:
                    l2.append((0 - i, l // i))
                    l2.append((i, 0 - (l // i)))

    def factorpoly(num):
        result = []
        for i in l2:
            for j in l1:
                t1 = j[0] * i[1]
                t2 = j[1] * i[0]
                if t1 + t2 == num:
                    result.append(("(" + str(j[0]) + "x + " + str(i[0]) + ")(" + str(j[1]) + "x + " + str(i[1]) + ")"))
                t1 = j[0] * i[0]
                t2 = j[1] * i[1]
                if t1 + t2 == num:
                    result.append(("(" + str(j[0]) + "x + " + str(i[1]) + ")(" + str(j[1]) + "x + " + str(i[0]) + ")"))
        if len(result) == 0:
            print("no factors")
        else:
            z = []
            for i in result:
                if i not in z:
                    z.append(i)
                    print(i)

    factorpoly(b)
