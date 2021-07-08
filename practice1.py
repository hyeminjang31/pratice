print('N 입력 : ')
n=int(input())
print('k 입력 : ')
k=int(input())
print('m 입력 : ')
m=int(input())

print(str(n)+'개의 숫자 입력')

l=list(map(int,input().split()))

l.sort()

first=l[n-1]
second=l[n-2]

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)
