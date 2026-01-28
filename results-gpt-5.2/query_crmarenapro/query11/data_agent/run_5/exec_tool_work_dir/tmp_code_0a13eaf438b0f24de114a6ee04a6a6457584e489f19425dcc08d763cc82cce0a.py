code = """import json
ops = var_call_S7uvfm4kteOTHf84y4eAbyA0
olis = var_call_RV8QKqh44lzWIK1CZK39O8Az
prods = var_call_PkbzSetN3sKYOXQIquYXbjCC
prod_name_by_id = {p['Id'].replace('#',''): (p.get('Name') or '').strip() for p in prods}
# find product whose name indicates AI processing unit
candidates = []
for r in olis:
    pid = (r['Product2Id'] or '').replace('#','')
    name = prod_name_by_id.get(pid,'')
    if 'AI' in name.upper():
        candidates.append(pid)
# deterministic: sort unique
pid = sorted(set(candidates))[0] if candidates else None
print('__RESULT__:')
print(json.dumps(pid))"""

env_args = {'var_call_S7uvfm4kteOTHf84y4eAbyA0': [{'Id': '006Wt000007B0g2IAC', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}, {'Id': '006Wt000007B7TcIAK', 'AccountId': '001Wt00000PGXrNIAX', 'ContactId': '003Wt00000Jqy8SIAR', 'CloseDate': '2021-06-15'}], 'var_call_RV8QKqh44lzWIK1CZK39O8Az': [{'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '#01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hTUkIAM'}, {'OpportunityId': '006Wt000007B7TcIAK', 'Product2Id': '01tWt000006hV8LIAU'}, {'OpportunityId': '006Wt000007B0g2IAC', 'Product2Id': '01tWt000006hV9xIAE'}], 'var_call_PkbzSetN3sKYOXQIquYXbjCC': [{'Id': '01tWt000006hTUkIAM', 'Name': 'CloudLink Designer'}, {'Id': '01tWt000006hV8LIAU', 'Name': 'AI Cirku-Tech'}, {'Id': '#01tWt000006hV9xIAE', 'Name': 'OptiPower Manager'}]}

exec(code, env_args)
