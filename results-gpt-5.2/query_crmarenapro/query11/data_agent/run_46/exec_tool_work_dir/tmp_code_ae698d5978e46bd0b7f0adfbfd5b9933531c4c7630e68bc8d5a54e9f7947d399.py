code = """import json
import pandas as pd

opp = pd.DataFrame(var_call_9gXDEBoB54stkVRjXZcmU0n8)
ord_items = pd.DataFrame(var_call_u8o7lrE1kdWUjqGBiZjzRgyu)
prods_ai = pd.DataFrame(var_call_bCNWPzMVRZVqjABIJ8VsNsgz)

# normalize ids
for df,col in [(opp,'Product2Id'),(ord_items,'Product2Id'),(prods_ai,'ProductId')]:
    if col in df.columns:
        df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False).str.strip()

# Candidate product ids from last month transactions for this contact (prefer orders, else opportunities)
order_prod_ids = set(ord_items['Product2Id_norm'].dropna().tolist()) if not ord_items.empty else set()
opp_prod_ids = set(opp['Product2Id_norm'].dropna().tolist()) if not opp.empty else set()

# identify AI processing unit product: best effort match on product name containing both 'ai' and maybe 'unit'
prods_ai['name_norm'] = prods_ai['Name'].astype(str).str.strip().str.lower()

def is_ai_processing_unit(name: str) -> bool:
    return ('ai' in name) and (('unit' in name) or ('processing' in name) or ('apu' in name) or ('aip' in name))

prods_ai['is_target'] = prods_ai['name_norm'].apply(is_ai_processing_unit)

# If none match strict, fall back to any product in last-month items that has 'ai' in name.

def pick_from(candidate_ids):
    if not candidate_ids:
        return None
    sub = prods_ai[prods_ai['ProductId_norm'].isin(candidate_ids)].copy()
    if sub.empty:
        return None
    target = sub[sub['is_target']]
    if not target.empty:
        return target.iloc[0]['ProductId_norm']
    return sub.iloc[0]['ProductId_norm']

picked = pick_from(order_prod_ids) or pick_from(opp_prod_ids)

print('__RESULT__:')
print(json.dumps(picked))"""

env_args = {'var_call_oevEILm1V2YHmV0UvKJTIUIj': [], 'var_call_qXkDPqy2k2QNNCOXUca4qA7U': [{'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'AccountId': '001Wt00000PGXrNIAX'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP'}], 'var_call_UhOjyjIjvnmy18u1zYdvdzwd': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_9gXDEBoB54stkVRjXZcmU0n8': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_u8o7lrE1kdWUjqGBiZjzRgyu': [{'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'Product2Id': '01tWt000006hV8LIAU'}], 'var_call_bCNWPzMVRZVqjABIJ8VsNsgz': [{'ProductId': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'ProductId': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'ProductId': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'ProductId': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'ProductId': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'ProductId': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'ProductId': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'ProductId': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'ProductId': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'ProductId': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'ProductId': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}], 'var_call_cd1QUW7g9Uqcso8W6KS7bePV': []}

exec(code, env_args)
