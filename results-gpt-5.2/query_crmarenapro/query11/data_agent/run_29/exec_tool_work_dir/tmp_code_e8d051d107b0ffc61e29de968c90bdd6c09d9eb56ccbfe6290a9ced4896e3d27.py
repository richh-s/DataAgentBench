code = """import json, pandas as pd
ops = pd.DataFrame(var_call_rmLlMJfDmnMeC0mnze0hQ7n9)
prods = pd.DataFrame(var_call_WCaBlDuAO1ngzRb6cHqcZSHq)
ops['Product2Id_clean'] = ops['Product2Id'].str.replace('#','', regex=False)
prods['Id_clean'] = prods['Id'].str.replace('#','', regex=False)
df = ops.merge(prods, left_on='Product2Id_clean', right_on='Id_clean', how='left')
# pick AI processing unit: name contains 'ai'
df['name_l'] = df['Name'].fillna('').str.lower().str.strip()
ai_df = df[df['name_l'].str.contains('ai')]
# if multiple, pick first by latest CloseDate then stable
ai_df = ai_df.sort_values(['CloseDate','Product2Id_clean'], ascending=[False, True])
product_id = None
if len(ai_df) > 0:
    product_id = ai_df.iloc[0]['Product2Id_clean']
result = product_id
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_danZ1v5o0Zp1T2Khlbc5PDwq': [], 'var_call_rmLlMJfDmnMeC0mnze0hQ7n9': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV58IAE'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hVczIAE'}], 'var_call_WCaBlDuAO1ngzRb6cHqcZSHq': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '#01tWt000006hV58IAE', 'Name': 'SecureFlow Suite'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVczIAE', 'Name': 'CollabDesign Studio'}]}

exec(code, env_args)
