code = """import json, pandas as pd
olis = pd.DataFrame(var_call_7I1ZRxRGMrjeCI5OuUSISJ2r)
prods = pd.DataFrame(var_call_9CvYKfL5HBfbOLlJwrhfNL9a)
# normalize ids
olis['Product2Id_norm'] = olis['Product2Id'].str.replace('#','', regex=False)
prods['Id_norm'] = prods['Id'].str.replace('#','', regex=False)
df = olis.merge(prods, left_on='Product2Id_norm', right_on='Id_norm', how='left')
# pick AI processing unit: heuristic product name contains 'AI' and not null
ai_df = df[df['Name'].fillna('').str.contains('AI', case=False, regex=False)]
# choose most recent (all same date), then first
product_id = None
if not ai_df.empty:
    product_id = ai_df.iloc[0]['Product2Id_norm']
res = json.dumps(product_id)
print('__RESULT__:')
print(res)"""

env_args = {'var_call_JcvjWrza9PKEB5TFGDeJKBCf': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_l2x9PLlycgjT33qjyvsIOrtU': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Status': 'Activated  ', 'Product2Id': '01tWt000006hV8LIAU', 'ProductName': 'AI Cirku-Tech'}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Status': 'Activated', 'Product2Id': '01tWt000006hTUkIAM', 'ProductName': 'CloudLink Designer'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Status': 'Activated', 'Product2Id': '01tWt000006hV57IAE', 'ProductName': 'PulseSim Pro'}], 'var_call_meHpFrjoTNoMclSK2POh4GSr': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_II7xdcsFMLoMagA1wZBQPyJ5': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}], 'var_call_7I1ZRxRGMrjeCI5OuUSISJ2r': [{'OpportunityLineItemId': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'OpportunityLineItemId': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'OpportunityLineItemId': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'OpportunityLineItemId': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_9CvYKfL5HBfbOLlJwrhfNL9a': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
