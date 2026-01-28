code = """import json, pandas as pd
ops = pd.DataFrame(var_call_evZp6nD6OURx6TcVhTBvxTCv)
olis = pd.DataFrame(var_call_UHBFQnjo9XIXcbsMmvBLmDGD)
prods = pd.DataFrame(var_call_LAScfneAd07ydvwRdeBtqZBs)
if ops.empty or olis.empty or prods.empty:
    out = None
else:
    olis['Product2Id_clean'] = olis['Product2Id'].str.replace('#','', regex=False)
    prods['Id_clean'] = prods['Id'].str.replace('#','', regex=False)
    m = olis.merge(prods, left_on='Product2Id_clean', right_on='Id_clean', how='left')
    # pick AI processing unit: heuristic Name contains 'AI'
    ai = m[m['Name'].fillna('').str.contains('AI', case=False, na=False)]
    if ai.empty:
        out = None
    else:
        # if multiple, pick first by OpportunityId
        out = ai.iloc[0]['Product2Id_clean']
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_evZp6nD6OURx6TcVhTBvxTCv': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_UHBFQnjo9XIXcbsMmvBLmDGD': [{'Id': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_LAScfneAd07ydvwRdeBtqZBs': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
