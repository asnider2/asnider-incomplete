from dataclasses import dataclass
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import requests
from bs4 import BeautifulSoup
import json

@dataclass
class Recipe:
    name: str
    time: str
    serving_size: int
    instructions: list
    ingredients: list

def get_driver():
    """Change only if you are using a different browser. Default on the stencil is google chrome."""
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)

def scrape_recipe_page(url):
    """Scrapes a single webpage and saves the information in a dataclass called Recipe."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    name = soup.find('h1', class_='entry-title').text.strip()

    time = soup.find('span', class_='recipe-time').text.strip()
    serving_size = int(soup.find('span', class_='serving-size').text.strip())

    ingredients = [li.text.strip() for li in soup.find_all('li', class_='ingredient')]
    instructions = [p.text.strip() for p in soup.find_all('p', class_='recipe-directions')]

    return Recipe(name, time, serving_size, instructions, ingredients)

def scrape_all_recipes():
    """Scrapes all the recipes on Damn Delicious and saves to a dictionary of Recipe dataclasses."""
    url = "https://damndelicious.net/recipe-index/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    recipe_links = [article.find('h2', class_='entry-title').a['href'] for article in soup.find_all('article', class_='post')]

    recipes = {}

    for link in recipe_links:
        recipe = scrape_recipe_page(link)
        recipes[recipe.name] = recipe

    return recipes

# Call the function and store the result in a variable
recipe_dict = scrape_all_recipes()