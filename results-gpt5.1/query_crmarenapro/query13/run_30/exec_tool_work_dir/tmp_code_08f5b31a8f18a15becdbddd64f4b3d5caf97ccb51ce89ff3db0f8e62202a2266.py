code = """import json, pandas as pd

opp_data = var_call_kr5qi0YypdVJGd5RM94ROBB9
with open(var_call_1KtdI4ea6rNSGnuslBRWrwNQ, 'r') as f:
    order_items = json.load(f)

df_opp = pd.DataFrame(opp_data)
df_orders = pd.DataFrame(order_items)

for col in ['AccountId']:
    df_opp[col] = df_opp[col].astype(str).str.lstrip('#').str.rstrip()
    df_orders[col] = df_orders[col].astype(str).str.lstrip('#').str.rstrip()

merged = df_orders.merge(df_opp[['AccountId','OwnerId']], on='AccountId', how='inner', suffixes=('_order','_opp'))

merged['Quantity'] = pd.to_numeric(merged['Quantity'])
merged['UnitPrice'] = pd.to_numeric(merged['UnitPrice'])
merged['sales_amount'] = merged['Quantity'] * merged['UnitPrice']

sales_by_agent = merged.groupby('OwnerId_opp')['sales_amount'].sum().reset_index()

if not sales_by_agent.empty:
    top_agent = sales_by_agent.sort_values('sales_amount', ascending=False).iloc[0]['OwnerId_opp']
    result = top_agent
else:
    result = None

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dCrTHsXNaWdI4vwskT0pW9ER': ['Contract', 'Lead', 'Opportunity', 'OpportunityLineItem', 'Quote', 'QuoteLineItem'], 'var_call_kr5qi0YypdVJGd5RM94ROBB9': [{'OpportunityId': '#006Wt000007B5bTIAS', 'AccountId': '001Wt00000PGYx5IAH', 'OwnerId': '005Wt000003NJ53IAG', 'ContractId': '800Wt00000DDe3OIAT', 'CompanySignedDate': '2022-09-20'}, {'OpportunityId': '006Wt000007B6u8IAC', 'AccountId': '001Wt00000PGovMIAT', 'OwnerId': '005Wt000003NEa3IAG', 'ContractId': '800Wt00000DE2vLIAT', 'CompanySignedDate': '2022-06-29'}, {'OpportunityId': '006Wt000007B8PgIAK', 'AccountId': '#001Wt00000PGZZoIAP', 'OwnerId': '005Wt000003NBp4IAG', 'ContractId': '800Wt00000DE0FHIA1', 'CompanySignedDate': '2022-08-02'}, {'OpportunityId': '006Wt000007BAY1IAO', 'AccountId': '001Wt00000PGZmfIAH', 'OwnerId': '005Wt000003NJmbIAG', 'ContractId': '800Wt00000DE0TiIAL', 'CompanySignedDate': '2022-09-10'}, {'OpportunityId': '006Wt000007BBqXIAW', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NCegIAG', 'ContractId': '800Wt00000DDNlnIAH', 'CompanySignedDate': '2022-09-02'}, {'OpportunityId': '006Wt000007BBs9IAG', 'AccountId': '001Wt00000PGtdJIAT', 'OwnerId': '005Wt000003NGwoIAG', 'ContractId': '800Wt00000DE98oIAD', 'CompanySignedDate': '2022-11-10'}, {'OpportunityId': '006Wt000007BCLCIA4', 'AccountId': '001Wt00000PGRnYIAX', 'OwnerId': '005Wt000003NGFHIA4', 'ContractId': '800Wt00000DE9GrIAL', 'CompanySignedDate': '2022-06-30'}, {'OpportunityId': '#006Wt000007BEgMIAW', 'AccountId': '001Wt00000PHRTfIAP', 'OwnerId': '005Wt000003NJmcIAG', 'ContractId': '800Wt00000DE9YbIAL', 'CompanySignedDate': '2022-11-22'}, {'OpportunityId': '#006Wt000007BFaoIAG', 'AccountId': '001Wt00000PHVqdIAH', 'OwnerId': '005Wt000003NDEBIA4', 'ContractId': '800Wt00000DDzZLIA1', 'CompanySignedDate': '2022-10-26'}, {'OpportunityId': '006Wt000007BHBBIA4', 'AccountId': '#001Wt00000PGzSaIAL', 'OwnerId': '005Wt000003NBp4IAG', 'ContractId': '800Wt00000DE9qLIAT', 'CompanySignedDate': '2022-09-01'}, {'OpportunityId': '006Wt000007BHCpIAO', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NJkzIAG', 'ContractId': '800Wt00000DDeg6IAD', 'CompanySignedDate': '2022-07-18'}, {'OpportunityId': '#006Wt000007BHJFIA4', 'AccountId': '001Wt00000PHVtpIAH', 'OwnerId': '005Wt000003NHzJIAW', 'ContractId': '800Wt00000DE9rxIAD', 'CompanySignedDate': '2022-09-19'}], 'var_call_1KtdI4ea6rNSGnuslBRWrwNQ': 'file_storage/call_1KtdI4ea6rNSGnuslBRWrwNQ.json'}

exec(code, env_args)
