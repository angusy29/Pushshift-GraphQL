# Pushshift-GraphQL

[![Build Status](https://travis-ci.org/angusy29/Pushshift-GraphQL.svg?branch=master)](https://travis-ci.org/angusy29/Pushshift-GraphQL)

Personal project to experiment with GraphQL.

Provides a GraphQL wrapper around Pushshift's Reddit REST API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

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

## Built With

* [flask](http://flask.pocoo.org) - Web microframework
* [graphene](https://docs.graphene-python.org/en/latest/) - Library for building GraphQL APIs
* [pushshift.io](https://github.com/pushshift/api) - Provides Reddit data for this project via REST API
