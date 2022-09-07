# Author: Hanifa and Hadassah
import requests

# Define the app id and key to obtain the API url
app_id = 'cfa351f0'
app_key = '2cb19dac6e5fcd7360a95967167b5b1b'

# Get ingredient from user
ingredient: str = input("Enter an ingredient: ")

# Words to use to test the input: cheese, tomato, butter

# Author:hadassah
# Try to ask additional question but only ran into errors
# Get dietary needs from users
# dietary: str = input("Enter a preferred dietary need?  ")
# words to use gluten free, vegetarian, vegan,celiac,kids meal,e.t.c
# Get the amount of time they want to send making this
# time: str = input("How long max would you like to work of this recip ?")
# time 40 minutes

# Get the relevant API url based on the user input
url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)
response = requests.get(url)

# Get output into json format
recipe = response.json()

# Authors: Hanifa and Amiira and Hadassah

# Project: Create a search engine that will take ingredients and give a
# recipe given the ingredients.

# from random import randrange For picking out a recipe

# pprint(recipe)  # Pretty print the API response and inspect
recipe_list = recipe['hits']  # Find the relevant list with dictionaries inside

# THE FOLLOWING CODE IS A MISTAKE ###
#  Pick a random recipe
# recipe_number = int(recipe['to'])  # Get total number of recipes
# index = randrange(recipe_number)  # Get random number within the total
#
#  Get single recipe to work from
# single_recipe = recipe_list[index]
# pprint(single_recipe)
# # Print the ingredients
# print('You will need: \n')
# pprint(single_recipe['recipe']['ingredientLines'])
# # Print the instructions
# print('\nInstructions: \n')
# END OF MISTAKE SECTION ##

# Create a for loop that goes through every item in the list of recipes
for recipe in recipe_list:
    print(recipe['recipe']['label'] + ':')  # Print the title of the recipe
    print(recipe['recipe']['url'] + '\n')  # Print the url to the recipe

# Author: Hanifa
# Extended Task
# Re-order recipe_list based on the number of elements in the 'ingredientLines' list
ordered_recipeList = sorted(recipe_list, key=lambda x: len(x['recipe']['ingredientLines']))

# Print the new ordered list
print('Ordered recipe list: From lowest ==> highest no. ingredients')
for recipe in ordered_recipeList:
    print(recipe['recipe']['label'] + ':')
    print(recipe['recipe']['url'] + '\n')


# Author : Hadassah
# Extended Task : Save the results to a file
def save(food, list_of_recip):
    f = open("saving.txt", "w")
    f.write("This is what you searched before: ")
    f.write("\n")
    f.write("{}\n".format(food))
    f.write("\n")
    f.write("{}\n".format(list_of_recip))
    print("SAVED")
    f.close()

    if input("Would you like to see what you have saved ? (y/n) ") == 'y':
        f = open("saving.txt", "r")
        print(f.read())
    else:
        print("You can always check when your ready :)")
        return


pass

if input("Would you like to save? (y/n) ") == 'y':
    save(ingredient, recipe)
else:
    print("You can always save whenever your ready :)")
