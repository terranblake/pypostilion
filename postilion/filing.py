from . import session
from . import BASE_URL
from .formatting.filing import columns

from pandas import DataFrame
from pandas.io.json import json_normalize


class Filing(object):

# improve class so that it maps all values from
# the filing model as members of a class instance
	def __init__(self):
		pass


	@staticmethod
	def get(id):
		path = BASE_URL + '/filings/' + id
		response = session.get(path)
		return response.json()


	@staticmethod
	def getByCompany(company):
		path = BASE_URL + '/filings?company=' + company
		response = session.get(path)
		norm_response = json_normalize(response.json())

		df = DataFrame(norm_response)
		# df.rename(columns=columns, inplace=True)
		return df