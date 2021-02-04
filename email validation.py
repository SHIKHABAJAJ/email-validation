import regex as re
email=input("Enter email address to check validation : ").strip()
valid=re.compile(r'[_]?+[a-z0-9]+[._-]?+[a-z0-9]+[@]\w+[.]\w{2,3}$')

if valid.match(email):
    print("Valid email address")
else:
    print("Invalid email address")


