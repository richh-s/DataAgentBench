code = """import re, json
from pathlib import Path

# Load full civic docs text
path = Path(var_call_b5gOQ5oEO2vFnJj7jNsajWac)
import pandas as pd
civic_docs = pd.read_json(path)
text = " ".join(civic_docs['text'].tolist())

# Heuristic: disaster projects often have FEMA/CalOES in name, which we can detect
# But project names are clearer in Funding table; classify by name patterns there.

funding_path = Path(var_call_FwBf5k4NUcz45jzPgglCNDWs)
funding = pd.read_json(funding_path)

# Identify disaster-type projects as those whose names contain FEMA, CalOES, CalJPIA, or explicitly 'Disaster'
mask_disaster = funding['Project_Name'].str.contains('FEMA|CalOES|CalJPIA|Disaster', case=False, regex=True)

# Now, among those, determine which started in 2022 using civic text heuristics: look for '2022' near project name
projects_2022 = []
for name in funding.loc[mask_disaster, 'Project_Name']:
    # Build a loose regex to find project name (without suffixes) followed by some chars then 2022
    base_name = re.sub(r'\s*\(.*?\)', '', name)  # remove parentheses suffixes
    pattern = re.escape(base_name[:40])  # first 40 chars as anchor
    if re.search(pattern + r'.{0,120}?2022', text, flags=re.IGNORECASE|re.DOTALL):
        projects_2022.append(name)

# Filter funding to those disaster projects that appear to have 2022 start
funding_2022_disaster = funding[funding['Project_Name'].isin(projects_2022)].copy()
funding_2022_disaster['Amount'] = funding_2022_disaster['Amount'].astype(int)

total_funding = int(funding_2022_disaster['Amount'].sum())

result = {"total_disaster_funding_2022": total_funding, "projects_count": int(len(funding_2022_disaster)), "projects": funding_2022_disaster[['Project_Name','Amount']].to_dict(orient='records')}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_b5gOQ5oEO2vFnJj7jNsajWac': 'file_storage/call_b5gOQ5oEO2vFnJj7jNsajWac.json', 'var_call_FwBf5k4NUcz45jzPgglCNDWs': 'file_storage/call_FwBf5k4NUcz45jzPgglCNDWs.json'}

exec(code, env_args)
