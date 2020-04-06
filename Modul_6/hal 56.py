def gabungkanDuaListUrut(A, B):
    a = len(A) ; b = len(B)

    C = list()
    i = 0 ; j = 0

    while i<a and j<b :
        if A[i] < B[j]:
            C.append(A[i])
            i += 1
        else :
           C.append(B[j])
           j += 1

    while i < a:
        C.append(A[i])
        i += 1

    while j < b:
        C.append(B[j])
        j += 1

    return C
