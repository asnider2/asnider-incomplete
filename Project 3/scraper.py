from bs4 import BeautifulSoup
# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
Place your answers to the Design check questions here:

1. The listings are structured under a class called "results cl-results-page" and each listing is a class itself. In
those listing classes there are classes for the details and the info like price bedrooms etc is in a list

2. We can directly use the data but we have to probably convert the information into numerical values and exclude
listings that do not have all the fields we want

3.I will probably structure my data as a class calle dlisting with properties like title price bedrooms etc.

4. Because we are looking to to find the average number of bedrooms across all of the cities,  find the city with the
highest average price for a given number of bedrooms and the most commonly-occuring “interesting” word in a citymy
query functions will be called average_bed(Listing)-> float, highest_price(Listing)-> int, and word_common_city(Listing)-> List

"""
################## CHROME ###################
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    """Change only if you are using a different browser. Default on the stencil is google chrome."""
    service = ChromeService(ChromeDriverManager().install())
    return webdriver.Chrome(service=service)
#############################################

##################### DO NOT CHANGE #######################

def craigslist_get_city(city_name: str, driver: webdriver):
    """Returns a BeautifulSoup object for a given city from Craigslist"""


    url = f"https://{city_name}.craigslist.org/search/apa"
    driver.get(url)

    ## The difference here from previous webscraping examples done in lab/class is this one step!
    ## Instead of using requests, we will be using a driver.
    try:
        # WebDriverWait with EC is used to stop program execution temporarily
        # until the specified condition is met or the maximum wait time is reached
        # Here, we wait up to 10 seconds before timing out if it does not find the elements with the class name 'result-title'.
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "result-title"))
        )
    except Exception as e:
        print("Exception while waiting for page elements:", e)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    return soup

def local_get_city(city_name: str) -> BeautifulSoup:
    """Returns a BeautifulSoup object for a given city from the local filesystem"""

    # Files must be in this directory
    file_template = "localdata/{}.html"
    try:
        with open(file_template.format(city_name), "r") as f:
            return BeautifulSoup(f.read(), "html.parser")
    except:
        raise NoCityError("No city named {} found".format(city_name))
##################### DO NOT CHANGE #######################


CITIES = [
    "providence",
    "atlanta",
    "austin",
    "boston",
    "chicago",
    "dallas",
    "denver",
    "detroit",
    "houston",
    "lasvegas",
    "losangeles",
    "miami",
    "minneapolis",
    "newyork",
    "philadelphia",
    "phoenix",
    "portland",
    "raleigh",
    "sacramento",
    "sandiego",
    "seattle",
    "washingtondc",
]


class NoCityError(Exception):
    pass

class Listing:
    def __init__(self, city, price, bedrooms ,description):
        self.location = city
        self.price = price
        self.bedrooms = bedrooms
        self.description = description


def scrape_data(city_pages: dict):
    """Scrapes data from a collection of pages.
    The keys of city_pages are city names. The values are BeautifulSoup objects."""
    options = []
    for city, soup in city_pages.items():
        for listing in soup.find_all("li",class_="result-row"):
            #get price
            price_text = listing.find("span", class_="result-price")
            if price_text:
                price= int(price_text.test.strip('$'))
            else:
                None
            #get bedrooms
            bedrooms_text = listing.find("span", class_= 'housing')
            if bedrooms_text:
                bedrooms= int(bedrooms_text.strip().split("br")[0])
            else:
                 None
            #get desciption
            desc_text = listing.find("a", class_= 'result-title hdrlnk')
            if desc_text:
                desc = int(desc_text.strip().split("br")[0])
            else:
                 None
            #update list
            if price and bedrooms and desc:
                valid_match = Listing(price, bedrooms, desc)
                options.append(valid_match)
    return options

def scrape_craigslist_data():
    """Scrape data from Craigslist"""
    return scrape_data({city: craigslist_get_city(city, get_driver()) for city in CITIES})


def scrape_local_data():
    """Scrape data from the local filesystem"""
    return scrape_data({city: local_get_city(city) for city in CITIES})


def interesting_word(word: str) -> bool:
    """Determines whether a word in a listing is interesting"""
    return word.isalpha() and word not in [
        "to",
        "at",
        "your",
        "you",
        "and",
        "for",
        "in",
        "the",
        "with",
        "bedroom",
        "bed",
        "bath",
        "unit",
    ]

def average_bed(city_listings: dict) -> float:
    """Calculate the average number of bedrooms across all listings in all cities."""
    total_bedrooms = 0
    count = 0
    for listings in city_listings.values():
        for listing in listings:
            if listing.bedrooms is not None:
                total_bedrooms += listing.bedrooms
                count += 1
    if count > 0:
        return total_bedrooms / count
    else:
        return 0

def highest_price(city_listings: dict, num_bedrooms: int) -> str:
    highest_avg_price = 0
    city_with_highest_price = None
    for city, listings in city_listings.items():
        filtered_listings = []
        total_price = 0
        for listing in listings:
            if listing.bedrooms == num_bedrooms:
                filtered_listings.append(listing)
                total_price += listing.price

        if filtered_listings:
            avg_price = total_price / len(filtered_listings)
            if avg_price > highest_avg_price:
                highest_avg_price = avg_price
                city_with_highest_price = city

    return city_with_highest_price


def word_common_city(city_listings: dict) -> str:
    """Find the most commonly occurring 'interesting' word in all listings."""
    word_count = {}
    for city, listings in city_listings.items():
        for listing in listings:
            words = listing.description.lower().split()
            for word in words:
                if interesting_word(word):
                    word_count[word] = word_count.get(word, 0) + 1
    return max(word_count, key=word_count.get, default=None)