# assignment

## install python library
	-lxml
	-BeautifulSoup
	-pandas
	-numpy
## Dependencies
	Python 3.6.x
	django 2.1.x
	ubuntu 18.04
### 1. Extract the data from IMDB movie website 
	- run imdbwebscrap.py
	- data are store in csv form 
### 2. from .csv we can generating the question and store in question.txt
	-here we have total 30 question
	-each question have 4 option 
### 3. migration database
	-python manage.py makemigration
	-python manange.py migrate
### 4. create superuser
	-python manage.py createsuperuser
### 5. Run development server
	-python manage.py runserver
### 6. there have two type of database
	-username,password and score 
	-question
### 7. At first page is look like 
	![home page](/images/4.png)
### 8. new registration 
	-provide the username and password
	- verify the username >> open code.txt 
	- enter the verify code than you are registration
	-During the registration the score of user set value 1 
	![registration](/images/5.png)
### 9. login 
	- enter the username and password
	![login](/images/7.png)
### 10. after login start a game quiz
	![quiz](/images/6.png)
	- 10 question is appear randomly and dynamically from the set of 30 question
	



# asignment
