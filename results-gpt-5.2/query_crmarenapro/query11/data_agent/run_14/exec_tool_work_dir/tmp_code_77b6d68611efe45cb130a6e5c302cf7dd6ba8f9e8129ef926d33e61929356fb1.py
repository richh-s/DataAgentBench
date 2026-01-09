code = """import json, pandas as pd
contact_acct = var_call_SaHkEC2vfsvH4QtGFqdgrV5G[0]['AccountId'].replace('#','')
orders = pd.DataFrame(var_call_G8HtDQQvmf6IgoYhSJGxSF8l)
items = pd.DataFrame(var_call_McKC3Qxgfl6rbqzpNT2s2wxj)
orders['AccountId_norm'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)
items['Product2Id_norm'] = items['Product2Id'].astype(str).str.replace('#','', regex=False)
# filter to contact account
orders_f = orders[orders['AccountId_norm']==contact_acct]
merged = items.merge(orders_f, on='OrderId', how='inner')
# load candidate AI products list and match
ai = pd.DataFrame(var_call_70HHUNlsPlhvEgNPlCbFNZeq)
ai['Id_norm'] = ai['Id'].astype(str).str.replace('#','', regex=False)
merged = merged.merge(ai[['Id_norm']], left_on='Product2Id_norm', right_on='Id_norm', how='inner')
prod_id = None
if len(merged)>0:
    # choose latest EffectiveDate
    merged['EffectiveDate'] = pd.to_datetime(merged['EffectiveDate'])
    prod_id = merged.sort_values('EffectiveDate', ascending=False).iloc[0]['Product2Id_norm']
result = json.dumps(prod_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_McKC3Qxgfl6rbqzpNT2s2wxj': [{'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderItemId': '#802Wt00000797O2IAI', 'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderItemId': '802Wt00000795XxIAI', 'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderItemId': '#802Wt0000079AQlIAM', 'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderItemId': '802Wt00000796euIAA', 'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_70HHUNlsPlhvEgNPlCbFNZeq': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_G8HtDQQvmf6IgoYhSJGxSF8l': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'Status': 'Activated  ', 'EffectiveDate': '2021-06-15'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'Status': 'Activated', 'EffectiveDate': '2021-06-01'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2021-06-01'}], 'var_call_SaHkEC2vfsvH4QtGFqdgrV5G': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
