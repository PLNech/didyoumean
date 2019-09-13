import sys
import sys
import urllib
from urllib.parse import quote
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


def getPage(url):
    request = Request(url)
    request.add_header('User-Agent',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20')
    response = urlopen(request)
    data = response.read()
    return data


def didYouMean(q):
    q = str(str.lower(q)).strip()
    url = "http://www.google.com/search?q=" + quote(q)
    html = getPage(url)
    soup = BeautifulSoup(html, 'html.parser')
    async_contexts = [item.attrs["data-async-context"] for item in soup.find_all() if
                      "data-async-context" in item.attrs]
    result = urllib.parse.unquote([q for q in async_contexts if "query:" in q][0].replace("query:", ""))
    return result


if __name__ == "__main__":
    if len(sys.argv) > 1:
        arg = sys.argv[1]
    else:
        arg = "vequ orloff"
    response = didYouMean(arg)
    print(response)
