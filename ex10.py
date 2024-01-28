from sys import argv

# Check if the correct number of command-line arguments is provided
if len(argv) != 2:
    print("Usage: python script_name.py your_name")
    exit(1)

# Unpack command-line arguments
script, user_name = argv

prompt = '>'

print("Hi %s, I'm the %s script" % (user_name, script))
print("I'd like to ask you a few questions")
print("Do you like me %s" % user_name)
likes = input(prompt)
print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
compute = input(prompt)

print("Alright so you said %r about liking me. You live in %r. Not sure where that is. And you have a %r computer. Nice" % (likes, lives, compute))
