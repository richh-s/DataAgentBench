code = """import json, pandas as pd
opp = pd.DataFrame(var_call_WjnItwIZZZVGwJJwRBghlOt7)
acct = var_call_ek0uIN5eeP5eU6zQLZJia3WP[0]['AccountId'].replace('#','')
orders = pd.DataFrame(var_call_zKlpViP1zEFyJG4VlAnTwsSe)
orders['AccountId_norm'] = orders['AccountId'].str.replace('#','', regex=False)
orders_contact = orders[orders['AccountId_norm'] == acct]
# candidate product ids from opps in June
opp['Product2Id_norm'] = opp['Product2Id'].str.replace('#','', regex=False)
# join with names
prod = pd.DataFrame(var_call_sDFThv7zjVDU6D7hbgV2qHct)
prod['Id_norm'] = prod['Id'].str.replace('#','', regex=False)
prod_map = dict(zip(prod['Id_norm'], prod['Name'].str.strip()))
# find AI processing unit by name heuristic
ai_candidates = [pid for pid,name in prod_map.items() if 'ai' in name.lower()]
# prefer ones appearing in June opps and/or orders
opp_pids = set(opp['Product2Id_norm'].tolist())
order_pids = set(orders_contact['Product2Id'].str.replace('#','', regex=False).tolist())
common = [pid for pid in ai_candidates if pid in opp_pids or pid in order_pids]
# pick first deterministic sorted
chosen = sorted(common)[0] if common else (sorted(ai_candidates)[0] if ai_candidates else None)
print('__RESULT__:')
print(json.dumps(chosen))"""

env_args = {'var_call_aVP665P2hkIBXQM0PiB40jwu': [], 'var_call_WjnItwIZZZVGwJJwRBghlOt7': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_ek0uIN5eeP5eU6zQLZJia3WP': [{'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_zKlpViP1zEFyJG4VlAnTwsSe': [{'Product2Id': '01tWt000006hV8LIAU', 'EffectiveDate': '2021-06-15', 'AccountId': '001Wt00000PGXrNIAX'}, {'Product2Id': '01tWt000006hTUkIAM', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL'}, {'Product2Id': '01tWt000006hV57IAE', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP'}, {'Product2Id': '01tWt000006hV58IAE', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP'}], 'var_call_sDFThv7zjVDU6D7hbgV2qHct': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
