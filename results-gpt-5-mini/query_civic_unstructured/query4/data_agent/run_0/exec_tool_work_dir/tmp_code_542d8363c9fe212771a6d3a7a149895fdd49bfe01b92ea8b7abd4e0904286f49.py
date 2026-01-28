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
        # detect spring 2022 mentions or March/April/May 2022
        if ('2022' in low) and (('spring' in low) or any(m in low for m in ['march','april','may'])):
            # ensure it's about beginning/advertise/begin construction or similar
            if not any(k in low for k in ['begin','advertise','advertised','start','started','began']):
                # still consider but give lower priority; we'll still try to extract nearby
                pass
            # search upward for title
            title = None
            for j in range(i-1, max(-1, i-13), -1):
                if j<0: break
                cand = lines[j].strip()
                if not cand: continue
                lowc = cand.lower()
                # skip template lines
                if lowc.startswith('(cid:') or lowc.startswith('page') or lowc.startswith('agenda'):
                    continue
                if any(skip in lowc for skip in ['project schedule','project description','updates','estimated schedule','recommend','agenda item']):
                    continue
                # accept if contains keywords
                if any(k in lowc for k in ['project','park','road','repair','improvements','study','facility','treatment','playground','walkway','median','drain','slope','retaining','signal','skate','green streets','water quality','resurfacing','repairs','rehab']):
                    title = cand
                    break
                # accept short title-case lines
                words = cand.split()
                if len(words)>=2 and len(words)<=7 and all(w[0].isupper() or (w.isupper()) or (w[0].isdigit()) for w in words if len(w)>0):
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

env_args = {'var_call_zPiRFhL3SBrfqfEgEhKn3UKe': 'file_storage/call_zPiRFhL3SBrfqfEgEhKn3UKe.json', 'var_call_7q0fOOmg9lDBZgyamUdO6zCn': ['(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Staff is currently working on the design of the project and anticipates', '(cid:131) The City has hired a consultant to design this project. The design has', '(cid:131) The project consultant has started the design of this project.', '(cid:131) The project design has begun and preliminary design should be', '(cid:190) Estimated Schedule:', '(cid:190) Project Description: The existing slope adjacent to the beach access stairs', '(cid:190) Project Description: The project consists of repairs the damaged shoulder on', '(cid:190) Project Description: This project consists of repairing damage storm drain', '(cid:190) Project Description: This project consists of the installation of four single-post', '(cid:190) Project Schedule', '(cid:190) Project Schedule:', 'Commission will then review the project in Spring 2022 before final', 'Commission will then review the project in Summer 2022 before final', 'anticipated to have a final design by March 2022. The project will be', 'approval by March 2022. The project will be advertised for construction', 'by March 2022. The project will be advertised for construction bids', 'construction of this project will begin in coordination with the PCH', 'for final approval. It is anticipated that the project will have final', 'is working on the project plans to prepare for public bidding.', 'project report and plans have been approved and final plans by', 'project will be advertised for construction bids with construction', 'project will begin in conjunction with the PCH Median Improvement', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'the Public Works Commission to revise the project scope.', 'the project', 'work related to the project. Staff has worked with the consultant over'], 'var_call_rMNESUQQ7jlg0ox6RNJGH9MP': ['anticipated to have a final design by March 2022. The project will be', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'shade structures at Malibu Bluffs Park.', 'sending this project out to bid during the Spring of 2022.', 'work related to the project. Staff has worked with the consultant over', 'Commission will then review the project in Spring 2022 before final', 'March 2022', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'facilities and roadway embankments that were damaged by the Woolsey', 'drains, culverts, debris basins, manholes, and other drainage structures', 'will begin in conjunction with the PCH Median Improvement', 'Metro.', 'project will be advertised for construction bids with construction', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'Median Improvement.', 'Commission will then review the project in Summer 2022 before final', 'August.', 'Caltrans. The project is currently out to bids with bids due December', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'is working on the project plans to prepare for public bidding.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.']}

exec(code, env_args)
