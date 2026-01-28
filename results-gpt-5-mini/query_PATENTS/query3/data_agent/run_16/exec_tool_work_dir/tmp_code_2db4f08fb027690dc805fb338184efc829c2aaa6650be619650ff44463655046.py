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

all_records = []
for rec in data:
    patents_info = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(patents_info)
    assignee = extract_assignee(patents_info)
    citations = []
    try:
        citations = json.loads(rec.get('citation') or '[]')
    except Exception:
        citations = []
    cited_pubnums = [c.get('publication_number') for c in citations if isinstance(c, dict) and c.get('publication_number')]
    primary_cpcs = []
    try:
        cpcs = json.loads(rec.get('cpc') or '[]')
        for c in cpcs:
            if isinstance(c, dict) and c.get('first'):
                code = c.get('code')
                if code:
                    primary_cpcs.append(code)
    except Exception:
        primary_cpcs = []
    if not primary_cpcs:
        try:
            cpcs = json.loads(rec.get('cpc') or '[]')
            if isinstance(cpcs, list) and len(cpcs)>0 and isinstance(cpcs[0], dict):
                code = cpcs[0].get('code')
                if code:
                    primary_cpcs = [code]
        except Exception:
            pass
    all_records.append({'pubnum': pubnum, 'assignee': assignee, 'cited_pubnums': cited_pubnums, 'primary_cpcs': primary_cpcs})

# Build set of Univ California pubnums from this subset
univ_pubnums = set([r['pubnum'] for r in all_records if r['assignee'] and 'UNIV' in r['assignee'] and 'CALIFORNIA' in r['assignee'] and r['pubnum']])

results = {}
for r in all_records:
    if not r['pubnum']:
        continue
    inter = set(r['cited_pubnums']).intersection(univ_pubnums)
    if inter:
        assignee = r['assignee'] or 'UNKNOWN'
        if 'UNIV' in assignee and 'CALIFORNIA' in assignee:
            continue
        codes = r['primary_cpcs']
        if not codes:
            continue
        if assignee not in results:
            results[assignee] = set()
        for c in codes:
            results[assignee].add(c)

records_out = []
all_codes = set()
for name, codes in results.items():
    records_out.append({'assignee': name, 'primary_cpcs': sorted(list(codes))})
    for c in codes:
        all_codes.add(c)

out = {'records': records_out, 'cpc_codes': sorted(list(all_codes))}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6eJOWXhg53i3nVbORiFLjbP6': ['publicationinfo'], 'var_call_1tuNt2y7YfWQjNjAnZxicsBc': ['cpc_definition'], 'var_call_7KvRqM8zN3008tYq0vYkzBDS': 'file_storage/call_7KvRqM8zN3008tYq0vYkzBDS.json', 'var_call_pQ1qydoxyORDr9d3xLsFlPrs': {'records': [], 'cpc_codes': []}, 'var_call_4ypPDsIDPskWsUQVGCQMWqIg': 'file_storage/call_4ypPDsIDPskWsUQVGCQMWqIg.json'}

exec(code, env_args)
