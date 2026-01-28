code = """import json, re, pandas as pd

# Load full civic docs from file
with open(var_call_GQohpNwzKQfcLQDDg2YyH4le, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_wQUbrlN0U1Q5DEkEdeSRiWNL

# Heuristic: disaster-related if name contains FEMA, CalOES, CalJPIA, or explicitly "Disaster"/"Recovery"/"Fire"
DISASTER_PATTERN = re.compile(r'(FEMA|CalOES|CalJPIA|Disaster|Recovery|Fire)', re.IGNORECASE)

# Build simple project info from civic docs: for each line that looks like a project with a leading year, attempt to capture name and any date-like token
project_infos = {}
for doc in civic_docs:
    text = doc.get('text', '')
    for line in text.split('\n'):
        line = line.strip()
        if not line:
            continue
        # project name line often starts with a year
        m = re.match(r'(20\d{2}[^\n]*)', line)
        if m:
            pname = m.group(1).strip()
            # store with minimal info; dates often embedded, we'll just keep full string
            if pname not in project_infos:
                project_infos[pname] = {'Project_Name': pname}

# Create DataFrame from funding
fund_df = pd.DataFrame(funding_records)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Determine which funding records are disaster-related by name pattern
fund_df['is_disaster'] = fund_df['Project_Name'].str.contains(DISASTER_PATTERN)

# Determine which look like projects that started in 2022 based on name containing '2022'
fund_df['is_2022_name'] = fund_df['Project_Name'].str.contains('2022')

# For this task, "started in 2022" we approximate by project name containing '2022' OR project appearing in civic docs with '2022' in its name
civic_project_names = list(project_infos.keys())

def started_2022(name):
    if '2022' in name:
        return True
    # fuzzy match against civic project names containing 2022
    for cp in civic_project_names:
        if '2022' in cp and cp.split('2022')[-1].strip() and cp.split('2022')[-1].strip() in name:
            return True
    return False

fund_df['started_2022'] = fund_df['Project_Name'].apply(started_2022)

# Filter disaster + started in 2022
mask = fund_df['is_disaster'] & fund_df['started_2022']
subset = fund_df[mask]

total_funding = int(subset['Amount'].sum())

result = {
    'total_disaster_funding_started_2022': total_funding,
    'matching_projects': subset[['Funding_ID','Project_Name','Amount']].to_dict(orient='records')
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_GQohpNwzKQfcLQDDg2YyH4le': 'file_storage/call_GQohpNwzKQfcLQDDg2YyH4le.json', 'var_call_wQUbrlN0U1Q5DEkEdeSRiWNL': 'file_storage/call_wQUbrlN0U1Q5DEkEdeSRiWNL.json', 'var_call_gbaRxp9EGTyTfTp2agElyMEb': ['civic_docs'], 'var_call_sfQKx7owcYhdd8ofvMSKpKEG': ['Funding']}

exec(code, env_args)
