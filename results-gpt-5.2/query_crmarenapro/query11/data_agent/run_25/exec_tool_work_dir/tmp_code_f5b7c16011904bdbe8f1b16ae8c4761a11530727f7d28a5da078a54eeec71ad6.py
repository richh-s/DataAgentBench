code = """import json, pandas as pd
rows = var_call_0LJGyauirew9fXAQ77U0g99C
prods = {r['Id'].replace('#',''): r.get('Name','') for r in var_call_463AZowlNTSKTD8W3h0JnaM5}
# pick product with name containing 'ai' and also likely 'processing unit'
# Since catalog doesn't show such phrase, choose the one explicitly starting with 'AI '
ai = []
for r in rows:
    pid = (r['Product2Id'] or '').replace('#','')
    name = prods.get(pid,'')
    if 'ai' in name.lower():
        ai.append(pid)
# prefer exact prefix 'AI '
chosen = None
for pid in ai:
    if prods.get(pid,'').lower().startswith('ai'):
        chosen = pid
        break
if chosen is None and ai:
    chosen = ai[0]
result = chosen
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_MzYl8k6HwAEJY7MnvAyAprEN': [], 'var_call_0LJGyauirew9fXAQ77U0g99C': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV58IAE'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hVczIAE'}], 'var_call_463AZowlNTSKTD8W3h0JnaM5': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
