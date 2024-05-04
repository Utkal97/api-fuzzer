""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies
req_collection = requests.RequestCollection([])
# Endpoint: /Elixirs, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Elixirs"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("Name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("Difficulty="),
    primitives.restler_fuzzable_group("fuzzable_group_tag", ['Unknown','Advanced','Moderate','Beginner','OrdinaryWizardingLevel','OneOfAKind']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("Ingredient="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("InventorFullName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("Manufacturer="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Elixirs"
)
req_collection.add_request(request)

# Endpoint: /Elixirs/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Elixirs"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Elixirs/{id}"
)
req_collection.add_request(request)

# Endpoint: /Feedback, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Feedback"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_static_string("Content-Type: application/json\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "feedbackType":
        """),
    primitives.restler_fuzzable_group("fuzzable_group_tag", ['General','Bug','DataError','Suggestion']  ,quoted=True),
    primitives.restler_static_string("""
    ,
    "feedback":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True),
    primitives.restler_static_string(""",
    "entityId":"""),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=True),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Feedback"
)
req_collection.add_request(request)

# Endpoint: /Houses, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Houses"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("query="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Houses"
)
req_collection.add_request(request)

# Endpoint: /Houses/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Houses"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Houses/{id}"
)
req_collection.add_request(request)

# Endpoint: /Ingredients, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Ingredients"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("Name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Ingredients"
)
req_collection.add_request(request)

# Endpoint: /Ingredients/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Ingredients"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Ingredients/{id}"
)
req_collection.add_request(request)

# Endpoint: /Spells, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Spells"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("Name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("Type="),
    primitives.restler_fuzzable_group("fuzzable_group_tag", ['None','Charm','Conjuration','Spell','Transfiguration','HealingSpell','DarkCharm','Jinx','Curse','MagicalTransportation','Hex','CounterSpell','DarkArts','CounterJinx','CounterCharm','Untransfiguration','BindingMagicalContract','Vanishment']  ,quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("Incantation="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Spells"
)
req_collection.add_request(request)

# Endpoint: /Spells/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Spells"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Spells/{id}"
)
req_collection.add_request(request)

# Endpoint: /Wizards, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Wizards"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("FirstName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("LastName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Wizards"
)
req_collection.add_request(request)

# Endpoint: /Wizards/{id}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("Wizards"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_uuid4("566048da-ed19-4cd3-8e0a-b7e0e1ec4d72", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: wizard-world-api.herokuapp.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/Wizards/{id}"
)
req_collection.add_request(request)
