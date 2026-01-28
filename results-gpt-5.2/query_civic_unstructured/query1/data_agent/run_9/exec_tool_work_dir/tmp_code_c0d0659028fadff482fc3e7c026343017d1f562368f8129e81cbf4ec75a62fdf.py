code = """import json, re, pandas as pd

# Load mongo docs (may be a filepath)
raw = var_call_Bz6lqWzcVUo8LbpjrAZux08D
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

# Extract project names under 'Capital Improvement Projects (Design)'
projects = set()
for d in docs:
    text = d.get('text','') or ''
    lines = [ln.strip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        if re.search(r'Capital Improvement Projects\s*\(Design\)', ln, re.I):
            # Collect subsequent non-empty lines until next section header
            j = i+1
            while j < len(lines):
                l = lines[j].strip()
                if re.search(r'Capital Improvement Projects\s*\((Construction|Not Started)\)', l, re.I) or re.search(r'Disaster Recovery Projects', l, re.I):
                    break
                # Likely project name line: avoid bullets/labels
                if l and not re.match(r'^(\(cid:|[\u2022\-\*]|Updates:|Project Schedule|Estimated Schedule|Final Design|Complete Design|Advertise|Begin Construction|Complete Construction|Project Description|Discussion:|RECOMMENDED ACTION|To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|Page\s+\d+\s+of\s+\d+|Agenda Item)', l, re.I):
                    # exclude lines with colon (labels)
                    if ':' not in l and len(l) > 3:
                        projects.add(l)
                j += 1

# Query funding for those projects > 50000
proj_list = sorted(projects)

# If none found, answer 0
if not proj_list:
    ans = 0
else:
    # Build SQL IN clause safely by escaping single quotes
    in_clause = ','.join(["'" + p.replace("'","''") + "'" for p in proj_list])
    sql = f"SELECT COUNT(DISTINCT Project_Name) AS cnt FROM Funding WHERE Amount > 50000 AND Project_Name IN ({in_clause});"
    # Can't query DB from python; instead compute by joining with funding table already? Not available.
    # So output project list and sql for next tool call.
    ans = {"projects": proj_list, "sql": sql}

print('__RESULT__:')
print(json.dumps(ans))"""

env_args = {'var_call_FL3Kk0SESyZGElJMufJ26n8u': [{'cnt': '276'}], 'var_call_Bz6lqWzcVUo8LbpjrAZux08D': 'file_storage/call_Bz6lqWzcVUo8LbpjrAZux08D.json'}

exec(code, env_args)
