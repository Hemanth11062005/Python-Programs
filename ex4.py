#More variables
'''Now we’ll do even more typing of variables and printing them out. This time we’ll use something
called a “format string.” Every time you put " (double- quotes) around a piece of text,
you have been making a string. A string is how you make something that your program might
give to a human. You print them, save them to fi les, send them to web servers, all sorts of things.
Strings are really handy, so in this exercise you will learn how to make strings that have variables
embedded in them. You embed variables inside a string by using specialized format sequences
and then putting the variables at the end with a special syntax that tells Python, “Hey, this is a
format string, put these variables in there.”
'''


my_name = "Hemanth Sai Nag"
my_age = 18
my_height = 180 #cm
my_weight = 74 #kg
my_eyes = 'Black' 
my_teeth = 'White'
my_hair = 'Brown'

print("Let's talk about %s"%my_name)
#or
print("Let's talk about",my_name,"today")

print("He's %d inches tall"%my_height)
print("he's got %s eyes and %s hair"%(my_eyes,my_hair))

# rounding a floaing point
float_number = 1.7333
print('Rounded value of "1.7333" is:',round(float_number))
