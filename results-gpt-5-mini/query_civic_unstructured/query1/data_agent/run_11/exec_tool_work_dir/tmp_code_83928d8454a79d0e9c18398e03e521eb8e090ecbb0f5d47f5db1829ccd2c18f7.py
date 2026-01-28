code = """import json
import re

# Load tool results from storage files
with open(var_call_ix0eo19rhuYMXCVB7NWYe7Bw, 'r') as f:
    funding_records = json.load(f)
with open(var_call_F5LLyuXJFu5iKRtBhKU2o7T2, 'r') as f:
    civic_docs = json.load(f)

# Process funding records
funding_list = []
for r in funding_records:
    name = r.get('Project_Name')
    amt = r.get('Amount')
    try:
        amt_int = int(str(amt).replace(',', '').strip())
    except Exception:
        try:
            amt_int = int(float(amt))
        except Exception:
            amt_int = None
    funding_list.append({'Project_Name': name, 'Amount': amt_int})

# Helper to extract design projects from a document text
def extract_design_projects_simple(text):
    projects = []
    if not text:
        return projects
    lower = text.lower()
    start = lower.find('capital improvement projects (design)')
    if start == -1:
        return projects
    # try to find end marker
    end = lower.find('capital improvement projects (construction)', start)
    if end == -1:
        end = lower.find('capital improvement projects (not started)', start)
    if end == -1:
        # fallback: take 2000 chars after start
        end = start + 2000
        if end > len(text):
            end = len(text)
    section = text[start:end]
    lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    keywords = ['project','improvements','repairs','study','plan','playground','walkway','resurfacing','traffic','park','skate','hvac','roof','crosswalk','median','signs','biofilter','storm','drain','culvert','retaining','slope','treatment','water']
    for line in lines:
        low = line.lower()
        if len(line) < 4:
            continue
        if any(k in low for k in keywords):
            # avoid header lines
            if low.startswith('capital improvement projects') or low.startswith('updates') or low.startswith('discussion') or low.startswith('recommended action'):
                continue
            # remove trailing bullets like (cid:131)
            cleaned = re.sub('\(cid:[0-9]+\)', '', line).strip()
            # remove multiple spaces
            cleaned = re.sub(' +', ' ', cleaned)
            if cleaned and cleaned not in projects:
                projects.append(cleaned)
    return projects

# Aggregate design projects
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    extracted = extract_design_projects_simple(text)
    for p in extracted:
        if p not in design_projects:
            design_projects.append(p)

# Normalization
def norm(s):
    if not s:
        return ''
    return re.sub('[^a-z0-9]', ' ', s.lower()).strip()

# Build funding map
funding_by_norm = {}
for f in funding_list:
    n = norm(f.get('Project_Name'))
    funding_by_norm.setdefault(n, []).append(f)

# Match
matched = {}
for d in design_projects:
    dn = norm(d)
    if not dn:
        continue
    matches = []
    for fn, frecs in funding_by_norm.items():
        if not fn:
            continue
        if dn == fn or dn in fn or fn in dn:
            for rec in frecs:
                if rec['Amount'] is not None and rec['Amount'] > 50000:
                    matches.append(rec)
    if matches:
        unique = {m['Project_Name']: m for m in matches}
        matched[d] = list(unique.values())

count = len(matched)
result = {'count': count, 'matched_projects': []}
for d, recs in matched.items():
    result['matched_projects'].append({'design_project_name': d, 'funding_records': recs})

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_vEj1i90GOr4rti3UfgFRVXSF': ['civic_docs'], 'var_call_I4QKKhsbpH5JYKZMz2RDAT9S': ['Funding'], 'var_call_ix0eo19rhuYMXCVB7NWYe7Bw': 'file_storage/call_ix0eo19rhuYMXCVB7NWYe7Bw.json', 'var_call_F5LLyuXJFu5iKRtBhKU2o7T2': 'file_storage/call_F5LLyuXJFu5iKRtBhKU2o7T2.json'}

exec(code, env_args)
