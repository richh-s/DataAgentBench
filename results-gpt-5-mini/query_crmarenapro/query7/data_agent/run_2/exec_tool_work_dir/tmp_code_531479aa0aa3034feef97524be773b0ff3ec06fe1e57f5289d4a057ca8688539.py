code = """import json
from pathlib import Path
p = Path(var_call_F2GbJOO3zAE0wQz2meym3NLf)
records = json.loads(p.read_text())

# We need to find which knowledge article was breached by the agent. We must determine if agent breached policy.
# Since the prompt: "Did the agent breach the policy, and if so, which knowledge article was breached? Return only the Id of the knowledge article or None"
# We need to inspect case history, emails, or livechat transcripts for case id and see if any knowledge article was referenced or breached.

# Load case we found earlier
case = None
p_case = Path(var_call_RLG5JpONgqWvewZv90bJ48cx)
case_info = json.loads(p_case.read_text())
if case_info['matches_count'] == 1:
    case = case_info['matches'][0]

# Query casehistory and emailmessage and livechattranscript for records related to this case id
from functions import query_db

# But we cannot call functions.query_db from here. Instead, we will output next steps: We'll run queries via query_db tool. 

print('__RESULT__:')
print(json.dumps({'status': 'ready', 'case_id': case['id']}))"""

env_args = {'var_call_DTi0EyEkxoeZsnKdSMahJq7J': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5ZbGqvuyMcAJQe8Cwppaoj6y': [], 'var_call_Q0Of0hSORM45Qge1URVUzXhz': 'file_storage/call_Q0Of0hSORM45Qge1URVUzXhz.json', 'var_call_RLG5JpONgqWvewZv90bJ48cx': {'matches_count': 1, 'matches': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG', 'status': 'Waiting on Customer'}]}, 'var_call_F2GbJOO3zAE0wQz2meym3NLf': 'file_storage/call_F2GbJOO3zAE0wQz2meym3NLf.json'}

exec(code, env_args)
