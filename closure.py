def A(x):
    def B():
        print(x)

    return B


A(7)()
