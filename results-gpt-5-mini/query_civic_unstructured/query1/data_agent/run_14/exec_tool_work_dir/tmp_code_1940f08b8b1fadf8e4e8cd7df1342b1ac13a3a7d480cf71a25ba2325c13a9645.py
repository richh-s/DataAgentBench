code = """import json, re, os

# helper to load possibly-filepath variables
def load_var(v):
    if isinstance(v, str) and os.path.exists(v):
        with open(v, 'r', encoding='utf-8') as f:
            return json.load(f)
    return v

# Load stored results
var_funding = load_var(var_call_GJgKFWFoYXX9ZQ06amDIgLQs)
var_civic = load_var(var_call_70j7EIEoi4BAitiidmGSdKTA)
var_design_extracted = load_var(var_call_7O0Xq1HhfA8phajgx6x7QkJf)
var_matches = load_var(var_call_bjnizwc8h5G9azsZTcW00DYU)

# Get design project list
design_projects = None
if isinstance(var_design_extracted, dict) and 'design_capital_projects_extracted' in var_design_extracted:
    design_projects = var_design_extracted['design_capital_projects_extracted']
else:
    # fallback: try to extract from civic docs directly
    design_projects = []
    for doc in var_civic:
        text = doc.get('text','')
        header = 'Capital Improvement Projects (Design)'
        i = text.find(header)
        if i==-1: continue
        j = len(text)
        for nh in ['Capital Improvement Projects (Construction)','Capital Improvement Projects (Not Started)']:
            k = text.find(nh, i+len(header))
            if k!=-1: j = min(j,k)
        section = text[i+len(header):j]
        for ln in section.splitlines():
            ln = ln.strip()
            if not ln: continue
            # heuristic keep lines with project-like words
            if re.search(r'project|road|park|walkway|drain|median|culvert|retaining|skate|playground|traffic|roof|signal|crosswalk|biofilter|water|storm|shoulder|paver', ln, re.I):
                if len(ln.split())<=12:
                    design_projects.append(ln)
    # dedup
    seen=set(); out=[]
    for p in design_projects:
        if p not in seen:
            seen.add(p); out.append(p)
    design_projects = out

# Normalize function
def norm(s):
    s = re.sub(r"\(.*?\)", "", s)
    s = re.sub(r"[^a-z0-9 ]", " ", s.lower())
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Build funding list amount>50k
funding = []
for r in var_funding:
    name = r.get('Project_Name','')
    amt_raw = r.get('Amount')
    try:
        amt = int(str(amt_raw))
    except:
        try:
            amt = int(float(str(amt_raw)))
        except:
            continue
    if amt>50000 and name:
        funding.append({'Project_Name': name, 'Amount': amt, 'norm': norm(name)})

# Now match: for each design project, see if any funding entry matches by normalized equality or substring
matched_design = {}
for dp in design_projects:
    dpn = norm(dp)
    if not dpn: continue
    for f in funding:
        fn = f['norm']
        if not fn: continue
        if dpn == fn or dpn in fn or fn in dpn:
            matched_design[dp] = {'Funding_Project_Name': f['Project_Name'], 'Amount': f['Amount']}
            break

count = len(matched_design)
result = {'count': count, 'matched_design_projects': matched_design}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_GJgKFWFoYXX9ZQ06amDIgLQs': 'file_storage/call_GJgKFWFoYXX9ZQ06amDIgLQs.json', 'var_call_VxneExt2hKcFVVPOdTv38nAJ': ['civic_docs'], 'var_call_70j7EIEoi4BAitiidmGSdKTA': 'file_storage/call_70j7EIEoi4BAitiidmGSdKTA.json', 'var_call_7O0Xq1HhfA8phajgx6x7QkJf': 'file_storage/call_7O0Xq1HhfA8phajgx6x7QkJf.json', 'var_call_bjnizwc8h5G9azsZTcW00DYU': 'file_storage/call_bjnizwc8h5G9azsZTcW00DYU.json'}

exec(code, env_args)
