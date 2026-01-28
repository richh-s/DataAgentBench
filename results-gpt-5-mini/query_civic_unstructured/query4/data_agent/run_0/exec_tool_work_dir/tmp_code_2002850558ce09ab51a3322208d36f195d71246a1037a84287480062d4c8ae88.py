code = """import json
from pathlib import Path
p = Path(var_call_zPiRFhL3SBrfqfEgEhKn3UKe)
data = json.loads(p.read_text())
keywords = ['project','park','road','study','facility','improvements','repair','repairs','restoration','treatment','improvement','walkway','playground','resurfacing','retaining wall','signal','skate','green streets','water quality','walkway','traffic study','median','drainage','slope','bluffs','canyon','storm drain','water','bridge']
start_terms = ['spring']
action_terms = ['begin','began','start','started']
found = []
for doc in data:
    text = doc.get('text','')
    lines = [ln.strip() for ln in text.splitlines()]
    curr = None
    for i,ln in enumerate(lines):
        low = ln.lower()
        # detect title lines
        if any(k in low for k in keywords) and len(ln)>2 and not low.startswith('(cid:'):
            # treat as potential project title
            curr = ln
            continue
        if curr:
            # look ahead in next few lines for spring 2022 with action
            look_range = lines[i:i+8]
            for l in look_range:
                ll = l.lower()
                if '2022' in ll and 'spring' in ll:
                    # require action term near
                    if any(a in ll for a in action_terms):
                        found.append(curr)
                        curr = None
                        break
            # also check current line i if contains spring 2022 and action
            if '2022' in low and 'spring' in low and any(a in low for a in action_terms):
                found.append(curr)
                curr = None
# deduplicate and clean
cleaned = []
seen = set()
for f in found:
    s = ' '.join(f.split())
    if s not in seen:
        cleaned.append(s)
        seen.add(s)

print('__RESULT__:')
print(json.dumps(cleaned))"""

env_args = {'var_call_zPiRFhL3SBrfqfEgEhKn3UKe': 'file_storage/call_zPiRFhL3SBrfqfEgEhKn3UKe.json', 'var_call_7q0fOOmg9lDBZgyamUdO6zCn': ['(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Staff is currently working on the design of the project and anticipates', '(cid:131) The City has hired a consultant to design this project. The design has', '(cid:131) The project consultant has started the design of this project.', '(cid:131) The project design has begun and preliminary design should be', '(cid:190) Estimated Schedule:', '(cid:190) Project Description: The existing slope adjacent to the beach access stairs', '(cid:190) Project Description: The project consists of repairs the damaged shoulder on', '(cid:190) Project Description: This project consists of repairing damage storm drain', '(cid:190) Project Description: This project consists of the installation of four single-post', '(cid:190) Project Schedule', '(cid:190) Project Schedule:', 'Commission will then review the project in Spring 2022 before final', 'Commission will then review the project in Summer 2022 before final', 'anticipated to have a final design by March 2022. The project will be', 'approval by March 2022. The project will be advertised for construction', 'by March 2022. The project will be advertised for construction bids', 'construction of this project will begin in coordination with the PCH', 'for final approval. It is anticipated that the project will have final', 'is working on the project plans to prepare for public bidding.', 'project report and plans have been approved and final plans by', 'project will be advertised for construction bids with construction', 'project will begin in conjunction with the PCH Median Improvement', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'the Public Works Commission to revise the project scope.', 'the project', 'work related to the project. Staff has worked with the consultant over']}

exec(code, env_args)
