# sepro-restful-flask
Project for the course Secure Programming

## Project description
This project consists of a simple Docker composition. The main part of the program is `flask-app` that is **a simple Flask-based Python application** that serves a simple **RESTful web API**. The other part of the program is a **PostgreSQL database** that is accessed with **Python SQLAlchemy**.

The REST API accepts POST requests, which can be used for creating something called secret slugs. The secret slugs are short strings that are saved in a database with an **UUID4** identifier. The slugs can be queried by their ID as well as deleted by it. The endpoints are defined below.

The REST API utilizes HTTP Basic Auth for authentication. All actions require user credentials and unauthorized users should not be able to access or remove other users' slugs.

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
- */users/register*
    - HTTP POST (created new user with given `username` and `password` in the request body)

## Security considerations
The REST API handles secret slugs and thus it is important that authentication is strong and works. HTTP Basic Auth works as a secure username:password authentication method but it relies on the strenght of the password. In this small project it was used due to its simplicity and straight-forward possibility to integrate it into a REST API that should be stateless. The application forces the user to pick a strong password.

UUID4 is used as the identifier format as such IDs are difficult to guess. Incrementing integers would be predictable and an attacker could target certain URLs by guessing some integers.

The other security consideration is the database and connectivity with it. By using SQLAlchemy, database models are enforced and the data is then inherintly validated. Such ORM library also helps in protection against SQL injections since actual SQL query strings are not constructed in this project itself. This leaves minimizes the chances of injection vulnerabilities to be present.

Since the project uses password authentication and passwords are stored in a database,
they need to be hashed. SHA-256 from `passlib` is used in this project as it suffices
for password hashing at the moment. The library's password verification method is also
used. The hashes are different even if the same password is used. This is because `passlib` uses a random salt for the hashes.

## Testing
The creation of secrets and user registration can be tested with cURL, for example.
```
HTTP POST User Registration
$ curl localhost:5000/users/register -X POST -H 'Content-Type: application/json' -d '{"username": "testi", "password": "averystrongandlongpassword"}'
{"username": "testi"}

HTTP POST New Slug
$ curl localhost:5000/secrets/viesti -X POST -H 'Content-Type: application/json' -u testi:averystrongandlongpassword
{"id": "dfb180ad-30a6-40f8-b569-2695f937b258", "slug": "viesti", "user": "testi"}

HTTP POST Get Slug by ID
$ curl localhost:5000/secrets/dfb180ad-30a6-40f8-b569-2695f937b258 -H 'Content-Type: application/json' -u testi:averystrongandlongpassword
{"id": "dfb180ad-30a6-40f8-b569-2695f937b258", "slug": "viesti", "user": "testi"}
```
Most of the security testing involved pinging the endpoints with cURL and checking that everything works correctly.

## Current flaws and fixes to them
Since this application is a simple experiment, it relies on HTTP basic authentication. It should probably be replaced with something more secure if the program was to be deployed into production. HTTP Basic Auth would suffice if all passwords were strong but public APIs should work with keys that are easily changed and they should limit access to resources. Simple username:password authentication provides access to all resources without any limits.

One very secure way to harden the authentication is using JWT, which was studied for this project but since it doesn't integrate well with Flask-RESTful - but rather with vanilla Flask - it was not used here.

The program is only designed to run locally so there is no proxy or anything in front of it. This means CORS and CSRF protection cannot be implemented easily.
Also HTTPS could be implemented, with Let's Encrypt for instance, if the program was running on a server with a public domain. However, Flask-RESTful supports
CORS out of the box and those settings have not been tampered with. Locally CORS isn't that important but other applications running on a different port cannot
access the REST API. For example if there was a React frontend running on port 8080, it would need to be included in the CORS headers.

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
