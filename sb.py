from random import randint

def roll_the_dice():
    return randint(1,6)


pl = ["A", "B", "C", "D"]
po = [0, 0, 0, 0]



# rolls dice
roll = roll_the_dice()


# i - returns the key

'''
-isolate each num string (parse/split)
    -convert t int
        -iterate compare between int and dict key
            -if == then concatenate
'''

s = "2658 8503 2582 3035 9951".split(" ") #return a list
d = {'a':1, 'b':2658}
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
#print(s.split(" "))
#print(s.find('2582'))

'''
for found in d.values():
    if found == x:
        print("true")
'''
ll = []
ll.remove
print(end = '')
s = "sssssssssssssssssssssssssssssssssssssssss\nssssssssssssssssssssssssss"
print(s, end=" yes!!!")
