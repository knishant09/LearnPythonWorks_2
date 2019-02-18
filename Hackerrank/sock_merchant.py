from collections import Counter


# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    print(ar)
    print(n)
    dict_1 = dict(Counter(ar))
    print(dict_1)

    print(dict_1.values())
   # print(type(dict_1.values()))

   # print(len(dict_1.values()))

    #print(sum(dict_1.values()))

    print("*********************")
    sum=0
    for i in dict_1.values():
        sum = sum + int(i // 2)

    print(sum)

    return sum



if __name__ == '__main__':


    n = int(input("Enter the number of socks:"))

    ar = list(map(int, input("Ënter the list of socks:").rstrip().split()))

    result = sockMerchant(n, ar)

    print(result)