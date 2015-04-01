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

    def get_iterator_list(self, response_data):
        return response_data.get('results')

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data):
        limit = 100
        params = iterator_request_kwargs.get('params', {'limit': limit, 'skip': -limit})
        params['skip'] = params['limit'] + params['skip']
        iterator_request_kwargs['params'] = params

        return iterator_request_kwargs


Parse = generate_wrapper_from_adapter(ParseClientAdapter)
