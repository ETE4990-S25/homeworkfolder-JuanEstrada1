def is_name_in_list(name, name_list):
    """Check if a given name is in the provided list."""
    return name in name_list

if __name__ == "__main__":
    # Example usage
    names = ["Alice", "Bob", "Charlie", "David"]
    input_name = input("Enter a name to check: ")
    
    if is_name_in_list(input_name, names):
        print(f"{input_name} is in the list!")
    else:
        print(f"{input_name} is NOT in the list.")
