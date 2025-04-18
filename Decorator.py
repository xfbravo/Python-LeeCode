Username="xf"
Password="12345"
def logging(game):
    def wrapper(*args,**kwargs):
        username=input("Enter your username:")
        while True:

            if username==Username:
                password=input("Enter your password:")
                while password!=Password:
                    if password==Password:
                        print("Login successful!")
                        break
                    else:
                        print("Incorrect password!")
                        password=input("Enter your password:")
                break
            else:
                print("Incorrect username!")
                username=input("Enter your username:")
        ref=game(*args,**kwargs)
        return ref
    return wrapper

@logging
def game():
    print("Welcome to the game!")
    print("You have successfully logged in.")
    # Game logic goes here
    # For example, let's just return a simple message
    return "Game started!"

game()