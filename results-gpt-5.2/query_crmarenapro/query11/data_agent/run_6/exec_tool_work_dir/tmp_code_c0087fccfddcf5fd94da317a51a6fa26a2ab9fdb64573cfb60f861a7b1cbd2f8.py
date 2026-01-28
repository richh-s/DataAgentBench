code = """import json, pandas as pd
opp = pd.DataFrame(var_call_0K4e8Qe0N68zVMfW8duwmCQQ)
oli = pd.DataFrame(var_call_ZGvblgnLtlXQ1eHB757aSpQC)
orders = pd.DataFrame(var_call_jYT0EYcTaXNJLk65YUohLgwO)
oi = pd.DataFrame(var_call_KQ8a1XibVm57ctkl7ZzZiUEA)
prod = pd.DataFrame(var_call_xmuA2a1WI7V0T70seaGKilc7)

# normalize ids
for df, col in [(oli,'Product2Id'),(oi,'Product2Id')]:
    df[col+'_norm'] = df[col].astype(str).str.replace('#','', regex=False)
prod['Id_norm'] = prod['Id'].astype(str).str.replace('#','', regex=False)

# last month order for this account
order_id = orders.sort_values('EffectiveDate', ascending=False).iloc[0]['OrderId'] if len(orders) else None

chosen = None
if order_id is not None and len(oi):
    cand = oi[oi['OrderId']==order_id]
    # if any product name indicates AI processing unit
    cand = cand.merge(prod, left_on='Product2Id_norm', right_on='Id_norm', how='left')
    mask = cand['Name'].fillna('').str.lower().str.contains('ai') & (cand['Name'].fillna('').str.lower().str.contains('unit') | cand['Name'].fillna('').str.lower().str.contains('processing') | cand['Name'].fillna('').str.lower().str.contains('apu'))
    if mask.any():
        chosen = cand[mask].iloc[0]['Product2Id_norm']

# fallback: use opportunity line items in last month and pick product with 'AI' in known names
if chosen is None and len(oli):
    oli2 = oli.merge(prod, left_on='Product2Id_norm', right_on='Id_norm', how='left')
    mask = oli2['Name'].fillna('').str.lower().str.contains('ai')
    if mask.any():
        chosen = oli2[mask].iloc[0]['Product2Id_norm']

print('__RESULT__:')
print(json.dumps(chosen))"""

env_args = {'var_call_vxEensfhZSzfp6UdwYHMoQNu': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Status': 'Activated  '}, {'OrderId': '801Wt00000PHVkCIAX', 'AccountId': '#001Wt00000PGoAaIAL', 'EffectiveDate': '2021-06-01', 'Status': 'Activated'}, {'OrderId': '801Wt00000PHWjTIAX', 'AccountId': '001Wt00000PGZZoIAP', 'EffectiveDate': '2021-06-01', 'Status': 'Activated'}], 'var_call_vsvbVzLoTsOsl0wIqYMopwMX': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVOTIA2', 'Name': 'UnitySim Essentials   '}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}], 'var_call_0K4e8Qe0N68zVMfW8duwmCQQ': [{'OpportunityId': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Discovery'}, {'OpportunityId': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'StageName': 'Negotiation'}], 'var_call_ZGvblgnLtlXQ1eHB757aSpQC': [{'OpportunityLineItemId': '#00kWt000002HKCZIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityLineItemId': '00kWt000002HMXmIAO', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityLineItemId': '00kWt000002HSmqIAG', 'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityLineItemId': '00kWt000002HTEHIA4', 'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_D734RxcKnNhMXYuirBpJR6a9': [], 'var_call_ZG0HIBhvaeGpzJ47yylqpgne': [], 'var_call_y5NQ1LwcC5tqGW0lTtvTUuZR': [{'Id': '003Wt00000Jqy8SIAR', 'AccountId': '#001Wt00000PGXrNIAX'}], 'var_call_KQ8a1XibVm57ctkl7ZzZiUEA': [{'OrderItemId': '802Wt00000795XxIAI', 'OrderId': '801Wt00000PHVkCIAX', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderItemId': '802Wt00000796euIAA', 'OrderId': '801Wt00000PHWjTIAX', 'Product2Id': '01tWt000006hV58IAE'}, {'OrderItemId': '#802Wt00000797O2IAI', 'OrderId': '801Wt00000PHVkCIAX', 'Product2Id': '01tWt000006hTUkIAM'}, {'OrderItemId': '#802Wt0000079AQlIAM', 'OrderId': '801Wt00000PHWjTIAX', 'Product2Id': '01tWt000006hV57IAE'}, {'OrderItemId': '802Wt0000079AU1IAM', 'OrderId': '801Wt00000PHRYWIA5', 'Product2Id': '01tWt000006hV8LIAU'}], 'var_call_jYT0EYcTaXNJLk65YUohLgwO': [{'OrderId': '801Wt00000PHRYWIA5', 'AccountId': '001Wt00000PGXrNIAX', 'EffectiveDate': '2021-06-15', 'Status': 'Activated  '}], 'var_call_xmuA2a1WI7V0T70seaGKilc7': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}], 'var_call_JrPoaU56wvk5t9RrXcKgGF9f': []}

exec(code, env_args)
