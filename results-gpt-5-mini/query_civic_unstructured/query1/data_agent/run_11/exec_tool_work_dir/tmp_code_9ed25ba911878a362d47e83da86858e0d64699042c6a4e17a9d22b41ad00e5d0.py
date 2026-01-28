code = """import json
import re

# Load tool results from storage files
with open(var_call_ix0eo19rhuYMXCVB7NWYe7Bw, 'r') as f:
    funding_records = json.load(f)
with open(var_call_F5LLyuXJFu5iKRtBhKU2o7T2, 'r') as f:
    civic_docs = json.load(f)

# Extract funding project names and amounts
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

# Function to extract design project names from a civic doc text
def extract_design_projects(text):
    projects = []
    lower = text.lower()
    # find the start of design section
    start = lower.find('capital improvement projects (design)')
    if start == -1:
        # try variant
        start = lower.find('capital improvement projects ( design )')
    if start == -1:
        return projects
    # find end of section by common next headers
    end_candidates = [
        'capital improvement projects (construction)',
        'capital improvement projects (not started)',
        '\n\ncapital improvement projects',
    ]
    end = len(text)
    for ec in end_candidates:
        pos = lower.find(ec, start+1)
        if pos != -1:
            end = min(end, pos)
    section = text[start:end]
    lines = section.splitlines()
    for line in lines:
        s = line.strip()
        if not s:
            continue
        low = s.lower()
        # skip obvious header lines
        if any(low.startswith(prefix) for prefix in ['capital improvement projects', 'updates', 'project schedule', 'recommended action', 'discussion']):
            continue
        if low.startswith('(cid:'):
            continue
        # skip lines that are clearly notes
        if ':' in s and len(s.split(':')[0]) < 30:
            # likely a key: value line
            continue
        # Exclude short words
        if len(s) < 4:
            continue
        # Heuristic: consider lines that contain keywords or Title Case
        keywords = ['project','improvements','repairs','study','plan','playground','walkway','resurfacing','traffic','park','skate','hvac','roof','crosswalk','median','signs','biofilter','storm','drain','culvert','retaining','slope','treatment','water']
        if any(k in low for k in keywords):
            projects.append(s)
            continue
        # If line looks like a project title (Title Case and multiple words)
        words = s.split()
        if len(words) <= 6 and any(w[0].isupper() for w in words if w):
            projects.append(s)
            continue
    # dedupe while preserving order
    seen = set()
    cleaned = []
    for p in projects:
        cp = re.sub(r'\s+', ' ', p).strip()
        if cp.lower() not in seen:
            seen.add(cp.lower())
            cleaned.append(cp)
    return cleaned

# Aggregate design projects from all documents
design_projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    extracted = extract_design_projects(text)
    for p in extracted:
        if p not in design_projects:
            design_projects.append(p)

# Normalization helper
def norm(s):
    if s is None:
        return ''
    return re.sub(r'[^a-z0-9]', ' ', s.lower()).strip()

# Build funding map by normalized name
funding_by_norm = {}
for f in funding_list:
    n = norm(f['Project_Name'])
    funding_by_norm.setdefault(n, []).append(f)

# Match design projects to funding records with Amount > 50000
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
        # dedupe by Project_Name
        unique = {m['Project_Name']: m for m in matches}
        matched[d] = list(unique.values())

count = len(matched)

result = {
    'count': count,
    'matched_projects': []
}
for d, recs in matched.items():
    result['matched_projects'].append({'design_project_name': d, 'funding_records': recs})

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_vEj1i90GOr4rti3UfgFRVXSF': ['civic_docs'], 'var_call_I4QKKhsbpH5JYKZMz2RDAT9S': ['Funding'], 'var_call_ix0eo19rhuYMXCVB7NWYe7Bw': 'file_storage/call_ix0eo19rhuYMXCVB7NWYe7Bw.json', 'var_call_F5LLyuXJFu5iKRtBhKU2o7T2': 'file_storage/call_F5LLyuXJFu5iKRtBhKU2o7T2.json'}

exec(code, env_args)
