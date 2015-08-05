# coding: utf-8

from tapioca import (
    TapiocaAdapter, generate_wrapper_from_adapter, JSONAdapterMixin)

from resource_mapping import RESOURCE_MAPPING


class ParseClientAdapter(JSONAdapterMixin, TapiocaAdapter):
    api_root = 'https://api.parse.com/1/'
    resource_mapping = RESOURCE_MAPPING

    def get_request_kwargs(self, api_params, *args, **kwargs):
        params = super(ParseClientAdapter, self).get_request_kwargs(
            api_params, *args, **kwargs)

        if 'headers' not in params:
            params['headers'] = {}

        params['headers'].update({
            'X-Parse-Application-Id': api_params.get('application_id'),
            'X-Parse-REST-API-Key': api_params.get('rest_api_key')})

        return params

    def get_iterator_list(self, response_data):
        return response_data.get('results')

    def get_iterator_next_request_kwargs(self,
            iterator_request_kwargs, response_data, response):
        limit = 100
        params = iterator_request_kwargs.get('params', {'limit': limit, 'skip': -limit})
        params['skip'] = params['limit'] + params['skip']
        iterator_request_kwargs['params'] = params

        return iterator_request_kwargs


Parse = generate_wrapper_from_adapter(ParseClientAdapter)
