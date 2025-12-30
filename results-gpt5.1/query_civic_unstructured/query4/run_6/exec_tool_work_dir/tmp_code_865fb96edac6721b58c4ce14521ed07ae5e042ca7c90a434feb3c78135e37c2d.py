code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_W9Jr6cnB6B7avp2eakeoLaXs
with open(path_docs, 'r') as f:
    docs = json.load(f)

texts = [d['text'] for d in docs]
full_text = '\n'.join(texts)

# Heuristic: project names are lines that look like title-case project lines, often followed by schedule info
lines = [l.strip() for l in full_text.split('\n') if l.strip()]

projects = []
current = None
for line in lines:
    # Detect date-like tokens
    if 'Project Schedule' in line or 'Estimated Schedule' in line or 'Project Description' in line:
        continue
    # Simple capture for patterns like "Begin Construction: Spring 2022" or "Begin construction: Spring 2022"
    m = re.search(r'Begin\s+Construction:?\s*(Spring|Summer|Fall|Winter)\s*(20\d{2})', line, re.IGNORECASE)
    if m and current is not None:
        season = m.group(1).capitalize()
        year = m.group(2)
        st = f"{year}-{season}"
        projects.append({'Project_Name': current, 'st': st})
        current = None
        continue
    # Sometimes start time as just "Spring 2022" in a schedule line
    m2 = re.search(r'(Spring|Summer|Fall|Winter)\s*(20\d{2})', line, re.IGNORECASE)
    if m2 and current is not None and 'Begin' in line:
        season = m2.group(1).capitalize()
        year = m2.group(2)
        st = f"{year}-{season}"
        projects.append({'Project_Name': current, 'st': st})
        current = None
        continue
    # Detect potential project title lines: end with 'Project' or 'Improvements' etc.
    if re.match(r'.*(Project|Improvements|Repairs|Repair|Study|Signs|Siren|Facility|Playground|Walkway|Road)', line) and len(line.split())>2 and line[0].isupper():
        current = line

# Filter projects that started in Spring 2022
spring_2022_projects = [p for p in projects if p['st'] == '2022-Spring']

# Load funding table
path_fund = var_call_0zbWOwo4H2yq7jVrrMeJWZdg
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

proj_names = [p['Project_Name'] for p in spring_2022_projects]

# Fuzzy match: match funding Project_Name that contains the civic project name or vice versa (case-insensitive)
matched_funding = []
for pn in proj_names:
    for _, row in fund_df.iterrows():
        fn = row['Project_Name']
        if pn.lower() in fn.lower() or fn.lower() in pn.lower():
            matched_funding.append({'Project_Name': pn, 'Funding_Project_Name': fn, 'Amount': int(row['Amount'])})

count_projects = len(spring_2022_projects)
# Sum unique funding records
if matched_funding:
    matched_df = pd.DataFrame(matched_funding).drop_duplicates(subset=['Funding_Project_Name'])
    total_funding = int(matched_df['Amount'].sum())
else:
    total_funding = 0

result = {'projects_started_spring_2022': count_projects, 'total_funding': total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_W9Jr6cnB6B7avp2eakeoLaXs': 'file_storage/call_W9Jr6cnB6B7avp2eakeoLaXs.json', 'var_call_0zbWOwo4H2yq7jVrrMeJWZdg': 'file_storage/call_0zbWOwo4H2yq7jVrrMeJWZdg.json'}

exec(code, env_args)
