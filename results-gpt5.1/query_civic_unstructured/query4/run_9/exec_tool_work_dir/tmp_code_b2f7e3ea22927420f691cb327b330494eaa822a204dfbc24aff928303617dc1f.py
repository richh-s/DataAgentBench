code = """import re, json, pandas as pd

path_civic = var_call_kdPV5Q110RU4aP18SXvq5Hp1
with open(path_civic, 'r') as f:
    civic = json.load(f)
texts = [d['text'] for d in civic]

projects = []
for text in texts:
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if len(line) < 120 and any(w in line for w in ['Project', 'Road', 'Park', 'Improvements', 'Repairs', 'Facility', 'Bridge', 'Biofilter', 'Sewer', 'Storm', 'Traffic', 'Skate']):
            context = '\n'.join(lines[i:i+8])
            m = re.search(r'Begin Construction[:\-]?\s*([A-Za-z]+\s+2022|Spring 2022|Summer 2022|Fall 2022|Winter 2022|2022-Spring|2022-March|2022-April|2022-May)', context, re.IGNORECASE)
            if not m:
                m = re.search(r'Start(?: Date)?[:\-]?\s*([A-Za-z]+\s+2022|Spring 2022|2022-[A-Za-z]+)', context, re.IGNORECASE)
            if m:
                st = m.group(1)
                projects.append({'Project_Name': line, 'st': st})

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

seen = {}
for p in spring_projects:
    seen[p['Project_Name']] = p['st']

spring_project_names = list(seen.keys())

path_fund = var_call_t90ZFosVa1094Ln4aMtLpcDM
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

mask = fund_df['Project_Name'].isin(spring_project_names)
matched = fund_df[mask]

result = {
    'spring_projects_extracted': spring_project_names,
    'num_projects_started_spring_2022': int(len(spring_project_names)),
    'num_projects_with_funding_records': int(matched.shape[0]),
    'total_funding_for_matched_projects': int(matched['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_kdPV5Q110RU4aP18SXvq5Hp1': 'file_storage/call_kdPV5Q110RU4aP18SXvq5Hp1.json', 'var_call_t90ZFosVa1094Ln4aMtLpcDM': 'file_storage/call_t90ZFosVa1094Ln4aMtLpcDM.json'}

exec(code, env_args)
