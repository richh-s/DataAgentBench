code = """import json, pandas as pd

contact = pd.DataFrame(var_call_Fr9U06Pva7f3PF2eVvOHoJiW)
orders = pd.DataFrame(var_call_MU31q9S1qV1Zfd3rCiZmsoz4)
opps = pd.DataFrame(var_call_0EpxfFSHld88DvtnTDRt040w)
prods = pd.DataFrame(var_call_2fh0uFSFdr7fwg6wA5yCTgqW)

acct = contact.loc[0,'AccountId'].replace('#','') if len(contact) else None

def norm(s):
    return None if s is None else str(s).replace('#','')

# Determine purchased last month (2021-06) for this contact via orders on account and opp line items on contact.
# First try orders: match account
orders['AccountId_norm'] = orders['AccountId'].map(norm)
orders['Product2Id_norm'] = orders['Product2Id'].map(norm)
orders_for_acct = orders[orders['AccountId_norm'] == acct]

# Identify AI processing unit: interpret as product name containing 'AI' and likely hardware; we'll filter products with 'AI'
prods['Product2Id_norm'] = prods['Id'].map(norm)
ai_prod_ids = set(prods['Product2Id_norm'].tolist())

cand = orders_for_acct[orders_for_acct['Product2Id_norm'].isin(ai_prod_ids)]

selected = None
if len(cand):
    selected = cand.iloc[0]['Product2Id_norm']
else:
    # fallback to opportunities for this contact
    opps['Product2Id_norm'] = opps['Product2Id'].map(norm)
    cand2 = opps[opps['Product2Id_norm'].isin(ai_prod_ids)]
    if len(cand2):
        selected = cand2.iloc[0]['Product2Id_norm']

print('__RESULT__:')
print(json.dumps(selected))"""

env_args = {'var_call_MU31q9S1qV1Zfd3rCiZmsoz4': [{'OrderId': '801Wt00000PHRYWIA5', 'EffectiveDate': '2021-06-15', 'AccountId': '001Wt00000PGXrNIAX', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '#001Wt00000PGoAaIAL', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'EffectiveDate': '2021-06-01', 'AccountId': '001Wt00000PGZZoIAP', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_Fr9U06Pva7f3PF2eVvOHoJiW': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_0EpxfFSHld88DvtnTDRt040w': [{'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'CloseDate': '2021-06-15', 'StageName': 'Discovery', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_2fh0uFSFdr7fwg6wA5yCTgqW': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}]}

exec(code, env_args)
