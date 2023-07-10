def fibo():
    a = 1
    b = 2
    c = a + b
    print(a)
    print(b)
    while c < 1000:
        print(c)
        a = b
        b = c
        c = a + b

print("ok")