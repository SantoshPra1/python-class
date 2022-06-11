from ast import Lambda


a =[1,2,3,4,5]
b =[6,7,8,9,10]

c =list(map(lambda i, j: i+j ,a,b))
print(c)