code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_lUjKkYUvnw5QmqGxnS0dfDbB
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

funding = pd.DataFrame(var_call_Sig9nD9Ha3fUy4O9U22gjlZf)
funding['Amount'] = funding['Amount'].astype(int)

texts = ' '.join(d['text'] for d in civic_docs)

# Simple heuristic: find project lines that look like names, then capture nearby status/date
projects = {}
for line in texts.split('\n'):
    line_stripped = line.strip()
    if not line_stripped:
        continue
    # Identify project name lines (start of line, capitalized words, contain key terms like Park, Playground, etc.)
    if any(k in line_stripped for k in ['Park', 'park', 'Playground', 'playground']):
        name = line_stripped
        if len(name.split()) < 2 or len(name) > 120:
            continue
        # initialize
        if name not in projects:
            projects[name] = {"Project_Name": name, "topic": [], "status": None, "et": None}

# Now scan for status/completion info
current_name = None
for line in texts.split('\n'):
    s = line.strip()
    if s in projects:
        current_name = s
        continue
    if not current_name:
        continue
    if 'Construction was completed' in s or 'construction was completed' in s or 'Construction was completed,' in s:
        # try to extract year
        m = re.search(r'(20\d{2})', s)
        year = m.group(1) if m else None
        projects[current_name]['status'] = 'completed'
        projects[current_name]['et'] = year
    elif 'Notice of completion filed' in s:
        m = re.search(r'(20\d{2})', s)
        year = m.group(1) if m else None
        if not projects[current_name]['status']:
            projects[current_name]['status'] = 'completed'
        projects[current_name]['et'] = projects[current_name]['et'] or year

# Build DataFrame of project info
proj_df = pd.DataFrame(projects.values())

# Mark park-related via name containing 'Park' or 'park'
proj_df['is_park'] = proj_df['Project_Name'].str.contains('Park', case=False, na=False)

# Filter completed in 2022
mask_2022 = (proj_df['status'] == 'completed') & (proj_df['et'] == '2022')
proj_2022_park = proj_df[mask_2022 & proj_df['is_park']]

# Join with funding on exact Project_Name match
merged = funding.merge(proj_2022_park[['Project_Name']], on='Project_Name', how='inner')

total_funding = int(merged['Amount'].sum()) if not merged.empty else 0

result = {"total_funding_park_completed_2022": total_funding,
          "projects": merged[['Project_Name','Amount']].to_dict(orient='records')}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_lUjKkYUvnw5QmqGxnS0dfDbB': 'file_storage/call_lUjKkYUvnw5QmqGxnS0dfDbB.json', 'var_call_Sig9nD9Ha3fUy4O9U22gjlZf': 'file_storage/call_Sig9nD9Ha3fUy4O9U22gjlZf.json'}

exec(code, env_args)
