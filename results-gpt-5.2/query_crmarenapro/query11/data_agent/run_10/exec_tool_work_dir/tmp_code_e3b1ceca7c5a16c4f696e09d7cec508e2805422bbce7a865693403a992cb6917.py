code = """import json, pandas as pd

opps = pd.DataFrame(var_call_1paPbWPsunNRX9DZWFvNtdAF)
olis = pd.DataFrame(var_call_G050YcjIQjk5DWNMTIXjeVQs)
orders = pd.DataFrame(var_call_yEtcv40UOyvu0SIRwpiqDyzc)
ai_products = pd.DataFrame(var_call_scABdDGonvDdfFhwLhs9Wbj3)

def norm(s):
    if pd.isna(s):
        return s
    return str(s).replace('#','').strip()

if not opps.empty:
    opps['AccountId_n'] = opps['AccountId'].map(norm)
if not orders.empty:
    orders['AccountId_n'] = orders['AccountId'].map(norm)
    orders['Product2Id_n'] = orders['Product2Id'].map(norm)
if not olis.empty:
    olis['Product2Id_n'] = olis['Product2Id'].map(norm)

ai_set = set(ai_products['Id'].map(norm).tolist())

# Prefer order items for the contact's account in the period, filtered to AI products
acct_ids = set(opps['AccountId_n'].dropna().unique().tolist())
ord_match = orders[orders['AccountId_n'].isin(acct_ids) & orders['Product2Id_n'].isin(ai_set)]

product_id = None
if not ord_match.empty:
    # pick most recent effective date then first
    ord_match = ord_match.sort_values(['EffectiveDate','OrderId'], ascending=[False, True])
    product_id = ord_match.iloc[0]['Product2Id_n']
else:
    oli_match = olis[olis['Product2Id_n'].isin(ai_set)]
    if not oli_match.empty:
        product_id = oli_match.iloc[0]['Product2Id_n']

print('__RESULT__:')
print(json.dumps(product_id))"""

env_args = {'var_call_yEtcv40UOyvu0SIRwpiqDyzc': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_scABdDGonvDdfFhwLhs9Wbj3': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_1paPbWPsunNRX9DZWFvNtdAF': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_G050YcjIQjk5DWNMTIXjeVQs': [{'Id': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'Id': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'Id': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'Id': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_coGvu1ev7aNA5522CXkdgHbk': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX'}, {'Id': '006Wt000007BBx1IAG', 'AccountId': '001Wt00000PGXrNIAX'}, {'Id': '#006Wt000007BIjxIAG', 'AccountId': '001Wt00000PGXrNIAX'}, {'Id': '006Wt000007BInBIAW', 'AccountId': '#001Wt00000PGXrNIAX'}]}

exec(code, env_args)
