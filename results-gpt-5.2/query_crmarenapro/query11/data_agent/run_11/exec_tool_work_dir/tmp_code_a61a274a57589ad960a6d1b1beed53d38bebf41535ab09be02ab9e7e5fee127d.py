code = """import json, pandas as pd
contact = pd.DataFrame(var_call_4uhxmasA3p9HpjsdxiQIZ5Ud)
orders = pd.DataFrame(var_call_ezTMyd2DmxF9vE5rruVsPSBy)
items = pd.DataFrame(var_call_j2lrJxvDhlCg4nRsPVaNMw01)

def norm(x):
    if pd.isna(x):
        return None
    return str(x).replace('#','').strip()

contact['AccountId_n'] = contact['AccountId'].map(norm)
orders['AccountId_n'] = orders['AccountId'].map(norm)
orders['OrderId_n'] = orders['OrderId'].map(norm)
items['OrderId_n'] = items['OrderId'].map(norm)
items['Product2Id_n'] = items['Product2Id'].map(norm)
items['ProductName_n'] = items['ProductName'].astype(str).str.strip()

acct = contact.loc[0,'AccountId_n'] if len(contact) else None
orders_c = orders[orders['AccountId_n']==acct]
merged = items.merge(orders_c[['OrderId_n','EffectiveDate']].rename(columns={'EffectiveDate':'OrderEffectiveDate'}), on='OrderId_n', how='inner')
ai = merged[merged['ProductName_n'].str.contains('AI', case=False, na=False)]
ai_last_month = ai[(ai['OrderEffectiveDate']>='2021-06-01') & (ai['OrderEffectiveDate']<'2021-07-01')]
prod_id = None
if len(ai_last_month):
    prod_id = ai_last_month.sort_values(['OrderEffectiveDate','OrderId_n']).iloc[-1]['Product2Id_n']
print('__RESULT__:')
print(json.dumps(prod_id))"""

env_args = {'var_call_AlmETN4Mv0xk0ITW5qSzZfSo': [], 'var_call_j2lrJxvDhlCg4nRsPVaNMw01': [{'OrderId': '801Wt00000PGVJKIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PGVJKIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '#01tWt000006hV9xIAE', 'ProductName': 'OptiPower Manager'}, {'OrderId': '801Wt00000PGVJKIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PGVJKIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'OrderId': '#801Wt00000PGVJLIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hVGPIA2', 'ProductName': 'QuantumPCB Modeler  '}, {'OrderId': '#801Wt00000PGVJLIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '#01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'OrderId': '#801Wt00000PGVJLIA5', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hVhpIAE', 'ProductName': 'OptiPower Max'}, {'OrderId': '801Wt00000PGnZVIA1', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PGnZVIA1', 'EffectiveDate': '2021-07-01', 'Product2Id': '#01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'OrderId': '801Wt00000PGnZVIA1', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PGnZVIA1', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHRLeIAP', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hVBZIA2', 'ProductName': 'EduTech Lab'}, {'OrderId': '801Wt00000PHRLeIAP', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV6jIAE', 'ProductName': 'EcoPCB Creator   '}, {'OrderId': '801Wt00000PHRLeIAP', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hVMrIAM', 'ProductName': 'TrainEDU Suite'}, {'OrderId': '801Wt00000PHRLeIAP', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV9xIAE', 'ProductName': 'OptiPower Manager'}, {'OrderId': '801Wt00000PHRLeIAP', 'EffectiveDate': '2021-07-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE', 'ProductName': 'SecureFlow Suite'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '#01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}], 'var_call_ezTMyd2DmxF9vE5rruVsPSBy': [{'OrderId': '801Wt00000PGVJKIA5', 'AccountId': '001Wt00000PHRF9IAP', 'Status': 'Activated', 'EffectiveDate': '2021-07-01'}, {'OrderId': '#801Wt00000PGVJLIA5', 'AccountId': '#001Wt00000PHRF9IAP', 'Status': 'Activated ', 'EffectiveDate': '2021-07-01'}, {'OrderId': '801Wt00000PGnZVIA1', 'AccountId': '001Wt00000PGoAaIAL', 'Status': 'Activated', 'EffectiveDate': '2021-07-01'}, {'OrderId': '801Wt00000PHRLeIAP', 'AccountId': '001Wt00000PHRF9IAP', 'Status': 'Activated', 'EffectiveDate': '2021-07-01'}, {'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'Status': 'Activated  ', 'EffectiveDate': '2021-06-15'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'Status': 'Activated', 'EffectiveDate': '2021-06-01'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'Status': 'Activated', 'EffectiveDate': '2021-06-01'}], 'var_call_4uhxmasA3p9HpjsdxiQIZ5Ud': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
