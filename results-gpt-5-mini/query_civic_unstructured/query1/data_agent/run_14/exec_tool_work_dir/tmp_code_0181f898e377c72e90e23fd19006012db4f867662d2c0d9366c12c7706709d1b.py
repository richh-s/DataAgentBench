code = """import json, re

with open(var_call_GJgKFWFoYXX9ZQ06amDIgLQs, 'r', encoding='utf-8') as f:
    funding_records = json.load(f)
with open(var_call_70j7EIEoi4BAitiidmGSdKTA, 'r', encoding='utf-8') as f:
    civic_docs = json.load(f)

# normalize function
def norm(s):
    s = re.sub(r"\(.*?\)", "", s)  # remove parentheticals
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return s

# build funding map for amounts >50k
funding_map = {}
for r in funding_records:
    try:
        amt = int(str(r.get('Amount')))
    except:
        try:
            amt = int(float(str(r.get('Amount'))))
        except:
            continue
    name = (r.get('Project_Name') or '').strip()
    if amt > 50000 and name:
        funding_map[name] = amt

funding_norm = {norm(k): (k,v) for k,v in funding_map.items()}

# keywords to identify project titles
keywords = ['project','improvement','improvements','repair','repairs','resurfacing','road','park','walkway','drain','median','culvert','retaining','skate','playground','traffic','roof','hvac','signal','crosswalk','biofilter','water','storm','diversion','shoulder','sidewalk','paver']

candidates = []
for doc in civic_docs:
    text = doc.get('text','')
    header = 'Capital Improvement Projects (Design)'
    idx = text.find(header)
    if idx == -1:
        continue
    # find end
    end_tokens = ['Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)','Capital Improvement Projects (Design)']
    end_idx = len(text)
    for t in end_tokens:
        j = text.find(t, idx+len(header))
        if j != -1:
            end_idx = min(end_idx, j)
    section = text[idx+len(header):end_idx]
    lines = [ln.strip() for ln in section.splitlines() if ln.strip()]
    for ln in lines:
        # skip meta lines
        low = ln.lower()
        if any(k in low for k in ['updates','project schedule','project description','estimated schedule','complete design','advertise','begin construction','(cid:','page','agenda','recommended action','discussion','to:','prepared by']):
            continue
        # must contain at least one keyword or end with 'Project'
        if not (any(k in low for k in keywords) or low.endswith('project')):
            continue
        # limit length
        if len(ln.split()) > 10:
            continue
        # clean
        cleaned = re.sub(r"\s+", " ", ln).strip(' -–—:\n')
        # remove trailing phrases like 'project' alone
        candidates.append(cleaned)

# deduplicate preserving order
seen = set(); unique_candidates = []
for c in candidates:
    if c not in seen:
        seen.add(c); unique_candidates.append(c)

# match candidates to funding_map
matches = []
matched_candidates = set()
for c in unique_candidates:
    cn = norm(c)
    # direct norm match
    if cn in funding_norm:
        fk, (orig_name, amt) = cn, funding_norm[cn]
        matches.append({'Design_Project_Name': c, 'Funding_Project_Name': orig_name, 'Amount': amt})
        matched_candidates.add(c)
        continue
    # try substring matching
    found = False
    for fn_norm,(orig_name, amt) in funding_norm.items():
        if fn_norm and (cn in fn_norm or fn_norm in cn):
            matches.append({'Design_Project_Name': c, 'Funding_Project_Name': orig_name, 'Amount': amt})
            matched_candidates.add(c)
            found = True
            break
    if found:
        continue

# count unique design projects matched
unique_design_matched = {}
for m in matches:
    key = m['Design_Project_Name']
    if key not in unique_design_matched:
        unique_design_matched[key] = m

result = {'design_capital_projects_with_funding_gt_50k_count': len(unique_design_matched),
          'projects': list(unique_design_matched.values())}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GJgKFWFoYXX9ZQ06amDIgLQs': 'file_storage/call_GJgKFWFoYXX9ZQ06amDIgLQs.json', 'var_call_VxneExt2hKcFVVPOdTv38nAJ': ['civic_docs'], 'var_call_70j7EIEoi4BAitiidmGSdKTA': 'file_storage/call_70j7EIEoi4BAitiidmGSdKTA.json', 'var_call_7O0Xq1HhfA8phajgx6x7QkJf': 'file_storage/call_7O0Xq1HhfA8phajgx6x7QkJf.json', 'var_call_bjnizwc8h5G9azsZTcW00DYU': 'file_storage/call_bjnizwc8h5G9azsZTcW00DYU.json'}

exec(code, env_args)
