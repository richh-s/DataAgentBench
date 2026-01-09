code = """import json, pandas as pd

def load(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

orders = pd.DataFrame(load(var_call_avRrrL17ZmERh3Gu0FxaN6Yo))
items = pd.DataFrame(load(var_call_VjarSkmTCXoJLkwVOB6yH1JO))
contracts = pd.DataFrame(load(var_call_Vp1EwQ9YlduJ3ajslH9ahbIb))

# normalize IDs by stripping leading '#' and whitespace
for df, col in [(orders,'Id'),(orders,'OwnerId'),(items,'OrderId'),(contracts,'AccountId')]:
    df[col] = df[col].astype(str).str.strip().str.lstrip('#')

# date window: past five months from 2022-11-25 => 2022-06-25 to 2022-11-25 inclusive
start = pd.to_datetime('2022-06-25')
end = pd.to_datetime('2022-11-25')

contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
eligible_accounts = set(contracts.loc[contracts['CompanySignedDate'].between(start, end), 'AccountId'].dropna().astype(str))

orders['EffectiveDate'] = pd.to_datetime(orders['EffectiveDate'], errors='coerce')
orders_filt = orders[orders['EffectiveDate'].between(start, end)].copy()

# keep only orders whose AccountId is in eligible accounts
if 'AccountId' in orders_filt.columns:
    orders_filt['AccountId'] = orders_filt['AccountId'].astype(str).str.strip().str.lstrip('#')
    orders_filt = orders_filt[orders_filt['AccountId'].isin(eligible_accounts)]

# compute sales per order
items['Quantity'] = pd.to_numeric(items['Quantity'], errors='coerce').fillna(0)
items['UnitPrice'] = pd.to_numeric(items['UnitPrice'], errors='coerce').fillna(0)
items['sales'] = items['Quantity'] * items['UnitPrice']

sales_by_order = items.groupby('OrderId', as_index=False)['sales'].sum()
merged = orders_filt.merge(sales_by_order, left_on='Id', right_on='OrderId', how='inner')

sales_by_agent = merged.groupby('OwnerId', as_index=False)['sales'].sum().sort_values('sales', ascending=False)
agent_id = None
if len(sales_by_agent) > 0:
    agent_id = sales_by_agent.iloc[0]['OwnerId']

print('__RESULT__:')
print(json.dumps(agent_id))"""

env_args = {'var_call_Vp1EwQ9YlduJ3ajslH9ahbIb': 'file_storage/call_Vp1EwQ9YlduJ3ajslH9ahbIb.json', 'var_call_avRrrL17ZmERh3Gu0FxaN6Yo': 'file_storage/call_avRrrL17ZmERh3Gu0FxaN6Yo.json', 'var_call_VjarSkmTCXoJLkwVOB6yH1JO': 'file_storage/call_VjarSkmTCXoJLkwVOB6yH1JO.json'}

exec(code, env_args)
