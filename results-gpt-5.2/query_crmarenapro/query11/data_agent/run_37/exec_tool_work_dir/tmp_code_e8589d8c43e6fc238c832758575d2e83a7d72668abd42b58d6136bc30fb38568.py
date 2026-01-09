code = """import json, pandas as pd

opp = pd.DataFrame(var_call_RwV8wSnQpBsXW89iGqPUC5FJ)
orders = pd.DataFrame(var_call_z2C6qKuKcxs5jfA4wXztt36I)
contact = var_call_f83vGjKyqUGcXsFCSzxIikY4[0]
acct = contact['AccountId'].replace('#','') if contact and contact.get('AccountId') else None

# Normalize IDs
for df in [opp, orders]:
    if not df.empty:
        for col in ['AccountId','Product2Id']:
            if col in df.columns:
                df[col] = df[col].astype(str).str.replace('#','', regex=False)

# Filter orders to contact account
if acct and not orders.empty:
    orders_acct = orders[orders['AccountId']==acct].copy()
else:
    orders_acct = orders.iloc[0:0].copy()

# Identify AI processing unit products using product names list
prod = pd.DataFrame(var_call_JTwTUVUBUMyX6TbKrqzlqMw9)
if not prod.empty:
    prod['Id_norm'] = prod['Id'].astype(str).str.replace('#','', regex=False)
    prod['Name_clean'] = prod['Name'].astype(str).str.strip().str.lower()
    ai_ids = set(prod.loc[prod['Name_clean'].str.contains('ai', na=False), 'Id_norm'].tolist())
else:
    ai_ids = set()

# Candidate purchases last month from opp line items and orders
cand = []
if not opp.empty:
    opp_ai = opp[opp['Product2Id'].isin(ai_ids)].copy()
    cand += opp_ai['Product2Id'].tolist()
if not orders_acct.empty:
    ord_ai = orders_acct[orders_acct['Product2Id'].isin(ai_ids)].copy()
    cand += ord_ai['Product2Id'].tolist()

product_id = cand[0] if cand else None

print('__RESULT__:')
print(json.dumps({'Product2Id': product_id}))"""

env_args = {'var_call_z2C6qKuKcxs5jfA4wXztt36I': [{'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'AccountId': '001Wt00000PGXrNIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_f83vGjKyqUGcXsFCSzxIikY4': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_RwV8wSnQpBsXW89iGqPUC5FJ': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_JTwTUVUBUMyX6TbKrqzlqMw9': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}]}

exec(code, env_args)
