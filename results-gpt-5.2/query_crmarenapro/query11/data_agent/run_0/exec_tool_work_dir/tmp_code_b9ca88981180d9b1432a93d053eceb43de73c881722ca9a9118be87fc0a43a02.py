code = """import json, pandas as pd
contact = var_call_0o2IMPE2BG6qsCyybOwV9QQG[0]
acct = contact['AccountId'].replace('#','') if contact.get('AccountId') else None
orders = pd.DataFrame(var_call_ICDVXBX6oPmmHDdMH4faoKfM)
if not orders.empty:
    orders['AccountId_clean'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)
    orders['Product2Id_clean'] = orders['Product2Id'].astype(str).str.replace('#','', regex=False)
    orders['ProductName_clean'] = orders['ProductName'].astype(str).str.strip()
    filt = orders[(orders['AccountId_clean']==acct) & (orders['ProductName_clean'].str.contains('AI', case=False, na=False))]
    prod_id = None
    if not filt.empty:
        # prefer exact AI processing unit-ish by choosing product with AI in name and earliest date in last month, stable
        filt = filt.sort_values(['EffectiveDate','ProductName_clean','Product2Id_clean'])
        prod_id = filt.iloc[0]['Product2Id_clean']
else:
    prod_id = None
result = prod_id
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_ICDVXBX6oPmmHDdMH4faoKfM': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '#01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}], 'var_call_0o2IMPE2BG6qsCyybOwV9QQG': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_StDeAPTjB85sTpzRCtIhS5Fa': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'CloseDate': '2021-06-15'}]}

exec(code, env_args)
