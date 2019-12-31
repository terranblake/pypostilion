from urllib.parse import urlencode

from pandas import DataFrame
from pandas.io.json import json_normalize

from . import session
from . import BASE_URL
from .formatting.filing import columns


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

	@staticmethod
	def get(ticker, year, statement, quarter=''):
		query = urlencode({
			'year': year,
			'quarter': quarter
		})

		path = BASE_URL + '/financials/' + statement + '/' + ticker + '?' + query
		print(path)

		response = session.get(path)
		print(response)
		return response.json()