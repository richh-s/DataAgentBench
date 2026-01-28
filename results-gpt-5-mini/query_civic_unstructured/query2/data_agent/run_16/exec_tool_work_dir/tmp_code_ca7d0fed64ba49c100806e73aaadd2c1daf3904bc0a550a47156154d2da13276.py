code = """import json
import re
import pandas as pd

# Load query results from storage-provided file paths
with open(var_call_1MY6sY7Ts9k0cWW2SLALkq1g, 'r') as f:
    civic_docs = json.load(f)
with open(var_call_ICB8tVrKgtUyY7Pq2B9yFWZU, 'r') as f:
    funding = json.load(f)

# Convert funding to DataFrame
fund_df = pd.DataFrame(funding)
# Ensure Amount is int
fund_df['Amount'] = fund_df['Amount'].astype(int)
fund_df['Project_Name_lower'] = fund_df['Project_Name'].str.lower()

park_projects_completed_2022 = set()

for doc in civic_docs:
    text = doc.get('text', '')
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'completed' in line.lower() and '2022' in line:
            # search upwards for project title
            for j in range(i-1, max(i-10, -1), -1):
                candidate = lines[j].strip()
                if not candidate:
                    continue
                # skip lines that look like markers or bullets or labels
                if candidate.lower().startswith('(cid:'):
                    continue
                if 'updates' in candidate.lower() or 'project schedule' in candidate.lower() or 'agenda' in candidate.lower():
                    continue
                # Heuristic: title lines often don't have colons and are not long
                if len(candidate) > 200:
                    continue
                # Found a plausible project title
                park_projects_completed_2022.add(candidate)
                break

# Also look for patterns like 'Complete Construction: April 2023' with 'Complete Construction:' followed by a year 2022 on same or next lines
for doc in civic_docs:
    text = doc.get('text', '')
    # find lines with 'Complete Construction:' and a 2022 somewhere in following two lines
    lines = text.splitlines()
    for i, line in enumerate(lines):
        if 'complete construction' in line.lower():
            # check this line and next two lines for 2022
            window = ' '.join(lines[i:i+3])
            if '2022' in window:
                # find title above
                for j in range(i-1, max(i-10, -1), -1):
                    candidate = lines[j].strip()
                    if not candidate:
                        continue
                    if candidate.lower().startswith('(cid:'):
                        continue
                    if 'updates' in candidate.lower() or 'project schedule' in candidate.lower():
                        continue
                    if len(candidate) > 200:
                        continue
                    park_projects_completed_2022.add(candidate)
                    break

# Filter to park-related projects: contain 'park' or 'playground' in the title (case-insensitive)
park_related = [p for p in park_projects_completed_2022 if re.search(r"\bpark\b|playground|bluffs", p, re.I)]

# For debugging, ensure unique sorted
park_related = sorted(park_related)

# Now match these to funding records
matched_fund_rows = []
matched_projects = {}
for proj in park_related:
    proj_low = proj.lower()
    # try exact match ignoring case
    exact = fund_df[fund_df['Project_Name_lower'] == proj_low]
    if not exact.empty:
        for _, r in exact.iterrows():
            matched_fund_rows.append(r)
            matched_projects[proj] = matched_projects.get(proj, []) + [r['Project_Name']]
        continue
    # try contains match
    contains = fund_df[fund_df['Project_Name_lower'].str.contains(re.sub(r"[^a-z0-9 ]", "", proj_low))]
    if not contains.empty:
        for _, r in contains.iterrows():
            matched_fund_rows.append(r)
            matched_projects[proj] = matched_projects.get(proj, []) + [r['Project_Name']]
        continue
    # try token subset match
    tokens = [t for t in re.split(r"\s+", re.sub(r"[^a-z0-9 ]", "", proj_low)) if len(t)>3]
    if tokens:
        def token_subset(s):
            return all(t in s for t in tokens)
        subset = fund_df[fund_df['Project_Name_lower'].apply(token_subset)]
        if not subset.empty:
            for _, r in subset.iterrows():
                matched_fund_rows.append(r)
                matched_projects[proj] = matched_projects.get(proj, []) + [r['Project_Name']]

# Sum unique funding rows (avoid double counting same funding row matched to multiple projects)
if matched_fund_rows:
    mf_df = pd.DataFrame(matched_fund_rows).drop_duplicates(subset=['Funding_ID'])
    total = int(mf_df['Amount'].sum())
else:
    mf_df = pd.DataFrame(columns=fund_df.columns)
    total = 0

# Prepare result
result = {
    'park_projects_found_in_docs': park_related,
    'matched_funding_project_names': list(mf_df['Project_Name']) if not mf_df.empty else [],
    'total_funding_for_parks_completed_2022': total
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_IUIYHWnuMtZDB0HgfEnBLdiw': ['civic_docs'], 'var_call_N62n9lfN1VWuV8YwS1C95L8v': ['Funding'], 'var_call_1MY6sY7Ts9k0cWW2SLALkq1g': 'file_storage/call_1MY6sY7Ts9k0cWW2SLALkq1g.json', 'var_call_ICB8tVrKgtUyY7Pq2B9yFWZU': 'file_storage/call_ICB8tVrKgtUyY7Pq2B9yFWZU.json'}

exec(code, env_args)
