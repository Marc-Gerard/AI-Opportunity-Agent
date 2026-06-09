import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    
    for tag in soup(["script", "style"]):
        tag.decompose()
    
    text = soup.get_text(separator=" ", strip=True)
    return text[:3000]