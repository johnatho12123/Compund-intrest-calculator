import matplotlib.pyplot as plt
import math
import time
import sys

def compund_intrest(principal,rate,time1):
    formula = principal*math.pow((1+rate),time1)
    print(formula)
    return formula

def simple_intrest(principal,rate,time1):
    formula = principal * (rate/100) * time1
    print(formula)
    return formula


principal = float(input("Prinicpal Amount($): "))
rate = int(input("Rate: "))
time1 = int(input("Years: "))
ci = compund_intrest(principal,rate,time1)
print(f"Compund Intrest: {ci} $")
ds = input("Do youwant it plotted to see the progression(y/n): ").lower()
if ds == "y":

    time.sleep(1)
    loop = [compund_intrest(principal,rate,t) for t in range(time1)]
    loop2 = [simple_intrest(principal,rate,i) for i in range(time1)]
    listed = list(loop)
    listed1 = list(loop2)
    x_axis = list(range(time1))
    y_axis = listed
    y2_axis = listed1
    plt.xlabel("Time")
    plt.ylabel("Money Growth")
    plt.plot(x_axis,y_axis,c = "green",label = "Compund Intrest")
    plt.plot(x_axis,y2_axis,c = "blue",label = "simple intrest")
    plt.grid(True)
    plt.show()

elif ds == "n":
    print("thank you for using the calculator")
    sys.exit()
else:
    print("the input doesnt fit the followed inputs")
    time.sleep(1)
    print("please rerun code")
    sys.exit()
