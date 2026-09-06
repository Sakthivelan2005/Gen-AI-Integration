l = [1,2,3,4,5,6]
r = []

#user defined funtion
def find_fact():
    import math
    for i in l:
        r.append(math.factorial(i))
    print(r)
find_fact()

# same in  Lambda function using map
import math
res = list(map(lambda i: math.factorial(i), l))
print(res)

#finding odd or even using filter
res = list(filter(lambda i: i%2 == 0, l));
print(res)

#Sum of array using reduce
import functools as f
res = f.reduce(lambda a,b : a+b, l )
print(res)

#Practise
import functools as f
res = f.reduce(lambda a,_, : a+[a[-1]+a[-2]], range(10-2),[0,1])
print(res)