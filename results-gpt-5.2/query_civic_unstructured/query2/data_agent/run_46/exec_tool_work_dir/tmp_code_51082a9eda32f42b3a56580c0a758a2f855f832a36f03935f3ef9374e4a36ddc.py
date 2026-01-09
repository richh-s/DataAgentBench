code = """import json
from pathlib import Path

path = var_call_IAjEG38NPHV2k30GgeyImnc8
records = json.loads(Path(path).read_text())

projects=set()
for r in records:
    txt=r.get('text','')
    lines=txt.splitlines()
    for i,line in enumerate(lines):
        if 'Construction was completed' in line or 'construction was completed' in line:
            if '2022' in line:
                # walk back to find a likely project title line (non-empty, not bullet)
                j=i-1
                while j>=0 and lines[j].strip()=='' :
                    j-=1
                if j>=0:
                    name=lines[j].strip()
                    # sometimes previous line is 'Point Dume Walkway Repairs' preceded by empty; accept
                    if len(name)>2 and 'Updates' not in name and 'Project' not in name and 'Schedule' not in name:
                        projects.add(name)

park_projects=sorted([p for p in projects if any(k in p.lower() for k in ['park','playground','bluffs','shade structure'])])

print('__RESULT__:')
print(json.dumps({'park_related_completed_2022_projects':park_projects,'all_completed_2022_projects':sorted(projects)}))"""

env_args = {'var_call_MOZsNnIPPWYP1qoseOtLs0aQ': ['Funding'], 'var_call_HoQHAK2gY25prZMY2Nx6G8gf': ['civic_docs'], 'var_call_IAjEG38NPHV2k30GgeyImnc8': 'file_storage/call_IAjEG38NPHV2k30GgeyImnc8.json'}

exec(code, env_args)
