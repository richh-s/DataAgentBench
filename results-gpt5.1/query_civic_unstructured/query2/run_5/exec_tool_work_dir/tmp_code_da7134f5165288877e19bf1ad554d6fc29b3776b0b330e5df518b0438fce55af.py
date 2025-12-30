code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_84Sl3ZB8yiNjquJOsuYNG09X)
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

texts = [d['text'] for d in civic_docs]

projects = []
for text in texts:
    # naive split on double newlines before project-like lines
    lines = text.split('\n')
    for line in lines:
        name = line.strip()
        if not name:
            continue
        # heuristic: project lines often contain words like 'Park' or 'Playground' etc
        if any(w in name for w in ['Park', 'Playground']):
            projects.append({'Project_Name': name})

# deduplicate
proj_names = sorted(set(p['Project_Name'] for p in projects))

# Build dataframe of funding
funding_df = pd.DataFrame(var_call_sEzFBeEa84fUjJ1lw23iKZED)
funding_df['Amount'] = funding_df['Amount'].astype(int)

# Filter park-related projects in funding by matching any park-related project name extracted
park_like = [n for n in proj_names if 'Park' in n or 'Playground' in n]

# However, we also need completed in 2022; search texts for 'Construction was completed, 2022' near project names
completed_2022_projects = set()
for text in texts:
    for m in re.finditer(r"(.*?)\n\(cid:190\) Updates: Construction was completed,? (November|December|October|September|August|July|June|May|April|March|February|January)? ?2022", text):
        # Backtrack to find project title above
        segment = text[:m.start()]
        seg_lines = segment.strip().split('\n')
        if seg_lines:
            title = seg_lines[-1].strip()
            if 'Park' in title or 'Playground' in title:
                completed_2022_projects.add(title)

# Also specific known ones from preview
for name in ['Bluffs Park Shade Structure', 'Broad Beach Road Water Quality Repair', 'Point Dume Walkway Repairs']:
    if 'Park' in name:
        completed_2022_projects.add(name)

# Now intersect with funding
funding_park = funding_df[funding_df['Project_Name'].isin(completed_2022_projects)]

total_funding = int(funding_park['Amount'].sum())

result = {'total_funding_completed_2022_park_projects': total_funding,
          'projects': funding_park[['Project_Name','Amount']].to_dict(orient='records')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_84Sl3ZB8yiNjquJOsuYNG09X': 'file_storage/call_84Sl3ZB8yiNjquJOsuYNG09X.json', 'var_call_sEzFBeEa84fUjJ1lw23iKZED': 'file_storage/call_sEzFBeEa84fUjJ1lw23iKZED.json'}

exec(code, env_args)
