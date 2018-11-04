# elasticdemo

## Table of Contents
- **Installation & Configuration**
	1. Python/Django API
	2. SQLite DB
	3. ElasticSearch
	4. Start the Django API
	5. Django MVC WebApp
- **Developer Notes**
	1. Useful Elasticsearch CURLS
	2. create super user

## Installation & Configuration
### 1. Python/Django API
1. Install Python 3.6X, this project uses Python 3.6.5
2. Install virtualenv - `pip3 install virtualenv`
3. Inside the `api/` directory
4. Create a virtualenv - `python3 -m venv env`
5. Activate the virtualenv - `source env/bin/activate`
6. Install dependencies - `pip install -r requirements.txt`

### 2. SQLite DB
1. Inside the `/api` directory
2. Activate the virtualenv (if not already active) - `source env/bin/activate`
3. Create the SQLite DB, migrations are included `python manage.py migrate`
4.  **Seeding the DB**
	1. open the django shell - `python manage.py shell`
	2. import the setup script - `from db_setup import db_setup`
	3. execute - `db_setup()`

### 3. ElasticSearch
1. Install docker for mac: https://store.docker.com/editions/community/docker-ce-desktop-mac
2. Pull the docker image: `docker pull docker.elastic.co/elasticsearch/elasticsearch:6.4.2`
3. Start Dev Mode: `docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.4.2`
4. **Seeding ElasticSearch**
   1. Inside the `/api` directory
   2. `./es_setup.sh`

### 4. Start the Django API
1. Inside the `/api` directory
2. `sudo python manage.py runserver 0.0.0.0:80`
3. To Test only the API visit `http://localhost:80/api/users/foo/?first_name=fred`

### 5. Django MVC WebApp
1. Install Python 3.6X, this project uses Python 3.6.5
2. Install virtualenv - `pip3 install virtualenv`
3. Inside the `webapp/` directory
4. Create a virtualenv - `python3 -m venv env`
5. Activate the virtualenv - `source env/bin/activate`
6. Install dependencies - `pip install -r requirements.txt`
7. Django may ask you to migrate but it is not nessessary. `python manage.py migrate`
8. Run the webapp `python manage.py runserver`
9. Open `http://127.0.0.1:8000` in the browser and you query for 'fred'
**NOTE:** The webapp is hardcoded and the API must be running on `127.0.0.1:80`.

## Developer Notes:
### Useful Elasticsearch CURLS
**Delete All docs**
`
curl -XDELETE localhost:9200/_all
`

**Add a single doc**
`
curl -XPUT -H'Content-Type: application/json' localhost:9200/foo/bar/1 -d '{"foo" : "bar"}'
`

**Add Bulk docs**
`
curl -X POST "localhost:9200/_bulk" -H 'Content-Type: application/json' -d'
{ "index" : { "_index" : "foo_index", "_type" : "docs", "_id" : "1" } }
{ "first_name" : "fred", "last_name" : "flinstone", "location" : "bedrock" }
{ "index" : { "_index" : "foo_index", "_type" : "docs", "_id" : "2" } }
{ "first_name" : "fred", "last_name" : "rogers", "location" : "land of make-believe" }
{ "index" : { "_index" : "foo_index", "_type" : "docs", "_id" : "3" } }
{ "first_name" : "lebron", "last_name" : "james", "location" : "los angeles" }
{ "index" : { "_index" : "bar_index", "_type" : "docs", "_id" : "4" } }
{ "first_name" : "fred", "last_name" : "krueger", "location" : "elm street" }
{ "index" : { "_index" : "bar_index", "_type" : "docs", "_id" : "5" } }
{ "first_name" : "fred", "last_name" : "mercury", "location" : "zanzibar" }
{ "index" : { "_index" : "bar_index", "_type" : "docs", "_id" : "6" } }
{ "first_name" : "bruce", "last_name" : "wayne", "location" : "gotham" }
{ "index" : { "_index" : "buzz_index", "_type" : "docs", "_id" : "7" } }
{ "first_name" : "charlie", "last_name" : "kelly", "location" : "philadelphia" }
{ "index" : { "_index" : "buzz_index", "_type" : "docs", "_id" : "8" } }
{ "first_name" : "mac", "last_name" : "mcdonald", "location" : "philadelphia" }
{ "index" : { "_index" : "baz_index", "_type" : "docs", "_id" : "9" } }
{ "first_name" : "deandra", "last_name" : "reynolds", "location" : "philadelphia" }
{ "index" : { "_index" : "baz_index", "_type" : "docs", "_id" : "10" } }
{ "first_name" : "dennis", "last_name" : "reynolds", "location" : "philadelphia" }
{ "index" : { "_index" : "baz_index", "_type" : "docs", "_id" : "11" } }
{ "first_name" : "frank", "last_name" : "reynolds", "location" : "philadelphia" }
{ "index" : { "_index" : "baz_index", "_type" : "docs", "_id" : "12" } }
{ "first_name" : "fred", "last_name" : "durst", "location" : "limp bizkit" }
'
`

## Django
### create super user
python manage.py createsuperuser --email YOUREMAIL --name admin