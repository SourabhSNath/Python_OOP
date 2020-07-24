from SuperUser import SuperUser

superuser = SuperUser("Sourabh", "SSN", "Engineer")

print(superuser.username)
print()
print(superuser)
print()
print(repr(superuser)) # no role in __repr__

print(superuser.username)

print(help(superuser))