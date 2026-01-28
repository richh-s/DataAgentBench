code = """import json, re
path = var_call_4ypPDsIDPskWsUQVGCQMWqIg
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

pubnum_pattern1 = re.compile(r'publication number\s*([A-Z0-9\-\.]+)', re.IGNORECASE)
pubnum_pattern2 = re.compile(r'\b([A-Z]{2,}-\d{4,}[A-Z0-9\-]*)\b')
assignee_pattern = re.compile(r'^(.*?)\s+(holds|owns|is the owner|assigned to|owned by)\b', re.IGNORECASE)
paren_pattern = re.compile(r'^(.*?)\s*\(')

def extract_pubnum(text):
    if not text:
        return None
    m = pubnum_pattern1.search(text)
    if m:
        return m.group(1)
    m2 = pubnum_pattern2.findall(text)
    if m2:
        return m2[0]
    return None

def extract_assignee(text):
    if not text:
        return None
    m = assignee_pattern.search(text)
    if m:
        return m.group(1).strip().upper()
    m2 = paren_pattern.search(text)
    if m2:
        return m2.group(1).strip().upper()
    return text.strip().split(',')[0].strip().upper()

univ_pubnums = set()
for rec in data:
    patents_info = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(patents_info)
    assignee = extract_assignee(patents_info)
    if assignee and 'UNIV' in assignee and 'CALIFORNIA' in assignee and pubnum:
        univ_pubnums.add(pubnum)

import json
print('__RESULT__:')
print(json.dumps({'univ_pubnums': sorted(list(univ_pubnums))}))"""

env_args = {'var_call_6eJOWXhg53i3nVbORiFLjbP6': ['publicationinfo'], 'var_call_1tuNt2y7YfWQjNjAnZxicsBc': ['cpc_definition'], 'var_call_7KvRqM8zN3008tYq0vYkzBDS': 'file_storage/call_7KvRqM8zN3008tYq0vYkzBDS.json', 'var_call_pQ1qydoxyORDr9d3xLsFlPrs': {'records': [], 'cpc_codes': []}, 'var_call_4ypPDsIDPskWsUQVGCQMWqIg': 'file_storage/call_4ypPDsIDPskWsUQVGCQMWqIg.json', 'var_call_9759AZMZ4LhwXhJD9RTo1qBM': {'records': [], 'cpc_codes': []}}

exec(code, env_args)
