code = """import json
from pathlib import Path
# Read the stored case match variable
varname = 'var_call_RLG5JpONgqWvewZv90bJ48cx'
# The storage provides the JSON text as the variable content. But we can access it via the environment: var_call_RLG5JpONgqWvewZv90bJ48cx
# In this execution context, storage variables are available directly. Let's load it.
case_info = var_call_RLG5JpONgqWvewZv90bJ48cx

case = None
if case_info.get('matches_count',0) >= 1:
    case = case_info['matches'][0]

print('__RESULT__:')
print(json.dumps({'status': 'ready', 'case_id': case['id']}))"""

env_args = {'var_call_DTi0EyEkxoeZsnKdSMahJq7J': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5ZbGqvuyMcAJQe8Cwppaoj6y': [], 'var_call_Q0Of0hSORM45Qge1URVUzXhz': 'file_storage/call_Q0Of0hSORM45Qge1URVUzXhz.json', 'var_call_RLG5JpONgqWvewZv90bJ48cx': {'matches_count': 1, 'matches': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG', 'status': 'Waiting on Customer'}]}, 'var_call_F2GbJOO3zAE0wQz2meym3NLf': 'file_storage/call_F2GbJOO3zAE0wQz2meym3NLf.json'}

exec(code, env_args)
