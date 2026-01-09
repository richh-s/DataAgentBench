code = """import json

rows = var_call_yxovWeTlStAgCfmSwWMbzrbc
# find product whose name indicates AI processing unit
candidates = []
for r in rows:
    name = (r.get('Name') or '').strip().lower()
    if 'ai' in name and ('unit' in name or 'processing' in name or True):
        candidates.append(r)

# Prefer exact match to AI Cirku-Tech if present
chosen = None
for r in candidates:
    if (r.get('Name') or '').strip().lower() == 'ai cirku-tech':
        chosen = r
        break
if chosen is None and candidates:
    chosen = candidates[0]

answer = chosen['Id'] if chosen else None
print('__RESULT__:')
print(json.dumps(answer))"""

env_args = {'var_call_pafo0sLFIPFOYQ3j4SMJlYsm': [{'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-15T10:27:45.000+0000', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'ContactId': '003Wt00000Jqy8SIAR', 'CreatedDate': '2021-03-01T10:15:30.000+0000', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_yxovWeTlStAgCfmSwWMbzrbc': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
