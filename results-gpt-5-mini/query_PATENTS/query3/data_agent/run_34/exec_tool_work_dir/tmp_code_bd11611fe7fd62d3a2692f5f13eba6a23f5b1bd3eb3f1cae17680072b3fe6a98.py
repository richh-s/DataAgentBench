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
    return sorted(matches, key=len, reverse=True)[0]

def extract_assignee(s):
    if not s:
        return None
    m = re.search(r'owned by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'is owned by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'held by\s+([^,\.]+)', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    m = re.search(r'([^,\.]+?)\s+holds the', s, re.IGNORECASE)
    if m:
        return m.group(1).strip()
    if ',' in s:
        return s.split(',')[0].strip()
    return s.strip()


result = []
for row in data:
    info = row.get('Patents_info','')
    assignee = extract_assignee(info) or ''
    if 'CALIFORNIA' in assignee.upper() and ('UNIV' in assignee.upper() or 'UNIVERSITY' in assignee.upper() or 'REGENTS' in assignee.upper()):
        pubnum = extract_pubnum(info)
        if pubnum:
            result.append(pubnum)

result = sorted(list(set(result)))
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_QrKpS3xCrEvOFTzyHkiOaGa7': ['publicationinfo'], 'var_call_04o2xQiS5aWuOHXcmBa2upJ6': ['cpc_definition'], 'var_call_iFNFnXpgt1jRdEhcOq4ig4jD': 'file_storage/call_iFNFnXpgt1jRdEhcOq4ig4jD.json', 'var_call_F0o6KLAYCTaTzUnkOyFIfKph': 'file_storage/call_F0o6KLAYCTaTzUnkOyFIfKph.json', 'var_call_euL4YTFiEWaffgYDXkUUpE6y': {'citing_map': {}, 'unique_codes': []}, 'var_call_TN169ZanZUXhtwpDfJvr6vx6': 'file_storage/call_TN169ZanZUXhtwpDfJvr6vx6.json'}

exec(code, env_args)
