import sys
from urllib.parse import quote
from urllib.request import Request, urlopen

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)


def get_page(url):
    request = Request(url)
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) '
                       'Chrome/19.0.1036.7 Safari/535.20')
    response = urlopen(request)
    data = response.read()
    return data


def did_you_mean(query, source_language="auto"):
    query = str(query).strip()
    url = "https://translate.google.com/#view=home&op=translate&sl=%s&tl=fr&text=" % source_language + quote(query)

    driver.get(url)
    div = driver.find_element_by_class_name("spelling-correction")
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
