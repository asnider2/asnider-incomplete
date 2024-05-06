from get_recipe import *
from get_recipe import AllRecipes

#Running the program

# Run and follow script


if __name__ == "__main__":
    while True:
        # Ask the user for the ingredient to search for
        user_ingredient = input("Enter the ingredient to search for recipes (enter 'quit' to exit): ").strip('"')

        # Check if the user wants to quit
        if user_ingredient.lower() == 'quit':
            break

        recipes_data = AllRecipes.get_dinner_ideas(user_ingredient)
        print("Recipe Names Found:")
        for index, recipe_data in enumerate(recipes_data, 1):
            print(f"{index}: {recipe_data['name']}")

        # Ask user to select a recipe for more details
        while True:
            try:
                recipe_choice = input("Enter the number of the recipe you want details for (enter 0 to skip, 'quit' to exit): ")
                if recipe_choice.lower() == 'quit':
                    break
                elif recipe_choice == '0':
                    break
                else:
                    recipe_choice = int(recipe_choice) - 1
                    selected_recipe_url = recipes_data[recipe_choice]['url']
                    break
            except (ValueError, IndexError):
                print("That's not a valid input. Please enter a number corresponding to a recipe, 0 to skip, or 'quit' to exit.")

            if recipe_choice.lower() == 'quit':
                break

        if recipe_choice == '0':
            # Skip directly to searching for another recipe or exit
            continue

        # Fetch detailed recipe information using the URL
        detailed_info = AllRecipes.get(selected_recipe_url)
        print("\nSelected Recipe Details:")
        print(f"Name: {detailed_info['name']}")

        # Ask if the user wants to see the ingredients
        see_ingredients = input("Do you want to see the ingredients for this recipe? (yes/no, 'quit' to exit): ")
        if see_ingredients.lower() == 'quit':
            break
        elif see_ingredients.lower() == 'yes':
            print("Ingredients:")
            for ingredient in detailed_info['ingredients']:
                print(f"- {ingredient}")

        # Ask if the user wants to see the steps
        see_steps = input("Do you want to see the directions for this recipe? (yes/no, 'quit' to exit): ")
        if see_steps.lower() == 'quit':
            break
        elif see_steps.lower() == 'yes':
            print("Steps:")
            for step_number, step in enumerate(detailed_info['steps'], start=1):
                print(f"Step {step_number}: {step}")

        # Ask the user if they want to search again
        search_again = input("Do you want to find another recipe? (yes/no, 'quit' to exit): ")
        if search_again.lower() != 'yes':
            break
        elif search_again.lower() == 'quit':
            break

#if denied run this line first
#chmod +x get_recipe.py
