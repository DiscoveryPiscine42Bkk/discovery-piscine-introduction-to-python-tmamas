import sys


params = sys.argv[1:]


if len(params) != 2:
    print("none")
else:
    keyword = params[0]
    text = params[1]

    count = text.count(keyword)

    if count > 0:
        print(count)
    else:
        print("none")
