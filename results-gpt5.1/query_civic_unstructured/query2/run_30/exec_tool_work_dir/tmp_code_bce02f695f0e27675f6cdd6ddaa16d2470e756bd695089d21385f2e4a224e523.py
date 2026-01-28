code = """import re, json, pandas as pd
from pathlib import Path

# Load full civic docs
path_docs = Path(var_call_0pmWozy7BnV9ZuSLhx77jG7x)
records_docs = json.loads(path_docs.read_text())
texts = [r['text'] for r in records_docs]

# Heuristic: extract lines that look like project entries near 'Park'
project_lines = []
for t in texts:
    for line in t.split('\n'):
        if 'park' in line.lower():
            project_lines.append(line.strip())

# Known pattern: project names are standalone lines, often followed by updates/completion info
# We'll capture some specific park-related project names and note completion year if mentioned
park_projects = {}
current_project = None
for t in texts:
    lines = [l.rstrip() for l in t.split('\n')]
    for i, line in enumerate(lines):
        # Detect a project line containing 'Park'
        if re.search(r'Park', line):
            current_project = line.strip()
            if current_project not in park_projects:
                park_projects[current_project] = {'completed_years': set()}
        if current_project:
            if 'Construction was completed' in line or 'construction was completed' in line.lower():
                # look for a year in the line or nearby lines
                context = ' '.join(lines[max(0,i-1):i+2])
                years = re.findall(r'20[0-9]{2}', context)
                for y in years:
                    park_projects[current_project]['completed_years'].add(y)

# Flatten to list of projects completed in 2022
completed_2022_projects = []
for name, info in park_projects.items():
    if '2022' in info['completed_years']:
        completed_2022_projects.append(name)

# Also look explicitly for lines saying 'Construction was completed, November 2022' and map to previous project name line
explicit_projects_2022 = set(completed_2022_projects)
for t in texts:
    lines = [l.rstrip() for l in t.split('\n')]
    for i, line in enumerate(lines):
        if 'Construction was completed, November 2022' in line:
            # walk backwards to find nearest line that looks like a project name (non-empty, not starting with bullet)
            for j in range(i-1, -1, -1):
                prev = lines[j].strip()
                if prev and not prev.startswith('(') and not prev.startswith('\u2022') and not prev.lower().startswith('updates'):
                    explicit_projects_2022.add(prev)
                    break

completed_2022_projects = sorted(explicit_projects_2022)

# Now load Funding table and sum amounts for matching projects that look park-related and completed in 2022
path_fund = Path(var_call_slWFvpzv7s2d7yxudorroxEW)
records_fund = json.loads(path_fund.read_text())
df = pd.DataFrame(records_fund)
# ensure numeric Amount
df['Amount'] = pd.to_numeric(df['Amount'])

# Determine mapping between extracted project lines and Funding.Project_Name via substring containment either way
funding_total = 0
matched_projects = []
for pname in completed_2022_projects:
    for fproj in df['Project_Name']:
        if pname.lower() in fproj.lower() or fproj.lower() in pname.lower():
            if 'park' in fproj.lower():
                amt = df.loc[df['Project_Name'] == fproj, 'Amount'].sum()
                funding_total += amt
                matched_projects.append({'doc_name': pname, 'fund_project': fproj, 'amount': float(amt)})

result = {'completed_2022_park_projects': completed_2022_projects, 'matched_projects': matched_projects, 'total_funding_park_2022_completed': float(funding_total)}

out = json.dumps(result)
print('__RESULT__:')
print(out)"""

env_args = {'var_call_0pmWozy7BnV9ZuSLhx77jG7x': 'file_storage/call_0pmWozy7BnV9ZuSLhx77jG7x.json', 'var_call_slWFvpzv7s2d7yxudorroxEW': 'file_storage/call_slWFvpzv7s2d7yxudorroxEW.json'}

exec(code, env_args)
