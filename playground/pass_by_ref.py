import ctypes



def increment(x):
    x += 1


def main():
    z = ctypes.c_int(5)
    increment(ctypes.ctypes.byref(z))
    print(z)


if __name__ == '__main__':
    main()
