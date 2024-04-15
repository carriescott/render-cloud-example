# Capstone - Agency API
## Capstone project for Udacity Full Stack Developer Nanodegree
The following project models a casting agency that is responsible for creating 
movies and managing and assigning actors to those movies.
It hosts a number of different endpoints that allow specific roles within the 
agency to perform a different actions such as creating,modifying 
and deleting movie and actor records.

## Project Motivation
The motivation behind this project was to create an application that challenges me 
and puts into practice a number of new skills I have learnt from the Udacity Full Stack Developer
Nanodegree course. 

## Prerequisite
If you would like to run this project locally please follow the steps below.

### 1. Install Postgres
The prerequisite to running the app locally is to have a PostgreSQL database available in your local, and the Postgres server must be up and running.
Verify the Portgres installation, and start the Postgres server using:
```bash
brew install postgresql
postgres --version
pg_ctl -D /usr/local/var/postgres start
pg_ctl -D /usr/local/var/postgres stop
```

### 2. Verify the database
Open the psql prompt to view the roles, and databases:
```
# Open psql prompt
psql [username]
# View the available roles
\du
# View databases
\list
```
A PostgreSQL database should be available in your Local, and the Postgres server must be up and running.

## Running the App Locally

### 1. Clone Repo
```
git clone https://github.com/carriescott/render-cloud-example.git
```
### 2. Create a virtual environment
Create a virtual environment that will help you keep the Python packages isolated from the ones already 
installed on your local machine.
```
cd render-cloud-example
# OPTIONAL - Create a Virtual environment
python3 -m venv myvenv
source myvenv/bin/activate
```

### 3. Install PIP Dependencies
Once your virtual environment is set up and running, install the required dependencies by running:
```bash
pip install -r requirements.txt
```
#### Key Pip Dependencies

- [Flask](http://flask.pocoo.org/) is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use to handle the lightweight SQL database. You'll primarily work in `app.py`and can reference `models.py`.

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross-origin requests from our frontend server.

### 4. Set up the environment variables
Change the DATABASE_URL, to reflect your environment.
```
# You should have setup.sh and requirements.txt available
chmod +x setup.sh
source setup.sh
# The setup.sh will run the following:
# export DATABASE_URL="postgresql://postgres@localhost:5432/postgres"
# export EXCITED="true"
# Change the DATABASE_URL, as applicable to you.
echo $DATABASE_URL
# postgresql://postgres@localhost:5432/postgres
echo $EXCITED
# true
```

### 5. Run the app
``` bash
python3 app.py
```

## API Reference

### Authentication
Successful authentication is required to perform various actions.
This API uses Auth0 to define a set of roles and permissions required for each endpoint as outlined below:
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

If you would like to test any of the endpoints outlined in the following section locally you will need to use one
of the above logins and grab the access token from the URL. You can then use this
token in the authorisation header for your request by passing it in as a bearer token

Login URL: https://carrie-capstone-agency.uk.auth0.com/authorize?audience=https://capstone-agency/&response_type=token&client_id=KvDDalEN7XIjgBD8zLBY8hIcSUU4jPhL&redirect_uri=https://render-cloud-example-0t2l.onrender.com/hello

### Endpoints and Expected Behaviour
To test the application in production you will need to use Postman or an equivalent, passing in the 
access token as described above using the following base url:

Base URL: `https://render-cloud-example-0t2l.onrender.com`

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








