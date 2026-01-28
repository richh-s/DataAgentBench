code = """import re, json
from pathlib import Path

# Load full civic docs
path = Path(var_call_V6M3AKnxaPZ2NomV2QZm3Dvv)
with open(path, 'r') as f:
    civic_docs = json.load(f)

texts = ' '.join(doc['text'] for doc in civic_docs)

# Heuristic: disaster-related project names often have FEMA/CalOES/CalJPIA or 'Disaster Recovery Projects'
# Extract project lines around those keywords and identify ones with 2022 in a start date.

# Simple approach: list all project-like capital/disaster entries with a year 2022 nearby
projects_2022 = set()

# Search for patterns like '\n<project name>\n' preceding 'Project Schedule' with some 2022 date
for match in re.finditer(r"\n([A-Z0-9][^\n]{5,80})\n[\s\S]{0,200}?2022", texts):
    name = match.group(1).strip()
    projects_2022.add(name)

# Also search explicitly for '(FEMA' etc near 2022
for match in re.finditer(r"\n([^\n]{5,80}FEMA[^\n]{0,40})\n[\s\S]{0,200}?2022", texts):
    projects_2022.add(match.group(1).strip())

# For this synthetic dataset, many project names in funding table likely exactly match phrases in the text.

# Now load funding table preview that we already have in memory (it should contain all rows)
funding = var_call_fsnMnMGYuVlZlVb0U5IhMidD

# Identify disaster-type projects by name heuristics: containing '(FEMA', '(CalOES', '(CalJPIA', or 'Disaster'

disaster_funding_2022 = 0
projects_counted = []
for row in funding:
    name = row['Project_Name']
    if not (('(FEMA' in name) or ('(CalOES' in name) or ('(CalJPIA' in name) or ('Disaster' in name)):
        continue
    # Assume all disaster projects with any 2022-related activity in docs started by 2022.
    # Use heuristic: if the base name (without parenthetical) appears in projects_2022 or the docs include '2022' and name.
    base_name = name.split('(')[0].strip()
    in_2022 = any(base_name in p for p in projects_2022)
    if not in_2022 and base_name:
        # Fallback: search directly in texts for 'base_name' within 200 chars of '2022'
        pattern = re.escape(base_name)
        if re.search(pattern + r"[\s\S]{0,200}?2022|2022[\s\S]{0,200}?" + pattern, texts):
            in_2022 = True
    if in_2022:
        disaster_funding_2022 += int(row['Amount'])
        projects_counted.append(name)

result = {"total_disaster_funding_started_2022": disaster_funding_2022, "projects_counted": projects_counted}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_V6M3AKnxaPZ2NomV2QZm3Dvv': 'file_storage/call_V6M3AKnxaPZ2NomV2QZm3Dvv.json', 'var_call_fsnMnMGYuVlZlVb0U5IhMidD': 'file_storage/call_fsnMnMGYuVlZlVb0U5IhMidD.json'}

exec(code, env_args)
