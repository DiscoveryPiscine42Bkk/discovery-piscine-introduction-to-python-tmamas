def add_one(x):
    x = x + 1
    print(f"Inside add_one: x = {x}")


num = 5
print(f"Before add_one: num = {num}")

add_one(num)

print(f"After add_one: num = {num}")
