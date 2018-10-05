import random
from sympy import symbols, diff

def linreg_data_gd(data, threshold=0.001):
    theta1, theta0 = symbols('theta1 theta0')
    theta1, theta0 = 100, 100
    theta0upd, theta1upd = 0,0
    while (abs(theta1upd - theta1)< threshold) and (abs(theta0upd - theta0)<threshold):
        theta1upd = theta1 - lr*()


if __name__=="__main__":

    linreg_data_gd(data, 0.001)