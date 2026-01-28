code = """import json
from pathlib import Path
p = Path(var_call_Q0Of0hSORM45Qge1URVUzXhz)
records = json.loads(p.read_text())

target = '500Wt00000DDyznIAD'

def normalize(s):
    if s is None:
        return ''
    s = str(s).strip()
    if s.startswith('#'):
        s = s[1:]
    return s.lower()

matches = [r for r in records if normalize(r.get('id')) == normalize(target)]

# If not found, try matching case-insensitive anywhere in id
if not matches:
    matches = [r for r in records if normalize(target) in normalize(r.get('id'))]

output = {'matches_count': len(matches), 'matches': matches}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_DTi0EyEkxoeZsnKdSMahJq7J': ['Case', 'knowledge__kav', 'issue__c', 'casehistory__c', 'emailmessage', 'livechattranscript'], 'var_call_5ZbGqvuyMcAJQe8Cwppaoj6y': [], 'var_call_Q0Of0hSORM45Qge1URVUzXhz': 'file_storage/call_Q0Of0hSORM45Qge1URVUzXhz.json'}

exec(code, env_args)
