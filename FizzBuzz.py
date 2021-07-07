def fizz_buzz(red):
    if (red % 3 == 0) and (red % 5 == 0):
        return "FizzBuzz"
    if red % 3 == 0:
        return "Fizz"
    if red % 5 == 0:
        return "Buzz"
    return red

x = int(input("Any no. range from 1-100: "))
print(fizz_buzz(x))

#alternate
#for n in range(100):
#    print ("Fizz"*(not n % 3) + "Buzz"*(not n % 5) or n)