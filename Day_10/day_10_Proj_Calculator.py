from art import logo
print(logo)

add = lambda n1, n2: n1 + n2
sub = lambda n1, n2: n1 - n2
mul = lambda n1, n2: n1 * n2
div = lambda n1, n2: n1 / n2

operations = {
  "+": add,
  "-": sub,
  "*": mul,
  "/": div
}

def calc():
  using = True
  ans = 0
  allowed_ops = ["+", "-", "*", "/"]
  n1_as_ans = False
  
  while using:
    
    if not n1_as_ans:
      n1 = float(input("Enter a number: "))
    else:
      n1 = ans
    for symbol in operations:
      print(symbol)
    op = input("Choose operation, (*+-/): ").lower()
    while op not in allowed_ops:
      op = input("Invalid Opetaion, chose from (+-*/): ")

    n2 = float(input("Enter other number: "))

    if op == "*" or op == "x":
      ans = mul(n1, n2)
      print(f" = {ans}")
    elif op == "/":
      ans = div(n1, n2)
      print(f" = {ans}")
    elif op == "+":
      ans = add(n1, n2)
      print(f" = {ans}")
    elif op == "-":
      ans = sub(n1, n2)
      print(f" = {ans}")
    ask_if_using = "null"
    while ask_if_using not in ["y", "n"]:
      ask_if_using = input("Would you like to keep calculating, y or n: ").lower()
    if ask_if_using == "n":
      using = False
    if ask_if_using == "y":
      n1_as_ans = True

  return ans

calc()