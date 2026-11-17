# Display welcome message and menu
print("Welcome to Maria Eduarda Gonçalves's Pizzeria!\nHere is our menu:")
print("Size     Savory Pizza (SP)     Sweet Pizza (SW)")
print(" S            $ 30.00              $ 34.00")
print(" M            $ 45.00              $ 48.00")
print(" L            $ 60.00              $ 66.00")

total = 0  # Accumulator variable for the order total
answer = "Y"  # Control variable for multiple orders

# Main loop: runs while the customer wants to keep ordering
while answer == "Y":
    # Ask for pizza flavor and validate input
    flavor = input("\nEnter the desired flavor (SP/SW): ").strip().upper()
    while flavor != "SP" and flavor != "SW":
        print("Invalid flavor. Please try again.")
        flavor = input("Enter the desired flavor (SP/SW): ").strip().upper()

    # Ask for pizza size and validate input
    size = input("Enter the desired size (S/M/L): ").strip().upper()
    while size != "S" and size != "M" and size != "L":
        print("Invalid size. Please try again.")
        size = input("Enter the desired size (S/M/L): ").strip().upper()

    # Nested conditionals to determine price and add to total
    if flavor == "SP":
        if size == "S":
            print("You ordered a Savory Pizza (Size S): $ 30.00")
            total += 30
        elif size == "M":
            print("You ordered a Savory Pizza (Size M): $ 45.00")
            total += 45
        else:
            print("You ordered a Savory Pizza (Size L): $ 60.00")
            total += 60
    else:
        if size == "S":
            print("You ordered a Sweet Pizza (Size S): $ 34.00")
            total += 34
        elif size == "M":
            print("You ordered a Sweet Pizza (Size M): $ 48.00")
            total += 48
        else:
            print("You ordered a Sweet Pizza (Size L): $ 66.00")
            total += 66

    # Ask if the customer wants to add more items
    answer = input("\nWould you like to order anything else? (Y/N): ").strip().upper()
    while answer != "Y" and answer != "N":
        print("Invalid option. Please enter Y or N.")
        answer = input("Would you like to order anything else? (Y/N): ").strip().upper()

# Display final order total
print(f"\nThank you for your order! Your total is: $ {total:.2f}")