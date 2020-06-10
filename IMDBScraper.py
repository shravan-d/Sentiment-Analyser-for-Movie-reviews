import urllib

import urllib.request
from bs4 import BeautifulSoup


#add link to the movie's imdb user reviews page
theurl = "https://www.imdb.com/title/tt6105098/reviews?ref_=tt_urv"
thepage = urllib.request.urlopen(theurl)
soup = BeautifulSoup(thepage, "html.parser")
i = 1
print(soup.title.text)
with open('reviews.txt', 'w') as f:
    for usereview in soup.find_all("div", {"class": "lister-item-content"}):
        f.write(usereview.find('a').text)



