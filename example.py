from postilion import Filing, Company, Financial


# get company by ticker
company_by_ticker = Company.getByTicker('rost')
# print(company_by_ticker)

# get all filings for a company
filings_by_company = Filing.getByCompany(company_by_ticker['_id'])
# print(filings_by_company)

# get all available statements
statements = Financial.statements()
# print(statements)

# get roles for a statement
roles = Financial.roles('income-statement')
print(roles)