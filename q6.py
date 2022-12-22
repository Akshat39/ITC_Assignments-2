side_1 = input("Enter the length of side a ")
side_2 = input("Enter the length of side b ")
side_3 = input("Enter the length of side c ")
if int(side_1) + int(side_2) > int(side_3) and int(side_2) + int(side_3) > int(side_1) and int(side_1) + int(side_3) > int(side_2):
    print("Yes")
else:
    print("No")