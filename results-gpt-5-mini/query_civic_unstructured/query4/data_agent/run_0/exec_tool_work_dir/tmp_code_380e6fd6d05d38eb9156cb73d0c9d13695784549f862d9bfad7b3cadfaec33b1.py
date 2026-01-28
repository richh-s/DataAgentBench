code = """import json
from pathlib import Path
p = Path(var_call_zPiRFhL3SBrfqfEgEhKn3UKe)
data = json.loads(p.read_text())
projects = []
for doc in data:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for i,ln in enumerate(lines):
        low = ln.lower()
        if 'spring' in low and '2022' in low:
            # search upward for a project title within 8 lines
            title = None
            for j in range(i-1, max(-1, i-9), -1):
                if j<0: break
                cand = lines[j].strip()
                if not cand: continue
                if cand.lower().startswith('(cid:'): continue
                # ignore generic headings
                if cand.lower().startswith('project schedule') or cand.lower().startswith('updates') or cand.lower().startswith('agenda item') or cand.lower().startswith('page'):
                    continue
                # if line contains words like 'project' or common nouns, accept
                if any(k in cand.lower() for k in ['project','park','road','repair','improvements','study','facility','treatment','playground','walkway','median','drain','slope','retaining','signal','skate','green streets','water quality']):
                    title = cand
                    break
                # also accept lines in Title Case with multiple words
                if len(cand.split())<=6 and len(cand)>5 and cand[0].isupper():
                    title = cand
                    break
            if title:
                projects.append(title)
# deduplicate preserving order
seen = set()
clean = []
for p in projects:
    s = ' '.join(p.split())
    if s not in seen:
        clean.append(s)
        seen.add(s)

print('__RESULT__:')
print(json.dumps(clean))"""

env_args = {'var_call_zPiRFhL3SBrfqfEgEhKn3UKe': 'file_storage/call_zPiRFhL3SBrfqfEgEhKn3UKe.json', 'var_call_7q0fOOmg9lDBZgyamUdO6zCn': ['(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Staff is currently working on the design of the project and anticipates', '(cid:131) The City has hired a consultant to design this project. The design has', '(cid:131) The project consultant has started the design of this project.', '(cid:131) The project design has begun and preliminary design should be', '(cid:190) Estimated Schedule:', '(cid:190) Project Description: The existing slope adjacent to the beach access stairs', '(cid:190) Project Description: The project consists of repairs the damaged shoulder on', '(cid:190) Project Description: This project consists of repairing damage storm drain', '(cid:190) Project Description: This project consists of the installation of four single-post', '(cid:190) Project Schedule', '(cid:190) Project Schedule:', 'Commission will then review the project in Spring 2022 before final', 'Commission will then review the project in Summer 2022 before final', 'anticipated to have a final design by March 2022. The project will be', 'approval by March 2022. The project will be advertised for construction', 'by March 2022. The project will be advertised for construction bids', 'construction of this project will begin in coordination with the PCH', 'for final approval. It is anticipated that the project will have final', 'is working on the project plans to prepare for public bidding.', 'project report and plans have been approved and final plans by', 'project will be advertised for construction bids with construction', 'project will begin in conjunction with the PCH Median Improvement', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'the Public Works Commission to revise the project scope.', 'the project', 'work related to the project. Staff has worked with the consultant over']}

exec(code, env_args)
