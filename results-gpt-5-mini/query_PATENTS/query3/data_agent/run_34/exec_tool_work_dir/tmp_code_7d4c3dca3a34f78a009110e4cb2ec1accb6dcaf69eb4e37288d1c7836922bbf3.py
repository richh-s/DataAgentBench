code = """import json, re
path = var_call_iFNFnXpgt1jRdEhcOq4ig4jD
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pubnum_re = re.compile(r'[A-Z]{2,}-[0-9]{4,}[0-9A-Z\-]*')

def extract_pubnum(s):
    if not s:
        return None
    matches = pubnum_re.findall(s)
    if not matches:
        return None
    matches = sorted(matches, key=len, reverse=True)
    return matches[0]

result = {}
for row in data:
    info = row.get('Patents_info','')
    pubnum = extract_pubnum(info)
    if pubnum:
        # parse cpc first codes
        cpc_field = row.get('cpc') or '[]'
        try:
            cpcs = json.loads(cpc_field)
        except Exception:
            cpcs = []
        primary_codes = [e.get('code') for e in cpcs if isinstance(e, dict) and e.get('first') and e.get('code')]
        result[pubnum] = {
            'rowid': row.get('rowid'),
            'assignee_info': info,
            'primary_codes': sorted(list(set(primary_codes)))
        }

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QrKpS3xCrEvOFTzyHkiOaGa7': ['publicationinfo'], 'var_call_04o2xQiS5aWuOHXcmBa2upJ6': ['cpc_definition'], 'var_call_iFNFnXpgt1jRdEhcOq4ig4jD': 'file_storage/call_iFNFnXpgt1jRdEhcOq4ig4jD.json', 'var_call_F0o6KLAYCTaTzUnkOyFIfKph': 'file_storage/call_F0o6KLAYCTaTzUnkOyFIfKph.json', 'var_call_euL4YTFiEWaffgYDXkUUpE6y': {'citing_map': {}, 'unique_codes': []}}

exec(code, env_args)
