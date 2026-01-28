code = """import json, re
from pathlib import Path

# Load civic docs
with open(var_call_ZGxPsl3QZckLx5Aftdn8Sa0X, 'r') as f:
    civic_docs = json.load(f)

# Load funding
with open(var_call_vzEtHYEO2mxMyHPnsAC47tFQ, 'r') as f:
    funding_records = json.load(f)

# Build funding dict map from project name to amount (sum if multiple entries for same name)
funding_map = {}
for rec in funding_records:
    name = rec.get('Project_Name')
    amt = rec.get('Amount')
    try:
        val = int(amt)
    except Exception:
        try:
            val = int(float(amt))
        except Exception:
            val = 0
    funding_map[name] = funding_map.get(name, 0) + val

# Helper to find a plausible project title line above a given index

def find_project_title(lines, idx):
    # Look upward up to 10 lines
    for j in range(idx-1, max(-1, idx-11), -1):
        line = lines[j].strip()
        if not line:
            continue
        # Skip obvious non-title lines
        low = line.lower()
        if low.startswith('updates') or low.startswith('project schedule') or low.startswith('estimated schedule') or low.startswith('project description'):
            continue
        if ':' in line:
            # lines with colon are likely descriptions/labels
            continue
        # Skip section headers
        if 'capital improvement projects' in low or 'disaster recovery projects' in low:
            continue
        # Skip page/agenda items
        if 'agenda item' in low or 'page ' in low:
            continue
        # Very long lines likely not titles
        if len(line) > 120:
            continue
        # Titles often look like Title Case or all caps words; accept
        return line
    return None

# Extract projects completed in 2022
park_related_projects_2022 = set()
pattern_completed_2022 = re.compile(r'\bcompleted\b', re.IGNORECASE)
pattern_year_2022 = re.compile(r'2022')

for doc in civic_docs:
    text = doc.get('text', '')
    # Normalize to lines
    lines = text.split('\n')
    for i, line in enumerate(lines):
        if pattern_completed_2022.search(line) and pattern_year_2022.search(line):
            # Found a line indicating completed in 2022
            title = find_project_title(lines, i)
            if not title:
                continue
            # Determine park-related by keywords in title
            title_low = title.lower()
            if ('park' in title_low) or ('playground' in title_low):
                park_related_projects_2022.add(title)

# Sum funding for these projects
total_funding = 0
missing_in_funding = []
for proj in sorted(park_related_projects_2022):
    if proj in funding_map:
        total_funding += funding_map[proj]
    else:
        # try matching variations: remove trailing words like 'project', 'repairs', etc? But we'll attempt case-insensitive exact
        # also try to match funding names that include extra qualifiers like '(FEMA Project)'
        # We'll try to find funding records that start with the project name
        matches = [name for name in funding_map.keys() if name.lower() == proj.lower() or name.lower().startswith(proj.lower())]
        if matches:
            total = sum(funding_map[m] for m in matches)
            total_funding += total
        else:
            missing_in_funding.append(proj)

result = {
    'park_completed_2022_projects': sorted(list(park_related_projects_2022)),
    'total_funding': total_funding,
    'missing_in_funding': missing_in_funding
}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_ZGxPsl3QZckLx5Aftdn8Sa0X': 'file_storage/call_ZGxPsl3QZckLx5Aftdn8Sa0X.json', 'var_call_vzEtHYEO2mxMyHPnsAC47tFQ': 'file_storage/call_vzEtHYEO2mxMyHPnsAC47tFQ.json'}

exec(code, env_args)
