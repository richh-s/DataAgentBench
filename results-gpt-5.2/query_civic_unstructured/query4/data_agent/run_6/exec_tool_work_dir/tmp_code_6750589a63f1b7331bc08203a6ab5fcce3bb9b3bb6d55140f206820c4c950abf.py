code = """import json, re
from pathlib import Path

raw = var_call_mx1G6d8ToeWOvqZuq5l9tJtM
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

occ=[]
for d in docs:
    text=d.get('text','') or ''
    for m in re.finditer(r'Begin Construction:\s*Spring', text, flags=re.I):
        occ.append(d.get('filename'))
        break

print('__RESULT__:')
print(json.dumps({'docs_with_begin_construction_spring':len(occ),'filenames':occ[:50]}))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json', 'var_call_3JwT436xGuftUeiSHIkaqygZ': {'count': 14, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_mx1G6d8ToeWOvqZuq5l9tJtM': 'file_storage/call_mx1G6d8ToeWOvqZuq5l9tJtM.json', 'var_call_J5blCmtBtTQJbp3EQoiQH9K0': {'count': 12, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'project will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.']}, 'var_call_t6Q7P9VGlG22QyuRyNrEOmCR': {'count': 0, 'projects': []}, 'var_call_YjEwby1mnmUcsNM3f4p4nXDX': {'count': 0, 'projects': []}}

exec(code, env_args)
