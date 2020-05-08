# URL Shortener Challenge

REST API built using the Django REST framework allowing users to create condensed versions of URLs with additional support for custom short links. Requirements:

  - python installed
  - familiarty with Django Restframework

# Usage
To create a new URL make a POST request to following end point http://localhost:8000/urls/

```
{
	"original_name": "my really long URL to be shortened",
	"latest_custom_url": "my cool short link"
}
```
Response:
```
{
    "original_name": "my-really-long-url-to-be-shortened",
    "shortened_version": "31071762",
    "latest_custom_url": "my-cool-short-link",
    "created_date": "2020-05-08T14:31:20.027329Z"
}
```
You can visit your new URL by navigating to the following endpoints:
  - http://localhost:8000/bit/31071762/ 
  - http://localhost:8000/bit/my-really-long-url-to-be-shortened/
  - http://localhost:8000/bit/my-cool-short-link/

And the output will be all the meta information about the URL along with some stats on how often its been visited.  Example:
```
{
    "id": 12,
    "original_name": "my-really-long-url-to-be-shortened",
    "shortened_version": "31071762",
    "latest_custom_url": "my-cool-short-link",
    "visits": {
        "total": 6,
        "grouped": {
            "2020-05-07": 1,
            "2020-05-08": 5
        }
    }
}
```


### Architectural Decisions (Acknowledgement of Shortcomings)
If you look at the Git history you'll notice this project was built from 10pm - 1am because I was on call for a different project hence had limited time here.  In retrospect I should have built this API in Flask (used daily at work) since I haven't touched Django for about a year and spent more time than I wanted looking at DJango documentation.  However, I wanted to demonstrate competence in the Framework.  

Django REST Framework was selected to leverage its out-of-the-box admin GUI and adherences to the MVC design pattern.  The glaring design flaw I committed for the sake of time is adding business logic to the views.  These operations would ideally be abstracted into a controller or middleware.  Other limitations are commented in the code. 

I would typically follow the repository pattern for this type of project and build an abstracted data or business logic layer.

Looking forward to talking through some of the other design choices and how it should ideally be designed.

### Installation

Set up your python virtual environment run the following commands in the root folder.

```sh
$ pip install django 
$ pip install djangorestframework
$ python manage.py makemigrations
$ python manage.py migrate 
$ python manage.py runserver
```

### Run Tests
```
./manage.py test
```