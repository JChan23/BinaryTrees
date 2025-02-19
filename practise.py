import time
start = time.time()

performance = ["75/3050", "30/4815", "460/4670", "250/1500", "160/1909", "330/1330", "210/1551"]

def gcd(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    return gcd(num2, num1%num2)

def simplify(array):
    split_fractions = []
    simplified = []
    for i in range(len(array)):
        s = array[i].split("/")
        split_fractions.append(s)
        GCD = gcd(int(s[0]), int(s[1]))
        s[0] = int(int(s[0])/GCD)
        s[1] = int(int(s[1])/GCD)
        final = str(s[0])+"/"+str(s[1])
        simplified.append(final)
    return tuple(simplified)

print(simplify(performance))

end = time.time()
print("elapsed time from start to end of algorithm:", end-start)






class Team:
    def __init__(self, tn, p1, p2, p3, p4, p5, r):
        self.__TeamName = tn
        self.__Player_1 = p1
        self.__Player_2 = p2
        self.__Player_3 = p3
        self.__Player_4 = p4
        self.__Player_5 = p5
        self.__Ranking = r
