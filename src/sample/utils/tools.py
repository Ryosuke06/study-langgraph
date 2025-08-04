from langchain_community.utilities import WikipediaAPIWrapper
from langchain_core.tools import tool
from langchain_google_community import GoogleSearchAPIWrapper

search = GoogleSearchAPIWrapper()
wiki = WikipediaAPIWrapper()

# おまじない。
# これにより、Function callingに乗っ取ったFMTのデータにコンパイルされる。
@tool
def searchGoogle(query: str):
    """Use this to get information from Google Search. (Do not use this tool in parallel processing)"""
    return search.results(query=query, num_results=10)

# おまじない。
# これにより、Function callingに乗っ取ったFMTのデータにコンパイルされる。
@tool
def searchWikipedia(query: str):
    """Use this to get information from Wikipedia."""
    return wiki.run(query)

# おまじないで作ったtoolを配列で包んで変数としておいておくだけ。
# さきほどnode.pyとかで参照されてた。
tools = [searchGoogle, searchWikipedia]