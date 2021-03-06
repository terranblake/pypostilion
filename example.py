from postilion import Filing, Company, Financial


# get company by ticker
company_by_ticker = Company.getByTicker('rost')
# print(company_by_ticker)

# get all filings for a company
filings_by_company = Filing.getByCompany(company_by_ticker['_id'])
# print(filings_by_company.head())

# get all available statements
statements = Financial.statements()
# print(statements)

# get roles for a statement
roles = Financial.roles('income-statement')
# print(roles)

# get a financial statement by ticker, statement, year and quarter
statement = Financial.get(
	ticker='rost',
	year='2017',
	statement='income-statement',
	# quarter=None
)
print(statement)