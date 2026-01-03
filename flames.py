name1 = input("Enter first name: ").lower().replace(" ", "")
name2 = input("Enter second name: ").lower().replace(" ", "")

list1 = list(name1)
list2 = list(name2)

# Remove common letters
for ch in list1[:]:
    if ch in list2:
        list1.remove(ch)
        list2.remove(ch)

count = len(list1) + len(list2)

flames = ["F", "L", "A", "M", "E", "S"]

index = 0
while len(flames) > 1:
    index = (index + count - 1) % len(flames)
    flames.pop(index)

result = flames[0]

if result == "F":
    print("Relationship: Friends")
elif result == "L":
    print("Relationship: Love")
elif result == "A":
    print("Relationship: Affection")
elif result == "M":
    print("Relationship: Marriage")
elif result == "E":
    print("Relationship: Enemies")
elif result == "S":
    print("Relationship: Siblings")
    
    