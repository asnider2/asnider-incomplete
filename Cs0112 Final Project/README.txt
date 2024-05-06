Goal
This section should describe, in your own words, the goal of your project.
The goal of this project is to provide users with recipe ideas, ingredients, and preparation steps based on a specific
ingredient they have. Originally, the intention was to allow users to input a list of ingredients they have on hand and find recipes that match those ingredients. 
However, due to challenges in cross-referencing ingredients, the approach was adjusted to simply ask the user for a single ingredient and provide recipe suggestions 
based on that ingredient.

The goal of this project is to find recipes ideas, ingredients and steps based on a specfic item that you have.

Implementation
This section should describe the actual implementation of your project.
What design decisions did you make? What data structures did you use? What functions, classes, and methods did you
develop, and what were they for?

Search Functionality:
The search method in the AllRecipes class performs a search on the AllRecipes website based on a given ingredient.
It retrieves relevant recipe data such as name, URL, rating, and image.

Getting the Recipe:
The get method in the AllRecipes class retrieves detailed information about a specific recipe by fetching the recipe's
webpage using its URL. It then extracts the recipe's name, list of ingredients, and preparation steps, organizing them
into a dictionary.

User Interaction:
The script interacts with the user in a simple command-line interface. It prompts the user to input an ingredient to
search for recipes. After displaying the search results, the user can select a recipe for more details. The script then
presents the detailed recipe information, including the list of ingredients. Optionally, the user can choose to view
the preparation steps.

Results
This section should describe the results of your hard work.
Did you accomplish all of your goals? Feel free to include any measurements you did,
example program inputs and outputs, or screenshots. This is also the place to tell us about testing: how did you ensure
that your code is correct?

My original goal was for the input to be a list of ingredients that you had laying around but I had problems finding
ways to cross reference ingredients. Instead I had the script ask if you want to see the steps after viewing the
ingredients to see if you have them. I didn't test my code in the traditional way. I tested the script commands by
putting invalid answers.
