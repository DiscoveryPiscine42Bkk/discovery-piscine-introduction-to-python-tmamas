import sys

params = sys.argv[1:]

if len(params) != 2:
    print("none")
else:
    try:
        start = int(params[0])
        end = int(params[1])
        range_list = list(range(start, end))
        print(range_list)
    except ValueError:
        print("none")
