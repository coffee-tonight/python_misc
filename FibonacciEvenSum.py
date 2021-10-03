# Install Git in this pc from your phone....
# Let's first try to achieve the fibonacci sequence
n = int(input("Till what number do you want to calculate?"))
series = [0, 1]

def fib(n):
    a = 0
    b = 1
    
    for i in range(2, n):
        c = a + b
        a = b
        b = c
        if c >= n:
            break
        series.append(c)
fib(n)

print(series)
sm = 0
for i in series:
    if i % 2 == 0:
        sm += i
print(sm)
print("Total number of terms = ", len(series))