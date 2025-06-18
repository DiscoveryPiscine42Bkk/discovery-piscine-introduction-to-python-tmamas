original_array = [2, 8, 9, 48, 8, 22, -12, 2]


new_array = [x + 2 for x in original_array if (x + 2) > 5]


print("Original array:", original_array)
print("New array (only > 5):", new_array)
