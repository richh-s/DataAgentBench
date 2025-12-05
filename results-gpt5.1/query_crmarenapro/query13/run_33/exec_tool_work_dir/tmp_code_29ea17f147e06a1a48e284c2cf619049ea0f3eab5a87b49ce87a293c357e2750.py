code = """import json
import pandas as pd

df = pd.DataFrame(var_call_r7hh6bMVpOidIUUSoKNjMlk1)
for col in ['Quantity', 'UnitPrice']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df['SalesAmount'] = df['Quantity'] * df['UnitPrice']
result = df.groupby('OwnerId')['SalesAmount'].sum().reset_index()
max_owner = result.sort_values('SalesAmount', ascending=False).iloc[0]['OwnerId']

out = json.dumps(max_owner)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_metV330ls2q4aTyCsVivtZNL': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_r7hh6bMVpOidIUUSoKNjMlk1': [{'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '4.0', 'UnitPrice': '399.99', 'CompanySignedDate': '2022-08-02'}, {'OpportunityId': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '8.0', 'UnitPrice': '529.99', 'CompanySignedDate': '2022-06-30'}, {'OpportunityId': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '30.0', 'UnitPrice': '649.99', 'CompanySignedDate': '2022-06-29'}, {'OpportunityId': '006Wt000007BCLCIA4', 'OwnerId': '005Wt000003NGFHIA4', 'Quantity': '15.0', 'UnitPrice': '399.99', 'CompanySignedDate': '2022-06-30'}, {'OpportunityId': '006Wt000007B6u8IAC', 'OwnerId': '005Wt000003NEa3IAG', 'Quantity': '50.0', 'UnitPrice': '529.99', 'CompanySignedDate': '2022-06-29'}, {'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '2.0', 'UnitPrice': '529.99', 'CompanySignedDate': '2022-08-02'}, {'OpportunityId': '006Wt000007B8PgIAK', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '3.0', 'UnitPrice': '549.99', 'CompanySignedDate': '2022-08-02'}, {'OpportunityId': '006Wt000007BHBBIA4', 'OwnerId': '005Wt000003NBp4IAG', 'Quantity': '10.0', 'UnitPrice': '399.99', 'CompanySignedDate': '2022-09-01'}, {'OpportunityId': '006Wt000007BAY1IAO', 'OwnerId': '005Wt000003NJmbIAG', 'Quantity': '7.0', 'UnitPrice': '529.99', 'CompanySignedDate': '2022-09-10'}, {'OpportunityId': '006Wt000007BHCpIAO', 'OwnerId': '005Wt000003NJkzIAG', 'Quantity': '8.0', 'UnitPrice': '599.99', 'CompanySignedDate': '2022-07-18'}]}

exec(code, env_args)
