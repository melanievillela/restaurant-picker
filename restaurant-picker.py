import random
import pickle
#Get the dictionary of restaurants
with open("restaurant_list.pkl", "rb") as pickle_file:
    restaurants = pickle.load(pickle_file)

spacer = "***************"

def welcome_options():    
    print("Would you like to:\n   1) View the list of restaurants\n   2) Add a new restaurant to the list\n   3) Remove a restaurant in the list\n   4) Choose a random restaurant to eat at ")
    print("Please type in 1, 2, 3 or 4 or write esc to exit")
    global answer 
    answer = input()
    user_options()

def user_options():
    if answer == "1":
        #Show list of restaurants
        print("Restaurants:")
        print(spacer)
        for restaurant in restaurants:
            print (restaurant)
        print(spacer)
        welcome_options()
    elif answer == "2":
        #Add restaurant to dictionary
        original_length = len(restaurants)
        print("Restaurant Name: ")
        name = input()
        if name in restaurants:
            print("That restaurant already exists in your list of restaurants.")
            user_options()
        else: 
            print("Restaurant Cuisine (American, Mexican, Seafood etc...) ")
            cuisine = input()
            #Add new restaurant into dictionary
            restaurants[name] = cuisine
            #Save dictionary
            save_changes()            
            new_length = len(restaurants)
            if new_length > original_length:
                print("Restaurant added!")
                welcome_options()
            else:
                print("Restaurant not added! Try again.")
                welcome_options()
    elif answer == "3":
        #Delete a restaurant
        original_length = len(restaurants)
        print("Restaurants:")
        print(spacer)
        for restaurant in restaurants:
            print (restaurant)
        print(spacer)
        print("To delete a restaurant type in the restaurant name: ")
        name = input()
        #Check if restaurant exists
        if name in restaurants:
            restaurants.pop(name)
            save_changes()
            new_length = len(restaurants)
            if new_length < original_length:
                print("Restaurant deleted!")
                welcome_options()
            else:
                print("Restaurant not deleted! Try again.")
                welcome_options()
        else:
            print("Restaurant does not exist! Try again.")       
            welcome_options()
    elif answer == "4":
        #Pick random restaurant
        randomize_restaurants()
        welcome_options()
    elif answer == "esc":
        exit()
    else:
        print("Sorry that is not an option please try again!")
        welcome_options()

def randomize_restaurants():
    #Turn dictionary into array to use random int
    random_restaurant_list = []
    for restaurant in restaurants:
        random_restaurant_list.append(restaurant)
    length = len(restaurants)
    random_restaurant = random.randint(1,length) 
    print(spacer)   
    print(random_restaurant_list[random_restaurant])
    print(spacer)

def save_changes():
    with open("restaurant_list.pkl", "wb") as pickle_file:
        pickle.dump(restaurants, pickle_file)     

print("Welcome to the Restaurant Picker!")
welcome_options()
