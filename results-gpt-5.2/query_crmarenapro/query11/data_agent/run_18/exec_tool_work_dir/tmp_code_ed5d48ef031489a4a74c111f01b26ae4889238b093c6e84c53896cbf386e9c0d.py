code = """import json, pandas as pd
contact = pd.DataFrame(var_call_Pz5MRVJo5qZquvcYoCiKs2QF)
orders = pd.DataFrame(var_call_1sXFNXJnsS8veFBMld0ocNRC)
products = pd.DataFrame(var_call_Vkztlj42mBbPzQCrUF02Ti2J)

contact_acct = contact.loc[0,'AccountId'].replace('#','')
orders['AccountId_clean'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)
rel_orders = orders[orders['AccountId_clean']==contact_acct].copy()

rel_orders = rel_orders.merge(products, left_on='Product2Id', right_on='Id', how='left')
# AI processing unit heuristic: name contains 'AI' and ('unit' or 'processing')
rel_orders['name_l'] = rel_orders['Name'].fillna('').str.lower()
ai_proc = rel_orders[rel_orders['name_l'].str.contains('ai') & (rel_orders['name_l'].str.contains('unit') | rel_orders['name_l'].str.contains('processing'))]
if ai_proc.empty:
    # fallback: any product with 'ai' in name for that month
    ai_proc = rel_orders[rel_orders['name_l'].str.contains('ai')]

product_id = None
if not ai_proc.empty:
    product_id = ai_proc.iloc[0]['Product2Id']

print('__RESULT__:')
print(json.dumps({'Product2Id': product_id}))"""

env_args = {'var_call_1sXFNXJnsS8veFBMld0ocNRC': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_Vkztlj42mBbPzQCrUF02Ti2J': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_Pz5MRVJo5qZquvcYoCiKs2QF': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_bCCJhW7wHeQB18hknUzDVPZw': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}]}

exec(code, env_args)
