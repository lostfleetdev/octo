from duckduckgo_search import DDGS
from newspaper import Article

def swfl(query, num_results=5): # search web for link
    results = DDGS().text(query, max_results=num_results)
    links = [result["href"] for result in results]
    return links

"""
from bs4 import BeautifulSoup
import requests
import re



def swfl(query, num_results=5): # search web for link
    results = DDGS().text(query, max_results=num_results)
    links = [result["href"] for result in results]
    return links

def l2txt(link):  # link to cleaned text
    r = requests.get(link)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    # Remove script and style elements
    for script_or_style in soup(["script", "style"]):
        script_or_style.decompose()
    
    # Get text and clean extra spaces
    text = soup.get_text()
    text = re.sub(r'\s+', ' ', text).strip()  # Collapse whitespace and trim
    return text 
    
"""

def main():
    lin = swfl("obama", 3)
    t = 
    
    with open("data.txt", "w", encoding="utf-8") as f:
       f.write(t)

if __name__ == "__main__":
    main()