#Assignment: Pick apart your user's input p35

user = input("Tell me your password:")
print("The first letter your entered was: ", user[0].upper())

#Assignment: Turn your user into a l33t h4x0r p45

message = input("Enter some text: ")

message = message.replace("a", "4")
message = message.replace("b", "8")
message = message.replace("e", "3")
message = message.replace("l", "1")
message = message.replace("o", "0")
message = message.replace("s", "5")
message = message.replace("t", "7")

print(message)

#Assignment: Perform calculations on user input p48

first = float(input("Insert the first number -"))
second = float(input("Insert the second number -"))
print(f'{first} to the power of {second} = ', first ** second)
