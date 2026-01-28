code = """import json, re
path = var_call_S5WHrUq87C0A9bOdZ4etAQM8
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Build mapping publication_number -> assignee for all records
pubnum_pattern1 = re.compile(r'publication number\s*([A-Z0-9\-\.]+)', re.IGNORECASE)
pubnum_pattern2 = re.compile(r'\b([A-Z]{2,}-\d{4,}[A-Z0-9\-\.]*)\b')
assignee_pattern = re.compile(r'^(.*?)\s+(holds|owns|is the owner|assigned to|owned by)\b', re.IGNORECASE)
paren_pattern = re.compile(r'^(.*?)\s*\(')

def extract_pubnum(text):
    if not text:
        return None
    m = pubnum_pattern1.search(text)
    if m:
        return m.group(1).strip().strip('.')
    m2 = pubnum_pattern2.findall(text)
    if m2:
        return m2[0].strip().strip('.')
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

pub_to_assignee = {}
records = []
for rec in data:
    patents_info = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(patents_info)
    assignee = extract_assignee(patents_info)
    citations = []
    try:
        citations = json.loads(rec.get('citation') or '[]')
    except Exception:
        citations = []
    cited_pubnums = [ (c.get('publication_number') or '').strip().strip('.') for c in citations if isinstance(c, dict) and c.get('publication_number')]
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
    records.append({'pubnum': pubnum, 'assignee': assignee, 'cited_pubnums': cited_pubnums, 'primary_cpcs': primary_cpcs})
    if pubnum:
        pub_to_assignee[pubnum] = assignee

# Identify all Univ California pubnums
univ_pubnums = set([p for p,a in pub_to_assignee.items() if a and 'UNIV' in a and 'CALIFORNIA' in a])

# Find citing assignees (excluding Univ California) that cite any of these pubnums
citing = {}
for r in records:
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
        if assignee not in citing:
            citing[assignee] = set()
        for c in codes:
            citing[assignee].add(c)

out = {'num_univ_pubnums': len(univ_pubnums), 'univ_pubnums_sample': sorted(list(univ_pubnums))[:20], 'citing': {k: sorted(list(v)) for k,v in citing.items()}}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6eJOWXhg53i3nVbORiFLjbP6': ['publicationinfo'], 'var_call_1tuNt2y7YfWQjNjAnZxicsBc': ['cpc_definition'], 'var_call_7KvRqM8zN3008tYq0vYkzBDS': 'file_storage/call_7KvRqM8zN3008tYq0vYkzBDS.json', 'var_call_pQ1qydoxyORDr9d3xLsFlPrs': {'records': [], 'cpc_codes': []}, 'var_call_4ypPDsIDPskWsUQVGCQMWqIg': 'file_storage/call_4ypPDsIDPskWsUQVGCQMWqIg.json', 'var_call_9759AZMZ4LhwXhJD9RTo1qBM': {'records': [], 'cpc_codes': []}, 'var_call_vpxwh4RP4fL68KADXzklEsS4': {'univ_pubnums': ['AU-2005269556-A1.', 'AU-3353000-A.', 'HR-P20201231-T1.', 'KR-20110004413-A.', 'US-2003112494-A1.', 'US-2005234013-A1.', 'US-2009031436-A1.', 'US-2017087258-A1.', 'US-2021282642-A1.', 'US-7052856-B2.', 'US-7745569-B2.', 'WO-2017136335-A1.', 'WO-2023212447-A2.']}, 'var_call_S5WHrUq87C0A9bOdZ4etAQM8': 'file_storage/call_S5WHrUq87C0A9bOdZ4etAQM8.json'}

exec(code, env_args)
