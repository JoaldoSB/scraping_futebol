import requests
from bs4 import BeautifulSoup

# URL da página de busca da notícia
url = "https://ge.globo.com/espiao-estatistico/"

# Fazendo a requisição HTTP
response = requests.get(url)
html = response.text

# Parsing do HTML com BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Procurando as manchetes das notícias
noticias = soup.find_all('a', class_='feed-post-link')

print("espião estatística:\n")
for noticia in noticias[:5]:  # Limite de 5 notícias
    titulo = noticia.get_text(strip=True)
    link = noticia['href']
    print(f"- {titulo}\n  {link}")
