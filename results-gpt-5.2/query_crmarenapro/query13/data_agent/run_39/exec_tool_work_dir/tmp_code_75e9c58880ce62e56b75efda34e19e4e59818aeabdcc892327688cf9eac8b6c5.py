code = """import json, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

contracts = pd.DataFrame(load(var_call_fyzHIxuvWc51aVFt3uG6aO3L))
opps = pd.DataFrame(load(var_call_6YugpIsFfjgu2VBYFrGwXQp3))
orders = pd.DataFrame(load(var_call_T3J9oSiHi3L8Y99vq2AJyAGx))
items = pd.DataFrame(load(var_call_x5B12CDxKDSKK663Lg03SjRG))

# normalize ids: strip whitespace, remove leading '#'
for df, col in [(contracts,'Id'), (opps,'ContractID__c'), (orders,'Id'), (items,'OrderId')]:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip().str.replace(r'^#','', regex=True)
# contracts Id too
contracts['Id'] = contracts['Id'].astype(str).str.strip().str.replace(r'^#','', regex=True)

# filter contracts in past five months relative to 2022-11-25 => from 2022-06-25 inclusive
contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
start = pd.Timestamp('2022-06-25')
end = pd.Timestamp('2022-11-25')
eligible_contracts = set(contracts.loc[(contracts['CompanySignedDate']>=start) & (contracts['CompanySignedDate']<=end), 'Id'].dropna())

# eligible opportunities by contract
opps['ContractID__c'] = opps['ContractID__c'].replace({'None': None, 'nan': None})
eligible_opps = set(opps.loc[opps['ContractID__c'].isin(eligible_contracts), 'Id'].astype(str).str.strip().str.replace(r'^#','', regex=True))

# eligible orders: order id equals opportunity id (after normalization)
orders['Id_norm'] = orders['Id'].astype(str).str.strip().str.replace(r'^#','', regex=True)
orders['OwnerId_norm'] = orders['OwnerId'].astype(str).str.strip().str.replace(r'^#','', regex=True)
eligible_orders = orders.loc[orders['Id_norm'].isin(eligible_opps), ['Id_norm','OwnerId_norm']]

# compute sales per order from items
items['OrderId_norm'] = items['OrderId'].astype(str).str.strip().str.replace(r'^#','', regex=True)
items['Quantity'] = pd.to_numeric(items['Quantity'], errors='coerce')
items['UnitPrice'] = pd.to_numeric(items['UnitPrice'], errors='coerce')
items['sales'] = items['Quantity'] * items['UnitPrice']
order_sales = items.groupby('OrderId_norm', as_index=False)['sales'].sum()

merged = eligible_orders.merge(order_sales, left_on='Id_norm', right_on='OrderId_norm', how='inner')
agent_sales = merged.groupby('OwnerId_norm', as_index=False)['sales'].sum().sort_values('sales', ascending=False)

agent_id = agent_sales.iloc[0]['OwnerId_norm'] if len(agent_sales)>0 else None

print('__RESULT__:')
print(json.dumps({'agent_id': agent_id}))"""

env_args = {'var_call_fyzHIxuvWc51aVFt3uG6aO3L': 'file_storage/call_fyzHIxuvWc51aVFt3uG6aO3L.json', 'var_call_6YugpIsFfjgu2VBYFrGwXQp3': 'file_storage/call_6YugpIsFfjgu2VBYFrGwXQp3.json', 'var_call_T3J9oSiHi3L8Y99vq2AJyAGx': 'file_storage/call_T3J9oSiHi3L8Y99vq2AJyAGx.json', 'var_call_x5B12CDxKDSKK663Lg03SjRG': 'file_storage/call_x5B12CDxKDSKK663Lg03SjRG.json'}

exec(code, env_args)
