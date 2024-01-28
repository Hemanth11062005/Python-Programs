'''
Asking Questions
Now it is time to pick up the pace. I have got you doing a lot of printing so that you get used to
typing simple things, but those simple things are fairly boring. What we want to do now is get
data into your programs. This is a little tricky because you have to learn to do two things that may
not make sense right away, but trust me and do it anyway. It will make sense in a few exercises.
Most of what software does is the following:
1. Take some kind of input from a person.
2. Change it.
3. Print out something to show how it changed.
So far you have only been printing, but you haven’t been able to get any input from a person or
change it. You may not even know what “input” means, so rather than talk about it, let’s have you
do some and see if you get it. In the next exercise, we’ll do more to explain it.
'''


'''print("How old are you"),
age = raw_input()
print("how tall are you?"),
height = raw_input()'''
# it is not working in my laptop and currrent python version you may try like below:

age = int(input("Enter your age: "))
height = int(input("Enter your height: "))
weight = int(input("Enter your weight: "))

print("So, you're %r years old, %r tall, and %r heavy" % (age, height, weight))
