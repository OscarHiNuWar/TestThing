def odd(balls,pick,power=False):
    from math import factorial as fact
    p_ball = 1
    if power:
        p_ball = int(input("Enter Number of Powerballs: "))
    return print("{:,}".format((fact(balls))/(fact(5)*fact(balls-pick))*p_ball))

odd(69,6)