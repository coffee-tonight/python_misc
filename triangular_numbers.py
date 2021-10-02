def tn(n):
    if n == 0:
        return 0
    else:
        return n + tn(n-1)

x = []
def cp(k):
    s = k
    i = 2
    while (k > 1):
        while(k % i == 0):
            x.append(i)
            k /= i
        i += 1
        if len(x) == 100:
            print(s)
            break
j = 1
while (j > 0):
    cp(tn(j))
    j += 1
