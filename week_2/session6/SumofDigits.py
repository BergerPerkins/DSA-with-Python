def sod(num):
    #base case condition
    if num < 10:
        return num
    #recursive function call
    else:
        return num%10 + sod(num//10)





num = 12345
result = sod(num)
print(result)