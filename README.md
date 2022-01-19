# DevelopsToday assessment test

### Upvotes url:

`api/news/vote/<int:id>` 

## Heroku app:

[damp-sierra-17362](http://damp-sierra-17362.herokuapp.com/swagger/)

## Docker container:

```docker
docker build .
```

```docker
docker-compose build
```



## Postman Collection:

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/15166429-6dd4ddb7-c01f-4baa-bf89-11e7a85de2e5?action=collection%2Ffork&collection-url=entityId%3D15166429-6dd4ddb7-c01f-4baa-bf89-11e7a85de2e5%26entityType%3Dcollection%26workspaceId%3Dc6916df8-d42f-4837-bd7a-e22e57c6fbd3#?env%5BDevelopsToday%5D=W3sia2V5IjoidXJsIiwidmFsdWUiOiJodHRwOi8vZGFtcC1zaWVycmEtMTczNjIuaGVyb2t1YXBwLmNvbS8iLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6ImlkIiwidmFsdWUiOiIxIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJhdXRob3JfaWQiLCJ2YWx1ZSI6IjEiLCJlbmFibGVkIjp0cnVlfSx7ImtleSI6IlVzZXJuYW1lIiwidmFsdWUiOiJ1c2VyIiwiZW5hYmxlZCI6dHJ1ZX0seyJrZXkiOiJQYXNzd29yZCIsInZhbHVlIjoiQ2hhbmdlTWUiLCJlbmFibGVkIjp0cnVlfV0=)

## Local:
#### Clone the repository.
Install pipenv:

`pip install pipenv`

#### Install dependencies: 

`pipenv install`

#### Run 

`pipenv shell`



#### Make and migrate 

`python manage.py makemigrations`
 
 `python manage.py migrate`
 
#### Run server
 
 `python manage.py runserver`
