code = """import json
import re

# load original query results
with open(var_call_GJgKFWFoYXX9ZQ06amDIgLQs, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_70j7EIEoi4BAitiidmGSdKTA, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# normalize funding
funding = []
for r in funding_records:
    try:
        amt = int(str(r.get('Amount')))
    except:
        try:
            amt = int(float(str(r.get('Amount'))))
        except:
            continue
    name = r.get('Project_Name','').strip()
    funding.append({'Project_Name': name, 'Amount': amt})

# funded >50k
funded = [f for f in funding if f['Amount'] > 50000]

# extract design projects from civic docs
def extract_design_projects(text):
    header = 'Capital Improvement Projects (Design)'
    idx = text.find(header)
    if idx == -1:
        return []
    next_headers = ['Capital Improvement Projects (Construction)', 'Capital Improvement Projects (Not Started)', 'Capital Improvement Projects (Design)']
    end_idx = len(text)
    for nh in next_headers:
        j = text.find(nh, idx + len(header))
        if j != -1:
            end_idx = min(end_idx, j)
    section = text[idx + len(header):end_idx]
    lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    projects = []
    for ln in lines:
        low = ln.lower()
        if any(k in low for k in ['updates', 'project schedule', 'project description', 'estimated schedule', 'complete design', 'advertise', 'begin construction', '(cid:', 'page', 'agenda', 'recommended action', 'discussion', 'to:', 'prepared by']):
            continue
        if len(ln.split()) > 15:
            continue
        if ln.endswith(':'):
            continue
        if re.search('[A-Za-z]', ln):
            cleaned = ln.lstrip('-–— ').rstrip(' -–—')
            if len(cleaned) < 3:
                continue
            projects.append(cleaned)
    seen = set(); out = []
    for p in projects:
        if p not in seen:
            seen.add(p); out.append(p)
    return out

all_design_projects = []
for doc in civic_docs:
    txt = doc.get('text','')
    ps = extract_design_projects(txt)
    all_design_projects.extend(ps)

# unique
unique_design_projects = []
seen = set()
for p in all_design_projects:
    if p not in seen:
        seen.add(p); unique_design_projects.append(p)

# normalize helper
def norm(s):
    return re.sub(r"[^a-z0-9]"," ", s.lower()).strip()

# match funded to design projects
matches = []
matched_funding_names = set()
for f in funded:
    fn = f['Project_Name']
    fn_norm = norm(fn)
    for dp in unique_design_projects:
        dp_norm = norm(dp)
        if not dp_norm:
            continue
        # exact or case-insensitive
        if fn_norm == dp_norm:
            matches.append({'Funding_Project_Name': fn, 'Amount': f['Amount'], 'Design_Project_Name': dp})
            matched_funding_names.add(fn)
            break
        # substring either way
        if dp_norm in fn_norm or fn_norm in dp_norm:
            matches.append({'Funding_Project_Name': fn, 'Amount': f['Amount'], 'Design_Project_Name': dp})
            matched_funding_names.add(fn)
            break

# Also check design projects that directly match funding names (other direction)
for dp in unique_design_projects:
    dpn = norm(dp)
    if not dpn:
        continue
    for f in funded:
        fn = f['Project_Name']
        if fn in matched_funding_names:
            continue
        fnn = norm(fn)
        if dpn == fnn or dpn in fnn or fnn in dpn:
            matches.append({'Funding_Project_Name': fn, 'Amount': f['Amount'], 'Design_Project_Name': dp})
            matched_funding_names.add(fn)
            break

# unique matches by funding project name
unique_matches = []
seen = set()
for m in matches:
    key = m['Funding_Project_Name']
    if key not in seen:
        seen.add(key)
        unique_matches.append(m)

result = {'count': len(unique_matches), 'matches': unique_matches}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GJgKFWFoYXX9ZQ06amDIgLQs': 'file_storage/call_GJgKFWFoYXX9ZQ06amDIgLQs.json', 'var_call_VxneExt2hKcFVVPOdTv38nAJ': ['civic_docs'], 'var_call_70j7EIEoi4BAitiidmGSdKTA': 'file_storage/call_70j7EIEoi4BAitiidmGSdKTA.json', 'var_call_7O0Xq1HhfA8phajgx6x7QkJf': 'file_storage/call_7O0Xq1HhfA8phajgx6x7QkJf.json'}

exec(code, env_args)
