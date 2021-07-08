n,m = map(int,input().split())
max_data=0
for i in range(n):
    data=map(int,input().split())
    list_min=min(data)
    max_data=max(max_data,list_min)

print(max_data)
