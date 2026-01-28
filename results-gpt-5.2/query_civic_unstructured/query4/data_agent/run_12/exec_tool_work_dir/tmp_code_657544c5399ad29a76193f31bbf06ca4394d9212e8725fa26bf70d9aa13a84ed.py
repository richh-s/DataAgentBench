code = """import json, re

raw = var_call_hfv6gVDdrgKpYyCiZVl8LQPr
if isinstance(raw, str):
    with open(raw, 'r', encoding='utf-8') as f:
        docs = json.load(f)
else:
    docs = raw

spring2022_projects = set()

bad_substrings = [
    'advertised', 'this date', 'beginning', 'damaged by', 'woolsey',
    'finalizing', 'working on', 'scheduled', 'sending', 'shade structures',
    'timber', 'fire.', 'roadway', 'embankments', 'bid documents', 'public bidding'
]

def looks_like_project(s):
    if len(s) < 5 or len(s) > 120:
        return False
    sl = s.lower()
    if any(b in sl for b in bad_substrings):
        return False
    # likely title case / contains key words
    return bool(re.search(r'(Road|Park|PCH|Canyon|Storm|Drain|Water|Signal|Street|Bridge|Facility|Trail|Playground|Slope|Retaining)', s))

for d in docs:
    lines = d.get('text','').splitlines()
    for i,line in enumerate(lines):
        if re.search(r'Begin Construction\s*:\s*Spring\s+2022', line, re.IGNORECASE):
            j=i-1
            while j>=0:
                cand = lines[j].strip()
                if cand and not cand.startswith('(cid:') and 'project schedule' not in cand.lower() and 'estimated schedule' not in cand.lower() and 'updates' not in cand.lower():
                    if looks_like_project(cand):
                        spring2022_projects.add(cand)
                    break
                j-=1

proj_list = sorted(spring2022_projects)
print('__RESULT__:')
print(json.dumps({"spring_2022_projects": proj_list, "count": len(proj_list)}))"""

env_args = {'var_call_WF7nOmUatVD8vw8PJCkI3sVH': ['Funding'], 'var_call_wRmXiS5fuWvTjHJBViejlb7C': ['civic_docs'], 'var_call_RU0Eeenz3jeZ4nl37lbeV0m4': 'file_storage/call_RU0Eeenz3jeZ4nl37lbeV0m4.json', 'var_call_hfv6gVDdrgKpYyCiZVl8LQPr': 'file_storage/call_hfv6gVDdrgKpYyCiZVl8LQPr.json', 'var_call_HWhFLWT6n0CRM4VBlAo3cr4K': {'spring_2022_projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 14}}

exec(code, env_args)
