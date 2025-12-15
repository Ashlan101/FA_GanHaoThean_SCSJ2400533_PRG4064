import datetime
today = datetime.date.today()
print(today)

print("Welcome to the Swimming Pool Membership System")
today = datetime.date.today()
print("Today is", today)

username = input("Enter your name:")
age = int(input("Enter your age:"))
membertype = input("Enter your membership type:")
print("Your name is:", username)
print("Your age is:", age)
print("Your member type is:", membertype)

if age < 12:
    print("Not eligible for membership")
elif age > 60:
    print("Senior membership granted")
else:
    print("Standard membership granted")

sessions = int(input("How many sessions do you want to book?"))
for x in range(sessions):
    print("Booking session", x + 1)
