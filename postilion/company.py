from . import session
from . import BASE_URL
from .formatting.company import columns

from pandas import DataFrame
from pandas.io.json import json_normalize


class Company(object):

# improve class so that it maps all values from
# the filing model as members of a class instance
	def __init__(self):
		pass


	@staticmethod
	def get(id):
		path = BASE_URL + '/companies/' + id
		response = session.get(path)
		return response.json()


	@staticmethod
	def getByTicker(ticker):
		path = BASE_URL + '/companies?ticker=' + ticker
		response = session.get(path)
		return response.json()