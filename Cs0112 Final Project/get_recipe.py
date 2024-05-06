import requests
from bs4 import BeautifulSoup
import urllib.parse
import urllib.request
import ssl

class AllRecipes(object):
    @staticmethod
    def search(search_string, sort_by='rating', order='desc'):
        """
        Search for recipes by ingredient.

        Parameters:
        - search_string (str): The ingredient to search for.
        - sort_by (str): The sorting criteria ('rating' by default).
        - order (str): The order of sorting ('desc' by default).

        Returns:
        - list: A list of dictionaries containing recipe information.
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
        Search for recipes based on the given ingredient and print the results.

        Parameters:
        - search_string (str): The ingredient to search for.

        Returns:
        - list: A list of dictionaries containing recipe names and URLs.
        """
        search_results = AllRecipes.search(search_string)
        for result in search_results:
            print(result)
        # Extract just the names and URLs from the search results
        recipes_data = [{"name": recipe['name'], "url": recipe['url']} for recipe in search_results]
        return recipes_data

    @staticmethod
    def get(url):
        """
        Get detailed information about a recipe from the given URL.

        Parameters:
        - url (str): The URL of the recipe.

        Returns:
        - dict: A dictionary containing detailed recipe information.
        """
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
        """
        Extract the name of the recipe from the BeautifulSoup object.

        Parameters:
        - soup (BeautifulSoup): The BeautifulSoup object of the recipe page.

        Returns:
        - str: The name of the recipe.
        """
        return soup.find("span", class_="card__title-text").text.strip()

    @staticmethod
    def _get_ingredients(soup):
        """
        Extract the ingredients of the recipe from the BeautifulSoup object.

        Parameters:
        - soup (BeautifulSoup): The BeautifulSoup object of the recipe page.

        Returns:
        - list: A list of ingredients.
        """
        ingredients_list = soup.find("ul", class_="mntl-structured-ingredients__list")
        if ingredients_list:
            ingredients = [li.get_text().strip() for li in ingredients_list.find_all("li")]
            return ingredients
        else:
            return []

    @staticmethod
    def _get_steps(soup):
        """
        Extract the preparation steps of the recipe from the BeautifulSoup object.

        Parameters:
        - soup (BeautifulSoup): The BeautifulSoup object of the recipe page.

        Returns:
        - list: A list of preparation steps.
        """
        steps_list = soup.find("ol", class_="mntl-sc-block-group--OL")
        if steps_list:
            steps = [li.find("p").get_text().strip() for li in steps_list.find_all("li")]
            return steps
        else:
            return []
