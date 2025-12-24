from sort_and_print import get_last_three_sorted

def main():
    items = []
    print("Please enter 10 items to build your list.")

    while len(items) < 10:
        user_input = input(f"Enter item {len(items) + 1}: ")
        items.append(user_input)

    # Use the reusable function from the other script
    last_three = get_last_three_sorted(items)

    print("\nThe last 3 items in your sorted list:")
    for item in last_three:
        print(item.upper())

if __name__ == "__main__":
    main()