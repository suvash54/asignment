import lxml
import re
import numpy as np
import pandas as pd

from bs4 import BeautifulSoup
from requests import get

url1 = "https://www.imdb.com/search/title?count=100&title_type=feature,tv_series&ref_=nv_wl_img_2"

class IMDB(object):
	"""docstring for IMDB"""
	def __init__(self, url):
		super(IMDB, self).__init__()
		page = get(url)

		self.soup = BeautifulSoup(page.content, 'lxml')

	def articleTitle(self):
		return self.soup.find("h1", class_="header").text.replace("\n","")

	def bodyContent(self):
		content = self.soup.find(id="main")
		return content.find_all("div", class_="lister-item mode-advanced")

	def movieData(self):
		movieFrame = self.bodyContent()
		movieTitle = []

		movieDate = []
		movieRunTime = []
		movieGenre = []
		#movieRating = []
		#movieScore = []
		#movieDescription = []
		movieDirector = []
		movieStars = []
		#movieVotes = []
		#movieGross = []
		moviecerti = []
		movietype = []
		moviemetascore = []
		for movie in movieFrame:
			movieFirstLine = movie.find("h3", class_="lister-item-header")
			movi_name = movieFirstLine.find("a").text
			movie_date = re.sub(r"[()]","", movieFirstLine.find_all("span")[-1].text)
			try:
				movie_runtime = movie.find("span", class_="runtime").text[:-4]
			except:
				pass
			movieseline = movie.find("p", class_="text-muted")
			movie_genere = movieseline.find("span", class_="genre").text[1:]

			try:
				movie_certi = movieseline.find("span", class_="certificate").text
			except:
				pass
			moviethline = movie.find("div", class_="ratings-bar")

			try:
				m = moviethline.find("div", class_="inline-block ratings-metascore")
				metascore = m.find("span").text[:-8]
			except:
				pass







			direct = movie.find_all("p")[2]
			movie_director = direct.find_all("a")[0].text
			if movie_runtime:
				if movie_certi:
					if metascore:
						movieTitle.append(movi_name)
						movieDate.append(movie_date)
						movieRunTime.append(movie_runtime)
						movieGenre.append(movie_genere)
						moviecerti.append(movie_certi)
						moviemetascore.append(metascore)
						movieDirector.append(movie_director)

			'''
			movieTitle.append(movieFirstLine.find("a").text)
			
			movieDate.append(re.sub(r"[()]","", movieFirstLine.find_all("span")[-1].text))
			try:
				movieRunTime.append(movie.find("span", class_="runtime").text[:-4])
			except:
				movieRunTime.append(np.nan)
			movieseline = movie.find("p", class_="text-muted")
			movieGenre.append(movieseline.find("span",class_="genre").text[1:])

			try:

				moviecerti.append(movieseline.find("span",class_="certificate").text)
			except:
				moviecerti.append(np.nan)

			try: #meta score
				moviethline = movie.find("div", class_="ratings-bar")
				m = moviethline.find("div", class_="inline-block ratings-metascore")
				metascore = m.find("span").text[:-8]
				moviemetascore.append(metascore)
			except:
				moviemetascore.append(np.nan)

			try:  # director
				direct = movie.find_all("p")[2]
				movie_director = direct.find_all("a")[0].text
				movieDirector.append(movie_director)
			except:
				movieDirector.append(np.nan)

			if movieRunTime:
				print(movieRunTime)'''


		movieData = [movieTitle,movieDate,movieRunTime,movieGenre,moviecerti,moviemetascore,movieDirector]

		return movieData






'''
			movieCast = movie.find("p", class_="")

			try:
				casts = movieCast.text.replace("\n","").split('|')
				casts = [x.strip() for x in casts]
				casts = [casts[i].replace(j, "") for i,j in enumerate(["Director:", "Stars:"])]
				movieDirector.append(casts[0])
				movieStars.append([x.strip() for x in casts[1].split(",")])
			except:
				casts = movieCast.text.replace("\n","").strip()
				movieDirector.append(np.nan)
				movieStars.append([x.strip() for x in casts.split(",")])
'''





if __name__ == '__main__':
	site1 = IMDB(url1)
	print("Subject: ", site1.articleTitle())
	data = site1.movieData()
	print(len(data[0]))
	col = ['movieTitle','movieDate','movieRunTime','movieGenre','moviecerti','moviemetascore','movieDirector']
	da = {}
	for i in range(len(data)):
		da[col[i]]=data[i][:20]

		#print(data[i][:])
	df = pd.DataFrame(da,columns=['movieTitle','movieDate','movieRunTime','movieGenre','moviecerti','moviemetascore','movieDirector'])
	#df.columns = [movieTitle,movieDate,movieRunTime,movieGenre,moviecerti,moviemetascore,movieDirector]
	df.to_csv(r'imdb.csv',index = False, header=True)
	print(df)