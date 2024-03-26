from random import randint

def roll_the_dice():
    return randint(1,6)


# i - returns the key

'''
-isolate each num string (parse/split)
    -convert t int
        -iterate compare between int and dict key
            -if == then concatenate
'''


'''
for i in s:
    if list(d.keys())[list(d.values()).index(i)] is True:
        print("true")
    else:
        print("false")
'''
'''
list(my_dict.keys())[list(my_dict.values()).index(100)]
'''


'''
for found in d.values():
    if found == x:
        print("true")
'''
# exploring assertions in while loops
    #syntax  assert <e>[, asertion message] where e is any object being test

s = "2658 8503 2582 3035 9951".split(" ") #return a list
d = {'a':1, 'b':2658}

x = 5
y = 7
z = 0
while z < 3:
    z += 1
    print(z)
    assert x == y, f"{x} is not equivalent to {y}"
    print(z)
    
