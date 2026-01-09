code = """import json
opps = var_call_1Vhaacz0Hee6BAA1YR8TXNrR
olis = var_call_jjRBOnTADNswwgIQ2zTNpq5X
prods = var_call_LyebTPqJRDyOy6DqyG6r9mB7
ai_ids = {p['Id'].replace('#','') for p in prods if p.get('Name') and ('ai' in p['Name'].lower() or 'ai' in (p.get('Description') or '').lower())}
# find product2id from line items that is AI-related
ai_purchased = []
for r in olis:
    pid_clean = (r.get('Product2Id') or '').replace('#','')
    if pid_clean in ai_ids:
        ai_purchased.append(pid_clean)
# choose most recent opp by CloseDate then first matching product
# map oppid to close
close_map = {o['Id']: o['CloseDate'] for o in opps}
ai_purchased_sorted = sorted(ai_purchased, key=lambda pid: 0)
# pick first unique
pid = None
for x in ai_purchased:
    if x:
        pid = x
        break
print('__RESULT__:')
print(json.dumps(pid))"""

env_args = {'var_call_1Vhaacz0Hee6BAA1YR8TXNrR': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-01T10:15:30.000+0000'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15', 'CreatedDate': '2021-03-15T10:27:45.000+0000'}], 'var_call_jjRBOnTADNswwgIQ2zTNpq5X': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_LyebTPqJRDyOy6DqyG6r9mB7': [{'Id': '01tWt000006hUgwIAE', 'Name': 'AI DesignShift'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}, {'Id': '01tWt000006hVI1IAM', 'Name': 'AIOptics Vision'}, {'Id': '01tWt000006hVMrIAM', 'Name': 'TrainEDU Suite'}, {'Id': '01tWt000006hVQ5IAM', 'Name': 'CircuitSync Pro'}, {'Id': '#01tWt000006hVY9IAM', 'Name': 'EduFlow Academy'}, {'Id': '01tWt000006hVebIAE', 'Name': 'CircuitAI Innovator'}, {'Id': '01tWt000006hVjSIAU', 'Name': 'InnoTrain Hub'}, {'Id': '01tWt000006hVmfIAE', 'Name': 'EduTech Advance'}, {'Id': '01tWt000006hVt7IAE', 'Name': 'PCB EcoModel  '}]}

exec(code, env_args)
