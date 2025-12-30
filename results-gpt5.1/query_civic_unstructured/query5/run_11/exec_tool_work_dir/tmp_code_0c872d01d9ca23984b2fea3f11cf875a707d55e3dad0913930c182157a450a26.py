code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path = var_call_NM0ZyMu9Tei19S2JtBRoTSMN
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(d.get('text','') for d in civic_docs)

# Extract lines that look like project listings with years and classify disaster-related
lines = [l.strip() for l in texts.split('\n') if l.strip()]
projects = []
for l in lines:
    if re.search(r'\b20(19|20|21|22|23|24)\b', l):
        # heuristic: line with year and some keywords
        name = l
        # disaster if FEMA/CalOES or disaster/fir e keywords
        disaster = bool(re.search(r'FEMA|CalOES|CalJPIA|disaster|fire', l, re.I))
        if disaster:
            projects.append(name)

# We need names of disaster-related projects that started in 2022.
# Very rough: look for '2022' in the line and treat whole line as project name.
proj_2022 = [p for p in projects if '2022' in p]

# Clean project names by removing extra schedule text after two spaces or ' - '
cleaned = []
for p in proj_2022:
    c = re.split(r'  | - ', p)[0].strip(' :')
    cleaned.append(c)

unique_projects_2022 = sorted(set(cleaned))

# Load funding table preview already materialized in var_call_kmbgxlRh9ZXbDRoMUktU6ExY
funding_path = var_call_kmbgxlRh9ZXbDRoMUktU6ExY
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

fdf = pd.DataFrame(funding_records)
fdf['Amount'] = fdf['Amount'].astype(int)

# Disaster-related projects in Funding table: names containing FEMA/CalOES/CalJPIA or parentheses with those.
mask_disaster = fdf['Project_Name'].str.contains('FEMA|CalOES|CalJPIA', case=False, regex=True)
# Also include ones where we matched names from docs (if any match)
if unique_projects_2022:
    name_mask = fdf['Project_Name'].isin(unique_projects_2022)
    mask_disaster = mask_disaster | name_mask

# For "started in 2022" we additionally require project name to include '2022' as heuristic
mask_2022 = fdf['Project_Name'].str.contains('2022')

target = fdf[mask_disaster & mask_2022]

total_funding = int(target['Amount'].sum())

result = {"total_funding_disaster_started_2022": total_funding,
          "matched_project_names": target['Project_Name'].tolist()}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_NM0ZyMu9Tei19S2JtBRoTSMN': 'file_storage/call_NM0ZyMu9Tei19S2JtBRoTSMN.json', 'var_call_kmbgxlRh9ZXbDRoMUktU6ExY': 'file_storage/call_kmbgxlRh9ZXbDRoMUktU6ExY.json'}

exec(code, env_args)
