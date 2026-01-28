code = """import json
# load funding table
path = var_call_mbCmLsvprE4E7ueAj3jGLGuz
with open(path, 'r', encoding='utf-8') as f:
    funding = json.load(f)

# Convert amounts to integers and normalize project names
for r in funding:
    try:
        r['Amount'] = int(r['Amount'])
    except:
        try:
            r['Amount'] = int(float(r['Amount']))
        except:
            r['Amount'] = 0
    r['Project_Name_norm'] = r['Project_Name'].strip().lower()

# We'll search for projects that have start scheduled in Spring 2022 from civic docs
civic_path = var_call_4fX4CVxqrzrg2HK6TiF57mL4
with open(civic_path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# crude extraction: find lines containing 'Spring 2022' or 'March 2022' or 'April 2022' or 'May 2022' and capture nearest preceding project-like line
import re
spring_terms = ['spring 2022','march 2022','april 2022','may 2022']
lines_all = []
for doc in docs:
    for ln in doc.get('text','').splitlines():
        lines_all.append(ln.strip())

projects_found = []
for i,ln in enumerate(lines_all):
    low = ln.lower()
    if any(term in low for term in spring_terms):
        # look back for title within 20 lines
        title = None
        for j in range(i-1, max(-1, i-30), -1):
            l = lines_all[j].strip()
            if not l:
                continue
            if len(l.split())>15:
                continue
            if any(k in l.lower() for k in ['updates:','project schedule','project description','agenda','item','page']):
                continue
            # if good candidate
            if any(w in l.lower() for w in ['project','road','park','repairs','improvements','slope','walkway','median','signal','drain','bluffs','broad beach','latigo','trancas']):
                title = l
                break
            # title-case fallback
            words = l.split()
            if 1 < len(words) <= 10 and sum(1 for w in words if w[0].isupper())>=1:
                title = l
                break
        if title:
            projects_found.append(title)

# normalize and dedupe
seen = set()
proj_list = []
for p in projects_found:
    q = p.strip().strip(':-. ') 
    if q.lower() not in seen:
        seen.add(q.lower())
        proj_list.append(q)

# Now try to match to funding table by substring matching
matched = []
unmatched = []
for p in proj_list:
    pnorm = p.lower()
    matches = [r for r in funding if pnorm in r['Project_Name_norm'] or r['Project_Name_norm'] in pnorm]
    if matches:
        for m in matches:
            matched.append({'project_text': p, 'funding_project_name': m['Project_Name'], 'amount': m['Amount']})
    else:
        # try fuzzy substring: check if key nouns match
        nouns = [w for w in re.split(r"[\s,()/-]+", pnorm) if len(w)>4]
        found_any = False
        for r in funding:
            for n in nouns:
                if n in r['Project_Name_norm']:
                    matched.append({'project_text': p, 'funding_project_name': r['Project_Name'], 'amount': r['Amount']})
                    found_any = True
                    break
            if found_any:
                break
        if not found_any:
            unmatched.append(p)

# aggregate unique funding projects and total amount
funding_by_project = {}
for m in matched:
    key = m['funding_project_name']
    funding_by_project.setdefault(key, 0)
    funding_by_project[key] += m['amount']

result = {
    'extracted_projects_count': len(proj_list),
    'extracted_projects': proj_list,
    'matched_count': len(funding_by_project),
    'matched_projects': funding_by_project,
    'total_matched_funding': sum(funding_by_project.values()),
    'unmatched_projects': unmatched
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_w2CjMMHrCINpDfT1q9U0L5Po': ['civic_docs'], 'var_call_8Z022tJgpWErMfAG6q81W7g0': ['Funding'], 'var_call_4fX4CVxqrzrg2HK6TiF57mL4': 'file_storage/call_4fX4CVxqrzrg2HK6TiF57mL4.json', 'var_call_wLZaeaQ7NxPf0C4BLM2c93F1': ['manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'A kick-off meeting was held in late December.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'started and is anticipated to be completed by the Spring of 2022.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'within the City.', 'final design is complete and the project will be advertised for', 'management services was approved by Council on March 14, 2022.', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'the project costs.', 'scheduled for the July 11, 2022 Council meeting.', 'Median Improvement.', 'work related to the project. Staff has worked with the consultant over', 'meeting was held on May 16, 2022 and the design is underway.', 'guardrails within the project limits.', 'The project is currently out to bid with proposals due August 4, 2022.', 'August.', 'evaluating the project costs and calculating each parcels estimated', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', 'shade structures at Malibu Bluffs Park.', 'and schedule a kick-off meeting in early December 2021.', 'than the available budget for the project.', 'Caltrans. The project is currently out to bids with bids due December', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'is working on the project plans to prepare for public bidding.', 'Commission hearing on November 15, 2021.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.'], 'var_call_Q6DaVeLL41zbH0QWuvOPxtte': ['(cid:131) Complete Design: March 2022', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'sending this project out to bid during the Spring of 2022.', '(cid:131) Complete Design: Spring 2022', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'March 2022', '(cid:131) Complete Design: February 2022', '(cid:131) The project consultant has started the design of this project.', 'A kick-off meeting was held in late December.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', '(cid:131) The City has hired a consultant to design this project. The design has', 'intersection floods and causes debris to block the road. An extended storm', '(cid:131) Complete Design: Winter 2021', 'within the City.', 'will begin in conjunction with the PCH Median Improvement', '(cid:131) Staff reviewed proposals for engineering design services and has', '(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', 'project will be advertised for construction bids with construction', '(cid:131) The project design has begun and preliminary design should be', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'Median Improvement.', 'work related to the project. Staff has worked with the consultant over', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', '(cid:131) Complete Design: Winter 2021/2022', 'shade structures at Malibu Bluffs Park.', 'and schedule a kick-off meeting in early December 2021.', 'Caltrans. The project is currently out to bids with bids due December', '(cid:131) Complete Design: January 2022', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.'], 'var_call_XhmxAPDCg3vjtN4xtiuuZwCB': ['(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: February 2022', 'project will be advertised for construction bids with construction', '(cid:131) Complete Design: December 2021', '(cid:131) Complete Design: Winter 2021', '(cid:131) Advertise for Bidding: December 2022', '(cid:131) Advertise: Spring 2022', '(cid:131) Complete Design: Fall 2022', '(cid:131) Complete Design: Winter 2021/2022', '(cid:131) Complete Design: Winter 2022', '(cid:131) Advertise: Winter 2022', '(cid:131) Complete Design: Spring 2023', '(cid:131) Complete Design: January 2022', '(cid:131) Advertise: February 2022'], 'var_call_qFDaXHmMqfzSGh0Xwayx64LQ': ['anticipated to have a final design by March 2022. The project will be', 'sending this project out to bid during the Spring of 2022.', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'project will be advertised for construction bids with construction', 'facilities and roadway embankments that were damaged by the Woolsey', 'evaluating the project costs.', 'the project costs.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'evaluating the project costs and calculating each parcels estimated', 'shade structures at Malibu Bluffs Park.', 'is working on the project plans to prepare for public bidding.'], 'var_call_mbCmLsvprE4E7ueAj3jGLGuz': 'file_storage/call_mbCmLsvprE4E7ueAj3jGLGuz.json'}

exec(code, env_args)
