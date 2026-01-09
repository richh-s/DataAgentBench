code = """import json, re
import pandas as pd
from pathlib import Path

data_path = var_call_9atFmASAN5gjJGCoAtdm8LnV
# load full json list
records = json.loads(Path(data_path).read_text())

def extract_copies(desc: str):
    if desc is None:
        return None
    d = desc.lower()
    if 'binary' in d and 'non-binary' not in d:
        return None
    m = re.search(r'(?:duplicated|repeated|appears|appearing|seen)\s+(\d+)\s+times', d)
    if not m:
        m = re.search(r'cop(?:ied|ies)\s+(\d+)\s+times', d)
    if not m:
        m = re.search(r'appears\s+(\d+)\s+times', d)
    return int(m.group(1)) if m else None

best = None
for r in records:
    copies = extract_copies(r.get('repo_data_description'))
    if copies is None:
        continue
    tup = (copies, r.get('id'), r.get('sample_repo_name'), r.get('sample_path'))
    if best is None or tup[0] > best[0]:
        best = tup

out = {
    'repo_name': best[2] if best else None,
    'file_id': best[1] if best else None,
    'sample_path': best[3] if best else None,
    'copies': best[0] if best else None
}
print('__RESULT__:')
print(json.dumps(out))"""

env_args = {'var_call_d1TEdnEwCLSbZC9hlbHrj7SH': [], 'var_call_9atFmASAN5gjJGCoAtdm8LnV': 'file_storage/call_9atFmASAN5gjJGCoAtdm8LnV.json'}

exec(code, env_args)
