code = """import json, re, pandas as pd

# Load full results if needed
civic_path = var_call_dT5NmHeIinSiboM9nMIh1l8g
funding_path = var_call_9HaJu2T7bn9HruLzPpgQGkLT

with open(civic_path, 'r') as f:
    civic_docs = json.load(f)
with open(funding_path, 'r') as f:
    funding_records = json.load(f)

# Very rough heuristic extraction: project lines often look like stand-alone lines with capital letters and the word 'Project' or similar.
projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Split into lines
    for line in text.split('\n'):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        # Assume project name if it contains 'Project' or 'Improvements' or 'Repairs' or 'Park' etc., and is not too long
        if len(line_stripped) < 120 and re.search(r"(Project|Improvements|Repairs|Park|Road|Bridge|Drain|Facility|Study|Signals)", line_stripped):
            # avoid obvious non-titles
            if not line_stripped.lower().startswith(('updates', 'project description', 'project schedule', 'estimated schedule')):
                projects.append(line_stripped)

# Deduplicate
projects = sorted(set(projects))

# For this question, we need projects that started in Spring 2022.
# We'll look for patterns like 'Begin Construction: Spring 2022' or 'Start: 2022-Spring' near the project name.

spring_2022_projects = set()
for doc in civic_docs:
    text = doc.get('text', '')
    # For each known project name, search within a window around its occurrence
    for pname in projects:
        idx = text.find(pname)
        if idx == -1:
            continue
        window = text[idx: idx + 500]  # look ahead
        if re.search(r"(Spring\s*2022|2022[-/ ]Spring|March 2022|April 2022|May 2022)", window, re.IGNORECASE):
            spring_2022_projects.add(pname)

# Now join with funding records on Project_Name exact match
funding_df = pd.DataFrame(funding_records)
funding_df['Amount'] = funding_df['Amount'].astype(int)

spring_2022_list = list(spring_2022_projects)
matched = funding_df[funding_df['Project_Name'].isin(spring_2022_list)]

result = {
    'spring_2022_projects_found_in_docs': spring_2022_list,
    'projects_with_funding_match': matched['Project_Name'].tolist(),
    'count_projects_started_spring_2022_with_funding': int(matched['Project_Name'].nunique()),
    'total_funding_for_these_projects': int(matched['Amount'].sum())
}

out = json.dumps(result)
print("__RESULT__:")
print(out)"""

env_args = {'var_call_dT5NmHeIinSiboM9nMIh1l8g': 'file_storage/call_dT5NmHeIinSiboM9nMIh1l8g.json', 'var_call_9HaJu2T7bn9HruLzPpgQGkLT': 'file_storage/call_9HaJu2T7bn9HruLzPpgQGkLT.json'}

exec(code, env_args)
