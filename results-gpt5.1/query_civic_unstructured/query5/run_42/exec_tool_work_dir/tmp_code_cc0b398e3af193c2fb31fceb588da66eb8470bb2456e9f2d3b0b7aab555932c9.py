code = """import re, json
from pathlib import Path

# Load full civic docs results
path_docs = Path(var_call_7fZ4utP4jXBfBIOIshw9ACs7)
with open(path_docs, 'r') as f:
    docs = json.load(f)

# Load full funding table
path_funding = Path(var_call_Hf8XLxonaF78LYBOOsdUPM3E)
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Identify disaster-related projects from civic docs with start dates in 2022
projects_2022_disaster = set()

for doc in docs:
    text = doc.get('text', '')
    # Heuristic: project lines often end with 'Project' or 'Improvements' etc.
    # We will look for lines that mention '(FEMA' or '(CalOES' or '(CalJPIA' or 'Disaster' and also a 2022 date.
    for line in text.split('\n'):
        if not any(k in line for k in ['FEMA', 'CalOES', 'CalJPIA', 'Disaster']):
            continue
        if '2022' not in line:
            # Also allow dates on nearby lines: simple heuristic skipped for brevity
            continue
        # Clean line to derive project name by stripping dates like '2022', seasons, etc.
        cleaned = re.sub(r'\b2022\b.*', '', line).strip(' -:\u2022')
        # Further trim leading bullets
        cleaned = re.sub(r'^[\d\)\(\.\s]+', '', cleaned)
        if len(cleaned) > 3:
            projects_2022_disaster.add(cleaned)

# Map funding records to these projects by exact name match
project_names_2022_disaster = set(projects_2022_disaster)

# Also, from funding table, treat any project with FEMA/CalOES/CalJPIA in its name as disaster-type; but
# we still need them to have started in 2022 from docs. We'll join by names that appear in both sources.

# First, collect names from docs (all, not just with FEMA) where a project line includes '2022' and looks like a project
all_projects_2022 = set()
for doc in docs:
    for line in doc.get('text','').split('\n'):
        if '2022' in line and any(w in line for w in ['Project', 'Improvements', 'Repairs', 'Drain', 'Storm']):
            cleaned = re.sub(r'\b2022\b.*', '', line).strip(' -:\u2022')
            cleaned = re.sub(r'^[\d\)\(\.\s]+', '', cleaned)
            if len(cleaned) > 3:
                all_projects_2022.add(cleaned)

# Disaster type heuristics from name
DISASTER_KEYS = ['FEMA', 'CalOES', 'CalJPIA', 'Storm', 'Drainage', 'Drain', 'Fire']
for name in list(all_projects_2022):
    if any(k.lower() in name.lower() for k in DISASTER_KEYS):
        project_names_2022_disaster.add(name)

# Now sum funding amounts for funding records whose Project_Name matches one of these

total = 0
matched_projects = []
for row in funding:
    pname = row['Project_Name']
    if pname in project_names_2022_disaster:
        try:
            amt = int(row['Amount'])
        except Exception:
            try:
                amt = float(row['Amount'])
            except Exception:
                amt = 0
        total += amt
        matched_projects.append({'Project_Name': pname, 'Amount': amt})

result = {'total_funding_disaster_projects_started_2022': total, 'matched_projects': matched_projects}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_7fZ4utP4jXBfBIOIshw9ACs7': 'file_storage/call_7fZ4utP4jXBfBIOIshw9ACs7.json', 'var_call_Hf8XLxonaF78LYBOOsdUPM3E': 'file_storage/call_Hf8XLxonaF78LYBOOsdUPM3E.json'}

exec(code, env_args)
