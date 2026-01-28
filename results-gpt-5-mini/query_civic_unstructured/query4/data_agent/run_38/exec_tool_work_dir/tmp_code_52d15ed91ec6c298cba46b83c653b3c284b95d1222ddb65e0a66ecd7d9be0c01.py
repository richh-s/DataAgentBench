code = """import json, re
path = var_call_4fX4CVxqrzrg2HK6TiF57mL4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

# patterns indicating start in spring 2022
start_patterns = [r"begin(ning)? in (the )?spring of 2022", r"begin(ning)? in spring 2022", r"begin(ning)? in (April|March|May) 2022", r"begin(ning)? in (Apr|Mar|May) 2022", r"begin construction: (spring|march|april|may) 2022", r"begin construction: spring 2022", r"begin construction: april 2022", r"begin construction: march 2022", r"begin construction: may 2022", r"begin construction: spring 2023"]
start_regex = re.compile("(" + ")|(".join(start_patterns) + ")", re.IGNORECASE)

# also catch Advertise: Spring 2022 followed by Begin Construction: Summer or Begin Construction: Spring
# but we focus on explicit begin construction in spring or phrasing "beginning in April 2022" etc.

project_title_pattern = re.compile(r"^[A-Za-z0-9\-\'\(\)\,\./& ]{3,120}$")

found = []
for doc in docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for i,line in enumerate(lines):
        if start_regex.search(line):
            # search backward up to 20 lines for a plausible project title
            title = None
            for j in range(i-1, max(-1, i-40), -1):
                l = lines[j].strip()
                if not l:
                    continue
                low = l.lower()
                if low.startswith('page') or low.startswith('agenda') or low.startswith('item'):
                    continue
                if any(x in low for x in ['updates:', 'project schedule', 'project description', 'project updates', 'estimated schedule', 'project is', 'updates:']):
                    continue
                # Heuristic: Lines that look like project titles often are Title Case or contain keywords
                if any(kw in low for kw in ['project','park','road','repairs','improvements','study','plan','treatment','retaining','slope','walkway','skate park','median','signal','synchronization','resurfacing']):
                    title = re.sub(r"\s+", ' ', l)
                    break
                # fallback: reasonably short line with uppercase letters
                words = l.split()
                if 1 < len(words) <= 10 and sum(1 for w in words if w[0].isupper()) >= 1:
                    title = re.sub(r"\s+", ' ', l)
                    break
            if title:
                found.append(title)

# dedupe preserving order
unique = []
seen = set()
for p in found:
    key = p.strip().lower()
    if key not in seen:
        seen.add(key)
        unique.append(p.strip())

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_w2CjMMHrCINpDfT1q9U0L5Po': ['civic_docs'], 'var_call_8Z022tJgpWErMfAG6q81W7g0': ['Funding'], 'var_call_4fX4CVxqrzrg2HK6TiF57mL4': 'file_storage/call_4fX4CVxqrzrg2HK6TiF57mL4.json', 'var_call_wLZaeaQ7NxPf0C4BLM2c93F1': ['manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'A kick-off meeting was held in late December.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'started and is anticipated to be completed by the Spring of 2022.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'within the City.', 'final design is complete and the project will be advertised for', 'management services was approved by Council on March 14, 2022.', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'the project costs.', 'scheduled for the July 11, 2022 Council meeting.', 'Median Improvement.', 'work related to the project. Staff has worked with the consultant over', 'meeting was held on May 16, 2022 and the design is underway.', 'guardrails within the project limits.', 'The project is currently out to bid with proposals due August 4, 2022.', 'August.', 'evaluating the project costs and calculating each parcels estimated', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', 'shade structures at Malibu Bluffs Park.', 'and schedule a kick-off meeting in early December 2021.', 'than the available budget for the project.', 'Caltrans. The project is currently out to bids with bids due December', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'is working on the project plans to prepare for public bidding.', 'Commission hearing on November 15, 2021.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.'], 'var_call_Q6DaVeLL41zbH0QWuvOPxtte': ['(cid:131) Complete Design: March 2022', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'sending this project out to bid during the Spring of 2022.', '(cid:131) Complete Design: Spring 2022', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'March 2022', '(cid:131) Complete Design: February 2022', '(cid:131) The project consultant has started the design of this project.', 'A kick-off meeting was held in late December.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', '(cid:131) The City has hired a consultant to design this project. The design has', 'intersection floods and causes debris to block the road. An extended storm', '(cid:131) Complete Design: Winter 2021', 'within the City.', 'will begin in conjunction with the PCH Median Improvement', '(cid:131) Staff reviewed proposals for engineering design services and has', '(cid:131) Complete Design: April 2022', '(cid:131) Advertise: Spring 2022', 'project will be advertised for construction bids with construction', '(cid:131) The project design has begun and preliminary design should be', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'Median Improvement.', 'work related to the project. Staff has worked with the consultant over', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', '(cid:131) Complete Design: Winter 2021/2022', 'shade structures at Malibu Bluffs Park.', 'and schedule a kick-off meeting in early December 2021.', 'Caltrans. The project is currently out to bids with bids due December', '(cid:131) Complete Design: January 2022', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.']}

exec(code, env_args)
