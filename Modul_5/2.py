def swap(A,p,q):
    tmp=A[p]
    A[p]=A[q]
    A[q]=tmp

def bubleSort(A):
    n=len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j]>A[j+1]:
                swap(A,j,j+1)


def gabungDuaSort(A,B):
    C=A+B
    bubleSort(C)
    print(C)

def gabungDua(A,B):
    bubleSort(A)
    bubleSort(B)
    C = A + B
    print(C)

    
a=[4,2,6,1,8,9,5,7,9]
b=[1,6,8,5,4,9]
print("ini yang diurutkan a dan b dan c")
gabungDuaSort(a,b)
print("ini yang hanya diurutkan a dan b nya saja")
gabungDua(a,b)
