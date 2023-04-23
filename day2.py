def solve(a, b, c):
    d = b**2 - 4*a*c
    if d < 0:
        print("No real roots exist")
    elif d == 0:
        x = -b/(2*a)
        print("The root is", x)
    else:
        x1 = (-b + d**0.5)/(2*a)
        x2 = (-b - d**0.5)/(2*a)
        print("The roots are", x1, "and", x2)


solve(1, 2, 1)
solve(1, 2, 3)
solve(1, 5, 6)