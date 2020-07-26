import lxml
import re
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from requests import get

url = "https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2"
page = get(url)
soup = BeautifulSoup(page.content, 'lxml')

content = soup.find(id="main")
articleTitle = soup.find("h1", class_="header").text.replace("\n","")

    #movie frame
movie_frame = content.find_all("div",class_="lister-item mode-advanced")

    #first frame of movie list
movie_line = movie_frame[0].find("h3",class_='lister-item-header')
    #movie name
movie_name = movie_line.find("a").text  #The Old Guard
print(movie_name)

    #moviedate
movieDate = re.sub(r"[()]","", movie_line.find_all("span")[-1].text)  # '2020'
print(movieDate)

    ## for certificate runtime
movieseline = movie_frame[0].find("p",class_="text-muted")

    # movie runtime
movie_runtime = movieseline.find("span",class_="runtime").text[:-4]
print(movie_runtime)

    # movie certificate
movie_certificate = movieseline.find("span",class_="certificate").text
print(movie_certificate)

    # movie type or genere
movie_gener = movieseline.find("span",class_="genre").text[1:]
print(movie_gener)

    ## metascore of movie
moviethline = movie_frame[0].find("div",class_="ratings-bar")
m = moviethline.find("div",class_="inline-block ratings-metascore")
metascore = m.find("span").text[:-8]
print(metascore)

# movie_director
direct = movie_frame[0].find_all("p")[2]
movie_director = direct.find_all("a")[0].text
print(movie_director)




