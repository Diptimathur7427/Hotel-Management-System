import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load room data
rooms_df = pd.read_csv("rooms.csv")

# Food Menu
food_menu = {
    "Pizza": 200,
    "Burger": 100,
    "Coffee": 80
}

# Activities
activities = {
    "Swimming": 500,
    "Gym": 300,
    "Spa": 1000
}

# Login system
def login():
    print("\n1. Manager Login\n2. Customer Login")
    choice = input("Enter choice: ")

    if choice == "1":
        user = input("Enter username: ")
        pwd = input("Enter password: ")
        if user == "admin" and pwd == "123":
            print("Manager Login Successful")
            manager_menu()
        else:
            print("Wrong credentials")

    elif choice == "2":
        customer_menu()

# Manager menu
def manager_menu():
    print("\n--- ROOM STATUS ---")
    print(rooms_df)

# Customer system
def customer_menu():
    name = input("\nEnter your name: ")

    print("\nAvailable Rooms:")
    print(rooms_df)

    room_type = input("Select room: ")
    days = int(input("Enter days: "))

    room_price = int(rooms_df[rooms_df["Room"] == room_type]["Price"])
    room_total = room_price * days

    # Food
    food_total = 0
    while True:
        print("\nFood Menu:", food_menu)
        f = input("Order food (or 'done'): ")
        if f == "done":
            break
        if f in food_menu:
            food_total += food_menu[f]

    # Activities
    act_total = 0
    while True:
        print("\nActivities:", activities)
        a = input("Choose activity (or 'done'): ")
        if a == "done":
            break
        if a in activities:
            act_total += activities[a]

    # Final Bill
    total = np.sum([room_total, food_total, act_total])

    print("\n------ FINAL BILL ------")
    print("Room Charges:", room_total)
    print("Food Charges:", food_total)
    print("Activity Charges:", act_total)
    print("TOTAL =", total)

    # Save data
    df = pd.DataFrame([[name, room_type, days, room_total, food_total, act_total, total]],
                      columns=["Name","Room","Days","RoomBill","FoodBill","ActivityBill","Total"])

    df.to_csv("customers.csv", mode='a', header=False, index=False)

    # Graph
    plt.bar(["Room","Food","Activity"], [room_total, food_total, act_total])
    plt.title("Bill Distribution")
    plt.show()

# Run system
login()