code = """import re, json, pandas as pd

# civic docs
path = var_call_kdPV5Q110RU4aP18SXvq5Hp1
with open(path, 'r') as f:
    civic = json.load(f)
texts = [d['text'] for d in civic]

# very simple heuristic: lines that look like project titles, capture following context for dates
projects = []
for text in texts:
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        # project name: line with 'Project' or typical capital project phrases, avoid long narrative lines
        if len(line) < 120 and any(w in line for w in ['Project', 'Road', 'Park', 'Improvements', 'Repairs', 'Facility', 'Bridge', 'Biofilter', 'Sewer', 'Storm', 'Traffic', 'Skate']):
            context = '\n'.join(lines[i:i+8])
            # find start date patterns
            m = re.search(r'Begin Construction[:\-]?\s*([A-Za-z]+\s+2022|Spring 2022|Summer 2022|Fall 2022|Winter 2022|2022-Spring|2022-March|2022-April|2022-May)', context, re.IGNORECASE)
            if not m:
                m = re.search(r'Start(?: Date)?[:\-]?\s*([A-Za-z]+\s+2022|Spring 2022|2022-[A-Za-z]+)', context, re.IGNORECASE)
            if m:
                st = m.group(1)
                projects.append({'Project_Name': line, 'st': st})

# filter spring 2022 (March-May or explicit Spring 2022)
def is_spring_2022(s):
    s_lower = s.lower()
    if '2022' not in s_lower:
        return False
    if 'spring' in s_lower:
        return True
    for mon in ['march', 'april', 'may']:
        if mon in s_lower:
            return True
    return False

spring_projects = [p for p in projects if is_spring_2022(p['st'])]

# dedupe by name
seen = {}
for p in spring_projects:
    seen[p['Project_Name']] = p['st']

spring_project_names = list(seen.keys())

# load funding
path_f = var_call_t90ZFosVa1094Ln4aMtLpcDM
with open(path_f, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# fuzzy-ish join by exact match on project name
mask = fund_df['Project_Name'].isin(spring_project_names)
matched = fund_df[mask]

result = {
    'spring_projects_extracted': spring_project_names,
    'num_projects_with_funding': int(matched.shape[0]),
    'total_funding': int(matched['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kdPV5Q110RU4aP18SXvq5Hp1': 'file_storage/call_kdPV5Q110RU4aP18SXvq5Hp1.json', 'var_call_t90ZFosVa1094Ln4aMtLpcDM': 'file_storage/call_t90ZFosVa1094Ln4aMtLpcDM.json'}

exec(code, env_args)
