code = """import json, re, pandas as pd

# Load full civic docs
with open(var_call_Cq1r4ggybWXoYuzzhWNhX2Fv, 'r') as f:
    civic_docs = json.load(f)

funding_records = var_call_uPuBrdttHgl3Q5yHZAKrVYkS

# Very rough heuristic: project lines often end with 'Project' or 'Improvements' etc.; dates nearby.
projects = []
for doc in civic_docs:
    text = doc.get('text','')
    # Split into lines
    lines = text.split('\n')
    for i, line in enumerate(lines):
        name = line.strip()
        if not name:
            continue
        # Heuristic: consider reasonably long capital project-like lines
        if any(k in name for k in ['Project','Improvements','Repairs','Resurfacing','Playground','Park','Bridge','Drain','Culvert','Water Treatment','Warning','Traffic Study','Median']) and len(name.split())<=15:
            # Search next few lines for a schedule with 'Begin Construction' or 'Start' and a Spring 2022 date
            window = '\n'.join(lines[i:i+8])
            # Look for patterns like 'Spring 2022' or March/April/May 2022
            if re.search(r'(Spring 2022|2022-Spring|March 2022|April 2022|May 2022)', window):
                projects.append({'Project_Name': name, 'context': window})

# Deduplicate by Project_Name
seen = {}
for p in projects:
    seen.setdefault(p['Project_Name'], p)
projects_unique = list(seen.values())

# Match to funding table by exact Project_Name
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

spring2022_funded = funding_df[funding_df['Project_Name'].isin([p['Project_Name'] for p in projects_unique])]

result = {
    'projects_started_spring_2022_count': int(len(projects_unique)),
    'projects_with_funding_count': int(len(spring2022_funded)),
    'total_funding_for_matched_projects': int(spring2022_funded['Amount'].sum()),
    'identified_projects': [p['Project_Name'] for p in projects_unique]
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_Cq1r4ggybWXoYuzzhWNhX2Fv': 'file_storage/call_Cq1r4ggybWXoYuzzhWNhX2Fv.json', 'var_call_uPuBrdttHgl3Q5yHZAKrVYkS': 'file_storage/call_uPuBrdttHgl3Q5yHZAKrVYkS.json'}

exec(code, env_args)
