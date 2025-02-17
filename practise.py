import time

start = time.time()

performance = ["2/6", "2/4", "6/16"]
split_fractions = []
simplified = ()

def gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)

for i in range(len(performance)):
    s = performance[i].split("/")
    split_fractions.append(s)
    GCD = gcd(int(s[0]), int(s[1]))
    s[0] = int(int(s[0])/GCD)
    s[1] = int(int(s[1])/GCD)
    final = str(s[0])+"/"+str(s[1])
    print(final)

end = time.time()
print("elapsed time from start to end of algorithm:", end-start)
