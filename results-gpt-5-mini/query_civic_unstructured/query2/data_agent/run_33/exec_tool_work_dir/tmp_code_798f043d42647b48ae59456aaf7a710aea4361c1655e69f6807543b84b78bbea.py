code = """import json
import re
import pandas as pd

# Load the results from earlier tool calls. These variables contain file paths to the JSON results.
with open(var_call_s5Sf1sLBWUAmmTXBqNBgDVPn, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_B3cOZcIzwasXby51pMoWCzCG, 'r') as f:
    funding_records = json.load(f)

# Normalize funding dataframe
funding_df = pd.DataFrame(funding_records)
# Ensure Amount is numeric
funding_df['Amount'] = pd.to_numeric(funding_df['Amount'], errors='coerce').fillna(0).astype(int)

# Function to extract completed-in-2022 project titles from a document text
def extract_completed_2022_projects(text):
    projects = []
    lines = text.splitlines()
    for i, line in enumerate(lines):
        low = line.lower()
        # check if this line indicates completion in 2022
        if 'completed' in low and '2022' in low:
            # search backward for a plausible project title line
            title = None
            for j in range(max(0, i-10), i)[::-1]:
                candidate = lines[j].strip()
                if not candidate:
                    continue
                # skip lines that look like metadata or bullet markers
                if candidate.startswith('(cid:') or candidate.lower().startswith('page') or candidate.lower().startswith('agenda'):
                    continue
                # candidate should be reasonably short and contain letters
                if len(candidate) <= 120 and re.search('[A-Za-z]', candidate):
                    title = candidate
                    break
            if title:
                projects.append(title)
    return projects

# Aggregate projects from all documents
completed_projects = []
for doc in civic_docs:
    text = doc.get('text','')
    completed_projects.extend(extract_completed_2022_projects(text))

# Deduplicate and normalize whitespace
completed_projects = [re.sub('\s+', ' ', p).strip() for p in completed_projects]
completed_projects = list(dict.fromkeys(completed_projects))

# Filter for park-related projects (name contains 'park' case-insensitive)
park_projects = [p for p in completed_projects if 'park' in p.lower()]

# For debugging, also include projects with 'playground' or 'walkway' that may be park-related
# but we'll stick to 'park' as primary criteria per user request

# Match with funding records by exact Project_Name
matched_funding = funding_df[funding_df['Project_Name'].isin(park_projects)]

total_funding = int(matched_funding['Amount'].sum())

# Prepare output
output = {
    'park_projects_completed_2022': park_projects,
    'matched_funding_records': matched_funding[['Funding_ID','Project_Name','Funding_Source','Amount']].to_dict(orient='records'),
    'total_funding': total_funding
}

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_B3cOZcIzwasXby51pMoWCzCG': 'file_storage/call_B3cOZcIzwasXby51pMoWCzCG.json', 'var_call_Wx9sBVIXluqh7TjyDQANyuuO': ['civic_docs'], 'var_call_s5Sf1sLBWUAmmTXBqNBgDVPn': 'file_storage/call_s5Sf1sLBWUAmmTXBqNBgDVPn.json'}

exec(code, env_args)
