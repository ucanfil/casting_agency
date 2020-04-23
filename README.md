# Backend Casting Agency API

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

Working within a virtual environment whenever using Python for projects is recommended. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `/` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py.

## Database Setup
With Postgres running, restore a database using the castingexport.psql file. From the root `/` folder in terminal run:
```bash
psql casting < castingexport.psql
```

## Running the server

From within the root `/` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application.


## Database Setup for Testing
With Postgres running, restore a test database using the casting.psql. From the root `/` folder in terminal run:
```bash
dropdb casting_test
createdb casting_test
psql casting_test < castingexport.psql
```

## Environment Variables
All JWT tokens for differents roles locates as environment variable in `./setup.sh` file, please run:

```
source ./setup.sh
```

### Testing
To run the tests, with your flask server running open a different tab. Here first run if you haven't:

```
source ./setup.sh
```

This will make some environment variables available to you in order to use in your tests. Then within the same command line, run:

```
dropdb trivia_test
createdb trivia_test
psql casting_test < castingexport.psql
python test_app.py
```


## API Reference

<!-- #### Base URL -->
At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://localhost:5000/`. which is set as a proxy in the frontend configuration.

<!-- #### Authentication -->
This version of the application does not require authentication or API keys.

#### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": False,
  "error: 400,
  "message": "bad request
}
```
The API will return four error types when requests fail:
* 400: Bad Request
* 404: Resource Not Found
* 405: Method not allowed
* 422: Not Processable

## Important: To test app endpoints on Heroku in curl commands below, change $HOSTNAME variable with $HOST_HEROKU
### Endpoints
  * GET '/movies'
    * General
      * Fetches a list consist of movie dicts.
      * Request Arguments: None
      * Returns: List of movies objects and success value.

    * Sample: `curl -H "Accept: application/json" -H "Authorization: Bearer $JWT_CASTING_ASSISTANT" $HOSTNAME/movies --request GET`
      ```
        {
            "movies":[
                {
                    "id":1,
                    "release_date":"Mon, 15 Mar 1971 00:00:00 GMT",
                    "title":"Clockwork Orange"
                },
                {
                    "id":2,
                    "release_date":"Tue, 12 Oct 1999 00:00:00 GMT",
                    "title":"Fight Club"
                },
                {
                    "id":3,
                    "release_date":"Thu, 25 Mar 1993 00:00:00 GMT",
                    "title":"Beautiful Life"
                }
            ],
            "success":true
        }
      ```

  * GET '/movies/1'
    * General
      * Fetches the given movie and success value.
      * Request Arguments: `<int:movie_id>`
      * Returns: The movie in question and success value.

    * Sample: `curl -H "Accept: application/json" -H "Authorization: Bearer $JWT_CASTING_ASSISTANT" $HOSTNAME/movies/1 --request GET`
      ```
        {
            "movie": {
                "id": 1,
                "release_date": "Mon, 15 Mar 1971 00:00:00 GMT",
                "title": "Clockwork Orange"
            },
            "success": true
        }
      ```

  * POST '/movies'
    * General
      * Posts the given movie in json format to db.
      * Request Arguments: `title, release_date`
      * Returns: Inserted movie dict and success value.

    * Sample: `curl -H "Content-Type: application/json" -X POST -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" -d '{"title":"Eyes Wide Shut","release_date":"12-05-1999"}' $HOSTNAME/movies`
      ```
        {
            "insert": {
                "release_date": "12-05-1999",
                "title": "Eyes Wide Shut"
            },
            "success": true
        }
      ```

  * PATCH '/movies/<int:movie_id>'
    * General
      * Patches the given movie.
      * Request Arguments: `<int:movie_id>, title, release_date`
      * Returns: Inserted movie dict and success value.

    * Sample: `curl -H "Content-Type: application/json" -X PATCH -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" -d '{"title":"Eyes Wide Shut","release_date":"12-05-1998"}' $HOSTNAME/movies/5`
      ```
        {
            "insert": {
                "release_date": "12-05-1998",
                "title": "Eyes Wide Shut"
            },
            "success": true
        }
      ```

  * DELETE '/movies/<int:movie_id>'
    * General
      * Deletes the movie that has given
      * Request Arguments: `movie_id`
      * Returns: Success value.

    * Sample: `curl -H "Content-Type: application/json" -X DELETE -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" $HOSTNAME/movies/5`
      ```
        {
          "success": true,
          "delete": 5
        }
      ```

  * GET '/actors'
    * General
      * Fetches a list consist of actor dicts.
      * Request Arguments: None
      * Returns: List of actors objects and success value.

    * Sample: `curl -H "Accept: application/json" -H "Authorization: Bearer $JWT_CASTING_ASSISTANT" $HOSTNAME/actors --request GET`
      ```
        {
            "actors": [
                {
                    "age": "74",
                    "gender": "M",
                    "id": 1,
                    "name": "Al Pacino"
                },
                {
                    "age": "45",
                    "gender": "F",
                    "id": 2,
                    "name": "Angelina Jolie"
                },
                {
                    "age": "89",
                    "gender": "M",
                    "id": 3,
                    "name": "Anthony Hopkins"
                },
                {
                    "age": "84",
                    "gender": "M",
                    "id": 4,
                    "name": "Anthony Hopkins"
                }
            ],
            "success": true
        }
      ```

  * GET '/actors/1'
    * General
      * Fetches the given actor and success value.
      * Request Arguments: `<int:actor_id>`
      * Returns: The actor in question and success value.

    * Sample: `curl -H "Accept: application/json" -H "Authorization: Bearer $JWT_CASTING_ASSISTANT" $HOSTNAME/actors/1 --request GET`
      ```
        {
            "actor": {
                "age": "74",
                "gender": "M",
                "id": 1,
                "name": "Al Pacino"
            },
            "success": true
        }
      ```

  * POST '/actors'
    * General
      * Posts the given actor in json format to db.
      * Request Arguments: `name, age, gender`
      * Returns: Inserted actor dict and success value.

    * Sample: `curl -H "Content-Type: application/json" -X POST -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" -d '{"name":"John Doe","age":"45", "gender":"M"}' $HOSTNAME/actors`
      ```
        {
            "insert": {
                "age": "45",
                "name": "John Doe",
                "gender": "M"
            },
            "success": true
        }
      ```

  * PATCH '/actors/<int:actor_id>'
    * General
      * Patches the given actor.
      * Request Arguments: `<int:actor_id>, name, age, gender`
      * Returns: Inserted actor dict and success value.

    * Sample: `curl -H "Content-Type: application/json" -X PATCH -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" -d '{"name":"Jane Doe","age":"35", "gender":"F"}' $HOSTNAME/actors/5`
      ```
        {
            "actor": {
                "age": "35",
                "name": "Jane Doe",
                "gender": "F"
            },
            "success": true
        }
      ```

  * DELETE '/actors/<int:actor_id>'
    * General
      * Deletes the actor that has given
      * Request Arguments: `actor_id`
      * Returns: Success value.

    * Sample: `curl -H "Content-Type: application/json" -X DELETE -H "Authorization: Bearer $JWT_EXECUTIVE_PRODUCER" $HOSTNAME/actors/5`
      ```
        {
          "success": true,
          "delete": 5
        }
      ```



