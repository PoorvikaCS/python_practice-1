#home work-1
# Write a Python program that asks the user for their name and age, then prints a personalized greeting message. Use both the + operator and f-strings for output.
name=input("enter your name: ")
# print(name)
age=input("enter your age:")
# print(age)
print(f"hello , {name}! you are {age} years old") 


#home work-2
#Write a Python program that:
# Takes a sentence as input from the user.
# Prints the sentence in all uppercase and lowercase.
# Replaces all spaces with underscores.
# Removes leading and trailing whitespace
message="  python  is  awesome !   "
print(message)
print(message.upper())
print(message.lower())
print(message.replace (" " , "_"))
print(message.strip( )) 


# homework-3  Write a Python program that:
# Asks the user for a string.
# Prints how many characters are in the string, excluding spaces.
user_string = input("Enter a string: ")
char_count = len(user_string.replace(" ", ""))
print(f"Number of characters (excluding spaces): {char_count}")    


#homework-4   Write a Python program that uses escape sequences
print("hello\n\tworld!")
print("this is a blackslash: \ \ ")

