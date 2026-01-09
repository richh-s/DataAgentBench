code = """import json, re

path = var_call_rn7TZs6Br9Hucjj0u18Fvagq
with open(path, 'r', encoding='utf-8') as f:
    docs = json.load(f)

projects=set()
for d in docs:
    lines = d.get('text','').splitlines()
    for i, line in enumerate(lines):
        if re.search(r'(?i)begin\s+construction\s*:\s*spring\s+2022', line):
            # look back for last non-empty line that looks like a title (no period at end)
            for j in range(i-1, max(-1, i-40), -1):
                cand = lines[j].strip()
                if not cand:
                    continue
                if cand.lower().startswith('(cid') or cand.lower().startswith('page') or cand.lower().startswith('agenda item'):
                    continue
                if cand.endswith('.'):
                    continue
                if ':' in cand:
                    continue
                projects.add(cand)
                break

print('__RESULT__:')
print(json.dumps({'projects': sorted(projects), 'count': len(projects)}, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json', 'var_call_rn7TZs6Br9Hucjj0u18Fvagq': 'file_storage/call_rn7TZs6Br9Hucjj0u18Fvagq.json', 'var_call_WAybRsjHEQ4ukQh8zVFV5kJS': {'projects': ['Fire.', 'March 2022', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'meeting was held on May 16, 2022 and the design is underway.', 'project will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 17}, 'var_call_Mr3EU3oH8Dl8xM8jHPwNcLUy': {'projects': ['Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'meeting was held on May 16, 2022 and the design is underway.', 'project will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 15}, 'var_call_wBYaNRrcjlUUtxiblmGfWACO': {'projects': [], 'count': 0}}

exec(code, env_args)
