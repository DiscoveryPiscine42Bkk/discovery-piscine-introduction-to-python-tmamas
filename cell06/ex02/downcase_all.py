import sys

def downcase_it(s):
    return s.lower()

params = sys.argv[1:]

if not params:
    print("none")
else:
    for param in params:
        print(downcase_it(param))
