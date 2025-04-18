Username="xf"
Password="12345"
def logging(game):
    def wrapper(*args,**kwargs):
        username=input("Enter your username:")
        while username!=Username:
            print("Incorrect username!")
            username=input("Enter your username:")
            if username==Username:
                password=input("Enter your password:")
                while password!=Password:
                    print("Incorrect password!")
                    password=input("Enter your password:")
                    if password==Password:
                        print("Login successful!")
                        break
                    else:
                        print("Incorrect password!")
            else:
                print("Incorrect username!")
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