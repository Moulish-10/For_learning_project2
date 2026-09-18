a=10
b=12

print("==== Number Quessing game ====")

print("rules: \n 1.you have to enter a 3rd number.\n 2. The addition of 3 numbers will display. \n 3.Then you will find out the other two numbers.\n")
c = int(input("Enter a third number: "))

d = a+b+c

print(f"The some of three number is :{d} \n")
print("Guess the other 2 numbers...\n")
first_num = int(input("What is the 1st number : "))
sec_num = int(input("\nWhat is the 2nd number : "))

if a != first_num and b!= sec_num:
    print("Both predicted number is wrong...")
elif a == first_num and b == sec_num:
    print(f"\nBoth predicted number is correct.\n 1st number and 2nd number is : {first_num} & {sec_num}")
else:
    if a == first_num:
        print(f"\nyour 1st number is correct - The number is {first_num}")
    else:
        print(f"\nyour 1st number is wrong...")

    if b == sec_num:
        print(f"\nyour 2nd number is correct - The number is {sec_num}")
    else :
        print(f"\nyour 2nd number is wrong...")




