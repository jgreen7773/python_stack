# I'm using a T-diagram separately for each of these functions.

# 1
def a():
    return 5
print(a())
# Predicted: 5


# 2
def a():
    return 5
print(a()+a())
# Predicted: 10


# 3
def a():
    return 5
    return 10
print(a())
# Predicted: 10


# 4
def a():
    return 5
    print(10)
print(a())
# Predicted: 5, 10


# 5
def a():
    print(5)
x = a()
print(x)
# Predicted: 5


# 6
def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))
# Predicted: 3, 5...or (1+2) + (2+3) This print thing is interestingly confusing


# 7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Predicted: "25"


# 8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Predicted: 100, 10, 7         Hmm, why did it not return 7? Why is it over-ridden in a nesting? note for later....


# 9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Predicted: 7, 14, 7           Hahaha! I got it wrong again! It was 21! I'll get these specifics soon!


# 10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Predicted: 8                  Note here, that only the first "return" statement is effective! Ah Ha!


# 11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# Predicted: 500, 500, 300, 500


# 12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# Predicted: 500, 500, 500, 300, 500        I was wrong here, both the print AND the return will activate from a()


# 13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# Predicted: 500, 500, 500          I thought that the b=a() statement won't return anything, it returned 300
#                                       also, the print(b) after it returned 300. WHYYY doesn't it return both
#                                       of the 300's like before???
#                                   Could it have something to do with b being redefined both inside and outside
#                                       of the function?
# Answer: 500, 500, 300, 300        Oh I think I understand why, dang that's tricky...it did not return 2 300's
#                                       because how could it return b to the outside, if b was over-written?
#                                       


# 14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# Predicted: 1, 3, 2,               This has me scratching my head before I even answer, can I call a function
#                                       inside of a function, even if it hasn't been defined yet? Hmmm, code flow....
# Nice! I got it right!


# 15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# Predicted: 1, 3, 5, 10            Dangit! I got the answer right by chance, I forgot that y=a() will call the
#                                       function...and then print(y) only returned 10....
#                                   There is something valuable to be learned from this last piece.
#                                   Ok...when the function is called, it returns it's process
#                                   When the print statement is called, it returns it's end result
