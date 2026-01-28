code = """import json, re

raw = json.loads(var_call_WAybRsjHEQ4ukQh8zVFV5kJS)
projects = raw['projects']

# keep plausible project names: contains at least 2 words, not a sentence fragment, often has Project or Repairs/Improvements etc
keep=[]
for p in projects:
    if len(p.split())<2: 
        continue
    if p.endswith('.') and '(' not in p and 'Project' not in p and 'Improvements' not in p and 'Repairs' not in p:
        continue
    if re.search(r'\b(anticipated|beginning|damaged|facilities|is\s+finalizing|is\s+working|meeting\s+was|scheduled\s+for|sending\s+this|shade\s+structures|timber)\b', p, flags=re.I):
        continue
    if re.match(r'(?i)^(march\s+2022|fire\.)$', p.strip()):
        continue
    keep.append(p)

print('__RESULT__:')
print(json.dumps({'projects': keep, 'count': len(keep)}, ensure_ascii=False))"""

env_args = {'var_call_LDig9FmJRw9vPmKNbUKgBomP': ['Funding'], 'var_call_P1s7LCEzcpwRpCzrFpVtCvNc': ['civic_docs'], 'var_call_bFT0LzLw79r9xBgBKESnVmpw': 'file_storage/call_bFT0LzLw79r9xBgBKESnVmpw.json', 'var_call_rn7TZs6Br9Hucjj0u18Fvagq': 'file_storage/call_rn7TZs6Br9Hucjj0u18Fvagq.json', 'var_call_WAybRsjHEQ4ukQh8zVFV5kJS': {'projects': ['Fire.', 'March 2022', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'anticipated to have a final design by March 2022. The project will be', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'meeting was held on May 16, 2022 and the design is underway.', 'project will begin in conjunction with the PCH Median Improvement', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 17}}

exec(code, env_args)
