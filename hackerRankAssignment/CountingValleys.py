# __name__ = 'goldi'
def countingValleys(n, steps):
    print(n,steps)
    level, numOfValley = 0, 0
    for step in steps:
        if step == 'U':
            level += 1
            if level == 0:
                numOfValley += 1
        elif step == 'D':
            level -= 1
    return numOfValley

n= int(input("Enter number of steps"))
steps= input ("Enter path travelled")

result = countingValleys(n,steps)
print('result',result)