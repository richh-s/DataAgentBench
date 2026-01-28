code = """import json, pandas as pd

opps = pd.DataFrame(var_call_IAjWUtXkduIHBMkH3v7E5mJ8)
prods = pd.DataFrame(var_call_z1N1tCkwRLJBGFqRQ94c0kVs)
orders = pd.DataFrame(var_call_hOWUeq10or9HlKZf9JbL3bRZ)

# normalize ids
for df, col in [(opps,'Product2Id'), (prods,'Id'), (orders,'Product2Id')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

prods['Name_norm'] = prods['Name'].astype(str).str.strip()

# Find AI processing unit candidates from product names
keywords = ['ai','processing unit','apu']
mask = prods['Name_norm'].str.lower().str.contains('ai')  # broad but per request
ai_prod_norm_ids = set(prods.loc[mask, 'Id_norm'].tolist())

# prioritize purchased last month via orders tied to contact's account? we don't have contact link in orders; use opportunities for contact
opps_ai = opps[opps['Product2Id_norm'].isin(ai_prod_norm_ids)].copy()

# If multiple, pick the one that appears in last-month transactions; choose most frequent then deterministic
if not opps_ai.empty:
    chosen = opps_ai['Product2Id_norm'].value_counts().index[0]
else:
    # fallback to order items in last month that are AI products (no contact link)
    ord_ai = orders[orders['Product2Id_norm'].isin(ai_prod_norm_ids)]
    chosen = ord_ai['Product2Id_norm'].iloc[0] if not ord_ai.empty else None

print('__RESULT__:')
print(json.dumps(chosen))"""

env_args = {'var_call_hOWUeq10or9HlKZf9JbL3bRZ': [{'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderItemId': '#802Wt00000797O2IAI', 'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderItemId': '802Wt00000795XxIAI', 'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderItemId': '#802Wt0000079AQlIAM', 'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderItemId': '802Wt00000796euIAA', 'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_z1N1tCkwRLJBGFqRQ94c0kVs': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}], 'var_call_RmuYFi9azWiQB9Dn9LGQohrN': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_IAjWUtXkduIHBMkH3v7E5mJ8': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
