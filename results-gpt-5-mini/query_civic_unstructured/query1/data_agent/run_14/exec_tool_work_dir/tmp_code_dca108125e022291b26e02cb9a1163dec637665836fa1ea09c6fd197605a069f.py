code = """import json
import re

# Load results
with open(var_call_GJgKFWFoYXX9ZQ06amDIgLQs, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_70j7EIEoi4BAitiidmGSdKTA, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# Normalize funding records
funding = []
for r in funding_records:
    amt_raw = r.get('Amount')
    try:
        amt = int(str(amt_raw))
    except:
        try:
            amt = int(float(str(amt_raw)))
        except:
            continue
    name = r.get('Project_Name','').strip()
    funding.append({'Project_Name': name, 'Amount': amt})

funded_gt50k = {rec['Project_Name'] for rec in funding if rec['Amount'] > 50000}

# Extract design projects from civic documents
def extract_design_projects(text):
    header = 'Capital Improvement Projects (Design)'
    idx = text.find(header)
    if idx == -1:
        return []
    # determine end of section by known next headers
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
        # skip lines that are clearly metadata or sentences
        if any(k in low for k in ['updates', 'project schedule', 'project description', 'estimated schedule', 'complete design', 'advertise', 'begin construction', '(cid:', 'page', 'agenda', 'recommended action', 'discussion', 'to:', 'prepared by']):
            continue
        # skip if contains many words (likely sentences)
        if len(ln.split()) > 12:
            continue
        # skip lines that end with ':'
        if ln.endswith(':'):
            continue
        # heuristics: accept lines that contain letters and at least one lowercase or uppercase pattern
        if re.search('[A-Za-z]', ln):
            # remove leading bullets or punctuation
            cleaned = ln.lstrip('-–— ').rstrip(' -–—')
            # ignore short tokens like 'Updates' etc
            if len(cleaned) < 3:
                continue
            projects.append(cleaned)
    # deduplicate preserving order
    seen = set()
    out = []
    for p in projects:
        if p not in seen:
            seen.add(p)
            out.append(p)
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
        seen.add(p)
        unique_design_projects.append(p)

# Find funded matches (exact or case-insensitive)
funded_matches = []
funded_map_lower = {n.lower(): n for n in funded_gt50k}
for proj in unique_design_projects:
    if proj in funded_gt50k:
        amt = next((r['Amount'] for r in funding if r['Project_Name'] == proj), None)
        funded_matches.append({'Project_Name': proj, 'Amount': amt})
    else:
        key = proj.lower()
        if key in funded_map_lower:
            matched_name = funded_map_lower[key]
            amt = next((r['Amount'] for r in funding if r['Project_Name'] == matched_name), None)
            funded_matches.append({'Project_Name': matched_name, 'Amount': amt})

result = {
    'design_capital_projects_extracted_count': len(unique_design_projects),
    'design_capital_projects_extracted': unique_design_projects,
    'funded_projects_over_50k_count': len(funded_matches),
    'funded_projects_over_50k': funded_matches
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GJgKFWFoYXX9ZQ06amDIgLQs': 'file_storage/call_GJgKFWFoYXX9ZQ06amDIgLQs.json', 'var_call_VxneExt2hKcFVVPOdTv38nAJ': ['civic_docs'], 'var_call_70j7EIEoi4BAitiidmGSdKTA': 'file_storage/call_70j7EIEoi4BAitiidmGSdKTA.json'}

exec(code, env_args)
