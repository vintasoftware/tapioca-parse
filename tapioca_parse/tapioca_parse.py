# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter)

from resource_mapping import RESOURCE_MAPPING


class ParseClientAdapter(TapiocaAdapter):
    api_root = 'https://api.parse.com/1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params):
        application_id = api_params.get('application_id')
        rest_api_key = api_params.get('rest_api_key')
        return {
            'headers': {
                'X-Parse-Application-Id': application_id,
                'X-Parse-REST-API-Key': rest_api_key,
            }
        }

Parse = generate_wrapper_from_adapter(ParseClientAdapter)
