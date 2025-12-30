code = """import re, json, pandas as pd

# Load funding data
funding_records = var_call_Ma5tzcHh7AtnFIeI1BzXuZYK
funding_df = pd.DataFrame(funding_records)

# Normalize project name for joining
funding_df['Project_Name_norm'] = funding_df['Project_Name'].str.strip().str.lower()

# We will parse civic docs text into structured projects with name and status/type
civic_docs = var_call_T716yBXVNBl6HPnJ4BbqHEAY

projects = []
for doc in civic_docs:
    text = doc.get('text', '')
    # Simple heuristic: sections under headings like 'Capital Improvement Projects (Design)' etc.
    # Mark current status context
    current_status = None
    current_type = None
    for line in text.split('\n'):
        l = line.strip()
        if not l:
            continue
        lower = l.lower()
        if 'capital improvement projects' in lower:
            current_type = 'capital'
            if '(design)' in lower:
                current_status = 'design'
            elif '(construction)' in lower:
                current_status = 'completed'
            elif '(not started)' in lower:
                current_status = 'not started'
            continue
        # also some disaster projects could be in same report but question is about capital
        if current_type == 'capital' and current_status is not None:
            # Try to detect project name lines: skip narrative lines with 'updates', 'project schedule', etc.
            if re.match(r'^[A-Z0-9].*', l) and not any(word in lower for word in ['update', 'schedule', 'project description', 'agenda item', 'page ']):
                # Filter out headings that are not project names by simple heuristics
                if len(l.split()) <= 2 and 'project' not in lower and 'park' not in lower and 'road' not in lower and 'lane' not in lower and 'repairs' not in lower and 'improvements' not in lower and 'warning' not in lower and 'playground' not in lower and 'study' not in lower and 'facility' not in lower:
                    continue
                projects.append({
                    'Project_Name': l.strip(),
                    'status': current_status,
                    'type': current_type
                })

projects_df = pd.DataFrame(projects).drop_duplicates()
projects_df['Project_Name_norm'] = projects_df['Project_Name'].str.strip().str.lower()

# Join with funding where amount > 50000 (already filtered in SQL)
merged = pd.merge(funding_df, projects_df, on='Project_Name_norm', how='inner', suffixes=('_fund', '_proj'))

# Filter for capital type and design status
design_capital = merged[(merged['type'] == 'capital') & (merged['status'] == 'design')]

result_count = int(design_capital['Project_Name_norm'].nunique())

print("__RESULT__:")
print(json.dumps(result_count))"""

env_args = {'var_call_Ma5tzcHh7AtnFIeI1BzXuZYK': 'file_storage/call_Ma5tzcHh7AtnFIeI1BzXuZYK.json', 'var_call_T716yBXVNBl6HPnJ4BbqHEAY': 'file_storage/call_T716yBXVNBl6HPnJ4BbqHEAY.json'}

exec(code, env_args)
