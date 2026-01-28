code = """import json
from pathlib import Path
# var_call_ZGHZ6QXs13qGEiBL0mHSZTTR is a file path
p = Path(var_call_ZGHZ6QXs13qGEiBL0mHSZTTR)
casehistory = json.loads(p.read_text())
case_id = '#500Wt00000DDyznIAD'

def normalize(s):
    if s is None:
        return ''
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s.lower()

matches = [r for r in casehistory if normalize(r.get('caseid__c')) == normalize(case_id) or normalize(case_id) in normalize(r.get('caseid__c'))]

print('__RESULT__:')
print(json.dumps({'matches_count': len(matches), 'matches': matches}))"""

env_args = {'var_call_DTi0EyEkxoeZsnKdSMahJq7J': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5ZbGqvuyMcAJQe8Cwppaoj6y': [], 'var_call_Q0Of0hSORM45Qge1URVUzXhz': 'file_storage/call_Q0Of0hSORM45Qge1URVUzXhz.json', 'var_call_RLG5JpONgqWvewZv90bJ48cx': {'matches_count': 1, 'matches': [{'id': '#500Wt00000DDyznIAD', 'subject': 'Scalability Problems ', 'description': 'I am experiencing difficulties in scaling the QuantumPCB Modeler to meet our growing needs at GreenStar Electronics.', 'contactid': '003Wt00000JqoiZIAR', 'accountid': '001Wt00000PGaZCIA1', 'ownerid': '005Wt000003NHsrIAG', 'status': 'Waiting on Customer'}]}, 'var_call_F2GbJOO3zAE0wQz2meym3NLf': 'file_storage/call_F2GbJOO3zAE0wQz2meym3NLf.json', 'var_call_cHY1zEzgcBQKbjeqnTmNWIlo': {'status': 'ready', 'case_id': '#500Wt00000DDyznIAD'}, 'var_call_ZGHZ6QXs13qGEiBL0mHSZTTR': 'file_storage/call_ZGHZ6QXs13qGEiBL0mHSZTTR.json'}

exec(code, env_args)
