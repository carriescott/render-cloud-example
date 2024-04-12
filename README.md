# Capstone - Agency API
## Capstone project for Udacity Full Stack Developer Nanodegree

## Getting Setup

### Install Postgres
The prerequisite to running the app locally is to have a PostgreSQL database available in your local, and the Postgres server must be up and running.
Verify the Portgres installation, and start the Postgres server using:
```bash
brew install postgresql
postgres --version
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop
```

### Installing Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.


## Running the App Locally
**Create a virtual environment** - Once you have the starter file in your project directory, create a virtual environment that will help you keep the Python packages isolated from the ones already installed on your local machine.
``` bash
cd heroku_sample
python3 -m venv myvenv
source myvenv/bin/activate
```

**Set up the environment variables**
``` bash
chmod +x setup.sh
source setup.sh
echo $DATABASE_URL
echo $EXCITED
```

**Run the app**
``` bash
python3 app.py
```

## API Reference

### Authentication
Successful authentication is required to perform various actions.
This API uses Auth0 to define a set of roles and permissions required for each endpoint as outlined below:

App url: https://render-cloud-example-0t2l.onrender.com/
Login: https://carrie-capstone-agency.uk.auth0.com/authorize?audience=https://capstone-agency/&response_type=token&client_id=KvDDalEN7XIjgBD8zLBY8hIcSUU4jPhL&redirect_uri=https://render-cloud-example-0t2l.onrender.com/hello

- Casting Assistant
    - Can view actors and movies
    - Login
      - Email: assistant@email.com
      - Password: Tester99!
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
    - Modify actors or movies
    - Login
      - Email: director@email.com
      - Password: Tester99!
- Executive Producer
    - All permissions a Casting Director has and…
    - Add or delete a movie from the database
    - Login
      - Email: producer@email.com
      - Password: Tester99!


### Endpoints and Expected Behaviour
Base URL: `https:`

`GET '/actors'`

- Fetches a list of all registered actors
- Requires `get:actors` permission
- Request Arguments: None
- Returns: An array of objects

```json
{
  "actors": [
    {
      "id": 1,
      "name": "George Clooney",
      "age": 62,
      "gender": "Male"
    },
    {
      "id": 2,
      "name": "Meryl Streep",
      "age": 74,
      "gender": "Female"
    }
  ],
  "success": true
  }
```

`GET '/movies'`

- Fetches a list of all registered movies
- Requires `get:movies` permission
- Request Arguments: None
- Returns: An array of objects

```json
{
  "movies": [
    {
      "id": 1,
      "title": "Mary Poppins",
      "release_date": 1964
    },
    {
      "id": 2,
      "title": "Cinderella",
      "release_date": 1950
    }
  ],
  "success": true
  }
```

`DELETE '/actors/${id}'`

- Deletes a specified actor using the id of the actor
- Requires `delete:actor` permission
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code and the id of the actor.

```json
{
  "success": true,
  "deleted": 1
  }
```

`DELETE '/movies/${id}'`

- Deletes a specified movie using the id of the movie
- Requires `delete:movie` permission
- Request Arguments: `id` - integer
- Returns: Does not need to return anything besides the appropriate HTTP status code and the id of the movie.

```json
{
  "success": true,
  "deleted": 1
  }
```

`POST '/actors/create'`

- Creates an actor
- Requires `create:actor` permission
- Request Body:

```json
{
  "id": 2, 
  "name": "Meryl Streep", 
  "age": 74, 
  "gender": "Female"
}
```

- Returns: The newly created record and the appropriate HTTP status code.

```json
{
  "success": true,
  "actor": {
      "id": 2,
      "name": "Meryl Streep",
      "age": 74,
      "gender": "Female"
  }
}
```

`POST '/movies/create'`

- Creates a movie
- Requires `create:movie` permission
- Request Body:

```json
{
  "name": "Cinderella",
  "age": 1950
}
```

- Returns: The newly created record and the appropriate HTTP status code.

```json
{
  "success": true,
  "movie": {
    "id": 2,
    "title": "Cinderella",
    "release_date": 1950
  }
}
```

`PATCH '/actors/${id}/edit'`

- Edits a specified actor using the id of the actor
- Requires `edit:actor` permission
- Request Arguments: `id` - integer
- Request Body: One of the following fields must be provided
```json
{
  "name": "Meryl Streep",
  "age": 74,
  "gender": "Female"
}
```

- Returns: The newly created record and the appropriate HTTP status code.

```json
{
  "success": true,
  "actor": {
    "id": 2,
    "name": "Meryl Streep",
    "age": 74,
    "gender": "Female"
  }
}
```

`PATCH '/movies/${id}/edit'`

- Edits a specified movie using the id of the movie
- Requires `edit:movie` permission
- Request Arguments: `id` - integer
- Request Body: One of the following fields must be provided
```json
{
  "title": "Mary Poppins",
  "release_date": 1964
}
```

- Returns: The newly created record and the appropriate HTTP status code.

```json
{
  "success": true,
  "actor": {
    "id": 1,
    "title": "Mary Poppins",
    "release_date": 1964
  }
}
```








