students = {
    
    101: {"name": "Vansh", "Marks": [50, 60, 70, 80]},
    102: {"name": "Shivam", "Marks": [10, 12, 14, 18]},
    103: {"name": "Rohan", "Marks": [30, 40, 60, 120]},
    104: {"name": "Yash", "Marks": [20, 40, 60, 80]},
    105: {"name": "SONal", "Marks": [90, 80, 70, 60]}
}

for sid, details in students.items():
    avg = sum(details["Marks"])/len(details["Marks"])
    details["Average"] = avg
    details["Passed"] = avg >=30
    

print("Students who passed: ")
for sid, details in students.items():
    if details["Passed"]:
        print(details["name"])