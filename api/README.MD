# LMS API

## Getting Started

## Start Api in Docker Container (Recommended)

```sh
docker-compose up -d # starts a MongoDB container and a Reaction API container
docker-compose logs -f api # view Reaction API container logs
```

## Start Api locally

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment
We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```sh
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.


##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

Each time you open a new terminal session, run:

```sh
export FLASK_APP=api.py;
```

To run the server, execute:

```sh
flask run --reload
```
The `--reload` flag will detect file changes and restart the server automatically.


## API Reference
### Gating Started
  - Base URL: the backend app is hosted at http://127.0.0.1:5000, which set as a proxy in the frontend configuration.
  - Authentication: this application required authentication for some endpoints.

### Error Handling
  - Errors are returned as JSON object in the following format.
  ```json
  {
    'success': False,
    'error': 400,
    'message': "bad request"

  }
  ```

  - 404: Resource Not Found
  - 422: Not Processable

### End Points
  - GET: `/actors`
    - Return all registered actors.
    - Authentication: No
    - Sample: `curl http://127.0.0.1:5000/actors`
    ```json
    {
        "actors": [
          {
            "name": "Robert De Niro",
            "age": 60,
            "gender": "male"
          },
          {
            "name": " Denzel Washington ",
            "age": 50,
            "gender": "male"
          }
        ],
        "success":true
    }
    ```


  - POST: `/actors`
    - Create new actor
    - Authentication: yes
    - Permissions: `post:actors`
    - Sample: `curl -X POST http://127.0.0.1:5000/actors -H "Content-Type: application/json" -d '{"name":" Denzel Washington ","age":50, "gender":"male"}'`
    ```json
    {
        "actor":" Denzel Washington ",
        "success":true
    }
    ```

  - DELETE `/actors`
    - delete actor
    - Sample: `curl -X DELETE http://127.0.0.1:5000/actors/1`
    ```json
    {
      "deleted": 13,
      "success":true,
      "actors": [
          {
            "name": "Robert De Niro",
            "age": 60,
            "gender": "male"
          },
          {
            "name": " Denzel Washington ",
            "age": 50,
            "gender": "male"
          }
       ],
      "total_actors":18
    }
    ```
  - PATCH `/actors`
    - Update actor
    - Sample: `curl -X PUT http://127.0.0.1:5000/actors/1 -H "Content-Type: application/json" -d '{"age": 55}'`
    ```json
    {
      "updated": true,
      "success": true,
      "actors": [
        {
            "name": "Robert De Niro",
            "age": 60,
            "gender": "male"
          },
          {
            "name": " Denzel Washington ",
            "age": 50,
            "gender": "male"
          } 
      ],
      "total_actors": 3 
    }
    ```
  - GET: `/movies`
    - return all registered movies.
  - POST: `/movies`
    - create new movie
  - DELETE `/movies`
    - delete movie
  - PATCH `/movies`
    - update movie

## TODO

### Setup Auth0
1. Create a new Auth0 Account
2. Create a single page web app application
3. Create a new API and enable RBAC
4. Create new API permissions:
  - `get:actors`
  - `post:actors`
  - `delete:actors`
  - `patch:actors`
  - `get:movies`
  - `post:movies`
  - `delete:movies`
  - `patch:movies`
5. Create new roles for:
  - Casting Assistant
    - can `get:actors`
    - can `get:movies`
  - Casting Director
    - can perform all actions Casting Assistant has
    - can `post:actors`
    - can `delete:actors`
    - can `patch:actors`
    - can `patch:movies`
  - Executive Producer
    - can perform all actions