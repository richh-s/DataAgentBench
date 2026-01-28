code = """import json, re
import pandas as pd

# Load civic docs (may be a file path)
docs_src = var_call_TkVPrZucnCTe4WspWeWiKRFr
if isinstance(docs_src, str):
    with open(docs_src, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = docs_src

# Extract project names under Capital Improvement Projects (Design)
projects = set()

def extract_from_text(text: str):
    lines = [ln.strip() for ln in text.splitlines()]
    out = []
    in_design = False
    for ln in lines:
        if re.search(r'^Capital Improvement Projects\s*\(Design\)\s*$', ln, flags=re.I):
            in_design = True
            continue
        if in_design and re.search(r'^Capital Improvement Projects\s*\(Construction\)\s*$', ln, flags=re.I):
            break
        if in_design:
            if not ln:
                continue
            # stop if another major section starts
            if re.match(r'^(Disaster Recovery Projects|RECOMMENDED ACTION:|DISCUSSION:|Page \d+ of \d+|Agenda Item)', ln, flags=re.I):
                continue
            # candidate project line: no bullet marker, not an updates/schedule header
            if re.search(r'^(Updates:|Project Schedule|Estimated Schedule|Project Description:|\(cid:)', ln, flags=re.I):
                continue
            if ':' in ln and len(ln) < 60:
                # likely a label line like "To:"; skip
                continue
            # Heuristic: project names are title-like and not too long
            if 3 <= len(ln) <= 120 and not re.search(r'(Staff|City|Consultant|Complete Design|Advertise|Begin Construction)', ln, flags=re.I):
                # Avoid lines that are clearly narrative sentences
                if not re.search(r'\b(is|are|was|were|will|to|for|and)\b', ln, flags=re.I):
                    out.append(ln)
    return out

for d in docs:
    for pn in extract_from_text(d.get('text','')):
        projects.add(pn)

# Get funding projects > 50k (sum per project)
# Query DB for project-level totals > 50k
# (Cannot call query_db here; approximate using earlier count? We'll compute by loading via separate query outside python.)

result = {
    "design_projects_extracted": sorted(projects),
    "design_project_count_extracted": len(projects)
}
print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_NeEllH8kVvzbzjVCAPjBs0bE': [{'cnt': '276'}], 'var_call_TkVPrZucnCTe4WspWeWiKRFr': 'file_storage/call_TkVPrZucnCTe4WspWeWiKRFr.json'}

exec(code, env_args)
