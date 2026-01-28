code = """import json
import pandas as pd

# Load data from storage variables
contracts = pd.DataFrame(var_call_qS73Xx2crSLTzY5BadIVzG5o)
ops = pd.read_json(var_call_hQvKR5XvfxgsVFCxXywFNKDV)
orderitems = pd.read_json(var_call_OVZHIPqPBCrhmfhEtvNrq8Bx)
orders = pd.read_json(var_call_UTt3I1g6TAfHQyb7Nm6RrcaF)

# helper clean function
def clean_id(x):
    if pd.isna(x):
        return None
    s = str(x).strip()
    if s == 'None' or s == 'nan':
        return None
    if s.startswith('#'):
        s = s[1:]
    return s

# Clean contract ids and AccountIds
contracts['Id_clean'] = contracts['Id'].apply(clean_id)
contracts['AccountId_clean'] = contracts['AccountId'].apply(clean_id)

# Eligible contract ids set
eligible_contract_ids = set(contracts['Id_clean'].dropna().unique())

# Clean opportunities
ops['ContractID__c'] = ops['ContractID__c'].replace('None', None)
ops['ContractID__c_clean'] = ops['ContractID__c'].apply(clean_id)
ops['AccountId_clean'] = ops['AccountId'].apply(clean_id)

# Eligible opportunities: those whose ContractID__c is in eligible_contract_ids
eligible_ops = ops[ops['ContractID__c_clean'].isin(eligible_contract_ids)]
# derive eligible account ids from eligible opportunities
eligible_account_ids = set(eligible_ops['AccountId_clean'].dropna().unique())

# Also consider contract's AccountId as eligible (in case opportunities missing)
eligible_account_ids.update(set(contracts['AccountId_clean'].dropna().unique()))

# Clean orders
orders['Id_clean'] = orders['Id'].apply(clean_id)
orders['AccountId_clean'] = orders['AccountId'].apply(clean_id)
orders['OwnerId_clean'] = orders['OwnerId'].apply(clean_id)
orders['EffectiveDate'] = pd.to_datetime(orders['EffectiveDate'], errors='coerce')

start = pd.to_datetime('2022-06-25')
end = pd.to_datetime('2022-11-25')
# filter orders in date range
orders_in_range = orders[(orders['EffectiveDate'] >= start) & (orders['EffectiveDate'] <= end)]
# filter orders whose AccountId is in eligible_account_ids
orders_in_range = orders_in_range[orders_in_range['AccountId_clean'].isin(eligible_account_ids)]

# Clean orderitems
orderitems['OrderId_clean'] = orderitems['OrderId'].apply(clean_id)
# numeric conversion
orderitems['Quantity'] = pd.to_numeric(orderitems['Quantity'], errors='coerce').fillna(0)
orderitems['UnitPrice'] = pd.to_numeric(orderitems['UnitPrice'], errors='coerce').fillna(0)
orderitems['LineAmount'] = orderitems['Quantity'] * orderitems['UnitPrice']

# Keep orderitems for orders in range
order_ids_in_range = set(orders_in_range['Id_clean'].dropna().unique())
orderitems_in_range = orderitems[orderitems['OrderId_clean'].isin(order_ids_in_range)]

# Map OrderId to OwnerId
order_owner_map = orders_in_range.set_index('Id_clean')['OwnerId_clean'].to_dict()

# Aggregate sales per order
sales_per_order = orderitems_in_range.groupby('OrderId_clean')['LineAmount'].sum().to_dict()

# Aggregate sales per agent (OwnerId)
sales_per_agent = {}
for orderid, amount in sales_per_order.items():
    owner = order_owner_map.get(orderid)
    if owner:
        sales_per_agent[owner] = sales_per_agent.get(owner, 0) + float(amount)

# Find top agent
if not sales_per_agent:
    top_agent = None
else:
    # choose the agent with max sales; if tie, choose smallest id lexicographically
    max_amount = max(sales_per_agent.values())
    top_agents = [aid for aid, amt in sales_per_agent.items() if amt == max_amount]
    top_agent = sorted(top_agents)[0]

# Output
print("__RESULT__:")
print(json.dumps(top_agent))"""

env_args = {'var_call_qS73Xx2crSLTzY5BadIVzG5o': [{'Id': '800Wt00000DDNlnIAH', 'AccountId': '#001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-09-02'}, {'Id': '800Wt00000DDe3OIAT', 'AccountId': '001Wt00000PGYx5IAH', 'CompanySignedDate': '2022-09-20'}, {'Id': '800Wt00000DDeg6IAD', 'AccountId': '#001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-07-18'}, {'Id': '800Wt00000DDzZLIA1', 'AccountId': '001Wt00000PHVqdIAH', 'CompanySignedDate': '2022-10-26'}, {'Id': '#800Wt00000DDzvrIAD', 'AccountId': '001Wt00000PHHXXIA5', 'CompanySignedDate': '2022-08-30'}, {'Id': '800Wt00000DE0FHIA1', 'AccountId': '#001Wt00000PGZZoIAP', 'CompanySignedDate': '2022-08-02'}, {'Id': '800Wt00000DE0TiIAL', 'AccountId': '001Wt00000PGZmfIAH', 'CompanySignedDate': '2022-09-10'}, {'Id': '800Wt00000DE2vLIAT', 'AccountId': '#001Wt00000PGovMIAT', 'CompanySignedDate': '2022-06-29'}, {'Id': '800Wt00000DE98oIAD', 'AccountId': '001Wt00000PGtdJIAT', 'CompanySignedDate': '2022-11-10'}, {'Id': '800Wt00000DE9GrIAL', 'AccountId': '#001Wt00000PGRnYIAX', 'CompanySignedDate': '2022-06-30'}, {'Id': '#800Wt00000DE9ITIA1', 'AccountId': '#001Wt00000PGzM9IAL', 'CompanySignedDate': '2022-09-11'}, {'Id': '#800Wt00000DE9SAIA1', 'AccountId': '001Wt00000PGdzxIAD', 'CompanySignedDate': '2022-09-30'}, {'Id': '800Wt00000DE9YbIAL', 'AccountId': '001Wt00000PHRTfIAP', 'CompanySignedDate': '2022-11-22'}, {'Id': '#800Wt00000DE9lVIAT', 'AccountId': '#001Wt00000PFsjOIAT', 'CompanySignedDate': '2022-06-26'}, {'Id': '800Wt00000DE9qLIAT', 'AccountId': '001Wt00000PGzSaIAL', 'CompanySignedDate': '2022-09-01'}, {'Id': '800Wt00000DE9rxIAD', 'AccountId': '001Wt00000PHVtpIAH', 'CompanySignedDate': '2022-09-19'}], 'var_call_hQvKR5XvfxgsVFCxXywFNKDV': 'file_storage/call_hQvKR5XvfxgsVFCxXywFNKDV.json', 'var_call_OVZHIPqPBCrhmfhEtvNrq8Bx': 'file_storage/call_OVZHIPqPBCrhmfhEtvNrq8Bx.json', 'var_call_4CFr9E6R6NSHOBaY5VnpwmiU': 'file_storage/call_4CFr9E6R6NSHOBaY5VnpwmiU.json', 'var_call_UTt3I1g6TAfHQyb7Nm6RrcaF': 'file_storage/call_UTt3I1g6TAfHQyb7Nm6RrcaF.json'}

exec(code, env_args)
