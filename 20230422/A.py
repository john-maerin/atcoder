N = int(input())
S = (input())

count =0

for i in range(N):
    if(S[i]=="*"):
        if(count==1):
            print("in")
            break
        else:
            print("out")
            break
    if(S[i]=="|"):
        count += 1
        if(count==2):
            print("out")
            break
        
    
        


