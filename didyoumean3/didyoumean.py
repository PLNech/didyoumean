import sys
from urllib.parse import quote

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')



def did_you_mean(query, source_language="auto"):
    """
    Spell-checks a sentence.

    :param query: an input sentence to spellcheck.
    :param source_language: a specific language to translate from. Defaults to automated language detection.

    :return: the query after applying suggestions, or unmodified if none is found.
    """

    driver = webdriver.Chrome(options=options)
    query = str(query).strip()
    url = "https://translate.google.com/#view=home&op=translate&sl=%s&tl=en&text=" % source_language + quote(query)

    driver.get(url)
    div = driver.find_element_by_id("spelling-correction")
    a = div.find_element_by_tag_name("a")
    if a is not None:
        div = a
    suggestion = div.text.replace("Did you mean:", "").strip()
    return suggestion if len(suggestion) else query


if __name__ == "__main__":
    if len(sys.argv) > 2:
        result = did_you_mean(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        result = did_you_mean(sys.argv[1])
    else:
        result = did_you_mean("steak hache grille")
    print("Suggestion:", result)
