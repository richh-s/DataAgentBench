code = """import json, pandas as pd, os
path = var_call_RIpmvolDIhhq0giJRtKz4es9
with open(path, 'r') as f:
    data = json.load(f)
# Simple heuristic: search for articles mentioning "scalability" or "QuantumPCB Modeler" as potential policy/knowledge matches
df = pd.DataFrame(data)
mask = df['faq_answer__c'].str.contains('scalability', case=False, na=False) | df['faq_answer__c'].str.contains('QuantumPCB Modeler', case=False, na=False)
matched = df[mask]
result = None
if not matched.empty:
    # return first matching article id normalized (remove leading # if any)
    art_id = matched.iloc[0]['id']
    if isinstance(art_id, str):
        art_id = art_id.replace('#','')
    result = art_id
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ypU9WFO5FdNF5FMA90E3NAjL': [{'id': '#500Wt00000DDyznIAD'}], 'var_call_GYDdhTT0GxYelOkkTNohX2Tf': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'status': 'Waiting on Customer', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG'}], 'var_call_mhKIrcnLJqMwlyxSqARlncEb': [], 'var_call_rq1xoeVxG5cf35JOizAVbhch': [], 'var_call_PwYjpf1JA3w0vZlTCxJ38HzD': [], 'var_call_RIpmvolDIhhq0giJRtKz4es9': 'file_storage/call_RIpmvolDIhhq0giJRtKz4es9.json'}

exec(code, env_args)
