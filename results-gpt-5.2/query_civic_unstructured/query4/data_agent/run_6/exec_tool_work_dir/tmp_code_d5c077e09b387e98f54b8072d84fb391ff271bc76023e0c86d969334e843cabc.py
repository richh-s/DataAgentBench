code = """import json, re
from pathlib import Path

raw = var_call_mx1G6d8ToeWOvqZuq5l9tJtM
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

pattern = re.compile(r'(Begin Construction|Award Contract and Begin Construction):\s*Spring(?:/Summer)?\s*2022', re.I)

projects=set()
for d in docs:
    lines=[ln.strip() for ln in (d.get('text','') or '').splitlines()]
    for i, ln in enumerate(lines):
        if pattern.search(ln):
            # find title by scanning up to 30 lines for first line without cid bullets that looks like title
            title=None
            for j in range(i-1, max(-1, i-35), -1):
                cand=lines[j]
                if cand=='' or cand.startswith('(cid') or cand.startswith('Page') or cand.startswith('Agenda Item'):
                    continue
                if cand.lower().startswith('project schedule') or cand.lower().startswith('estimated schedule'):
                    continue
                if cand.lower().startswith('updates') or cand.lower().startswith('project description'):
                    continue
                if cand.endswith(')') or ('project' in cand.lower()):
                    title=cand
                    break
            if title:
                projects.add(title)

print('__RESULT__:')
print(json.dumps({'count':len(projects),'projects':sorted(projects)}))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json', 'var_call_3JwT436xGuftUeiSHIkaqygZ': {'count': 14, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_mx1G6d8ToeWOvqZuq5l9tJtM': 'file_storage/call_mx1G6d8ToeWOvqZuq5l9tJtM.json', 'var_call_J5blCmtBtTQJbp3EQoiQH9K0': {'count': 12, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'project will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.']}, 'var_call_t6Q7P9VGlG22QyuRyNrEOmCR': {'count': 0, 'projects': []}, 'var_call_YjEwby1mnmUcsNM3f4p4nXDX': {'count': 0, 'projects': []}, 'var_call_SlOqFapR35SHLFDsuRBT73c0': {'docs_with_begin_construction_spring': 16, 'filenames': ['malibucity_agenda__01262022-1835.txt', 'malibucity_agenda__01272021-1626.txt', 'malibucity_agenda__03022021-1648.txt', 'malibucity_agenda__03232022-1869.txt', 'malibucity_agenda__03242021-1665.txt', 'malibucity_agenda__04282021-1687.txt', 'malibucity_agenda__05262021-1701.txt', 'malibucity_agenda__06222022-1919.txt', 'malibucity_agenda__06232021-1714.txt', 'malibucity_agenda__07272022-1939.txt', 'malibucity_agenda__07282021-1732.txt', 'malibucity_agenda__08252021-1746.txt', 'malibucity_agenda__09222021-1765.txt', 'malibucity_agenda__10272021-1779.txt', 'malibucity_agenda__11102022-1995.txt', 'malibucity_agenda__12142021-1808.txt']}, 'var_call_YBip721IOrEFROm3PbWY2MQZ': [{'line': '(cid:131) Begin Construction: Spring 2022', 'context': ['anticipated to have a final design by March 2022. The project will be', 'advertised for construction bids shortly after this date.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring 2022', '']}, {'line': '(cid:131) Begin Construction: Spring/Summer 2022', 'context': ['advertised for construction bids after this date. A construction manager', 'agreement will be sent to City Council in March.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: March 2022', '(cid:131) Begin Construction: Spring/Summer 2022', '']}, {'line': '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', 'context': ['bids shortly after final approval. If possible, the construction of this', 'project will begin in conjunction with the PCH Median Improvement', 'Project Schedule:', '', '(cid:131) Complete Final Design: Spring 2022', '(cid:131) Advertise: Spring/Summer 2022', '(cid:131) Award Contract and Begin Construction: Spring/Summer 2022', '']}, {'line': '(cid:131) Begin Construction: Spring 2022', 'context': ['', 'sending this project out to bid during the Spring of 2022.', '', '(cid:190) Estimated Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '']}, {'line': '(cid:131) Begin Construction: Spring 2022', 'context': ['', 'is finalizing the bid documents.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: February 2022', '(cid:131) Begin Construction: Spring 2022', '']}, {'line': '(cid:131) Begin Construction: Spring 2022', 'context': ['', '(cid:131) The project consultant has started the design of this project.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '']}, {'line': '(cid:131) Begin Construction: Spring 2022', 'context': ['', '(cid:131) The project consultant has started the design of this project.', '', '(cid:190) Project Schedule:', '', '(cid:131) Complete Design: Spring 2022', '(cid:131) Begin Construction: Spring 2022', '']}]}

exec(code, env_args)
