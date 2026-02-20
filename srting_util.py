def vowels(s):
    vow = "aeiouAEIOU"
    count = 0

    for i in s:
        if i in vow:
            count += 1
    print(f"Total vowels in the given string is: {count}")

def greet(name):
    print(f"Hello {name}!! \nGood Morning!!")

if __name__ == "__main__":
    print("This script is executed directly.")
else:
    print("This script is imported as a module.")

