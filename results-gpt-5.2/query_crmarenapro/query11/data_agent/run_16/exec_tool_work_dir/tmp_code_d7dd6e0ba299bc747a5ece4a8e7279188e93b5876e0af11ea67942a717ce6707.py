code = """import json, pandas as pd

df = pd.DataFrame(var_call_mBqwoZlGbv5gsByyBjhc0aM3)
prod = pd.DataFrame(var_call_HwOBmhAilhjJNidoUYSOtyKw)

df['Product2Id_clean']=df['Product2Id'].str.replace('#','', regex=False)
prod['Id_clean']=prod['Id'].str.replace('#','', regex=False)

m = df.merge(prod, left_on='Product2Id_clean', right_on='Id_clean', how='left')
# pick AI processing unit: name contains 'ai'
ai = m[m['Name'].fillna('').str.lower().str.contains('ai')].copy()
# if multiple, pick first by CloseDate desc then OpportunityId
if not ai.empty:
    ai['CloseDate_dt']=pd.to_datetime(ai['CloseDate'])
    ai=ai.sort_values(['CloseDate_dt','OpportunityId'], ascending=[False, False])
    product_id = ai.iloc[0]['Product2Id_clean']
else:
    product_id = None

print('__RESULT__:')
print(json.dumps({'product_id': product_id}))"""

env_args = {'var_call_1VNy4zG2jpNMbpRHEOcYTRqH': [], 'var_call_LoCQDAR8390iZCH1io2ghbGz': [], 'var_call_mBqwoZlGbv5gsByyBjhc0aM3': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV58IAE'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hVczIAE'}], 'var_call_HwOBmhAilhjJNidoUYSOtyKw': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
