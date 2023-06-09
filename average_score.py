
"""
# Input
3
Ali Art:20 PE:20 20
Hassan Math:20 19 18
Asghar 20 19 10

Ali 
3 
Art:20 
PE:20 
Math:20

Ali 
4
Art:20 
PE:20 
Math:20

# Output
---------------------------------------------------
| Name    | Math    | Art     | PE      | AVG     |
---------------------------------------------------
| Ali     | 20      | 20      | 20      | 20      |
---------------------------------------------------
| Hassan  | 20      | 20      | 20      | 20      |
---------------------------------------------------
| Asghar  | 20      | 20      | 20      | 20      |
---------------------------------------------------
"""
my_list = []

try:
    for _ in range(int(input("How many of you have input? "))):
        name, *scors = input("enter name and scors: ").split(" ")

        sum_of_scors = 0
        for scor in scors:
            sum_of_scors += int(scor)

        my_list.append([name, *scors, f"{sum_of_scors/ len(scors) :.2f}"])

except ValueError:
    print("Please enter only integers")


Name_Course = ["Name", "Math", "Art", "PE", "AVG"]
new_Course = []
for item in Name_Course:
    new_Course.append(item.ljust(10))

    # new_list: |Name      |Math      |Art       |PE        |AVG       |

print(chr(11333) * 55)
print("|" + "|".join(new_Course) + "|")
print("-" * 55)

for item in my_list:
    my_list2 = []

    for i in item:
        my_list2.append(i.ljust(10))

    print("|" + "|".join(my_list2) + "|")
    print("-" * 55)
