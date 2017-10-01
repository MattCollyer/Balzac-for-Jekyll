Partner: Asad Malik
#
For our project we wanted to be able to take any instagram photo and turn it into ascii art. We did this by scraping the image source url and adding .html at the end. 

It works! (or at least it should)

Pretty neat stuff.

```
from bs4 import BeautifulSoup
import requests

print(Want to convert your Instagram photo into ASCII art?)
url = input('Enter your photo URL: ')

result = requests.get(url)
content = result.content
soup = BeautifulSoup(content, "html.parser")
url= soup.find("meta", property="og:image")
result1 = requests.get(url["content"]+".html")
content1 = result1.content

soup1 = BeautifulSoup(content1, "html.parser")
with open ("ASCII_art.html", "w") as f:
	f.write(str(soup1))

print('DONE! Check your directory!')
