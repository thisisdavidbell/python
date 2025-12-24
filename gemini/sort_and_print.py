def get_last_three_sorted(items):
    """Sorts a list and returns the last 3 items."""
    items.sort()
    return items[-3:]

def main():
    # 1. Create a list of 10 things (strings)
    items = [
        "zebra",
        "apple",
        "mango",
        "banana",
        "cherry",
        "date",
        "elderberry",
        "fig",
        "grape",
        "honeydew"
    ]

    # 2. Get the last 3 sorted items using the reusable function
    last_three = get_last_three_sorted(items)

    # 3. Print the last 3 items in upper case
    print("The last 3 items in the sorted list (uppercase):")
    for item in last_three:
        print(item.upper())

if __name__ == "__main__":
    main()
