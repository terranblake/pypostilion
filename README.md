# Postilion

#### postilion is a wrapper around the publicly available postilion api

## Installation

Use the package manager [pip]() to install postilion.

```bash
pip install postilion
```

## Usage

Import postilion
```python
import postilion as pst
```

Destructure classes from module
```python
from pst import Company, Filing, Financial
```

Get a company by ticker
```
company = Company.getByTicker('rost')
print(company)
```
```javascript
{
  "stats": {
    "lastSyncedFilingsAt": "1990-02-01T00:00:00.000Z",
    "lastSyncedEarningsAt": "1990-02-01T00:00:00.000Z"
  },
  "createdAt": "2019-12-31T00:26:01.473Z",
  "updatedAt": "2019-12-31T00:26:01.473Z",
  "_id": "5e0a9a840736540024ede660",
  "name": "ross stores, inc.",
  "ref": "sec",
  "refId": "0000745732",
  "refIndustryId": "5651",
  "state": "ca",
  "ticker": "rost",
  "__v": 0
}
```

Get all filings by company
```python
filings = Filing.getByCompany(company['_id'])
print(filings.head())
```
```console
                        _id       status                 createdAt                 updatedAt  ... source  type                                                url __v
0  5e0a9a880736540024ede667  downloading  2019-12-31T00:26:01.484Z  2019-12-31T00:26:01.484Z  ...    sec  10-K  https://www.sec.gov/Archives/edgar/data/745732...   0
1  5e0a9a880736540024ede666  downloading  2019-12-31T00:26:01.484Z  2019-12-31T00:26:01.484Z  ...    sec  10-K  https://www.sec.gov/Archives/edgar/data/745732...   0
2  5e0a9a870736540024ede665  downloading  2019-12-31T00:26:01.484Z  2019-12-31T00:26:01.484Z  ...    sec  10-K  https://www.sec.gov/Archives/edgar/data/745732...   0
3  5e0a9a870736540024ede664  downloading  2019-12-31T00:26:01.484Z  2019-12-31T00:26:01.484Z  ...    sec  10-K  https://www.sec.gov/Archives/edgar/data/745732...   0
4  5e0a9a860736540024ede663  downloading  2019-12-31T00:26:01.484Z  2019-12-31T00:26:01.484Z  ...    sec  10-K  https://www.sec.gov/Archives/edgar/data/745732...   0
```

Get supported financial statements
```python
statements = Financial.statements()
print(statements)
```
```javascript
['balance-sheet', 'income-statement', 'cash-flow-statement', 'partners-capital-statement', 'financial-services']
```

Get roles for a financial statement
```python
roles = Financial.roles('balance-sheet')
print(roles)
```
```javascript
['StatementOfIncome', 'StatementOfIncomeDiscontinuedOperationsAlternate', 'StatementOfIncomeFirstAlternative', 'StatementOfOtherComprehensiveIncome', 'StatementOfOtherComprehensiveIncomeAlternative', 'StatementOfOtherComprehensiveIncomeFouthAlternative', 'StatementOfOtherComprehensiveIncomeSecondAlternative', 'StatementOfOtherComprehensiveIncomeThirdAlternative', 'ReceivablesLoansNotesReceivableAndOthers', 'ReceivablesLoansNotesReceivableAndOthersLoansAlternate', 'RetirementBenefitsTmp011', 'RetirementBenefitsTmp012', 'RetirementBenefitsTmp02', 'RetirementBenefitsTmp03', 'RetirementBenefitsTmp04', 'RetirementBenefitsTmp041', 'RetirementBenefitsTmp05', 'RetirementBenefitsTmp06', 'RetirementBenefitsTmp07', 'RetirementBenefitsTmp08', 'RetirementBenefitsTmp09']
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)


