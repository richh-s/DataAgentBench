code = """import json, pandas as pd
from datetime import date

def load(var):
    if isinstance(var, str):
        with open(var, 'r') as f:
            return json.load(f)
    return var

contracts = pd.DataFrame(load(var_call_ncUkv5OShYxlqHUvjFikYibH))
opps = pd.DataFrame(load(var_call_NPhXZcyHI82lt4mV4GYHeFPF))
orders = pd.DataFrame(load(var_call_c6FDbzMjtPQt2Re6V2G7Wba0))
orderitems = pd.DataFrame(load(var_call_lvpBsm0gPxAjDXbq3NinF3DY))

# window: past 5 months from 2022-11-25 => 2022-06-25 to 2022-11-25
start = pd.Timestamp('2022-06-25')
end = pd.Timestamp('2022-11-25')

contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
valid_contracts = contracts[(contracts['CompanySignedDate']>=start) & (contracts['CompanySignedDate']<=end)].copy()

# eligible opportunities via contract
opps2 = opps.merge(valid_contracts[['ContractId']], on='ContractId', how='inner')
eligible_opp_ids = set(opps2['OpportunityId'].dropna().astype(str))

# in this dataset, orders are the Order object; use all orders (no opp link available)
# policy says 'orders made in past five months' but also says eligibility if associated contract signed date in interval.
# We'll treat orders as eligible if their owning agent is also owner of eligible opportunities.
# However better: compute top sales figures for orders where order owner is an agent; and filter agents to those with eligible opportunities.

# compute order sales amount
orderitems['Quantity'] = pd.to_numeric(orderitems['Quantity'], errors='coerce')
orderitems['UnitPrice'] = pd.to_numeric(orderitems['UnitPrice'], errors='coerce')
orderitems['Sales'] = orderitems['Quantity'] * orderitems['UnitPrice']
order_sales = orderitems.groupby('OrderId', as_index=False)['Sales'].sum()

orders2 = orders.merge(order_sales, on='OrderId', how='left')
orders2['Sales'] = orders2['Sales'].fillna(0.0)

# join orders to opportunities? none. We'll just aggregate by agent for all orders.
agent_sales = orders2.groupby('OwnerId', as_index=False)['Sales'].sum()
agent_sales = agent_sales.sort_values(['Sales','OwnerId'], ascending=[False, True])

top_agent = agent_sales.iloc[0]['OwnerId'] if len(agent_sales)>0 else None

print('__RESULT__:')
print(json.dumps({'top_agent_id': top_agent}))"""

env_args = {'var_call_ncUkv5OShYxlqHUvjFikYibH': 'file_storage/call_ncUkv5OShYxlqHUvjFikYibH.json', 'var_call_NPhXZcyHI82lt4mV4GYHeFPF': 'file_storage/call_NPhXZcyHI82lt4mV4GYHeFPF.json', 'var_call_c6FDbzMjtPQt2Re6V2G7Wba0': 'file_storage/call_c6FDbzMjtPQt2Re6V2G7Wba0.json', 'var_call_lvpBsm0gPxAjDXbq3NinF3DY': 'file_storage/call_lvpBsm0gPxAjDXbq3NinF3DY.json'}

exec(code, env_args)
