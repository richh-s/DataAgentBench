code = """import json, pandas as pd

contact = pd.DataFrame(var_call_OpBBaSz1gGEPbauN3TfhWbjw)
orders = pd.DataFrame(var_call_YiAn548RvzXHXNrv9F3MlTjA)

# normalize account ids (strip leading #)
contact['AccountId_norm'] = contact['AccountId'].astype(str).str.replace('#','', regex=False)
orders['AccountId_norm'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)

# filter orders for this contact's account
acct = contact.loc[0, 'AccountId_norm'] if len(contact) else None
rel_orders = orders[orders['AccountId_norm'] == acct].copy()

# among those, pick AI processing unit: product name contains 'AI'
ai_orders = rel_orders[rel_orders['ProductName'].astype(str).str.contains('AI', case=False, na=False)].copy()

product_id = None
if len(ai_orders):
    # last month (June) already filtered in query; pick latest effective date then first
    ai_orders['EffectiveDate_dt'] = pd.to_datetime(ai_orders['EffectiveDate'], errors='coerce')
    ai_orders = ai_orders.sort_values(['EffectiveDate_dt','OrderId'], ascending=[False, False])
    product_id = ai_orders.iloc[0]['Product2Id']

result = product_id
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_YiAn548RvzXHXNrv9F3MlTjA': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}], 'var_call_SEEnxnKDaMaF6RunVOsvZpmk': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_OpBBaSz1gGEPbauN3TfhWbjw': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_r9OwyuuWtOGwzBNpg9miKp3K': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}]}

exec(code, env_args)
