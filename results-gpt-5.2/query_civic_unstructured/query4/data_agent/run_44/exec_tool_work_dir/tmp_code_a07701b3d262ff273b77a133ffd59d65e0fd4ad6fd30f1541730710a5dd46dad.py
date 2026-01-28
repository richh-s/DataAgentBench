code = """import json
import pandas as pd
from pathlib import Path

fund = pd.DataFrame(json.loads(Path(var_call_x71KfKPOwdFLoF0ff4Yzb1Q2).read_text()))

target_projects = [
    'Marie Canyon Green Streets',
    'Broad Beach Road Water Quality Infrastructure Repairs (CalJPIA Project)',
    'Bluffs Park Shade Structure'
]

sub = fund[fund['Project_Name'].isin(target_projects)].copy()
sub['total_amount'] = sub['total_amount'].astype(int)
count = len(sub)
total = int(sub['total_amount'].sum())

print('__RESULT__:')
print(json.dumps({'count': count, 'total_funding': total, 'projects': sub.to_dict(orient='records')}, ensure_ascii=False))"""

env_args = {'var_call_STc47Hfs7JDMpc3RELxloaMP': 'file_storage/call_STc47Hfs7JDMpc3RELxloaMP.json', 'var_call_jYX42JPGN9j3efwnUYbgiC6p': 'file_storage/call_jYX42JPGN9j3efwnUYbgiC6p.json', 'var_call_VFk7ieEWLo8sf37657CdXAh5': {'projects': [], 'count': 0}, 'var_call_x71KfKPOwdFLoF0ff4Yzb1Q2': 'file_storage/call_x71KfKPOwdFLoF0ff4Yzb1Q2.json'}

exec(code, env_args)
