def faktorPrima(x) :
    bilanganList = []
    loop = 2
    while loop <= x:
        if x % loop == 0 :
            x /= loop
            bilanganList.append(loop)
        else:
            loop += 1
    return bilanganList
