code = """import json, pandas as pd
opp = pd.DataFrame(var_call_nY4Est3sPUIep3xWPD4kPYuQ)
oli = pd.DataFrame(var_call_y75yvLG2NhyvqaXEVHaWU83P)
prod = pd.DataFrame(var_call_j8cQpDdSWS0RjSCqC7dMq93d)

if oli.empty:
    ans = None
else:
    oli['OpportunityId_clean'] = oli['OpportunityId'].astype(str).str.replace('#','', regex=False)
    oli['Product2Id_clean'] = oli['Product2Id'].astype(str).str.replace('#','', regex=False)
    opp_ids = set(opp['OpportunityId'].astype(str).str.replace('#','', regex=False))
    oli = oli[oli['OpportunityId_clean'].isin(opp_ids)]

    prod['Id_clean'] = prod['Id'].astype(str).str.replace('#','', regex=False)
    ai_prod_ids = set(prod['Id_clean'])
    match = oli[oli['Product2Id_clean'].isin(ai_prod_ids)]

    ans = match['Product2Id_clean'].iloc[0] if not match.empty else None

print('__RESULT__:')
print(json.dumps({'product_id': ans}))"""

env_args = {'var_call_nY4Est3sPUIep3xWPD4kPYuQ': [{'OpportunityId': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'OpportunityId': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_y75yvLG2NhyvqaXEVHaWU83P': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '#006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV58IAE'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}, {'OpportunityId': '#006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hVczIAE'}], 'var_call_j8cQpDdSWS0RjSCqC7dMq93d': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}]}

exec(code, env_args)
