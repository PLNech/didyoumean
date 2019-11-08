import logging
import sys
from urllib.parse import quote

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')

# logging.basicConfig(level=logging.INFO)
log = logging.getLogger()


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
    # log.debug(driver.execute_script("return document.documentElement.outerHTML;"))
    div = driver.find_element_by_id("spelling-correction")
    log.info("<div>: [%s]" % div.get_attribute('innerHTML'))
    try:
        a = div.find_element_by_tag_name("a")
        a_html = a.get_attribute('innerHTML')
        log.info("<a>: [%s]" % a_html)
        if len(a_html):
            div = a
    except NoSuchElementException:
        pass
    suggestion = div.text.replace("Did you mean:", "").strip()
    log.info("Suggestion: %s" % suggestion)
    return suggestion if len(suggestion) else query


if __name__ == "__main__":
    if len(sys.argv) > 2:
        result = did_you_mean(sys.argv[1], sys.argv[2])
    elif len(sys.argv) > 1:
        result = did_you_mean(sys.argv[1])
    else:
        result = did_you_mean("steak hache  grille")
    print("Suggestion:", result)
