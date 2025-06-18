import sys

params = sys.argv[1:]

if len(params) != 1:
    print("none")
else:
    string = params[0]
    z_count = string.count('z')

    if z_count > 0:
        for _ in range(z_count):
            print('z')
    else:
        print("none")
