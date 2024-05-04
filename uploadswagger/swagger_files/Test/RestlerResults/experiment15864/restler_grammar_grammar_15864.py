""" THIS IS AN AUTOMATICALLY GENERATED FILE!"""
from __future__ import print_function
import json
from engine import primitives
from engine.core import requests
from engine.errors import ResponseParsingException
from engine import dependencies

_event_registry_repository_deployments_post_id = dependencies.DynamicVariable("_event_registry_repository_deployments_post_id")

def parse_eventregistryrepositorydeploymentspost(data, **kwargs):
    """ Automatically generated response parser """
    # Declare response variables
    temp_7262 = None

    if 'headers' in kwargs:
        headers = kwargs['headers']


    # Parse body if needed
    if data:

        try:
            data = json.loads(data)
        except Exception as error:
            raise ResponseParsingException("Exception parsing response, data was not valid json: {}".format(error))
        pass

    # Try to extract each dynamic object

        try:
            temp_7262 = str(data["id"])
            
        except Exception as error:
            # This is not an error, since some properties are not always returned
            pass



    # If no dynamic objects were extracted, throw.
    if not (temp_7262):
        raise ResponseParsingException("Error: all of the expected dynamic objects were not present in the response.")

    # Set dynamic variables
    if temp_7262:
        dependencies.set_variable("_event_registry_repository_deployments_post_id", temp_7262)

req_collection = requests.RequestCollection([])
# Endpoint: /event-registry-management/engine, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-management"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("engine"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-management/engine"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/channel-definitions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channel-definitions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nameLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nameLikeIgnoreCase="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keyLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keyLikeIgnoreCase="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("createTime="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("createTimeAfter="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("createTimeBefore="),
    primitives.restler_fuzzable_object("{ \"fuzz\": false }"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("resourceName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("resourceNameLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("categoryLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("categoryNotEquals="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deploymentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("parentDeploymentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("latest="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("onlyInbound="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("onlyOutbound="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("implementation="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['name','id','key','category','deploymentId','version']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/channel-definitions"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/channel-definitions/{channelDefinitionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channel-definitions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/channel-definitions/{channelDefinitionId}"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/channel-definitions/{channelDefinitionId}/model, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channel-definitions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("model"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/channel-definitions/{channelDefinitionId}/model"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/channel-definitions/{channelDefinitionId}/resourcedata, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("channel-definitions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourcedata"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/channel-definitions/{channelDefinitionId}/resourcedata"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nameLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("categoryNotEquals="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("parentDeploymentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("parentDeploymentIdLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tenantIdLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tenantId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("withoutTenantId="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['id','name','deployTime','tenantId']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/deployments"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deploymentName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("tenantId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    
    {

        'post_send':
        {
            'parser': parse_eventregistryrepositorydeploymentspost,
            'dependencies':
            [
                _event_registry_repository_deployments_post_id.writer()
            ]
        }

    },

],
requestId="/event-registry-repository/deployments"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments/{deploymentId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_event_registry_repository_deployments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/deployments/{deploymentId}"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments/{deploymentId}, method: Delete
request = requests.Request([
    primitives.restler_static_string("DELETE "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_event_registry_repository_deployments_post_id.reader(), quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/deployments/{deploymentId}"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments/{deploymentId}/resourcedata/{resourceName}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_event_registry_repository_deployments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourcedata"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/deployments/{deploymentId}/resourcedata/{resourceName}"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments/{deploymentId}/resources, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_event_registry_repository_deployments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resources"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/deployments/{deploymentId}/resources"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/deployments/{deploymentId}/resources/**, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("deployments"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string(_event_registry_repository_deployments_post_id.reader(), quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resources"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("**"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/deployments/{deploymentId}/resources/**"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/event-definitions, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-definitions"),
    primitives.restler_static_string("?"),
    primitives.restler_static_string("version="),
    primitives.restler_fuzzable_int("1"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("name="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nameLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("nameLikeIgnoreCase="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("key="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keyLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("keyLikeIgnoreCase="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("resourceName="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("resourceNameLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("category="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("categoryLike="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("categoryNotEquals="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("deploymentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("parentDeploymentId="),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("latest="),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("&"),
    primitives.restler_static_string("sort="),
    primitives.restler_fuzzable_group("sort", ['name','id','key','category','deploymentId','version']  ,quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/event-definitions"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/event-definitions/{eventDefinitionId}, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-definitions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/event-definitions/{eventDefinitionId}"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/event-definitions/{eventDefinitionId}/model, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-definitions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("model"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/event-definitions/{eventDefinitionId}/model"
)
req_collection.add_request(request)

# Endpoint: /event-registry-repository/event-definitions/{eventDefinitionId}/resourcedata, method: Get
request = requests.Request([
    primitives.restler_static_string("GET "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-repository"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-definitions"),
    primitives.restler_static_string("/"),
    primitives.restler_fuzzable_string("fuzzstring", quoted=False),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("resourcedata"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-repository/event-definitions/{eventDefinitionId}/resourcedata"
)
req_collection.add_request(request)

# Endpoint: /event-registry-runtime/event-instances, method: Post
request = requests.Request([
    primitives.restler_static_string("POST "),
    primitives.restler_basepath("/flowable-rest/event-registry-api"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-registry-runtime"),
    primitives.restler_static_string("/"),
    primitives.restler_static_string("event-instances"),
    primitives.restler_static_string(" HTTP/1.1\r\n"),
    primitives.restler_static_string("Accept: application/json\r\n"),
    primitives.restler_static_string("Host: developer-docs.flowable.com\r\n"),
    primitives.restler_static_string("Content-Type: "),
    primitives.restler_static_string("application/json"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_refreshable_authentication_token("authentication_token_tag"),
    primitives.restler_static_string("\r\n"),
    primitives.restler_static_string("{"),
    primitives.restler_static_string("""
    "eventDefinitionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["oneEvent:1:158"]),
    primitives.restler_static_string(""",
    "eventDefinitionKey":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["oneEvent"]),
    primitives.restler_static_string(""",
    "channelDefinitionId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["myChannel:1:123"]),
    primitives.restler_static_string(""",
    "channelDefinitionKey":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["myChannel"]),
    primitives.restler_static_string(""",
    "eventPayload":
        {
            "nodeType":"""),
    primitives.restler_fuzzable_group("nodeType", ['ARRAY','BINARY','BOOLEAN','MISSING','NULL','NUMBER','OBJECT','POJO','STRING']  ,quoted=True),
    primitives.restler_static_string(""",
            "array":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "null":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "float":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "number":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "object":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "pojo":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "short":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "int":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "long":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "double":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "textual":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "boolean":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "binary":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "valueNode":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "containerNode":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "missingNode":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "integralNumber":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "floatingPointNumber":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "bigDecimal":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string(""",
            "bigInteger":"""),
    primitives.restler_fuzzable_bool("true"),
    primitives.restler_static_string("""
        }
    ,
    "tenantId":"""),
    primitives.restler_fuzzable_string("fuzzstring", quoted=True, examples=["tenant1"]),
    primitives.restler_static_string("}"),
    primitives.restler_static_string("\r\n"),

],
requestId="/event-registry-runtime/event-instances"
)
req_collection.add_request(request)
