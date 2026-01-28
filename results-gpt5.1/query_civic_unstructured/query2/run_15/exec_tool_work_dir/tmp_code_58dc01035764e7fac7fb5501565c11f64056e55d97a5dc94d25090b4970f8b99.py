code = """import re, json, pandas as pd, os, textwrap

# Load full civic docs
path_docs = var_call_H990rB8ZcX9xgp1oP2yuKt7n
with open(path_docs, 'r') as f:
    docs = json.load(f)
texts = [d['text'] for d in docs]
full_text = "\n".join(texts)

# Heuristic: park-related projects: names containing 'Park' or 'Playground' or 'Skate Park'
# Extract project lines that look like project titles (start of line, some text, then possibly 'Project')
lines = full_text.split('\n')
project_lines = []
for i, line in enumerate(lines):
    clean = line.strip()
    if not clean:
        continue
    if re.search(r'Park|Playground|Skate Park', clean, re.IGNORECASE):
        # Exclude generic mentions like 'Public Works Quarterly Update flier'
        if len(clean) < 200:
            project_lines.append(clean)

project_names = sorted(set(project_lines))

# Load funding table
funding = var_call_8IHsNiJsGRcwYURuwiwvnazD
# funding is already list of dicts

# Build dataframe
fdf = pd.DataFrame(funding)
# normalize Amount
fdf['Amount'] = pd.to_numeric(fdf['Amount'])

# Identify park-related funded projects by name containing Park/Playground/Skate
mask_park = fdf['Project_Name'].str.contains(r'Park|Playground|Skate', case=False, regex=True)
park_funding = fdf[mask_park].copy()

# Now need those that were completed in 2022.
# We'll infer completion year from civic text: search nearby context for 'Construction was completed' or 'completed' with a date 2022.

completed_2022_projects = set()
for pn in park_funding['Project_Name'].unique():
    pattern = re.escape(pn)
    for m in re.finditer(pattern, full_text):
        start = max(0, m.start()-400)
        end = min(len(full_text), m.end()+400)
        ctx = full_text[start:end]
        if re.search(r'Construction was completed[^\n]*2022|completed,?\s*November 2022|completed,?\s*December 2022|completed November 2022', ctx):
            completed_2022_projects.add(pn)
            break

# If specific known from preview: 'Bluffs Park Shade Structure' and 'Point Dume Walkway Repairs' text shows completed November 2022.
# Also Broad Beach Road Water Quality Repair- park? No.

# Filter to completed 2022 park-related funded projects
mask_completed = park_funding['Project_Name'].isin(completed_2022_projects)
completed_park_funding_2022 = park_funding[mask_completed]

total_funding = int(completed_park_funding_2022['Amount'].sum())

result = {
    'project_names_detected_in_text': project_names[:50],
    'park_funded_projects': park_funding['Project_Name'].unique().tolist(),
    'completed_2022_projects_detected': sorted(list(completed_2022_projects)),
    'total_funding_completed_park_2022': total_funding
}

res_json = json.dumps(result)
print("__RESULT__:")
print(res_json)"""

env_args = {'var_call_H990rB8ZcX9xgp1oP2yuKt7n': 'file_storage/call_H990rB8ZcX9xgp1oP2yuKt7n.json', 'var_call_8IHsNiJsGRcwYURuwiwvnazD': 'file_storage/call_8IHsNiJsGRcwYURuwiwvnazD.json'}

exec(code, env_args)
