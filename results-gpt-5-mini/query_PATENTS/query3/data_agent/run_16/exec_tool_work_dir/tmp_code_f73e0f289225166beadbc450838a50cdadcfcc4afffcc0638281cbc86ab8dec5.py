code = """import json, re
# load full publication data and univ pubnums
path_all = var_call_S5WHrUq87C0A9bOdZ4etAQM8
path_univ = var_call_vpxwh4RP4fL68KADXzklEsS4
with open(path_all, 'r', encoding='utf-8') as f:
    all_data = json.load(f)
univ_info = json.loads(open(path_univ, 'r', encoding='utf-8').read())
univ_pubnums = set([p.strip().strip('.') for p in univ_info.get('univ_pubnums', [])])

# helper functions
pubnum_norm = lambda s: (s or '').strip().strip('.')

# assignee extraction more general: look for tokens 'assigned to', 'owned by', 'is owned by', 'owned by', 'holds', 'is assigned to', 'assignee' etc
assignee_regex = re.compile(r'^(.*?)\s+(?:holds|owns|is the owner|assigned to|owned by|is owned by|is assigned to|has|owner is)\b', re.IGNORECASE)
paren_pattern = re.compile(r'^(.*?)\s*\(')

def extract_assignee(text):
    if not text:
        return None
    m = assignee_regex.search(text)
    if m:
        return m.group(1).strip().upper()
    m2 = paren_pattern.search(text)
    if m2:
        return m2.group(1).strip().upper()
    return text.strip().split(',')[0].strip().upper()

# iterate through all_data and find records that cite any univ pubnum
citing = {}
for rec in all_data:
    patents_info = rec.get('Patents_info') or ''
    assignee = extract_assignee(patents_info) or 'UNKNOWN'
    # skip univ california assignees
    if 'UNIV' in assignee and 'CALIFORNIA' in assignee:
        continue
    # parse citations
    cited = []
    try:
        cited = json.loads(rec.get('citation') or '[]')
    except Exception:
        cited = []
    cited_pubnums = [pubnum_norm(c.get('publication_number') or '') for c in cited if isinstance(c, dict) and c.get('publication_number')]
    # check intersection
    if not set(cited_pubnums).intersection(univ_pubnums):
        continue
    # extract primary cpcs
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
    if not primary_cpcs:
        continue
    # record
    if assignee not in citing:
        citing[assignee] = set()
    for code in primary_cpcs:
        citing[assignee].add(code)

out = {'citing': {k: sorted(list(v)) for k,v in citing.items()}}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6eJOWXhg53i3nVbORiFLjbP6': ['publicationinfo'], 'var_call_1tuNt2y7YfWQjNjAnZxicsBc': ['cpc_definition'], 'var_call_7KvRqM8zN3008tYq0vYkzBDS': 'file_storage/call_7KvRqM8zN3008tYq0vYkzBDS.json', 'var_call_pQ1qydoxyORDr9d3xLsFlPrs': {'records': [], 'cpc_codes': []}, 'var_call_4ypPDsIDPskWsUQVGCQMWqIg': 'file_storage/call_4ypPDsIDPskWsUQVGCQMWqIg.json', 'var_call_9759AZMZ4LhwXhJD9RTo1qBM': {'records': [], 'cpc_codes': []}, 'var_call_vpxwh4RP4fL68KADXzklEsS4': {'univ_pubnums': ['AU-2005269556-A1.', 'AU-3353000-A.', 'HR-P20201231-T1.', 'KR-20110004413-A.', 'US-2003112494-A1.', 'US-2005234013-A1.', 'US-2009031436-A1.', 'US-2017087258-A1.', 'US-2021282642-A1.', 'US-7052856-B2.', 'US-7745569-B2.', 'WO-2017136335-A1.', 'WO-2023212447-A2.']}, 'var_call_S5WHrUq87C0A9bOdZ4etAQM8': 'file_storage/call_S5WHrUq87C0A9bOdZ4etAQM8.json', 'var_call_dHh0OJFbrdgYdMXZf84wCoyW': {'num_univ_pubnums': 0, 'univ_pubnums_sample': [], 'citing': {}}}

exec(code, env_args)
