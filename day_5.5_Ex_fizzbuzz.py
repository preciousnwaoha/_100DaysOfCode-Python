'''
When the number is divisible by 3 then instead of printing the number it should print "Fizz"
When the number is divisible by 5 then instead of printing the number it should print "Buzz"
When the number is divisible by both 3 and 5 then instead of printing the number it should print "FizzBuzz"
'''

for n in range(1, 100):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)