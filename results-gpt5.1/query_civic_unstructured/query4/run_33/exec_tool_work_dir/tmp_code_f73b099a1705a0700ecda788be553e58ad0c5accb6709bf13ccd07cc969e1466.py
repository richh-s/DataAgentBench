code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_wY5FcABslEHs0Rl2GPaPbJTu
with open(path_docs, 'r') as f:
    docs = json.load(f)

projects = []
for d in docs:
    text = d.get('text', '')
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    for i, line in enumerate(lines):
        if ('project' in line.lower()) or re.search(r'\bImprovements\b|Repairs|Resurfacing|Playground|Study|Facility', line):
            name = line.strip('\u2022 ').strip('-').strip()
            st = None
            for j in range(i, min(i+6, len(lines))):
                m = re.search(r'Begin (Construction|Design):?\s*([^\n]+)', lines[j], re.I)
                if m:
                    st = m.group(2).strip()
                    break
            if st:
                projects.append({'Project_Name': name, 'st': st})

spring_2022_projects = []
for p in projects:
    st = p['st']
    if not st:
        continue
    s_low = st.lower()
    if ('2022' in s_low) and ('spring' in s_low or 'march' in s_low or 'april' in s_low or 'may' in s_low):
        spring_2022_projects.append(p)

funding = pd.DataFrame(var_call_eDW4WV93wNQVPGMybcsMM2i1)
funding['Amount'] = funding['Amount'].astype(int)

spring_df = pd.DataFrame(spring_2022_projects)
if not spring_df.empty:
    merged = spring_df.merge(funding, on='Project_Name', how='left')
    count_projects = merged['Project_Name'].nunique()
    total_funding = int(merged['Amount'].fillna(0).sum())
else:
    count_projects = 0
    total_funding = 0

result = {'num_projects_spring_2022': int(count_projects), 'total_funding_spring_2022': total_funding}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_wY5FcABslEHs0Rl2GPaPbJTu': 'file_storage/call_wY5FcABslEHs0Rl2GPaPbJTu.json', 'var_call_eDW4WV93wNQVPGMybcsMM2i1': 'file_storage/call_eDW4WV93wNQVPGMybcsMM2i1.json'}

exec(code, env_args)
