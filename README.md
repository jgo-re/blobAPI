# Blob API.
Simple Django backend for  a pastebin clone.

# Requirements
Install Python.

Create a `.env` file with 
```
DATABASE_URL=sqlite:///db.sqlite3
SECRET_KEY=DJANGO_SECRET_KEY
```

Change the `CORS_ALLOWED_ORIGINS` variable in `./blobAPI/settings.py` to allow localhost or live domains.

# Commands
`python3 -m venv venv` - create python environment for project.

`. \venv\Scripts\activate` - activate python environment.

`pip install -r requirements.txt` - install packages from requirements.

`python manage.py runserver` - run the server.


# Endpoints
Retrieving an entry:
`GET /b/{key}` 

```
{
    "Key": "{key}",
    "Value": "This is a value",
    "CreatedOn": "2022-04-17T22:59:56.551795Z"
}
```

Creating a new entry:
```
POST /b/
body : 
{
    "Value":"This is a value"
}
```
Responds with the newly created key e.g. `"-eiJQbn3mA"`


#Frontend
See https://github.com/jgo-re/jgo-re.github.io