a=10
def abc():
    global a
    a=20
    print(a)
print(a)
abc()
print(a)
