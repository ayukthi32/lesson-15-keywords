#activity3
for x in range(10):
    if x % 20 == 0:
        print("twist" , x)
    elif x % 15 ==0 :
        print("buzz")
    elif x % 5 == 0:
        print("fizz")
    elif x % 3 == 0:
        pass
    else:
        print(x)