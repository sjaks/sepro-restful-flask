# sepro-restful-flask
Project for the course Secure Programming

## Project description
This project consists of a simple Docker composition. The main part of the program is `flask-app` that is **a simple Flask-based Python application** that serves a simple **RESTful web API**. The other part of the program is a **PostgreSQL database** that is accessed with **Python SQLAlchemy**.

The REST API accepts POST requests, which can be used for creating something called secret slugs. The secret slugs are short strings that are saved in a database with an **UUID4** identifier. The slugs can be queried by their ID as well as deleted by it. The endpoints are defined below.

The REST API utilizes **JWT** for authentication. All actions require tokens and unauthorized users should not be able to access or remove other users' slugs.

### Environmental variables

- **POSTGRES_PASSWORD** database password *(change me)*
- **POSTGRES_USER** database username
- **POSTGRES_DB** database name
- **POSTGRES_URI** URI to the postgres database

## Endpoints

- */secrets/\<uuid\>*
    - HTTP GET (get a secret slug by its id)
    - HTTP DELETE (delete a secret slug by its id)
- */secrets/\<slug\>*
    - HTTP POST (create a new secret slug with given value)

## Security considerations
The REST API handles secret slugs and thus it is important that authentication is strong and works.

UUID4 is used as the identifier format as such IDs are difficult to guess. Incrementing integers would be predictable and an attacker could target certain URLs by guessing some integers.

The other security consideration is the database and connectivity with it. By using SQLAlchemy, database models are enforced and the data is then inherintly validated. Such ORM library also helps in protection against SQL injections since actual SQL query strings are not constructed in this project itself. This leaves minimizes the changes of injection vulnerabilities to be present.

## Testing
```
$ curl localhost:5000/secrets/viesti -X POST
{"id": "dfb180ad-30a6-40f8-b569-2695f937b258", "slug": "viesti"}

curl localhost:5000/secrets/dfb180ad-30a6-40f8-b569-2695f937b258
{"id": "dfb180ad-30a6-40f8-b569-2695f937b258", "slug": "viesti"}
```
1. a
2. b
3. c

## Current flaws and fixes to them
Since this application is small, the JWT secret key is stored as an environmental variable. In a larger production-ready application, the secret key should be managed properly, in a safer manner.

## Running the program
Make sure the latest version of the program has been cloned.
Then run docker-compose inside of the project root.
```
git clone https://github.com/sjaks/sepro-restful-flask.git
cd sepro-restful-flask
docker-compose up
```
To rebuild the docker images with docker-compose,
run `docker-compose up --build flask-app database`.

*Be sure to alter the environmental variables.*
