code = """import json, re
import pandas as pd

path = var_call_rqk86h5PbRqU7Jnxdv2SDM7u
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract project names under sections that indicate Design status
# Heuristic: find blocks following 'Capital Improvement Projects (Design)' or 'Disaster Recovery Projects (Design)'
section_pat = re.compile(r'(Capital Improvement Projects \(Design\)|Disaster Recovery Projects \(Design\))\s*(.*?)(?=\n\s*(Capital Improvement Projects \(|Disaster Recovery Projects \(|Page \d+ of \d+|Agenda Item|\Z))', re.S|re.I)

projects=set()
for d in docs:
    text=d.get('text','') or ''
    for m in section_pat.finditer(text):
        block=m.group(2)
        # project names appear as standalone lines (not bullets) followed by blank line and then updates
        for line in block.splitlines():
            line=line.strip()
            if not line:
                continue
            # skip bullets/labels
            if line.startswith(('(cid', 'Updates', 'Project Schedule', 'Estimated Schedule', 'Project Description', 'RECOMMENDED', 'DISCUSSION', 'To:', 'Prepared by', 'Approved by', 'Date prepared', 'Meeting date', 'Subject:')):
                continue
            # likely project title: mostly letters/numbers/& and not too long
            if len(line) < 3 or len(line) > 120:
                continue
            if re.match(r'^[\W_]+$', line):
                continue
            # exclude schedule lines containing ':'
            if ':' in line:
                continue
            # Exclude lines that are clearly sentences
            if line.endswith('.'):
                continue
            # keep if contains at least one letter and not start with 'Page'
            if re.search(r'[A-Za-z]', line) and not line.lower().startswith('page '):
                projects.add(line)

# Get funded projects > 50k
funded = functions.query_db(db_name='funding_database', query='SELECT DISTINCT Project_Name FROM Funding WHERE Amount > 50000;')
funded_set=set(r['Project_Name'] for r in funded)

# Intersect
count = len(projects & funded_set)

print('__RESULT__:')
print(json.dumps({'design_projects_count_over_50000': count, 'n_design_projects_extracted': len(projects)}))"""

env_args = {'var_call_tFCzG6Ku9PapCLRhaw4QyROM': [{'cnt': '276'}], 'var_call_rqk86h5PbRqU7Jnxdv2SDM7u': 'file_storage/call_rqk86h5PbRqU7Jnxdv2SDM7u.json'}

exec(code, env_args)
