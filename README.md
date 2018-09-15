# Pushshift-GraphQL

[![Build Status](https://travis-ci.org/angusy29/Pushshift-GraphQL.svg?branch=master)](https://travis-ci.org/angusy29/Pushshift-GraphQL)

Personal project to experiment with GraphQL.

Provides a GraphQL wrapper around Pushshift's Reddit REST API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Requirements can be installed via:
```
pip3 install -r requirements.txt
```

### Installing

Start the Flask server via:
```
cd src
python3 server.py
```

This server will run at http://localhost:5000

GraphiQL interactive IDE will be accessible via http://localhost:5000/graphql

### Example query
Visit http://localhost:5000/graphql to make queries
```
{
  submissions(subreddit:"pics", size:100) {
    author
    title
    num_comments
  }
}
```

## Running the tests

```
cd tests
pytest
```

## GraphQL API

### Limitation
This project consists of GraphQL endpoints which either call Pushshift's REST API, or Pushshift's Elasticsearch store.

The GraphQL endpoint `submissions` calls Pushshift's REST API. By calling the REST API, at its core our GraphQL query is just
querying against the dataset returned by the REST API, and not the collective dataset in its entirety.

This was the motivation to extend the functionality of this project to integrate with Pushshift's Elasticsearch.

### Endpoints

* To be documented


## Built With

* [flask](http://flask.pocoo.org) - Web microframework
* [graphene](https://docs.graphene-python.org/en/latest/) - Library for building GraphQL APIs
* [pushshift.io](https://github.com/pushshift/api) - Provides Reddit data for this project via REST API
* [elastic.pushshift.io](https://elastic.pushshift.io) - Pushshift's Elasticsearch store

## Currently in progress

* Integrate with Pushshift's Elasticsearch
