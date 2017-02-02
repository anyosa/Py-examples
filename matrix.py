A=[]
PAR=[]
IMPAR=[]

for i in range(0,20):
    A.append(int(input("entra com um valor:")))
    if(A[i]%2==0):
        PAR.append(A[i])
    else:
        IMPAR.append(A[i])
print(A)
print(PAR)
print(IMPAR)
