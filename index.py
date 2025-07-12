#Assignment 1
#q1 for loop
divisible_by_3_and_5 = []
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        divisible_by_3_and_5.append(i)
print(divisible_by_3_and_5)
#q2
string = "Ahad is a boy"
string2 = ""
for i in string:
    if i == " ":
        string2 += "_"
    else:
        string2 += i
print(string2)


#q3
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = []

for item in list1:
    if item in list2:
        common_elements.append(item)
print(common_elements)


#while loop
#q1
my_list = [10, 20, 30, 40, 50]
while my_list:
    my_list.pop()
    print(my_list) output

#q2
num = 100
while num >= 1:
    print(num)
    num /= 2


#q3
total = 0
while total <= 100:
    num = int(input("Enter a number: "))
    total += num
    print(f"Current total: {total}")