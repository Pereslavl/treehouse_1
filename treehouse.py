first_name = input("Whaat is your name?")
print("Hello,", first_name)
if first_name == "Sergey":
    print(first_name, "is learning Python")
elif first_name == "Vika":
    print(first_name, "you too learning Python")
else:
    print("You should totally learn Python, {}!".formate(first_name))
    print("Have a nice day {}!".format(first_name))
    print("Have a bad day {}!".format(first_name))
