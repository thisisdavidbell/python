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

    # 2. Sort the list (alphabetically)
    items.sort()

    # 3. Print the last 3 items in upper case
    # We use slicing [-3:] to get the last three elements
    print("The last 3 items in the sorted list (uppercase):")
    for item in items[-3:]:
        print(item.upper())

if __name__ == "__main__":
    main()
