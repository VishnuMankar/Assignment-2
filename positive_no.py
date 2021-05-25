list = list(map(int, input("Enter numbers with space as sepration : ").split(" ")))
list_of_positive = []
for i in list:
    if i > 0 :
        list_of_positive.append(i)
print(list_of_positive)