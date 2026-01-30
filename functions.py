print("functions learning")

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("john", "doe")
print(full_name)  # Output: John Doe
