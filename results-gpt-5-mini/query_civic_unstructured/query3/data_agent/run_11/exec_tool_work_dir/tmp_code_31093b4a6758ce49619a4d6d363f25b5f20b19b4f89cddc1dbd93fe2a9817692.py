code = """import json, re
# Read the civic_docs query result stored in var_call_2ajh9JRnLUZjcgZaBU1zv32y
path = var_call_2ajh9JRnLUZjcgZaBU1zv32y
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects = []
proj_set = set()
# Patterns to identify candidate project lines
proj_keyword_re = re.compile(r"\b(Project|Improvements|Repairs|Repair|Facility|Park|Playground|Study|Plan|Plan:|Master Plan|Walkway|Retaining Wall|Drive|Road)\b", re.I)

for doc in docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for i, ln in enumerate(lines):
        s = ln.strip()
        if not s:
            continue
        # consider lines that are not very long and contain a keyword
        if proj_keyword_re.search(s) and len(s) < 200:
            # context window
            start = max(0, i-2)
            end = min(len(lines), i+8)
            context = '\n'.join(lines[start:end]).lower()
            # check for fema or emergency in context or doc
            if 'fema' in context or 'emergency' in context or 'emergency warning' in context:
                name = s
                # normalize whitespace
                name = re.sub(r'\s+', ' ', name).strip()
                if name not in proj_set:
                    proj_set.add(name)
                    # determine status from context
                    status = None
                    if re.search(r'construction was completed|complete construction|notice of completion|completed,', context):
                        status = 'completed'
                    elif re.search(r'waiting|awaiting|awaiting final|awaiting approval|not started|identified', context):
                        status = 'not started'
                    elif re.search(r'preliminary design|preliminary|working with the consultant to finalize the design|finalize the design|complete design|design phase|design is|project is in the preliminary design|project is in preliminary design', context):
                        status = 'design'
                    elif re.search(r'currently under construction|is currently under construction|begin construction|begin construction:', context):
                        # mark as design (in-progress) if no better match
                        status = 'design'
                    else:
                        # fallback: if doc contains fema and no clear status, set not started
                        status = 'not started'

                    projects.append({'Project_Name': name, 'Status': status, 'Context': context[:400]})

# Also deduplicate and sort
projects = sorted(projects, key=lambda x: x['Project_Name'])

# Print results as JSON string
print("__RESULT__:")
print(json.dumps(projects))"""

env_args = {'var_call_2ajh9JRnLUZjcgZaBU1zv32y': 'file_storage/call_2ajh9JRnLUZjcgZaBU1zv32y.json'}

exec(code, env_args)
