code = """import json, pandas as pd
opp_lines = pd.DataFrame(var_call_ssRNlVp24T5Ojp5RGSAzQDrl)
prods = pd.DataFrame(var_call_UrRodiVuJEMBsSYaCqfAr8Mj)
if not opp_lines.empty:
    opp_lines['Product2Id_clean'] = opp_lines['Product2Id'].astype(str).str.replace('#','', regex=False)
else:
    opp_lines['Product2Id_clean'] = []
if not prods.empty:
    prods['Id_clean'] = prods['Id'].astype(str).str.replace('#','', regex=False)
else:
    prods['Id_clean'] = []
merged = opp_lines.merge(prods, left_on='Product2Id_clean', right_on='Id_clean', how='left')
# find AI processing unit by name containing 'AI'
ai = merged[merged['Name'].fillna('').str.contains('AI', case=False, na=False)]
product_id = None
if not ai.empty:
    product_id = ai.iloc[0]['Product2Id_clean']
result = json.dumps(product_id)
print('__RESULT__:')
print(result)"""

env_args = {'var_call_Oe2ZJDoYZTEZE5AJXmqmCNDY': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}], 'var_call_ssRNlVp24T5Ojp5RGSAzQDrl': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_UrRodiVuJEMBsSYaCqfAr8Mj': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
