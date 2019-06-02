[![Coverage Status](https://coveralls.io/repos/github/FilipTokarski/open_movie_database_api/badge.svg?branch=master)](https://coveralls.io/github/FilipTokarski/open_movie_database_api?branch=master)
# Open Movie Database api with Django REST Framework  

### Visit website here: https://ftdev.pl  

This project utilizes Django, Django Rest Framework and Open Movie Database API.  
It has three endpoints:
* /movies  
* /comments
* /top  
  
***
## /movies  
Get request reutrns list of all movies present in the database  
Post request requires a title:  
>{  
>   "Title": "Some movie title"  
>}  

It returns an object fetched from Omdb API and saves it to database.

## /comments  
Get request returns list of all comments. You can also filter commments based on movie id, example:  
>/comments/?movie_id=3  

Post request requires providing movie id and comment body, example:  
> {  
>  "movie": 1,  
>  "content": "Awesome movie!"  
>}  

## /top
Get request returns list of movies based on a number of comments, along with their rank. By default it lists an 'all time' ranking, but you can narrow the results by providing start and end dates, example:  
> /top/?date_start=2019-05-20&date_end=2019-05-25  

****  
To run this code on your local machine, please clone the repository to your local folder, create a Python virtual environment (Python version=3.7.2), activate it and install packages listed in requirements.txt file.  
Please be aware that this will also require setting up a PostgreSQL database - some orm commands may cause errors with Django's default SQLite database.  


````
python manage.py runserver
````