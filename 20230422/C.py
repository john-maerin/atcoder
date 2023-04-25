L = int(input())
dango = input()
count = 0
sd = -1
flag = 0
o_flag = 0

for i in range(L):
    if (dango[i] == "o"):
        count += 1
        o_flag =1
    if (dango[i] == "-"):
        flag = 1
        if ((sd < count) and (count!=0)):
            sd = count
        count = 0
if ((flag==1) and (o_flag ==1)):
    print(max(count,sd))
else:
    print(-1)