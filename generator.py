# def fib(pos):
#     a,b=0,1
#     n=0
#     while n<pos:
#         a,b=b,a+b
#         n=n+1
#         yield a
#
# g=fib(1000)
# for i in range(1000-1):
#     print(next(g))
def gen():
    i=0
    while i<5:
        temp=yield i
        print("temp:",temp)
        i+=1
g=gen()

print(g.send(None))
print(g.send("hello"))
print(g.send("world"))
print(g.send("python"))

