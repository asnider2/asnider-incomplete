import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import ssl

class AllRecipes(object):
    @staticmethod
    def search(search_string, sort_by='rating', order='desc'):
        """
        Search recipes by ingredient with options to sort by rating, prep time, etc.
        """
        base_url = "https://allrecipes.com/search?"
        query_url = urllib.parse.urlencode({"q": search_string})
        url = base_url + query_url
        req = urllib.request.Request(url)
        req.add_header('Cookie', 'euConsent=true')
        handler = urllib.request.HTTPSHandler(context=ssl._create_unverified_context())
        opener = urllib.request.build_opener(handler)
        response = opener.open(req)
        html_content = response.read()
        soup = BeautifulSoup(html_content, 'html.parser')
        search_data = []
        articles = soup.findAll("a", {"class": "mntl-card-list-items"})
        articles = [a for a in articles if a["href"].startswith("https://www.allrecipes.com/recipe/")]
        for article in articles:
            data = {}
            try:
                data["name"] = article.find("span", {"class": "card__title"}).get_text().strip()
                data["url"] = article['href']
                data["rating"] = len(article.find_all("svg", {"class": "icon-star"}))
                if article.find("svg", {"class": "icon-star-half"}):
                    data["rating"] += 0.5
                data["image"] = article.find('img').get('data-src', article.find('img').get('src'))
            except Exception as e:
                continue  # Skip if there's an error processing this article
            if data:
                search_data.append(data)
        if sort_by == 'rating':
            search_data.sort(key=lambda x: x.get('rating', 0), reverse=(order == 'desc'))
        return search_data

    @staticmethod
    def get_dinner_ideas(search_string):
        """
        Search for recipes and print each result, then return a list of recipe names.
        """
        search_results = AllRecipes.search(search_string)
        for result in search_results:
            print(result)
        # Extract just the names from the search results
        names_list = [recipe['name'] for recipe in search_results]
        return names_list

    @staticmethod
    def get(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        recipe = {
            "name": AllRecipes._get_name(soup),
            "ingredients": AllRecipes._get_ingredients(soup),
            "steps": AllRecipes._get_steps(soup)
        }
        return recipe

    @staticmethod
    def _get_name(soup):
        return soup.find("h1", class_="recipe-title").text.strip()

    @staticmethod
    def _get_ingredients(soup):
        ingredients_list = soup.find("ul", class_="ingredients-list")
        ingredients = [li.get_text().strip() for li in ingredients_list.find_all("li")]
        return ingredients

    @staticmethod
    def _get_steps(soup):
        steps_list = soup.find("ol", class_="directions-list")
        steps = [li.get_text().strip() for li in steps_list.find_all("li")]
        return steps

if __name__ == "__main__":
    while True:
        # Ask the user for the ingredient to search for
        user_ingredient = input("Enter the ingredient to search for recipes: ").strip('"')
        search_results = AllRecipes.search(user_ingredient)
        print("Recipe Names Found:")
        for index, recipe in enumerate(search_results, 1):
            print(f"{index}: {recipe['name']}")

        # Ask user to select a recipe for more details
        recipe_choice = int(input("Enter the number of the recipe you want details for: ")) - 1
        selected_recipe = search_results[recipe_choice]

        # Fetch detailed recipe information
        detailed_info = AllRecipes.get(selected_recipe['url'])
        print("\nSelected Recipe Details:")
        print(f"Name: {detailed_info['name']}")
        print("Ingredients:")
        for ingredient in detailed_info['ingredients']:
            print(f"- {ingredient}")
        print("Steps:")
        for step_number, step in enumerate(detailed_info['steps'], start=1):
            print(f"Step {step_number}: {step}")

        # Ask the user if they want to search again
        search_again = input("Do you want to search again? (yes/no): ")
        if search_again.lower() != 'yes':
            break
