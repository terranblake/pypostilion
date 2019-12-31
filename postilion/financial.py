from . import session
from . import BASE_URL
from .formatting.filing import columns

from pandas import DataFrame
from pandas.io.json import json_normalize


class Financial(object):

# improve class so that it maps all values from
# the filing model as members of a class instance
	def __init__(self):
		pass


	@staticmethod
	def statements():
		path = BASE_URL + '/financials'
		response = session.get(path)
		return response.json()


	@staticmethod
	def roles(statement):
		path = BASE_URL + '/financials/' + statement
		response = session.get(path)
		return response.json()