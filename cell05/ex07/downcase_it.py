import sys

params = sys.argv[1:]

if len(params) == 1:
    print(params[0].lower())
else:
    print("none")
