""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /api/version, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("version"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/version"
)
req_collection.add_request(request)

# Endpoint: /api/stats, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("stats"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("max="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/stats"
)
req_collection.add_request(request)

# Endpoint: /api/baskets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("max="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("skip="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("name", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}/responses/{method}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("responses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("method", ['GET','HEAD','POST','PUT','PATCH','DELETE','CONNECT','OPTIONS','TRACE']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}/responses/{method}"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}/responses/{method}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("responses"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("method", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}/responses/{method}"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}/requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("max="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("skip="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("in="),
    primitives.restler_fuzzable_group("in", ['any','body','query','headers'] , default_enum="any" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}/requests"
)
req_collection.add_request(request)

# Endpoint: /api/baskets/{name}/requests, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/api/baskets/{name}/requests"
)
req_collection.add_request(request)

# Endpoint: /baskets, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("max="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("skip="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("name", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}/responses/{method}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("responses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_group("method", ['GET','HEAD','POST','PUT','PATCH','DELETE','CONNECT','OPTIONS','TRACE']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}/responses/{method}"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}/responses/{method}, method: Put
request = requests.Request([
    primitives.restler_static_string("PUT "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("responses"),
    primitives.restler_static_string("/"),
    primitives.restler_custom_payload_uuid4_suffix("method", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}/responses/{method}"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}/requests, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requests"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("max="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("skip="),
    primitives.restler_fuzzable_int("RESTlerInt"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("q="),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("in="),
    primitives.restler_fuzzable_group("in", ['any','body','query','headers'] , default_enum="any" ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}/requests"
)
req_collection.add_request(request)

# Endpoint: /baskets/{name}/requests, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath(""),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("baskets"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("RESTlerString", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("requests"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: rbaskets.in\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/baskets/{name}/requests"
)
req_collection.add_request(request)
