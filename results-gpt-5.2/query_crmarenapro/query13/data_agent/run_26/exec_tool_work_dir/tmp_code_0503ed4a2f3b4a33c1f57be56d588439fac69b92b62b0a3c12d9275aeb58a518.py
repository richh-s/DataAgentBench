code = """import json, pandas as pd
from datetime import date

def load(v):
    if isinstance(v, str) and v.endswith('.json'):
        with open(v, 'r') as f:
            return json.load(f)
    return v

contracts = pd.DataFrame(load(var_call_xbt3ZTl8T776utyBUEHVnI5z))
orders = pd.DataFrame(load(var_call_zY7dgXAsTQp6xBbtVBnMPovJ))
order_items = pd.DataFrame(load(var_call_AyGhF7Yrh20zUwoLitDzPlGt))

# normalize ids (strip leading # and whitespace)
for df, cols in [(contracts,['ContractId']), (orders,['OrderId','OwnerId']), (order_items,['OrderId'])]:
    for c in cols:
        df[c] = df[c].astype(str).str.strip().str.lstrip('#')

contracts['CompanySignedDate'] = pd.to_datetime(contracts['CompanySignedDate'], errors='coerce')
orders['EffectiveDate'] = pd.to_datetime(orders['EffectiveDate'], errors='coerce')

# window: past five months from 2022-11-25 inclusive => start 2022-06-25
start = pd.Timestamp('2022-06-25')
end = pd.Timestamp('2022-11-25')
eligible_contracts = set(contracts.loc[(contracts['CompanySignedDate']>=start)&(contracts['CompanySignedDate']<=end), 'ContractId'].dropna().tolist())

# eligible opportunities by contract
opps = pd.DataFrame(load(var_call_s4PWqU7wn1oKkGEw586Ujw7d))
opps['ContractId'] = opps['ContractId'].astype(str).str.strip().str.lstrip('#')
opps['OwnerId'] = opps['OwnerId'].astype(str).str.strip().str.lstrip('#')
eligible_opp_owner = opps.loc[opps['ContractId'].isin(eligible_contracts), ['OpportunityId','OwnerId']]

# compute order sales in past 5 months
order_items['Quantity'] = pd.to_numeric(order_items['Quantity'], errors='coerce').fillna(0)
order_items['UnitPrice'] = pd.to_numeric(order_items['UnitPrice'], errors='coerce').fillna(0)
order_items['Sales'] = order_items['Quantity'] * order_items['UnitPrice']

orders_win = orders.loc[(orders['EffectiveDate']>=start)&(orders['EffectiveDate']<=end), ['OrderId','OwnerId']]
# sum sales per order
sales_per_order = order_items.groupby('OrderId', as_index=False)['Sales'].sum()
orders_sales = orders_win.merge(sales_per_order, on='OrderId', how='left').fillna({'Sales':0})
agent_sales_orders = orders_sales.groupby('OwnerId', as_index=False)['Sales'].sum()

# top agent by order sales
if agent_sales_orders.empty:
    top_agent = None
else:
    top_agent = agent_sales_orders.sort_values(['Sales','OwnerId'], ascending=[False, True]).iloc[0]['OwnerId']

print('__RESULT__:')
print(json.dumps(None if top_agent is None else str(top_agent)))"""

env_args = {'var_call_xbt3ZTl8T776utyBUEHVnI5z': 'file_storage/call_xbt3ZTl8T776utyBUEHVnI5z.json', 'var_call_s4PWqU7wn1oKkGEw586Ujw7d': 'file_storage/call_s4PWqU7wn1oKkGEw586Ujw7d.json', 'var_call_AyGhF7Yrh20zUwoLitDzPlGt': 'file_storage/call_AyGhF7Yrh20zUwoLitDzPlGt.json', 'var_call_zY7dgXAsTQp6xBbtVBnMPovJ': 'file_storage/call_zY7dgXAsTQp6xBbtVBnMPovJ.json'}

exec(code, env_args)
