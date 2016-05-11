# Flocabulary Engineering Interview
## Problem Description
As the programming step in our interview process, your challenge is to implement a URL shortener in Django, using MySQL or Postgres as a database and ReactJS on the front end. 

You should host your application on Heroku, and explain some of the key decisions you faced in building the application. 

Please share the code with us in the form of a GitHub repository.

We look forward to seeing your work!

## Implementation Notes
I used the following tools for this project:

- Django
- Django Rest Framework
- Postgres
- Heroku

There are three options for interacting with this application.

__Application frontend__

View results in react tables, add results in form through REST API.

https://get-url-shorty.herokuapp.com/

__Direct Link to Short URL__

View or share a link directly. This will forward you to the site mapped to this short URL.

https://get-url-shorty.herokuapp.com/<short-url>

ex. http://127.0.0.1:8000/k

_API Endpoints_

Use the graphical navigation built in to these endpoints from Django REST Framework or, use the same endpoints with curl or httpie. These endpoints use ID (from the Postgres database) rather than short URL for reference.

_API Root_ https://get-url-shorty.herokuapp.com/api/
_URL List_ https://get-url-shorty.herokuapp.com/api/url/
_URL Detail_ https://get-url-shorty.herokuapp.com/api/url/<id>/
_Go to URL_ http://127.0.0.1:8000/api/url/<id>/go/

## Future Improvements
- Authentication (integration with social login)
- Improve test coverage for Django models, etc.
- Add stats tracking for each URL (display stats on a tracking page for each URL).
- Add pagination for List of URLS on homepage
- Make creation of new Short URL optimistic (display before response is processed)
- Manage state using Redux rather than React/jQuery
- alternate/more fun implementations of the url_converter class (maybe use dictionary words like xkcd correct horse battery staple passwords!)
