# LMS API

## Getting Started

### Terminal Commands

Note: make sure you have *pip* and *virtualenv* installed.

```sh
Initial installation: make install

To run test: make tests

To run application: make run

To run all commands at once : make all
```

View the app in this url: `http://127.0.0.1:5000/`

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database. Since we want you to focus on auth, we handle the heavy lift for you in `./src/database/models.py`. We recommend skimming this code first so you know how to interface with the Drink model.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.


## API Reference
 - NOTE: all the APIs are protected that means you must be a user in this app and has one of those role privileges
  - Assistant
    - can `get:actors`
    - can `get:movies`
  - Director
    - can perform all actions Casting Assistant has
    - can `post:actors`
    - can `delete:actors`
    - can `patch:actors`
    - can `patch:movies`
  - Producer
    - can perform all actions

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

#### Actors
  - GET: `/actors`
    - Requires auth `get:actors`
    - Return all registered actors.
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
    - Requires auth `post:actors`
    - Create new actor
    - Permissions: `post:actors`
    - Sample: `curl -X POST http://127.0.0.1:5000/actors -H "Content-Type: application/json" -d '{"name":" Denzel Washington ","age":50, "gender":"male"}'`
    ```json
    {
        "actor":" Denzel Washington ",
        "success":true
    }
    ```

  - DELETE `/actors`
    - Requires auth `delete:actors`
    - Delete actor
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
    - Requires auth `patch:actors`
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
#### Movies
  - GET: `/movies`
    - Requires auth `get:movies`
    - Return all registered movies.
     ```json
    {
        "movies": [
          {
            "name": "Name of the movie",
            "about": "about the movie"
          },
          {
            "name": "Name of the movie",
            "about": "about the movie"
          }
        ],
        "success":true
    }
    ```
  - POST: `/movies`
    - Requires auth `post:movies`
    - Create new movie
  - DELETE `/movies`
    - Requires auth `delete:movies`
    - Delete movie
  - PATCH `/movies`
    - Requires auth `patch:movies`
    - Update movie
     ```json
    {
      "updated": true,
      "success": true,
      "movies": [
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

## Customize your own Auth0
    - By default and for reviewing pourpose I've prepred an Auth0 account and I put all the information inside `.evn.example`
    if you need to make your own Auth0 follow the instruction to create and configer your Auth0 appliction.

### Setup Auth0 for your own
1. Create a new Auth0 Account from [here](https://auth0.com/)
2. Create a single page web app application.
3. Create a new API and enable RBAC.
4. Change .env file
    - *AUTH0_DOMAIN* your auth0 domain name
    - *API_AUDIENCE* your audience URL
    - *ALGORITHMS* by default is `[RS256]` you can change it if you need.
5. Create new API permissions:
  - `get:actors`
  - `post:actors`
  - `delete:actors`
  - `patch:actors`
  - `get:movies`
  - `post:movies`
  - `delete:movies`
  - `patch:movies`
6. Create new roles for:
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

  - Now your Auth0 is ready 🌱.


### Testing
this is all testing scenarios for Movies and Actors API

````
test_delete_actors_assistant_role (test_actors_api.ApiTestCase) ... ok
test_delete_actors_director_role (test_actors_api.ApiTestCase) ... ok
test_delete_actors_producer_role (test_actors_api.ApiTestCase) ... ok
test_delete_actors_producer_role_404 (test_actors_api.ApiTestCase) ... ok
test_get_actors (test_actors_api.ApiTestCase) ... ok
test_get_actors_unAuthorize (test_actors_api.ApiTestCase) ... ok
test_index (test_actors_api.ApiTestCase) ... ok
test_patch_actors_assistant_role (test_actors_api.ApiTestCase) ... ok
test_patch_actors_director_role (test_actors_api.ApiTestCase) ... ok
test_patch_actors_producer_role (test_actors_api.ApiTestCase) ... ok
test_post_actors_assistant_role (test_actors_api.ApiTestCase) ... ok
test_post_actors_director_role (test_actors_api.ApiTestCase) ... ok
test_post_actors_producer_role (test_actors_api.ApiTestCase) ... ok
test_post_actors_unprocessable (test_actors_api.ApiTestCase) ... ok
test_delete_movies_assistant_role (test_movies_api.ApiTestCase) ... ok
test_delete_movies_director_role (test_movies_api.ApiTestCase) ... ok
test_delete_movies_producer_role (test_movies_api.ApiTestCase) ... ok
test_delete_movies_producer_role_404 (test_movies_api.ApiTestCase) ... ok
test_get_movies (test_movies_api.ApiTestCase) ... ok
test_get_movies_unAuthorize (test_movies_api.ApiTestCase) ... ok
test_index (test_movies_api.ApiTestCase) ... ok
test_patch_movies_assistant_role (test_movies_api.ApiTestCase) ... ok
test_patch_movies_director_role (test_movies_api.ApiTestCase) ... ok
test_patch_movies_producer_role (test_movies_api.ApiTestCase) ... ok
test_post_movies_assistant_role (test_movies_api.ApiTestCase) ... ok
test_post_movies_director_role (test_movies_api.ApiTestCase) ... ok
test_post_movies_producer_role (test_movies_api.ApiTestCase) ... ok
test_post_movies_unprocessable (test_movies_api.ApiTestCase) ... ok

````
