def greeting(message):
    new_message = message.capitalize()
    print("Hey hey")
    return new_message

user_entry = input("What greeting do you want?")
greeting = greeting(user_entry)
print(greeting)
