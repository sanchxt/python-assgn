def addPrefix(name, gender):
    if gender.upper() == 'M':
        return "Mr. " + name
    elif gender.upper() == 'F':
        return "Ms. " + name
    else:
        return "unknown gender"


user_name = input("Name: ")
user_gender = input("Gender (M/F): ")

# Call the function and display the result
result = addPrefix(user_name, user_gender)
print("Result:", result)
