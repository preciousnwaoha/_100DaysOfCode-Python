#Write your code below this line 👇

def prime_checker(number):
  is_prime = True
  for i in range(2, number):
    if number%i == 0:
      is_prime = False
      print(f"{number} is not a prime number")
      return
    
  print(f"{number} is a prime number")


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



