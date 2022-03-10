# using *args to provide any number of args to a function
# def add(*args):
#     return sum(args)


# print(add(1,2,3,4,5,6,7,8,9))


def calculate(ans, **kwargs):
    for (key, value) in kwargs.items():
        if key == "add":
            ans += value
        if key == "minus":
            ans -= value
        if key == "multiply":
            ans *= value
        if key == "divide":
            ans /= value
    return ans


print(calculate(2, add=3, multiply=5, divide=3, minus=1))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")


new_car = Car(model="GT-R")
print(new_car.make, new_car.model)
