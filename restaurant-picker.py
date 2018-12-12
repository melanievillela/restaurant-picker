restaurants = {
    "Cheddars" : "American",
    "Arandas" : "Mexican",
    "Gyro House" : "Greek",
    "Catfish Station" : "Seafood",
    "CT Banh Mi" : "Vietnamese",
    "The Catch" : "Seafood",
    "Pho & More" : "Vietnamese",
    "Bonsai Fusion" : "Japanese",
    "Mamacitas" : "Mexican",
    "Chilis" : "American"
}

def welcome_options():
    global original_length 
    original_length = len(restaurants)
    print("Welcome to the Restaurant Picker!")
    print("Would you like to:\n   1) View the list of restaurants\n   2) Add a new restaurant to the list\n   3) Choose a random restaurant to eat at? ")
    print("Please type in 1, 2 or 3")
    global answer 
    answer = input()
    return answer
    user_options()

def user_options():
    if answer == "1":
        for restaurant in restaurants:
            print (restaurant)
        welcome_options()
    elif answer == "2":
        print("Restaurant Name: ")
        name = input()
        print("Restaurant Cuisine (American, Mexican, Seafood etc...) ")
        cuisine = input()
        restaurants[name] = cuisine
        new_length = len(restaurants)
        if new_length > original_length:
            print("Restaurant added!")
            welcome_options()
        else:
            print("Restaurant not added!")
    else:
        print (answer)

welcome_options()
