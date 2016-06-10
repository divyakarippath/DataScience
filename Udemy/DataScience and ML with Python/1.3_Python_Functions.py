def square(x):
    return x*x
def othertask(f,x):
    return f(x)
print square(2)

#function as parameter
print othertask(square,5)

#lambda function - define function inline
print othertask(lambda x:x*x*x,3)
