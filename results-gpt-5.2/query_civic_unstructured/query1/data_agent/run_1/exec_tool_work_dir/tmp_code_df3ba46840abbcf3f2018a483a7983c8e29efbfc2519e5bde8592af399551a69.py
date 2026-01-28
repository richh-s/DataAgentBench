code = """import json, re, pandas as pd

# Load funding > 50000
fund_path = var_call_Jims3puwvUHWJioYw1CyXeFW
with open(fund_path,'r',encoding='utf-8') as f:
    funding = json.load(f)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = pd.to_numeric(fund_df['Amount'], errors='coerce')
fund_projects = set(fund_df.loc[fund_df['Amount']>50000,'Project_Name'].dropna().astype(str))

# Load civic docs
docs_path = var_call_SxojWHDpzzjteMlbajf9dNmI
with open(docs_path,'r',encoding='utf-8') as f:
    docs = json.load(f)

# Extract project names under "Capital Improvement Projects (Design)" blocks
proj_design_capital = set()
for d in docs:
    text = d.get('text','') or ''
    # normalize newlines
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'^Capital Improvement Projects \(Design\)\s*$', ln, flags=re.I):
            j = i+1
            while j < len(lines):
                l = lines[j].strip()
                if re.match(r'^Capital Improvement Projects \(', l, flags=re.I) and re.search(r'\(Design\)', l, flags=re.I) is None:
                    break
                if re.match(r'^(Disaster Recovery Projects|Capital Improvement Projects \(Construction\)|Capital Improvement Projects \(Not Started\))', l, flags=re.I):
                    break
                if not l or l.startswith('(') or l.startswith('Page ') or l.startswith('Agenda Item'):
                    j += 1
                    continue
                if re.match(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION:|DISCUSSION:|Project Schedule|Estimated Schedule|Updates:|Project Description:)', l):
                    j += 1
                    continue
                # project title lines tend to be standalone and followed by bullets/Updates
                if len(l) >= 4 and len(l) <= 120 and not l.endswith(':'):
                    if not re.search(r'\b(cid:|\u2019|\u201c|\u201d)', l):
                        proj_design_capital.add(l)
                j += 1

# Intersect with funded projects
count = len(proj_design_capital & fund_projects)

print('__RESULT__:')
print(json.dumps({'count': int(count)}))"""

env_args = {'var_call_USmpOSrSOowb8w19uixDB0NH': ['Funding'], 'var_call_Jims3puwvUHWJioYw1CyXeFW': 'file_storage/call_Jims3puwvUHWJioYw1CyXeFW.json', 'var_call_KbT9FJwHUOuewuIv6hq7phAm': ['civic_docs'], 'var_call_SxojWHDpzzjteMlbajf9dNmI': 'file_storage/call_SxojWHDpzzjteMlbajf9dNmI.json'}

exec(code, env_args)
