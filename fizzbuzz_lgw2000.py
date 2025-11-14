for i in range(1,32):
    if i % 5 == 0 or i % 3 == 0:
        print("fizz"*(i%3==0)+"buzz"*(i%5==0))
    else:
        print(i)