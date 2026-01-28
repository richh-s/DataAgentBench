code = """import json
# var_call_GUjH3Am9iF45XtlrDMOQFOOL is provided by previous query_db call
records = var_call_GUjH3Am9iF45XtlrDMOQFOOL

# Find the record with the maximum sales_amount (convert to float)
max_rec = None
max_amount = -float('inf')
for r in records:
    try:
        amt = float(r.get('sales_amount', 0))
    except Exception:
        amt = 0.0
    if amt > max_amount:
        max_amount = amt
        max_rec = r

agent_id = None
if max_rec:
    agent_id = max_rec.get('OwnerId')
    if isinstance(agent_id, str):
        agent_id = agent_id.strip()
        if agent_id.startswith('#'):
            agent_id = agent_id.lstrip('#')

# Print result in required format as a JSON string
print("__RESULT__:")
print(json.dumps(agent_id))"""

env_args = {'var_call_GUjH3Am9iF45XtlrDMOQFOOL': [{'OwnerId': '005Wt000003NIXCIA4', 'sales_amount': '46919.149999999994'}, {'OwnerId': '#005Wt000003NGtcIAG', 'sales_amount': '20739.574999999997'}, {'OwnerId': '#005Wt000003NIx1IAG', 'sales_amount': '17125.666'}, {'OwnerId': '005Wt000003NIaRIAW', 'sales_amount': '14837.707999999999'}, {'OwnerId': '005Wt000003NEoYIAW', 'sales_amount': '14783.725999999999'}, {'OwnerId': '005Wt000003NDJ0IAO', 'sales_amount': '9427.789'}, {'OwnerId': '005Wt000003NIiUIAW', 'sales_amount': '8159.834'}, {'OwnerId': '005Wt000003NJ9uIAG', 'sales_amount': '7229.346'}, {'OwnerId': '005Wt000003NDEBIA4', 'sales_amount': '5399.91'}, {'OwnerId': '#005Wt000003NJmbIAG', 'sales_amount': '4769.91'}]}

exec(code, env_args)
