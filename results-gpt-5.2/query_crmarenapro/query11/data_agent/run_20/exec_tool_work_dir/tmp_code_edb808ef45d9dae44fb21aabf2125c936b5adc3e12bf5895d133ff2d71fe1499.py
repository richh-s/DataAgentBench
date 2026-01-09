code = """import json, pandas as pd

df = pd.DataFrame(var_call_Djn1jTvjhIEt203aSXNjSkBN)
# normalize Product2Id by stripping leading '#'
df['Product2Id_norm'] = df['Product2Id'].astype(str).str.replace('#','', regex=False)
# get product names
prod_df = pd.DataFrame(var_call_xoTnXQOyPJbRzKNsJKpZhrRL)
prod_df['Id_norm'] = prod_df['Id'].astype(str).str.replace('#','', regex=False)
merged = df.merge(prod_df, left_on='Product2Id_norm', right_on='Id_norm', how='left')
# choose product most likely 'AI processing unit' -> heuristic: name contains 'cirku' maybe hardware; pick AI Cirku-Tech
candidates = merged[merged['Name'].fillna('').str.contains('Cirku', case=False, na=False)]
if len(candidates)==0:
    # fallback: any product name with 'AI' and maybe hardware-like
    candidates = merged
# pick first unique product id
prod_id = candidates['Product2Id_norm'].dropna().unique().tolist()
answer = prod_id[0] if prod_id else None
print('__RESULT__:')
print(json.dumps({'product_id': answer}))"""

env_args = {'var_call_Djn1jTvjhIEt203aSXNjSkBN': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_4sXcvzM2e7zy9eQvb3qAVGX4': [], 'var_call_xoTnXQOyPJbRzKNsJKpZhrRL': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}]}

exec(code, env_args)
