code = """import json, re
from pathlib import Path

path = Path(var_call_Xiaqyh7c6Gike1PzxAxLEez) if False else Path(var_call_Xiaqyh7c6Gike1PzxA4xLEez)
docs = json.loads(path.read_text())

spring22 = set()

name_pat = re.compile(r"^[A-Za-z0-9].{2,120}$")

for d in docs:
    lines = d.get('text','').splitlines()
    current = None
    for line in lines:
        s = line.strip()
        if not s:
            continue
        # set current project when seeing a standalone line followed by '(cid:190) Updates:' in original; approximate by detecting next tokens not possible in single pass
        # Instead: detect a project line as one that doesn't start with '(' and is followed later by '(cid:190) Updates:'; we'll do sliding window
    
# sliding window approach
for d in docs:
    lines = d.get('text','').splitlines()
    for i in range(len(lines)-1):
        s = lines[i].strip()
        if not s or s.startswith('(') or s.startswith('Page ') or s.startswith('Agenda Item'):
            continue
        nxt = lines[i+1]
        if 'Updates' in nxt:
            # project header
            proj = s
            # scan forward until next header or end, look for Begin Construction line with Spring 2022
            j=i+1
            while j < len(lines):
                t = lines[j].strip()
                if j!=i and t and not t.startswith('(') and (j+1)<len(lines) and 'Updates' in lines[j+1]:
                    break
                if 'Begin Construction' in t and 'Spring 2022' in t:
                    spring22.add(proj)
                j+=1

spring22 = sorted(spring22)
print('__RESULT__:')
print(json.dumps({'projects': spring22, 'count': len(spring22)}))"""

env_args = {'var_call_TpPn0yAmA3vLsADt1sJwRJSb': ['Funding'], 'var_call_357DOrmSTlhzjregOEGXC2P6': ['civic_docs'], 'var_call_DQLKJrtf3yYi1VEkTJZXOohY': 'file_storage/call_DQLKJrtf3yYi1VEkTJZXOohY.json', 'var_call_Iw0tspcMNdI7eyL6QtP7EKU2': {'spring22_projects': ['(cid:131) Advertise: Spring 2022', '(cid:131) Complete Design: February 2022', '(cid:131) Complete Design: January 2022', '(cid:131) Complete Design: March 2022', '(cid:131) Complete Design: Spring 2022', '(cid:131) Complete Design: Winter 2021', '(cid:131) Complete Design: Winter 2021/2022'], 'count': 7}, 'var_call_Xiaqyh7c6Gike1PzxA4xLEez': 'file_storage/call_Xiaqyh7c6Gike1PzxA4xLEez.json', 'var_call_KEyBGkmNBAjxvcnWF5GshHD6': {'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.'], 'count': 14}}

exec(code, env_args)
