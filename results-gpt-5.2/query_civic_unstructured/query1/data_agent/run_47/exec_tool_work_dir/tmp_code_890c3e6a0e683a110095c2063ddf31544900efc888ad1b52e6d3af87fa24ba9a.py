code = """import json, re
import pandas as pd

# Load civic docs from json file path
path = var_call_ZlyIG70BMoMqpaUG34RJQ2KT
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# Extract project names under section "Capital Improvement Projects (Design)"
projects_design_capital = set()

for d in docs:
    text = d.get('text','') or ''
    # Normalize line breaks
    lines = [ln.strip() for ln in text.splitlines()]
    # Find header line index
    idxs = [i for i,ln in enumerate(lines) if re.search(r'^Capital Improvement Projects\s*\(Design\)\s*$', ln, re.IGNORECASE)]
    for idx in idxs:
        # scan until next "Capital Improvement Projects (" with not Design or until Disaster Recovery Projects
        j = idx+1
        while j < len(lines):
            ln = lines[j].strip()
            if re.search(r'^Capital Improvement Projects\s*\(Construction\)', ln, re.IGNORECASE):
                break
            if re.search(r'^Capital Improvement Projects\s*\(Not Started\)', ln, re.IGNORECASE):
                break
            if re.search(r'^Disaster Recovery Projects', ln, re.IGNORECASE):
                break
            # candidate project line: non-empty, not bullet headers, not 'Updates', not 'Project Schedule', not page markers
            if ln and not re.match(r'^(\(cid:|•|\-|\u2022)', ln) and not re.search(r'^(Updates|Project Schedule|Estimated Schedule|Project Description|Page\s+\d+\s+of\s+\d+|Agenda Item)', ln, re.IGNORECASE):
                # Often project names are standalone lines; exclude lines ending with ':'
                if not ln.endswith(':') and len(ln) <= 120:
                    # exclude obvious non-project lines
                    if not re.search(r'^(To:|Prepared by:|Approved by:|Date prepared:|Meeting date:|Subject:|RECOMMENDED ACTION|DISCUSSION)', ln, re.IGNORECASE):
                        projects_design_capital.add(ln)
            j += 1

# Query funding projects > 50000 distinct names list
# We'll need names to join; fetch from DB

print('__RESULT__:')
print(json.dumps({'projects_design_capital': sorted(projects_design_capital), 'count_design_capital': len(projects_design_capital)}))"""

env_args = {'var_call_plwekHHhqasuFuajAwHtbUgg': [{'cnt': '276'}], 'var_call_ZlyIG70BMoMqpaUG34RJQ2KT': 'file_storage/call_ZlyIG70BMoMqpaUG34RJQ2KT.json'}

exec(code, env_args)
