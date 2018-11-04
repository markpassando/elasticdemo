# elasticdemo

## Installation & Configuration
- Python/Django API
- SQLite DB
- ElasticSearch
- Start the Django API
## Developer Notes
- Useful Elasticsearch CURLS
- create super user

### Python/Django API
- Install Python 3.6X, this project uses Python 3.6.5
- Install virtualenv - `pip3 install virtualenv`
- Inside the `api/` directory
- Create a virtualenv - `python3 -m venv env`
- Activate the virtualenv - `source env/bin/activate`
- Install dependencies - `pip install -r requirements.txt`

### SQLite DB
- Inside the `/api` directory
- Activate the virtualenv (if not already active) - `source env/bin/activate`
- Create the SQLite DB, migrations are included `python manage.py migrate`
- **Seeding the DB**
	- open the django shell - `python manage.py shell`
	- import the setup script - `from db_setup import db_setup`
	- execute - `db_setup()`

### ElasticSearch
- Install docker for mac: https://store.docker.com/editions/community/docker-ce-desktop-mac
- Pull the docker image: `docker pull docker.elastic.co/elasticsearch/elasticsearch:6.4.2`
- Start Dev Mode: `docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.4.2`
- **Seeding ElasticSearch**
- Inside the `/api` directory
- `./es_setup.sh`

### Start the Django API
- `sudo python manage.py runserver 0.0.0.0:80`
- To Test only the API visit `http://localhost:80/api/users/foo/?first_name=fred`

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