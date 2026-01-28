code = """import json, pandas as pd

contact = pd.DataFrame(var_call_ZxT1EHFT0HYjHsp8a4XXVooJ)
orders = pd.DataFrame(var_call_JWPIqVo6kvGd86gaCVOAlI0W)

# normalize ids by stripping leading '#'
contact['AccountId_norm'] = contact['AccountId'].astype(str).str.replace('#','', regex=False)
orders['AccountId_norm'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)

# filter to this contact's account and AI processing unit products
ai_orders = orders[(orders['AccountId_norm'] == contact.loc[0,'AccountId_norm']) & (orders['ProductName'].str.contains('AI', case=False, na=False))]

product_id = None
if len(ai_orders) > 0:
    # last month relative to 2021-07-15 is June 2021; already filtered
    # if multiple, pick latest effective date then first
    ai_orders['EffectiveDate_dt'] = pd.to_datetime(ai_orders['EffectiveDate'])
    ai_orders = ai_orders.sort_values(['EffectiveDate_dt','OrderId'], ascending=[False, False])
    product_id = ai_orders.iloc[0]['Product2Id']

out = json.dumps(product_id)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_JWPIqVo6kvGd86gaCVOAlI0W': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}], 'var_call_ZxT1EHFT0HYjHsp8a4XXVooJ': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_Sx5GDhRTxIWR7IfDhMqAhsLl': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15 00:00:00'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15 00:00:00'}]}

exec(code, env_args)
