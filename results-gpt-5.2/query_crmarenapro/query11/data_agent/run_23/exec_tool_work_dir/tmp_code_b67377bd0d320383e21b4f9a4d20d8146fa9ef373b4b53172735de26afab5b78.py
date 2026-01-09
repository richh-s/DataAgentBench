code = """import json, pandas as pd

contact = pd.DataFrame(var_call_Df8nsWOllMc9CAxj15WkktvG)
orders = pd.DataFrame(var_call_GDFZ3PHdNSDjeuNoiFf4F8qw)
ai_products = pd.DataFrame(var_call_Ybn5MIavdS2EVJHcUghLS7er)

if contact.empty:
    result = None
else:
    acct = str(contact.loc[0,'AccountId']).replace('#','')
    orders['AccountId_clean'] = orders['AccountId'].astype(str).str.replace('#','', regex=False)
    rel_orders = orders[orders['AccountId_clean'] == acct].copy()

    ai_set = set(ai_products['Id'].astype(str))
    rel_ai = rel_orders[rel_orders['Product2Id'].astype(str).isin(ai_set)]

    product_id = None
    if not rel_ai.empty:
        # choose latest effective date; tie-breaker first row
        rel_ai['EffectiveDate_dt'] = pd.to_datetime(rel_ai['EffectiveDate'])
        rel_ai = rel_ai.sort_values(['EffectiveDate_dt','OrderId'], ascending=[False, True])
        product_id = rel_ai.iloc[0]['Product2Id']

    result = product_id

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_GDFZ3PHdNSDjeuNoiFf4F8qw': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Product2Id': '01tWt000006hV8LIAU'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Product2Id': '01tWt000006hV58IAE'}], 'var_call_Df8nsWOllMc9CAxj15WkktvG': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_Ybn5MIavdS2EVJHcUghLS7er': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_jozJNrNqQAqC9LrFISU69Dc0': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}]}

exec(code, env_args)
