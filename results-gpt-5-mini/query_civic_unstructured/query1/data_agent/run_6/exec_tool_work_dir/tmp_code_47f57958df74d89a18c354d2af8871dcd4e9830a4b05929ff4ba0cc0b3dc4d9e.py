code = """import json, re, pandas as pd

# Load previous tool results from storage file paths
funding_path = var_call_6FsTuhWZB0dRWwswUanAjfgK
civic_path = var_call_9HxR8Xui7at4Mm2YfCWumBZ7

with open(funding_path, 'r', encoding='utf-8') as f:
    funding = json.load(f)
with open(civic_path, 'r', encoding='utf-8') as f:
    civic = json.load(f)

# Create DataFrame for funding
df = pd.DataFrame(funding)
# Ensure Amount is int
df['Amount'] = df['Amount'].astype(int)

# Extract project names from the 'Capital Improvement Projects (Design)' sections
design_projects = set()
for doc in civic:
    text = doc.get('text', '')
    # Find the Design section until the next major Capital Improvement Projects subsection
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(?:Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Capital Improvement Projects\s*\(|Capital Improvement Projects|$)', text, re.S | re.I)
    if not m:
        continue
    chunk = m.group(1)
    lines = [line.strip() for line in chunk.splitlines()]
    for line in lines:
        if not line:
            continue
        low = line.lower()
        # Filter out metadata/notes lines
        if low.startswith('(cid') or low.startswith('updates:') or low.startswith('project schedule:'):
            continue
        if low.startswith('page ') or low.startswith('agenda') or low.startswith('recommended action') or low.startswith('discussion'):
            continue
        if any(k in line for k in [':', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date']):
            # likely not a project title
            continue
        # Exclude lines that look like sentences (contain common verbs)
        if re.search(r'\b(is|are|will|work|staff|plans|project|city|consultant|complete|advertise|begin|design)\b', low):
            # but some project names may contain 'Project' or 'Design' etc; allow if line ends with 'Project' or contains 'Project' and is reasonably short
            if 'project' in low and len(line) < 100:
                pass
            else:
                # skip lines that are descriptive sentences
                continue
        # Keep plausible project lines
        if len(line) >= 3:
            design_projects.add(line)

# Now, for each extracted design project, sum funding amounts from Funding table where names match or contain each other (case-insensitive)
project_funding = {}
for proj in design_projects:
    total = 0
    for _, row in df.iterrows():
        fname = row['Project_Name']
        if proj.lower() in fname.lower() or fname.lower() in proj.lower():
            total += int(row['Amount'])
    project_funding[proj] = total

# Count how many have funding greater than 50000
count_over_50000 = sum(1 for v in project_funding.values() if v > 50000)
projects_over_50000 = sorted([p for p,v in project_funding.items() if v > 50000])

# Prepare JSON-serializable output
output = {'count': count_over_50000, 'projects_over_50000': projects_over_50000}

import json
print("----BEGIN PRINT FORMAT----")
print("print(\"__RESULT__:\")")
print("print('" + json.dumps(output).replace("'", "\\'") + "')")
print("----END PRINT FORMAT----")"""

env_args = {'var_call_KR7TJInlrgL5ul9zLeO5DE1h': ['civic_docs'], 'var_call_ZzN4zoXVJbIgtrVQCiQ2luo3': ['Funding'], 'var_call_6FsTuhWZB0dRWwswUanAjfgK': 'file_storage/call_6FsTuhWZB0dRWwswUanAjfgK.json', 'var_call_9HxR8Xui7at4Mm2YfCWumBZ7': 'file_storage/call_9HxR8Xui7at4Mm2YfCWumBZ7.json'}

exec(code, env_args)
