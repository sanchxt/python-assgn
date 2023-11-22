month_days = {
    'January': 31,
    'February': 28,
    'March': 31,
    'April': 30,
    'May': 31,
    'June': 30,
    'July': 31,
    'August': 31,
    'September': 30,
    'October': 31,
    'November': 30,
    'December': 31
}

inp = input("Enter a month: ")

if inp in month_days:
    print(f"{inp} has {month_days[inp]} days.")
else:
    print("Invalid month entered.")

print("\nAll months in alphabetical order:")
for month in sorted(month_days.keys()):
    print(month)

print("\nMonths with 31 days:")
for month, days in month_days.items():
    if days == 31:
        print(month)

print("\nMonths sorted by the number of days:")
for month, days in sorted(month_days.items(), key=lambda x: x[1]):
    print(f"{month}: {days} days")
