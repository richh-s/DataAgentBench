code = """import json, re
from pathlib import Path

raw = var_call_mx1G6d8ToeWOvqZuq5l9tJtM
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

fn_target='malibucity_agenda__01262022-1835.txt'
doc=next(d for d in docs if d.get('filename')==fn_target)
text=doc['text']
lines=[ln.strip() for ln in text.splitlines()]
idxs=[i for i,ln in enumerate(lines) if 'Begin Construction' in ln and 'Spring' in ln]
snips=[]
for i in idxs[:10]:
    snips.append({'line':lines[i],'context':lines[max(0,i-6):i+2]})
print('__RESULT__:')
print(json.dumps(snips))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json', 'var_call_3JwT436xGuftUeiSHIkaqygZ': {'count': 14, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_mx1G6d8ToeWOvqZuq5l9tJtM': 'file_storage/call_mx1G6d8ToeWOvqZuq5l9tJtM.json', 'var_call_J5blCmtBtTQJbp3EQoiQH9K0': {'count': 12, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'project will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.']}, 'var_call_t6Q7P9VGlG22QyuRyNrEOmCR': {'count': 0, 'projects': []}, 'var_call_YjEwby1mnmUcsNM3f4p4nXDX': {'count': 0, 'projects': []}, 'var_call_SlOqFapR35SHLFDsuRBT73c0': {'docs_with_begin_construction_spring': 16, 'filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__11102022-1995.txt', 'malibucity_agenda__12142021-1808.txt']}}

exec(code, env_args)
