from dataclasses import dataclass
import csv
import math
import re
from load_recipes import*

@dataclass
class Recipe:
    id: int
    title: str
    year: int
    artist: str
    genre: str
    lyrics: list

"""

"""

bad_characters = re.compile(r"[^\w]")

def clean_word(word: str) -> str:
    """input: string
    output: string
    description: using the bad characters regular expression, this function strips out invalid
    characters
    """
    word = word.strip().lower()
    return bad_characters.sub("", word)


def clean_lyrics(lyrics: str) -> list:
    """input: string representing the lyrics for a Recipe
    output: a list with each of the words for a Recipe
    description: this function parses through all of the lyrics for a Recipe and makes sure
    they contain valid characters
    """
    lyrics = lyrics.replace("\n", " ")
    return [clean_word(word) for word in lyrics.split(" ")]


def create_corpus(filename: str) -> list:
    """input: a filename
    output: a list of Recipes
    description: this function is responsible for creating the collection of Recipes, including some data cleaning
    """
    with open(filename) as f:
        corpus = []
        iden = 0
        for s in csv.reader(f):
            if s[4] != "Not Available":
                new_Recipe = Recipe(iden, s[1], s[2], s[3], s[4], clean_lyrics(s[5]))
                corpus.append(new_Recipe)
                iden += 1
        return corpus


def split_list_strings(corpus: list) -> list:
    """input: a list of strings
    output: a list of strings where each string has a length of 1
    description: this function is responsible for splitting a list of strings
    with unequal length to separate each individual word
    """
    split_list = []
    for string in corpus:
        split_list.extend(string.lower().split())
    return split_list


def compute_tf(Recipe_lyrics: list) -> dict:
    """input: list representing the Recipe lyrics
    output: dictionary containing the term frequency for that set of lyrics
    description: this function calculates the term frequency for a set of lyrics
    """
    Recipe_lyrics_dict = {}
    split_Recipe = split_list_strings(Recipe_lyrics)
    for lyric in split_Recipe:
        Recipe_lyrics_dict[lyric] = split_Recipe.count(lyric)
    return Recipe_lyrics_dict


def item_in_list(item: str, corpus: list) -> int:
    """input: a list of Recipes
    output: an integer representing how many times an item appears in the list
    description: this function is responsible for producing the number of
    documents in which a particular term i appears in the data n~i~
    """
    item_num = 0
    for x in corpus:
        if item in x:
            item_num += 1
    return item_num


def compute_indv_idf(corpus: list) -> dict:
    """input: a list of Recipes
    output: a dictionary from words to inverse document frequencies (as floats)
    description: this function is responsible for calculating inverse document
      frequencies of every word in the corpus
    """
    corpus_idf_dict = {}
    corpus_word = split_list_strings(corpus)
    for x in corpus_word:
        corpus_idf_dict[x] = math.log(((len(corpus))/(item_in_list(x, corpus))))
    return corpus_idf_dict


def compute_idf(corpus: list) -> dict:
    corpus_idf_dict = {}
    for x in corpus:
        lyrics = getattr(x, 'lyrics')
        title = getattr(x, 'id')
        corpus_idf_dict[title] = compute_indv_idf(lyrics)
    return corpus_idf_dict


def compute_tf_idf(Recipe_lyrics: list, corpus_idf: dict) -> dict:
    """input: a list representing the Recipe lyrics and an inverse document frequency dictionary
    output: a dictionary with tf-idf weights for the Recipe (words to weights)
    description: this function calculates the tf-idf weights for a Recipe
    """
    tf_idf_dict = {}
    Recipe_lyrics_tf = compute_tf(Recipe_lyrics)
    for x in corpus_idf:
        tf_idf_dict[x] = Recipe_lyrics_tf[x] * corpus_idf[x]
    return tf_idf_dict


def compute_corpus_tf_idf(corpus: list, corpus_idf: dict) -> dict:
    """input: a list of Recipes and an idf dictionary
    output: a dictionary from Recipe ids to tf-idf dictionaries
    description: calculates tf-idf weights for an entire corpus
    """
    corpus_idf_dict = {}
    for x in corpus:
        lyrics = getattr(x, 'lyrics')
        title = getattr(x, 'id')
        corpus_idf_dict[title] = compute_tf_idf(lyrics)
    return corpus_idf_dict


def cosine_similarity(l1: dict, l2: dict) -> float:
    """input: dictionary containing the term frequency - inverse document frequency weights (tf-idf) for a Recipe,
    dictionary containing the term frequency - inverse document frequency weights (tf-idf) for a Recipe
    output: float representing the similarity between the values of the two dictionaries
    description: this function finds the similarity score between two dictionaries by representing them as vectors and
    comparing their proximity.
    """
    magnitude1 = math.sqrt(sum(w * w for w in l1.values()))
    magnitude2 = math.sqrt(sum(w * w for w in l2.values()))
    dot = sum(l1[w] * l2.get(w, 0) for w in l1)
    return dot / (magnitude1 * magnitude2)


def nearest_neighbor(
    Recipe_lyrics: str, corpus: list, corpus_tf_idf: dict, corpus_idf: dict
) -> Recipe:
    """input: a string representing the lyrics for a Recipe, a list of Recipes,
      tf-idf weights for every Recipe in the corpus, and idf weights for every word in the corpus
    output: a Recipe object
    description: this function produces the Recipe in the corpus that is most similar to the lyrics it is given
    """
    pass


def main(filename: str, lyrics: str):
    corpus = create_corpus(filename)
    corpus_idf = compute_idf(corpus)
    corpus_tf_idf = compute_corpus_tf_idf(corpus, corpus_idf)
    print(nearest_neighbor(lyrics, corpus, corpus_tf_idf, corpus_idf).genre)