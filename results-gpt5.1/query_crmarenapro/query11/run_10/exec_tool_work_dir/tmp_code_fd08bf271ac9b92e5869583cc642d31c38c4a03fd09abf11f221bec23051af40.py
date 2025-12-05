code = """import json
opp_accts = var_call_VHyNhVCvqy4l3uH79CuNS7GR
orders = var_call_rUBM61nKHa1d6D7OKJM1jQyo
ai_products = var_call_73lvzEfFI8rMUHsFPgpWf3jk
acct_ids = {o['AccountId'].replace('#','') for o in opp_accts}
rel_orders = [o for o in orders if o['AccountId'].replace('#','') in acct_ids]
ai_prod_ids = {p['Id'].replace('#','') for p in ai_products}
rel_ai_orders = [o for o in rel_orders if o['Product2Id'].replace('#','') in ai_prod_ids]
rel_ai_orders_sorted = sorted(rel_ai_orders, key=lambda x: x['EffectiveDate'], reverse=True)
prod_id = rel_ai_orders_sorted[0]['Product2Id'].replace('#','') if rel_ai_orders_sorted else None
result = json.dumps(prod_id)
print("__RESULT__:")
print(result)"""

env_args = {'var_call_rUBM61nKHa1d6D7OKJM1jQyo': [{'Product2Id': '#01tWt000006hV9xIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hTUkIAM', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '#01tWt000006hV6jIAE', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hTUkIAM', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'AccountId': '001Wt00000PGoAaIAL', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV6jIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV9xIAE', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hVBZIA2', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hVMrIAM', 'AccountId': '001Wt00000PHRF9IAP', 'EffectiveDate': '2021-07-01'}, {'Product2Id': '01tWt000006hV8LIAU', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15'}, {'Product2Id': '01tWt000006hTUkIAM', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV57IAE', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01'}, {'Product2Id': '01tWt000006hV58IAE', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01'}], 'var_call_73lvzEfFI8rMUHsFPgpWf3jk': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_VHyNhVCvqy4l3uH79CuNS7GR': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX'}]}

exec(code, env_args)
