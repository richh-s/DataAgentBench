code = """import json, pandas as pd

df = pd.DataFrame(var_call_qSqef3yDvuPUEwiVcTJPpBlQ)
prod = pd.DataFrame(var_call_d4KhhMJnooLk4IkYPDK3Ez6h)

# normalize ids
for c in ['Product2Id']:
    df[c] = df[c].astype(str).str.replace('#','', regex=False)
prod['Id_norm'] = prod['Id'].astype(str).str.replace('#','', regex=False)

m = df.merge(prod, left_on='Product2Id', right_on='Id_norm', how='left')

# identify AI processing unit-like product: prefer description/name containing 'AI' and ('processing' and 'unit')
name_desc = (m['Name'].fillna('') + ' ' + m['Description'].fillna('')).str.lower()
mask = name_desc.str.contains('ai') & (name_desc.str.contains('processing') | name_desc.str.contains('unit') | name_desc.str.contains('ai-driven'))

candidates = m[mask].copy()

# if none, fall back to any with 'ai' in name/desc
if candidates.empty:
    mask2 = name_desc.str.contains('ai')
    candidates = m[mask2].copy()

# choose most recent by CloseDate then CreatedDate
if not candidates.empty:
    candidates['CloseDate_dt'] = pd.to_datetime(candidates['CloseDate'], errors='coerce')
    candidates['CreatedDate_dt'] = pd.to_datetime(candidates['CreatedDate'], errors='coerce')
    candidates = candidates.sort_values(['CloseDate_dt','CreatedDate_dt'], ascending=[False, False])
    product_id = candidates.iloc[0]['Product2Id']
else:
    product_id = None

print('__RESULT__:')
print(json.dumps({'Product2Id': product_id}))"""

env_args = {'var_call_bwNcK7dM846THv8nvdsKf0F4': [{'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderItemId': '#802Wt00000797O2IAI', 'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderItemId': '802Wt00000795XxIAI', 'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderItemId': '#802Wt0000079AQlIAM', 'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderItemId': '802Wt00000796euIAA', 'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_x1VlIpMixfpcDmBeSovBu8NZ': [], 'var_call_vnLJ3XMhB9kNQeMckfDLhqsX': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_qSqef3yDvuPUEwiVcTJPpBlQ': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'AccountId': '001Wt00000PGXrNIAX', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_d4KhhMJnooLk4IkYPDK3Ez6h': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer', 'Description': 'Cloud-based design collaboration tool enhancing team productivity across global projects.'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech', 'Description': 'AI-driven circuit design platform offering rapid prototyping and innovation support.'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager', 'Description': 'Enhanced power optimization tools for sustainable electronics development.'}]}

exec(code, env_args)
