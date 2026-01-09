code = """import json, pandas as pd

df_opp = pd.DataFrame(var_call_ZrwksbeY7CF9nTDALvg03RWF)
df_orders = pd.DataFrame(var_call_zi72ii75dA7mZoLPGZi4WNMr)
df_prods = pd.DataFrame(var_call_0Q4JBgMdXVNJ3SSaDDsvQb3b)

# normalize ids (remove leading '#')
for c in ['AccountId','ContactId']:
    if c in df_opp.columns:
        df_opp[c] = df_opp[c].astype(str).str.replace('#','', regex=False)
df_orders['AccountId'] = df_orders['AccountId'].astype(str).str.replace('#','', regex=False)

# filter orders to accounts tied to contact's opps last month
acct_ids = set(df_opp['AccountId'].dropna().unique().tolist())
df_orders2 = df_orders[df_orders['AccountId'].isin(acct_ids)].copy()

# join to products and pick AI processing unit: use name contains 'ai' and ('unit' or 'processing') if possible
prods = df_prods.copy()
prods['Name_norm'] = prods['Name'].astype(str).str.strip().str.lower()

df_orders2 = df_orders2.merge(prods[['Id','Name_norm']], left_on='Product2Id', right_on='Id', how='left')

cand = df_orders2.copy()
cand['is_ai'] = cand['Name_norm'].fillna('').str.contains('ai')
cand['is_processing_unit'] = cand['Name_norm'].fillna('').str.contains('processing') | cand['Name_norm'].fillna('').str.contains('unit')

# prefer rows that match both ai and processing/unit; else any ai
preferred = cand[cand['is_ai'] & cand['is_processing_unit']]
if preferred.empty:
    preferred = cand[cand['is_ai']]

prod_id = None
if not preferred.empty:
    prod_id = preferred.iloc[0]['Product2Id']

result = prod_id if prod_id is not None else None
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_zi72ii75dA7mZoLPGZi4WNMr': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_0Q4JBgMdXVNJ3SSaDDsvQb3b': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_ZrwksbeY7CF9nTDALvg03RWF': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}]}

exec(code, env_args)
