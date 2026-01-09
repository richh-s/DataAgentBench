code = """import json, re
import pandas as pd

path = var_call_0IOfBTuzQ6xbjdLixQphJanm
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Find blocks like: <Project Name> ... Project Schedule: ... Begin Construction: <when>
# We'll extract the Begin Construction value if present and mark as start.
projects = []
for d in docs:
    text = d.get('text','')
    # Normalize bullets and whitespace
    t = text.replace('\r','')
    # Split into lines for easier parsing
    lines = [ln.strip() for ln in t.split('\n')]
    # We'll look for project headings: lines that are non-empty and not too long, and followed soon by 'Updates:'
    for i, ln in enumerate(lines):
        if not ln or len(ln) > 120: 
            continue
        if ln.lower() in {'capital improvement projects (design)','capital improvement projects (construction)','capital improvement projects (not started)','disaster recovery projects (design)','disaster recovery projects (construction)','disaster recovery projects (not started)'}:
            continue
        # detect heading by presence of nearby 'Updates:' within next 5 lines
        window = '\n'.join(lines[i:i+8]).lower()
        if 'updates' in window and ('project schedule' in window or 'estimated schedule' in window):
            # candidate name
            name = ln
            # search in next 60 lines until blank line separating next project
            chunk = '\n'.join(lines[i:i+80])
            m = re.search(r'Begin\s+Construction\s*:\s*([^\n]+)', chunk, flags=re.IGNORECASE)
            if m:
                start = m.group(1).strip()
                projects.append({'Project_Name': name, 'start_raw': start, 'filename': d.get('filename')})

# Deduplicate by project name keeping earliest mention
df = pd.DataFrame(projects)
if df.empty:
    out = {'count': 0, 'total_funding': 0, 'projects': []}
else:
    df = df.drop_duplicates(subset=['Project_Name'], keep='first')
    # Identify Spring 2022 starts. Match explicit 'Spring 2022' or 'Spring, 2022' or 'Spring 2022.'
    mask = df['start_raw'].str.contains(r'\bSpring\b\s*,?\s*2022\b', case=False, regex=True, na=False)
    spring2022 = df[mask].copy()

    proj_names = spring2022['Project_Name'].tolist()

    # Query funding for these projects
    # Build SQL IN clause safely by escaping single quotes
    def esc(s):
        return s.replace("'","''")
    in_list = ','.join([f"'{esc(n)}'" for n in proj_names]) if proj_names else "''"
    sql = f"SELECT Project_Name, SUM(Amount) AS total_amount FROM Funding WHERE Project_Name IN ({in_list}) GROUP BY Project_Name;"

    # can't run query_db here; just output names and sql
    out = {'project_names': proj_names, 'funding_sql': sql, 'n_projects': int(len(proj_names))}

print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_cIwF1DzZYyGVbJgRQXIZE4Sd': ['Funding'], 'var_call_38K6ah1O9g5pFFoNyAINarzm': ['civic_docs'], 'var_call_0IOfBTuzQ6xbjdLixQphJanm': 'file_storage/call_0IOfBTuzQ6xbjdLixQphJanm.json'}

exec(code, env_args)
