code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_dzAmbL820r2mzYlvgOcJfIOQ
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding
path_fund = var_call_v3lEntZgSJ801nDZAVOpAoi4
with open(path_fund, 'r') as f:
    funding = json.load(f)

# Very heuristic: find lines that look like project entries with completion dates
park_projects_2022 = set()
for doc in civic_docs:
    text = doc.get('text','')
    # split into lines
    lines = text.split('\n')
    current_project = None
    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        # New project line: often ends with 'Project' or 'Park' etc and no colon
        if re.match(r'.*(Project|Park|Playground)$', stripped) and not stripped.startswith('('):
            current_project = stripped
        # Look for completed with 2022 in same or nearby lines
        if 'Construction was completed' in stripped or 'Construction was completed,' in stripped or 'Construction was completed ' in stripped or 'Construction was completed.' in stripped:
            if '2022' in stripped:
                if current_project and re.search(r'park', current_project, re.I):
                    park_projects_2022.add(current_project)
        if 'Construction was completed' in stripped and '2022' in stripped and current_project is None:
            # try to backtrack previous non-empty line
            pass

# Manually also catch explicit known ones from preview: Bluffs Park Shade Structure, Broad Beach Road Water Quality Repair, Point Dume Walkway Repairs, Marie Canyon Green Streets
# Only keep park-related by name containing 'Park'

# Build dataframe and match against funding projects by substring similarity (case-insensitive contains)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

park_keywords = ['park']
completed_2022_projects = []

# Scan civic docs for any line mentioning 'Construction was completed' and year 2022, and capture previous line as project name
for doc in civic_docs:
    lines = doc.get('text','').split('\n')
    for i, line in enumerate(lines):
        if 'Construction was completed' in line and '2022' in line:
            # backtrack to previous non-empty line
            j = i-1
            while j >=0 and not lines[j].strip():
                j -= 1
            if j>=0:
                pname = lines[j].strip()
                if any(k in pname.lower() for k in park_keywords):
                    completed_2022_projects.append(pname)

park_projects_2022.update(completed_2022_projects)

# Normalize project names for matching: use lowercase
fund_total = 0
matched_projects = []
for pname in park_projects_2022:
    pname_low = pname.lower()
    # try exact match first
    matches = fund_df[fund_df['Project_Name'].str.lower() == pname_low]
    if matches.empty:
        # try contains either way
        matches = fund_df[fund_df['Project_Name'].str.lower().str.contains(pname_low)]
    if matches.empty:
        matches = fund_df[fund_df['Project_Name'].str.lower().apply(lambda x: pname_low in x or x in pname_low)]
    if not matches.empty:
        amt = matches['Amount'].sum()
        fund_total += amt
        matched_projects.extend(matches['Project_Name'].tolist())

result = {
    'park_projects_completed_2022': sorted(list(park_projects_2022)),
    'matched_funding_projects': sorted(list(set(matched_projects))),
    'total_funding': int(fund_total)
}

res_str = json.dumps(result)
print("__RESULT__:")
print(res_str)"""

env_args = {'var_call_dzAmbL820r2mzYlvgOcJfIOQ': 'file_storage/call_dzAmbL820r2mzYlvgOcJfIOQ.json', 'var_call_v3lEntZgSJ801nDZAVOpAoi4': 'file_storage/call_v3lEntZgSJ801nDZAVOpAoi4.json'}

exec(code, env_args)
