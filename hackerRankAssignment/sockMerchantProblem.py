_name__= 'goldy'


from collections import Counter
# sockMerchant function


def sockmerchant(n,ar):
    # count = Counter(ar)
    # print("count value:", count)
    numofsocktobesold = 0
    for values in Counter(ar).values():
        numofsocktobesold += values//2
    return numofsocktobesold


n = int(input("Enter number of socks to be paired:"))
ar = list(map(int, input("enter socks color type:").rstrip().split()))
print("socks numbers", ar)
result = sockmerchant(n, ar)
print("Number of pair of socks to sell:", result)