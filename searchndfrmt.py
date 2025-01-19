from duckduckgo_search import DDGS
import json

def swfl(query, num_results=5): # search web for link
    results = DDGS().text(query, max_results=num_results)
    links = [result["href"] for result in results]
    body = [result["body"] for result in results]
    return links, results, body

def frmtjson(links):
	dat = {'links' : links}
	return json.dumps(dat, indent=4, separators=(',', ':'))


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
    text = re.sub(r'+', ' ', text).strip()  # Collapse whitespace and trim
    return text 
    
"""