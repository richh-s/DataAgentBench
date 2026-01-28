code = """import json, re
# load the query result JSON file path from storage variable
path = var_call_7KvRqM8zN3008tYq0vYkzBDS
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# helper to extract publication number from Patents_info
pubnum_pattern1 = re.compile(r'publication number\s*([A-Z0-9\-\.]+)', re.IGNORECASE)
pubnum_pattern2 = re.compile(r'\b([A-Z]{2,}-\d{4,}[A-Z0-9\-]*)\b')

def extract_pubnum(text):
    if not text:
        return None
    m = pubnum_pattern1.search(text)
    if m:
        return m.group(1)
    m2 = pubnum_pattern2.findall(text)
    if m2:
        # return the first that looks like a publication (prefer ones starting with two-letter code)
        return m2[0]
    return None

# helper to extract assignee from Patents_info
assignee_pattern = re.compile(r'^(.*?)\s+(holds|owns|is the owner|assigned to|owned by)\b', re.IGNORECASE)
paren_pattern = re.compile(r'^(.*?)\s*\(')

def extract_assignee(text):
    if not text:
        return None
    m = assignee_pattern.search(text)
    if m:
        return m.group(1).strip().upper()
    m2 = paren_pattern.search(text)
    if m2:
        return m2.group(1).strip().upper()
    # fallback: take first 40 chars
    return text.strip().split(',')[0].strip().upper()

# Build map of publication_number -> assignee for UNIV CALIFORNIA publications
univ_pubnums = set()
all_records = []
for rec in data:
    patents_info = rec.get('Patents_info') or ''
    pubnum = extract_pubnum(patents_info)
    assignee = extract_assignee(patents_info)
    # load citation list
    citations = []
    try:
        citations = json.loads(rec.get('citation') or '[]')
    except Exception:
        citations = []
    cited_pubnums = [c.get('publication_number') for c in citations if isinstance(c, dict) and c.get('publication_number')]
    # parse cpc field
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
    # if none marked first, take first code if exists
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
    if assignee and 'UNIV' in assignee and 'CALIFORNIA' in assignee:
        if pubnum:
            univ_pubnums.add(pubnum)

# Now find citing records where cited_pubnums intersects univ_pubnums and assignee != UNIV CALIFORNIA
results = {}
for r in all_records:
    if not r['pubnum']:
        continue
    # check if any cited pubnum is in univ_pubnums
    inter = set(r['cited_pubnums']).intersection(univ_pubnums)
    if inter:
        assignee = r['assignee'] or 'UNKNOWN'
        if 'UNIV' in assignee and 'CALIFORNIA' in assignee:
            continue
        # normalize assignee
        name = assignee
        codes = r['primary_cpcs']
        if not codes:
            continue
        if name not in results:
            results[name] = set()
        for c in codes:
            results[name].add(c)

# prepare output
records_out = []
all_codes = set()
for name, codes in results.items():
    codes_list = sorted(list(codes))
    records_out.append({'assignee': name, 'primary_cpcs': codes_list})
    for c in codes_list:
        all_codes.add(c)

out = {'records': records_out, 'cpc_codes': sorted(list(all_codes))}

import json
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_6eJOWXhg53i3nVbORiFLjbP6': ['publicationinfo'], 'var_call_1tuNt2y7YfWQjNjAnZxicsBc': ['cpc_definition'], 'var_call_7KvRqM8zN3008tYq0vYkzBDS': 'file_storage/call_7KvRqM8zN3008tYq0vYkzBDS.json'}

exec(code, env_args)
