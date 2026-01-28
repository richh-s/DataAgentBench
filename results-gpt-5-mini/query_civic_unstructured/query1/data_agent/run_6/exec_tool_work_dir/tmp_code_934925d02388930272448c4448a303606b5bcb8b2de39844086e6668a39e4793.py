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
    # Find the Design section until the next major subsection
    m = re.search(r'Capital Improvement Projects\s*\(Design\)(.*?)(?:Capital Improvement Projects\s*\(Construction\)|Capital Improvement Projects\s*\(Not Started\)|Capital Improvement Projects\s*\(|Capital Improvement Projects|$)', text, re.S | re.I)
    if not m:
        continue
    chunk = m.group(1)
    # Split into lines and look for lines that look like project titles
    lines = [line.strip() for line in chunk.splitlines()]
    for i, line in enumerate(lines):
        if not line:
            continue
        # Heuristics: project lines are shorter than 200 chars and often Title Case or contain numbers
        if len(line) > 200:
            continue
        # Skip obvious non-title lines
        low = line.lower()
        if low.startswith('(cid') or low.startswith('updates:') or low.startswith('project schedule:'):
            continue
        if any(kw in low for kw in ['prepared by', 'approved by', 'date prepared', 'meeting date', 'recommended action', 'discussion']):
            continue
        # If the line contains verbs indicating sentences, skip unless it ends with 'Project' or contains common project keywords
        if re.search(r'\b(is|are|will|staff|working|plans|projected|submitted|complete|advertise|begin|design)\b', low) and 'project' not in low and 'improvements' not in low and 'repairs' not in low and 'improvement' not in low:
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

output = {'count': count_over_50000, 'projects_over_50000': projects_over_50000}

print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_KR7TJInlrgL5ul9zLeO5DE1h': ['civic_docs'], 'var_call_ZzN4zoXVJbIgtrVQCiQ2luo3': ['Funding'], 'var_call_6FsTuhWZB0dRWwswUanAjfgK': 'file_storage/call_6FsTuhWZB0dRWwswUanAjfgK.json', 'var_call_9HxR8Xui7at4Mm2YfCWumBZ7': 'file_storage/call_9HxR8Xui7at4Mm2YfCWumBZ7.json'}

exec(code, env_args)
