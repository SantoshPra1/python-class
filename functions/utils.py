import random
def generate_name():
    list1 =['red','green','blue','yellow','black','purple','pink']

    list2 =['apple','orange','grapes','mango','gauava','litchi']

    list3 =['cat','dog','lion','cow','fish','tiger','wolf']

    p1 = random.choice(list1)
    p2 = random.choice(list2)
    p3 = random.choice(list3)
    return f'{p1}-{p2}-{p3}'