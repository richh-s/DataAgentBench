code = """import json, re
path = var_call_4fX4CVxqrzrg2HK6TiF57mL4
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

spring_regex = re.compile(r"(Spring\s*2022|Spring,?\s*2022|beginning in Spring 2022|beginning in the Spring of 2022|advertise: Spring 2022|advertise: Spring 2022|Advertise: Spring 2022)", re.IGNORECASE)

title_keywords = ['project','repairs','improvements','park','playground','study','plan','facility','repair','restoration','master plan','skate park','walkway','traffic study','water treatment','green streets','retaining wall','drainage','median','signals','slope','biofilter','trash screens','shade structure','road','bridge','synchronization','resurfacing']

found = []
for doc in docs:
    text = doc.get('text','')
    lines = [ln.rstrip() for ln in text.splitlines()]
    for i,line in enumerate(lines):
        if spring_regex.search(line):
            # search backward for a title within previous 12 non-empty lines
            title = None
            back = 0
            j = i-1
            while j>=0 and back<24:
                l = lines[j].strip()
                j -= 1
                if not l:
                    back += 1
                    continue
                low = l.lower()
                # skip lines that are clearly not titles
                if low.startswith('page') or low.startswith('agenda') or low.startswith('item'):
                    back += 1
                    continue
                if 'updates:' in low or 'project schedule' in low or low.endswith(':'):
                    back += 1
                    continue
                # if contains a keyword, take it
                if any(kw in low for kw in title_keywords):
                    title = re.sub(r"\s+", ' ', l)
                    break
                # heuristics: line with Title Case and few words
                words = l.split()
                if 1 < len(words) <= 10 and sum(1 for w in words if w[0].isupper()) >= 1:
                    title = re.sub(r"\s+", ' ', l)
                    break
                back += 1
            if title:
                found.append(title)

# dedupe preserving order
unique = []
seen = set()
for p in found:
    key = p.lower()
    if key not in seen:
        seen.add(key)
        unique.append(p)

print('__RESULT__:')
print(json.dumps(unique))"""

env_args = {'var_call_w2CjMMHrCINpDfT1q9U0L5Po': ['civic_docs'], 'var_call_8Z022tJgpWErMfAG6q81W7g0': ['Funding'], 'var_call_4fX4CVxqrzrg2HK6TiF57mL4': 'file_storage/call_4fX4CVxqrzrg2HK6TiF57mL4.json', 'var_call_wLZaeaQ7NxPf0C4BLM2c93F1': ['manufacturers for filters that will work in the proposed project area. It is', 'anticipated to have a final design by March 2022. The project will be', 'routed through Caltrans for final approval. It is anticipated that the', 'agreement will be sent to City Council in March.', 'for final approval. It is anticipated that the project will have final', 'project will begin in conjunction with the PCH Median Improvement', 'the project', 'sending this project out to bid during the Spring of 2022.', 'draft plans are expected to be completed in early 2022. The Planning', 'review by the Council.', 'consultant. It is anticipated that this agreement will go to Council in', 'March 2022', 'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'A kick-off meeting was held in late December.', 'project will be advertised for construction bids with construction', 'beginning in April 2022.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'started and is anticipated to be completed by the Spring of 2022.', 'drain towards the end of Clover Heights will help eliminate this issue.', 'that was damaged by the Woolsey Fire.', 'Fire.', 'evaluating the project costs.', 'within the City.', 'final design is complete and the project will be advertised for', 'management services was approved by Council on March 14, 2022.', 'PCH Signal Synchronization System Improvements Project', 'final approval. It is anticipated that the project will have final approval', 'will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'selected a qualified consultant. It is anticipated that the agreement will', 'Metro.', 'damaged by the Woolsey Fire.', 'beginning in Spring 2022.', 'at 24712 Malibu Road has been eroded and caused damage to Malibu Road.', 'the project costs.', 'scheduled for the July 11, 2022 Council meeting.', 'Median Improvement.', 'work related to the project. Staff has worked with the consultant over', 'meeting was held on May 16, 2022 and the design is underway.', 'guardrails within the project limits.', 'The project is currently out to bid with proposals due August 4, 2022.', 'August.', 'evaluating the project costs and calculating each parcels estimated', 'consultants to develop the master plan.', 'to develop the master plan. Proposals are due in September 2021.', 'shade structures at Malibu Bluffs Park.', 'and schedule a kick-off meeting in early December 2021.', 'than the available budget for the project.', 'Caltrans. The project is currently out to bids with bids due December', 'turn lane at the intersection of PCH and Trancas Canyon Road.', 'is working on the project plans to prepare for public bidding.', 'Commission hearing on November 15, 2021.', 'the Public Works Commission to revise the project scope.', 'Westward Beach Road.']}

exec(code, env_args)
