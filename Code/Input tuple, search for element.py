t = tuple(map(int, input("Enter tuple elements: ").split()))
key = int(input("Enter element to search: "))

print("Found at index:", t.index(key)) if key in t else print("Not found")
