import pytest
from scraper import*

example_listings ={
'CityA': [Listing(city='CityA', price=1000, bedrooms=1, description='Nice and cozy')],
'CityB': [Listing(city='CityB', price=2000, bedrooms=2, description='Nice view')],
'Atlamta' : [Listing(city= "Atlamta",price=1500, bedrooms=3, description="Atlanta apartment 1")]}

def test_average_bed():
    expected_average = 2
    empty_listings = {}
    empty_expected_average = 0

    assert average_bed(example_listings) == expected_average
    assert average_bed(empty_listings) == empty_expected_average
def test_highest_price():
    expected_city = 'CityB'
    assert highest_price(example_listings, 2) == expected_city
def test_word_common_city():
    expected_word = 'nice'
    assert word_common_city(example_listings) == expected_word

all_listings = scrape_craigslist_data()

print(all_listings)