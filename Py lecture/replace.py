name = input("Enter your name: ")
new_name = ""

for ch in name:
    if ch == "a":
        new_name += "z"
    else:
        new_name += ch

print(new_name)