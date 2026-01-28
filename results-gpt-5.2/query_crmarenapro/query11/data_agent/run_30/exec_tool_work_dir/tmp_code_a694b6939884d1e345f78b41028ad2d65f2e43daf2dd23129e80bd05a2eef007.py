code = """import json, pandas as pd

opp = pd.DataFrame(var_call_CTOOtUOI5gKX4uxjxcbemS25)
prod = pd.DataFrame(var_call_qiNqvZRZA8znkxV9WMmAwjHR)

# normalize product ids
opp['Product2Id_norm'] = opp['Product2Id'].astype(str).str.replace('#','', regex=False)
prod['Id_norm'] = prod['Id'].astype(str).str.replace('#','', regex=False)

merged = opp.merge(prod, left_on='Product2Id_norm', right_on='Id_norm', how='left')
# identify AI processing unit: name contains 'AI' and (processing/unit) or 'AI ' at start; best match in available list is AI Cirku-Tech
candidates = merged[merged['Name'].fillna('').str.strip().str.lower().str.contains('ai')]
# prefer those that look like processing unit keywords
kw = candidates[candidates['Name'].str.strip().str.lower().str.contains('processing|unit')]
if len(kw)==0:
    # fallback: pick AI Cirku-Tech if present else first AI candidate
    cirku = candidates[candidates['Name'].str.strip().eq('AI Cirku-Tech')]
    pick = cirku.iloc[0] if len(cirku)>0 else candidates.iloc[0]
else:
    pick = kw.iloc[0]

answer = pick['Product2Id_norm']
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_XfPodZ4rz7uMMS7rEZhXUlEk': [{'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderItemId': '#802Wt00000797O2IAI', 'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderItemId': '802Wt00000795XxIAI', 'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderItemId': '#802Wt0000079AQlIAM', 'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderItemId': '802Wt00000796euIAA', 'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_qiNqvZRZA8znkxV9WMmAwjHR': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_CTOOtUOI5gKX4uxjxcbemS25': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}]}

exec(code, env_args)
