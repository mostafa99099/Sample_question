data = []
a = 0
while True:
    if a <= 3:
        inpott = input("what's your name? ")
        data += inpott.split(" ")
        a += 1
    else:
        break
# data = []
# for i in range(4):
#     n = input("what's your name?").split(" ")
#     data.append(n)


kv = {"list1": [], "list2": [], "list3": [], "list4": []}
for indx, item in enumerate(data):
    if indx <= 3:
        kv["list1"].append(item)
    elif 3 < indx <= 7:
        kv["list2"].append(item)
    elif 7 < indx <= 11:
        kv["list3"].append(item)
    elif 11 < indx <= 15:
        kv["list4"].append(item)
    else:
        print("not defind")
my_list = []
my_list.append(kv["list1"])
my_list.append(kv["list2"])
my_list.append(kv["list3"])
my_list.append(kv["list4"])
name1, name2, name3, name4 = my_list[0], my_list[1], my_list[2], my_list[3]
# print(name1, name2, name3, name4)

print(data)
print(name1, name2, name3, name4)

# mostafa jafari 19 student
# ali rezaii 22 techear
# asghar ahmadi 33 worker
# ahamad ahamadi 32 maniger
