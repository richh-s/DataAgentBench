code = """import json, pandas as pd
ops = pd.DataFrame(var_call_pdkek3fDo4gGeLup54sukjCC)
orders = pd.DataFrame(var_call_gjzfXWq9eKFMwSqs1DKuW2bi)
acct_ids = set(ops['AccountId'].astype(str).str.replace('#','', regex=False).tolist())
orders['AccountId_clean'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)
orders_f = orders[orders['AccountId_clean'].isin(acct_ids)].copy()
# choose AI processing unit by name contains 'AI' (case-insensitive)
orders_f['is_ai'] = orders_f['ProductName'].astype(str).str.contains('AI', case=False, na=False)
ai = orders_f[orders_f['is_ai']].copy()
prod_id = None
if len(ai)>0:
    prod_id = ai.iloc[0]['Product2Id']
    if isinstance(prod_id, str):
        prod_id = prod_id.replace('#','')
res = prod_id if prod_id is not None else ''
print('__RESULT__:')
print(json.dumps(res))"""

env_args = {'var_call_gjzfXWq9eKFMwSqs1DKuW2bi': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '#01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}], 'var_call_pdkek3fDo4gGeLup54sukjCC': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}]}

exec(code, env_args)
