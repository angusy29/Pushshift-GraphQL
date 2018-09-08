# Pushshift-GraphQL

[![Build Status](https://travis-ci.org/angusy29/Pushshift-GraphQL.svg?branch=master)](https://travis-ci.org/angusy29/Pushshift-GraphQL)

Personal project to experiment with GraphQL.

This is a GraphQL wrapper over Pushshift's REST API.

## Accessing the server

Start the server via:
<pre><code>cd src
python3 server.py</code></pre>

The server will run at http://localhost:5000

Access http://127.0.0.1:5000/graphql for GraphiQL interactive IDE.

## Running queries

<pre><code>{
  subredditSubmissions(subreddit:"pics", size:100) {
    author
    pinned
    score
  }
}
</pre></code>
