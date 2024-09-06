from fontTools.misc.cython import returns


def greet(times):
    for i in range(times):
        print("round " + str(i+1) + " of saying hello")
        return

print("a new day ")
greet(5)

print("hi")

greet(4)
