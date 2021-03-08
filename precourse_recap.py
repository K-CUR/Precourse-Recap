popular_breed="Labrador"
guess=input("What is the UK's most popular breed of dog?")
while guess != popular_breed:
  print("Try again")
  guess = input()
else:
    print("You are correct!")


