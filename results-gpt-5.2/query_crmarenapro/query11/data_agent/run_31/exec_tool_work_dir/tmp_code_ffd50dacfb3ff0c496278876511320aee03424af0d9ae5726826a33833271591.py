code = """import json, pandas as pd
opps = pd.DataFrame(var_call_BMYScjMpFvjv18N5brSCXqQH)
olis = pd.DataFrame(var_call_QhwooPCn7jHLAErXAha1IhKd)
prods = pd.DataFrame(var_call_FeLGLKBF8LDeHmOZhC3gTyee)
if opps.empty or olis.empty or prods.empty:
    ans = None
else:
    olis['Product2Id_clean'] = olis['Product2Id'].str.replace('#','', regex=False)
    prods['Id_clean'] = prods['Id'].str.replace('#','', regex=False)
    m = olis.merge(prods, left_on='Product2Id_clean', right_on='Id_clean', how='left')
    # AI processing unit heuristic: product name contains 'AI'
    ai = m[m['Name'].fillna('').str.contains('AI', case=False, regex=False)]
    ans = ai['Product2Id_clean'].iloc[0] if not ai.empty else None
print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_BMYScjMpFvjv18N5brSCXqQH': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_QhwooPCn7jHLAErXAha1IhKd': [{'OpportunityLineItemId': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityLineItemId': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityLineItemId': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityLineItemId': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_FeLGLKBF8LDeHmOZhC3gTyee': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
