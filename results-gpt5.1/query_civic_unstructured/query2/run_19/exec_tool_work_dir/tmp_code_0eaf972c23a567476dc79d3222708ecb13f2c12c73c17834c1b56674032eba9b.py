code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_0TcYKsUaQsOYluyhAjzPgQN5
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = ' '.join(d['text'] for d in docs)

# Heuristic: park-related projects with 'Park' in name
project_patterns = [
    r'Trancas Canyon Park Playground',
    r'Trancas Canyon Park Upper and Lower Slopes Repair',
    r'Malibu Bluffs Park South Walkway Repairs',
    r'Malibu Bluffs Park South Walkway',
    r'Malibu Bluffs Park Roof Replacement Project',
    r'Bluffs Park Shade Structure',
    r'Bluffs Park Workout Station',
    r'Legacy Park Benches and Arbors Renovation',
    r'Legacy Park Paver Repair Project',
]

# Find completion info for 2022 in text
completed_2022_projects = set()
for name in project_patterns:
    # Find a window around each occurrence
    for m in re.finditer(re.escape(name), texts):
        window = texts[m.start():m.start()+400]
        if re.search(r'Construction was completed,?\s*(November|December|October)?\s*2022', window, re.IGNORECASE) or \
           re.search(r'completed\s+November\s+2022', window, re.IGNORECASE) or \
           re.search(r'completed\s+2022', window, re.IGNORECASE):
            completed_2022_projects.add(name)

# From preview we already saw "Bluffs Park Shade Structure" and "Point Dume Walkway Repairs" etc.
# Ensure specific known ones based on text: Bluffs Park Shade Structure completed November 2022.
completed_2022_projects.add('Bluffs Park Shade Structure')

# Load funding table
path_fund = var_call_h1J7lkC7p0Yt58e9SVqRxAB8
with open(path_fund, 'r') as f:
    funding = json.load(f)

fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)

# Filter to park-related by name containing 'Park'
park_df = fund_df[fund_df['Project_Name'].str.contains('Park', case=False, na=False)]

# Now restrict to those whose names are in completed_2022_projects
completed_park_df = park_df[park_df['Project_Name'].isin(completed_2022_projects)]

total_funding = int(completed_park_df['Amount'].sum())

result = {
    'completed_2022_park_projects': sorted(list(completed_2022_projects)),
    'funding_records': completed_park_df.to_dict(orient='records'),
    'total_funding': total_funding
}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_0TcYKsUaQsOYluyhAjzPgQN5': 'file_storage/call_0TcYKsUaQsOYluyhAjzPgQN5.json', 'var_call_h1J7lkC7p0Yt58e9SVqRxAB8': 'file_storage/call_h1J7lkC7p0Yt58e9SVqRxAB8.json'}

exec(code, env_args)
