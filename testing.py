
from tapioca_parse import Parse

from decouple import config


parse = Parse(application_id=config('APPLICATION_ID'),
    rest_api_key=config('REST_API_KEY'))

u = parse.users().get()
