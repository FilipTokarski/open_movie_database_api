# Open Movie Database api with Django REST Framework  

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

## /top/
Get request returns list of movies based on a number of comments, along with their rank. By default it lists an 'all time' ranking, but you can narrow the results by providing start and end dates, example:  
> /top/?date_start=2019-05-20&date_end=2019-05-25  

****  
