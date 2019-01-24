def read_my_name(func):
  name = "Fred"
  name_thing = func(name)

  return name_thing

def make_a_phrase(name):
  return f"Hi. My name is  {name}"

print(read_my_name(make_a_phrase))

def add(num1, num2):
  return num1 + num2

def subtract(num1, num2):
  return num1 - num2

def multiply(num1, num2):
  return num1 * num2

def calculator(func, num1, num2):
  return func(num1, num2)

result = calculator(multiply, 123, 8)
print(result)


# ============
  # decorator takes something simple and returns a customized version of that simple function

def interior_decorator(func):
  def add_curtains(color):
    if color == "orange":
      color = "ugly"
    func(color)
    print(f"But, now my house has {color} curtains")

  return add_curtains

def move_in():
  print("My house is empty.")

def redecorate():
  print("I used to have beige curtains.")

new_house = interior_decorator(move_in)
redecorated_house = interior_decorator(redecorate)

print("This is just the function itself", new_house)

# new_house()
# redecorated_house()


# =============

@interior_decorator
def moved_in(color):
  print("My house is still empty.")

# print("test:", moved_in("orange"))
moved_in("purple")
