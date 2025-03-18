favourite_food=[] #initialize empty list for favourite foods

while True:
    print("Favourite Food Manager")
    print("0.Exit")
    print("1.Add foods")
    print("2.Remove foods")
    print("3.View favourite all foods")

    choice=input("Choose an option : ") #from taken user input

    if choice=="0":
        print("Thanks for using Favourite Foods Manager")
        break
    elif choice=="1":
        food=input("Enter you favourite food name: ")
        favourite_food.append(food)
        print(f"{food} added Successfully")
    elif choice=="2":
        food = input("Enter a food name which you want to remove: ")
        favourite_food.remove(food)
        print(f"{food} remove Successfully")
    elif choice=="3":
        if favourite_food:
            print("Your Favourite food : ")
            for index,food in enumerate(favourite_food,start=1):
                print(f"{index}.{food}")

        else:
            print("Food list empty or didn't added yet !")

    else:
        print("Invalid Choice!")




