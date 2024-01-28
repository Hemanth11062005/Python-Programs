#string slicing

name = "Hemanth Sai Nag"

first_name = name[0:7]

print(first_name)

last_name = name[8:]

print(last_name)

funcky_name = name[: : 3]
print(funcky_name)

reversed_name = name[::-1]
print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4)

print(website1[slice])
print(website2[slice])