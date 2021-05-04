a = 2
while a == 2:
    print("HELLO SIR, PLEASE TELL US WHAT WE WILL DO. (+/-/x/*)")
    q = input()
    q2 = input("Please give us a number (top)")
    q3 = input("Please give us a number (bottom)")
    if q == "+":
        print(add(q2, q3))
    if q == "-":
        print(subtract(q2, q3))
    if q == "x":
        print(multiply(q2, q3))
    if q == "*":
        print(divide(q2, q3))
