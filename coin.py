n=1260
count=0

set = [500,100,50,10]

for coin in set:
    count+=n//coin
    n%=coin

print(count)
