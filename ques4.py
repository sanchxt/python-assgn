def swap_strings(string1, string2):
    temp = string1
    string1 = string2
    string2 = temp
    return string1, string2


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

print("Original Strings:")
print("String 1:", string1)
print("String 2:", string2)

string1, string2 = swap_strings(string1, string2)

print("\nAfter Swapping:")
print("String 1:", string1)
print("String 2:", string2)
