'''def decore(func):
    def inner(name):
        if name=='pradeep':
            print('hello',name,'good night')
        else:
            func(name)
    return inner

#@decore
def wish(a):
    print('hello',a,'good morning')

decorefunc=decore(wish)

decorefunc('pradeep')'''


'''wish('chandan')
wish('harshith')
wish('pradeep')'''

def decor(func):
    def inner(a,b):
        if b==0:
            print('we cant divid')
            return
        else:
            return func(a,b)
    return inner

@decor
def division(a,b):

    return a/b

res1=division(20,2)
#res2=division(20/0)

print(res1)
#print(res2)











