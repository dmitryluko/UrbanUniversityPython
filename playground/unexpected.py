def unexpected_behaviour_int():
    def check(x):
        if x + 1 is 1 + x:
            return False
        if x + 2 is not 2 + x:
            return False
        return True

    for i in range(-10, 10):
        print(f'i : {i}, check(i) : {check(i)}')



def string_interning():
    print('String interning:')
    str1 = 'This is a big demo string!'
    str2 = 'This is a big demo string!'

    str3 = 'This is no interning _ string!'
    str4 = 'This is no interning _ string!'

    print(str1 == str2)
    print(str1 is str2)

    print(str3 == str4)
    print(str3 is str4)


def main():
    unexpected_behaviour_int()
    string_interning()


if __name__ == '__main__':
    main()
