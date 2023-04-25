tmp = input().split()

N = int(tmp[0])
T = int(tmp[1])

C = input().split()
R = input().split()

if str(T) not in C:
    color = int(C[0])
    num = int(R[0])
    human = 1 
    for i in range(1,N):
        if(int(C[i])==color):
            if(int(R[i]) > num):
                num = int(R[i])
                human = i+1
    print(human)

else:
    color = T
    num = 0
    for i in range(N):
        if(int(C[i])==color):
            if(int(R[i]) > num):
                num = int(R[i])
                human = i+1
    print(human)


