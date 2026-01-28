code = """import json, re
from pathlib import Path

raw = var_call_mx1G6d8ToeWOvqZuq5l9tJtM
if isinstance(raw, str) and raw.endswith('.json'):
    docs = json.loads(Path(raw).read_text())
else:
    docs = raw

# Extract project names for which schedule indicates start/begin construction in Spring 2022
projects = set()

schedule_markers = {
    'Begin Construction: Spring 2022',
    'Award Contract and Begin Construction: Spring 2022',
    'Award Contract and Begin Construction: Spring/Summer 2022',
    'Begin Construction: Spring/Summer 2022',
    'Begin Construction: Spring, 2022',
}

for d in docs:
    lines = [ln.strip() for ln in (d.get('text','') or '').splitlines()]
    for idx, ln in enumerate(lines):
        if any(m in ln for m in schedule_markers):
            # walk upward to find nearest line that looks like a project title
            j = idx-1
            while j>=0:
                cand = lines[j]
                if cand and (not cand.startswith('(cid')) and (not cand.startswith('Page')) and (not cand.startswith('Agenda Item')):
                    # skip generic headers
                    if cand.lower().startswith('project schedule') or cand.lower().startswith('estimated schedule'):
                        j-=1
                        continue
                    # stop at section headers
                    if cand.endswith(')') or re.search(r'[A-Za-z]', cand):
                        # avoid picking update text lines
                        if cand.endswith('Project)') or cand.endswith('Project') or 'Park' in cand or 'Road' in cand or 'PCH' in cand or 'Storm' in cand or 'Facility' in cand or 'Signals' in cand or 'Green Streets' in cand:
                            projects.add(cand)
                            break
                j-=1

out = {'count': len(projects), 'projects': sorted(projects)}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_4zbtptmslrFMDJ0pQvTXodbd': ['Funding'], 'var_call_tgfFKO10EfK4xI3P4ci9kBpY': ['civic_docs'], 'var_call_R4XAkIbysGnUFFK0TcQb1VNg': 'file_storage/call_R4XAkIbysGnUFFK0TcQb1VNg.json', 'var_call_3JwT436xGuftUeiSHIkaqygZ': {'count': 14, 'projects': ['Fire.', 'Trancas Canyon Park Planting and Irrigation Repairs (CalJPIA/FEMA Project)', 'Trancas Canyon Park Slope Stabilization Project (CalJPIA Project)', 'advertised for construction bids shortly after this date.', 'beginning in Spring 2022.', 'damaged by the Woolsey Fire.', 'facilities and roadway embankments that were damaged by the Woolsey Fire.', 'is finalizing the bid documents.', 'is working on the project plans to prepare for public bidding.', 'scheduled for the April 11, 2022 Council meeting.', 'sending this project out to bid during the Spring of 2022.', 'shade structures at Malibu Bluffs Park.', 'that was damaged by the Woolsey Fire.', 'timber with non-combustible materials.']}, 'var_call_mx1G6d8ToeWOvqZuq5l9tJtM': 'file_storage/call_mx1G6d8ToeWOvqZuq5l9tJtM.json'}

exec(code, env_args)
