code = """import json, pandas as pd
ops = pd.DataFrame(var_call_UAhyRjrX3dMjLSI5mvIXqtc5)
orders = pd.DataFrame(var_call_FldSdQF7t6RhCutqJdHx9Y0G)
# normalize ids by removing leading '#'
for col in ['AccountId']:
    if col in ops.columns:
        ops[col] = ops[col].astype(str).str.replace('#','', regex=False).str.strip()
    if col in orders.columns:
        orders[col] = orders[col].astype(str).str.replace('#','', regex=False).str.strip()
orders['ProductName_norm'] = orders['ProductName'].astype(str).str.strip().str.lower()
# join orders to opportunities via AccountId (contact-specific context)
merged = orders.merge(ops[['AccountId']].drop_duplicates(), on='AccountId', how='inner')
# filter AI processing unit by name containing 'ai'
ai = merged[merged['ProductName_norm'].str.contains('ai')]
# choose most recent effective date
if len(ai)==0:
    prod_id = None
else:
    ai['EffectiveDate_dt'] = pd.to_datetime(ai['EffectiveDate'])
    prod_id = ai.sort_values('EffectiveDate_dt', ascending=False).iloc[0]['Product2Id']
result = json.dumps({'Product2Id': prod_id})
print('__RESULT__:')
print(result)"""

env_args = {'var_call_FldSdQF7t6RhCutqJdHx9Y0G': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}], 'var_call_UAhyRjrX3dMjLSI5mvIXqtc5': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'StageName': 'Negotiation'}]}

exec(code, env_args)
