# Estimating true height of a building from ten measured values

import math

K = 0.0
x_i_i = 0.0
x_i_i_1 = 0.0
p_i_i = 0.0
p_i_i_1 = 0.0


def initialize():
    global x_i_i_1, p_i_i_1
    x_i_i_1 = float(input("Estimate: >> "))
    p_i_i_1 = float(input("Estimate Variance: >> "))


def predict():
    global x_i_i_1, x_i_i, p_i_i_1, p_i_i
    x_i_i_1 = x_i_i
    p_i_i_1 = p_i_i


def calc_kalman_gain(_r):
    global K, p_i_i_1
    K = p_i_i_1 / (p_i_i_1 + _r)


def update_state(z_):
    global x_i_i, x_i_i_1, K
    x_i_i = x_i_i_1 + K * (z_ - x_i_i_1)


def update_covariance():
    global p_i_i, K, p_i_i_1
    p_i_i = (1 - K) * p_i_i_1


times = ["First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh", "Eighth", "Ninth", "Tenth",
         "Eleventh", "Twelfth", "Thirteenth", "Fourteenth", "Fifteenth", "Sixteenth", "Seventeenth",
         "Eighteenth", "Nineteenth", "Twentieth"]

initialize()
print()
for i in range(10):
    z = float(input(f"{times[i]} Measurement: >> "))
    r = float(input("Measurement Variance: >> "))
    calc_kalman_gain(r)
    update_state(z)
    update_covariance()
    predict()
    print(f"Estimated height so far: {x_i_i_1}")
    print()
print(f"Final estimated height: {x_i_i_1}")
print(f"Final standard deviation of estimated error: {math.sqrt(p_i_i_1)}")
