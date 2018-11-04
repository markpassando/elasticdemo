#!/bin/bash

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
echo "Elasticsearch SETUP IS COMPLETE" 