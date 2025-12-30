code = """import re, json, pandas as pd

# Load full civic docs
path_docs = var_call_NH60mxKpJ5em1laZhWB9dj3d
with open(path_docs, 'r') as f:
    civic_docs = json.load(f)

# Load funding table
path_funding = var_call_3mg2g7WN7DBdSBR4ESsHWzcB
with open(path_funding, 'r') as f:
    funding = json.load(f)

# Define Spring 2022 regex (months March-May 2022) and also patterns like '2022-Spring'
spring_patterns = [
    r"2022[- ]Spring",
    r"Spring 2022",
    r"March 2022", r"April 2022", r"May 2022",
    r"2022-03", r"2022-04", r"2022-05",
    r"2022-March", r"2022-April", r"2022-May"
]

text_all = "\n".join(doc['text'] for doc in civic_docs)

# Heuristic: project names are lines that look like title case with keywords like 'Project', 'Improvements', 'Repairs', etc.
lines = [l.strip() for l in text_all.split('\n') if l.strip()]
project_candidates = []
for i, line in enumerate(lines):
    if any(kw in line for kw in ["Project", "Improvements", "Repairs", "Resurfacing", "Drainage", "Slope", "Playground", "Park", "Bridge", "Culvert", "Water Treatment", "Warning", "Median", "Crosswalk", "Traffic", "HVAC", "Roof"]):
        # Look for nearby date info within next 5 lines
        nearby = " ".join(lines[i:i+6])
        if any(re.search(pat, nearby) for pat in spring_patterns):
            project_candidates.append(line)

# Deduplicate
project_candidates = sorted(set(project_candidates))

# Match against funding project names via simple string containment either way (case-insensitive)
fund_df = pd.DataFrame(funding)
fund_df['Amount'] = fund_df['Amount'].astype(int)
projects_started_spring = []
for cand in project_candidates:
    for pname in fund_df['Project_Name']:
        if cand.lower() in pname.lower() or pname.lower() in cand.lower():
            projects_started_spring.append(pname)

projects_started_spring = sorted(set(projects_started_spring))

subset = fund_df[fund_df['Project_Name'].isin(projects_started_spring)]
num_projects = subset['Project_Name'].nunique()
 total_funding = int(subset['Amount'].sum())

result = {"num_projects_started_spring_2022": int(num_projects), "total_funding": total_funding}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_NH60mxKpJ5em1laZhWB9dj3d': 'file_storage/call_NH60mxKpJ5em1laZhWB9dj3d.json', 'var_call_3mg2g7WN7DBdSBR4ESsHWzcB': 'file_storage/call_3mg2g7WN7DBdSBR4ESsHWzcB.json'}

exec(code, env_args)
