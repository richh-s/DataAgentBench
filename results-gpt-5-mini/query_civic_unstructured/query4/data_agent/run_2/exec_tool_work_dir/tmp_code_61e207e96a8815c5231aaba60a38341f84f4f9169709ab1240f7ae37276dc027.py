code = """import json, re

with open(var_call_3hqM1np6KkTn39C8KATGtjxs, 'r', encoding='utf-8') as f:
    docs = json.load(f)
with open(var_call_2Ym9gg8atfpTFNFLlyWXF5ZU, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# normalize funding
for rec in funding:
    try:
        rec['Amount'] = int(rec['Amount'])
    except:
        rec['Amount'] = 0
    # remove parenthetical notes and non-alnum
    name = re.sub(r"\([^)]*\)", "", rec['Project_Name'])
    name = re.sub(r"[^a-z0-9 ]", "", name.lower())
    name = re.sub(r"\s+", " ", name).strip()
    rec['norm_name'] = name

# indicators for Spring 2022
ind_re = re.compile(r"spring|march|april|may|2022[-/ ]?03|2022[-/ ]?04|2022[-/ ]?05|03[-/ ]?2022|04[-/ ]?2022|05[-/ ]?2022", re.IGNORECASE)

found = []
for doc in docs:
    text = doc.get('text','')
    for m in re.finditer(r"2022", text):
        i = m.start()
        window = text[max(0,i-60):i+60]
        if not ind_re.search(window):
            continue
        # find title by looking back up to 800 chars, prefer lines containing 'Project'
        context = text[max(0,i-800):i]
        lines = context.splitlines()
        candidate = None
        # first look for a line containing 'Project' (but not 'Project Schedule' or 'Project Description')
        for line in reversed(lines):
            s = line.strip()
            if not s: continue
            low = s.lower()
            if 'project schedule' in low or 'project description' in low or low.startswith('(cid') or low.startswith('page') or 'updates'==low.lower():
                continue
            if 'project' in low and len(s)>5 and len(s)<140:
                candidate = s
                break
        # fallback: previous heuristics
        if not candidate:
            for line in reversed(lines):
                s = line.strip()
                if not s: continue
                if s.lower().startswith('(cid') or s.lower().startswith('page'): continue
                if ':' in s and len(s.split(':')[0])<20:
                    # skip labels
                    continue
                if 3 < len(s) < 140:
                    candidate = s
                    break
        if candidate:
            candidate = re.sub(r"\s+", " ", candidate).strip()
            found.append(candidate)

# dedupe
seen = set(); projects = []
for p in found:
    key = p.lower()
    if key not in seen:
        seen.add(key); projects.append(p)

# normalize project names similar to funding
def norm(p):
    s = re.sub(r"\([^)]*\)", "", p)
    s = re.sub(r"[^a-z0-9 ]", "", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return s

fund_matches = []
unmatched = []
for p in projects:
    pn = norm(p)
    p_tokens = set([w for w in pn.split() if len(w)>2])
    matched_any = False
    for rec in funding:
        fn = rec['norm_name']
        f_tokens = set([w for w in fn.split() if len(w)>2])
        # exact containment
        if pn and (pn in fn or fn in pn):
            fund_matches.append(rec); matched_any=True; continue
        # word overlap
        if p_tokens and f_tokens:
            inter = p_tokens & f_tokens
            jacc = len(inter)/max(1, len(p_tokens|f_tokens))
            if jacc >= 0.5:
                fund_matches.append(rec); matched_any=True; continue
    if not matched_any:
        unmatched.append(p)

# dedupe matched funding records
unique_matches = []
seen_ids = set()
for r in fund_matches:
    if r['Funding_ID'] not in seen_ids:
        seen_ids.add(r['Funding_ID']); unique_matches.append(r)

count_projects = len(projects)
total_funding = sum(r['Amount'] for r in unique_matches)

out = {
    'extracted_projects': projects,
    'count_projects': count_projects,
    'matched_funding_records': [{ 'Funding_ID': rec['Funding_ID'], 'Project_Name': rec['Project_Name'], 'Amount': rec['Amount']} for rec in unique_matches],
    'total_funding': total_funding,
    'unmatched_projects': unmatched
}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_mrKUQUZqQpDRGmJMWm4fFH94': ['civic_docs'], 'var_call_3hqM1np6KkTn39C8KATGtjxs': 'file_storage/call_3hqM1np6KkTn39C8KATGtjxs.json', 'var_call_n9w8fx8eWTs8Wte7JafN2ugu': ['Funding'], 'var_call_2Ym9gg8atfpTFNFLlyWXF5ZU': 'file_storage/call_2Ym9gg8atfpTFNFLlyWXF5ZU.json', 'var_call_IRRlZUKwIOLmwYSMVYiFJuHZ': {'extracted_projects': [], 'count_projects': 0, 'matched_funding_records': [], 'total_funding': 0, 'unmatched_projects': []}}

exec(code, env_args)
