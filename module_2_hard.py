for k in range(3, 21):
    str_ = ''
    for i in range(1, k):
        for j in range(i + 1, k):
            if k % (j + i) == 0:
                str_ += str(i)
                str_ += str(j)

    print(k,str_)
