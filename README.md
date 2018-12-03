# quest_RESTful
this is my project copy
this is i am doing through commands
i am changing something in branch

web project
-----------
web normal application (vlc, photoshop)
platform (java jvm, python)
os

(
    tcp
    http,
    socket
)

json
-----

http
-----
client ------> server
client <------ server

request { object }
------------------
    url
        -> ip
        -> api path
        -> query string (https://www.google.com/search?id=1212)

        protocol://ip:port/apifullpath?querystring

    body
        formdata, json

    headers
    url patterning (url parameter)

types of request
----------------
GET

DELETE
POST
PUT


<a href="mailto:ranjit@google.com">mail me</a>
browser
-------
client (///) -----> UI server
html <---------text/html server
client -------> js/css UI server / CDN
client <----------- text/javascript, stylesheet server

client ---------> api backend server (python)
client <-----------application/json backend server

socket
------
client <-----> server <-----> client

json (Javascript Object Notation)
---------------------------------
{
  "people": [{
    "name": "Samarjit",
    "age": 27,
    "familyMembers": [2, 3]
  }]
}

RDBMS (sql database) (Oracle, sql server, Microsoft sql) | (no sql database) text
---------------------------------------------------------------------------------
Person
Address

Person
{
    name:
    age:
    address: {
        id:
        full_address:
        zipcode
    }
}

{
    name:
}

Address
{
    id:dsf
    full_address:
    zipcode
}

Normalization: spliting one kind of record to multiple kinds and establishing relation btw them

Architecture
----------------
MongoServer <--mongodb://username:password@host:27017/RestFull--> (driver == client) (pymongo, javamongo, mongodb)<---->Rest App<---->Client browser