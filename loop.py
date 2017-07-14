import random
#You shoudl have lists of mltiple courses (ex) sides, main courses and dessers) and randomly create a menu for dinner
sides = ["fries","chips","bread"]
main = ["pasta","pad thai","pizza"]
desserts = ["ice cream","cake","cupcakes"]

name = input("What's your name?  ")
print("Hello ",name,"! here's your meal:")

print(random.choice(sides))
print(random.choice(main))
print(random.choice(desserts))

#print("Your main course is ",random.choice(main),")
#print("Your dessert is ",random.choice(dessert),")
