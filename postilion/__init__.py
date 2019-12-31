import os
import requests


BASE_URL = 'http://sec-service-postilion.herokuapp.com/api'
# API_KEY = os.environ.get('TMDB_API_KEY', None)


# class APIKeyMissingError(Exception):
#     pass


# if not API_KEY:
#     raise APIKeyMissingError(
#         "All methods require an API key. See "
#         "https://developers.themoviedb.org/3/getting-started/introduction "
#         "for how to retrieve an authentication token from "
#         "The Movie Database"
#     )

session = requests.Session()
session.params = {}
# session.params['api_key'] = API_KEY

from .filing import Filing
from .company import Company
from .financial import Financial