code = """import json, pandas as pd
contracts = pd.DataFrame(var_call_o5iENTqIjsLWHKDXBzwMbCR6)
orders = pd.read_json(var_call_6ysHLXrInTFKhnYURslVkejE)
contracts['AccountId_clean'] = contracts['AccountId'].str.lstrip('#').str.strip()
orders['AccountId_clean'] = orders['AccountId'].str.lstrip('#').str.strip()
merged = orders.merge(contracts[['AccountId_clean']], on='AccountId_clean', how='inner')
merged['Quantity'] = merged['Quantity'].astype(float)
merged['UnitPrice'] = merged['UnitPrice'].astype(float)
merged['sales_amount'] = merged['Quantity'] * merged['UnitPrice']
result = merged.groupby('OwnerId', dropna=False)['sales_amount'].sum().reset_index()
result = result.sort_values('sales_amount', ascending=False).head(1)
answer = result['OwnerId'].iloc[0]
out = json.dumps(answer)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dZ9NFQNDsCvNPLv6Mkdeu2im': ['ProductCategory', 'Product2', 'ProductCategoryProduct', 'Pricebook2', 'PricebookEntry', 'Order', 'OrderItem'], 'var_call_VkWeeA4wZNPErF8fGvi2POBK': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_o5iENTqIjsLWHKDXBzwMbCR6': [{'ContractId': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'ContractId': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'ContractId': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'ContractId': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'ContractId': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'ContractId': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'ContractId': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'ContractId': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'ContractId': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'ContractId': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'ContractId': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'ContractId': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'ContractId': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'ContractId': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'ContractId': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'ContractId': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}], 'var_call_6ysHLXrInTFKhnYURslVkejE': 'file_storage/call_6ysHLXrInTFKhnYURslVkejE.json'}

exec(code, env_args)
