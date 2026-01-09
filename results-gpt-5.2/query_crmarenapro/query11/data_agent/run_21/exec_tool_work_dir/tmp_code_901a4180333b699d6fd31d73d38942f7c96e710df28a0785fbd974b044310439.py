code = """import json, pandas as pd
opp = pd.DataFrame(var_call_dcDs5ECccLhG2eLENCOEEeYI)
prod = pd.DataFrame(var_call_gQQtXvBL6wroEQEAeVI90Tp8)
opp['Product2Id_clean'] = opp['Product2Id'].str.replace('#','', regex=False)
prod['Id_clean'] = prod['Id'].str.replace('#','', regex=False)
merged = opp.merge(prod, left_on='Product2Id_clean', right_on='Id_clean', how='left')
# find AI processing unit by name/description heuristic: contains 'AI'
ai = merged[merged['Name'].str.contains('AI', case=False, na=False)]
# choose most relevant: latest CloseDate then any
ai_sorted = ai.sort_values(by=['CloseDate','OpportunityId']).reset_index(drop=True)
product_id = None
if len(ai_sorted):
    product_id = ai_sorted.loc[len(ai_sorted)-1, 'Id_clean']
print('__RESULT__:')
print(json.dumps({'product_id': product_id}))"""

env_args = {'var_call_dcDs5ECccLhG2eLENCOEEeYI': [{'Product2Id': '#01tWt000006hV8LIAU', 'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Product2Id': '01tWt000006hTUkIAM', 'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}, {'Product2Id': '01tWt000006hV8LIAU', 'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}, {'Product2Id': '01tWt000006hV9xIAE', 'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}], 'var_call_gQQtXvBL6wroEQEAeVI90Tp8': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
