code = """import json, re
from pathlib import Path

raw = var_call_mx1G6d8ToeWOvqZuq5l9tJtM
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

# Build candidate title list: lines that look like project titles (not headers), then associate schedules.
projects = set()

for d in docs:
    lines = [ln.rstrip() for ln in (d.get('text','') or '').splitlines()]
    # create stripped for checks
    s = [ln.strip() for ln in lines]
    for i, ln in enumerate(s):
        if re.search(r'\b(Begin Construction|Award Contract and Begin Construction)\s*:\s*Spring\s+2022\b', ln):
            # find nearest previous non-empty line that doesn't look like narrative
            j=i-1
            while j>=0:
                cand=s[j]
                if cand=='' or cand.startswith('(') or cand.startswith('Page') or cand.startswith('Agenda Item'):
                    j-=1; continue
                # skip bullets and schedule headers
                if cand.endswith(':') or cand.lower().startswith('project schedule') or cand.lower().startswith('estimated schedule'):
                    j-=1; continue
                # accept if it contains 'Project' or ends with ')'
                if ('project' in cand.lower()) or (cand.endswith(')')):
                    projects.add(cand)
                    break
                j-=1

out={'count':len(projects),'projects':sorted(projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json', 'var_call_3JwT436xGuftUeiSHIkaqygZ': {'count': 14, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_mx1G6d8ToeWOvqZuq5l9tJtM': 'file_storage/call_mx1G6d8ToeWOvqZuq5l9tJtM.json', 'var_call_J5blCmtBtTQJbp3EQoiQH9K0': {'count': 12, 'projects': ['Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)', 'Encinal Canyon Road Drainage Improvements (CalOES Project)', 'Encinal Canyon Road Drainage Improvements (FEMA/CalOES Project)', 'Latigo Canyon Road Roadway/Retaining Wall Improvements (FEMA Project)', 'Marie Canyon Green Streets', 'PCH Median Improvements Project', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'drain on Latigo Canyon Road located approximately 2,500 feet from PCH', 'on Latigo Canyon Road located approximately 2,500 feet from PCH that was', 'project will begin in conjunction with the PCH Median Improvement', 'shade structures at Malibu Bluffs Park.']}}

exec(code, env_args)
