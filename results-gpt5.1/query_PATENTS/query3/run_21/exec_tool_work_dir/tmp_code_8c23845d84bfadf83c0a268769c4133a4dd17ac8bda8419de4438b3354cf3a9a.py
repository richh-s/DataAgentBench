code = """import json, pandas as pd
from pathlib import Path

path = Path(var_call_yclU1bCm27mmuF5eNMS97xEb)
records = json.loads(path.read_text())

data = []
for r in records:
    info = r['Patents_info']
    if 'owned by UNIV CALIFORNIA' in info or 'assigned to UNIV CALIFORNIA' in info or 'holds' in info:
        # UC patents; we want their publication_numbers to match citations later
        # Extract publication_number pattern like 'pub. number XX-XXXXXXX-X'
        import re
        m = re.search(r'pub\. number ([A-Z]{2}-[0-9A-Z]+-[A-Z0-9]+)', info)
        if not m:
            continue
        pubnum = m.group(1)
        data.append({'uc_pub': pubnum, 'cpc': r['cpc']})

result = json.dumps(data[:50])
print("__RESULT__:")
print(result)"""

env_args = {'var_call_f5nD18lCH9HTL08v5QdyMQfM': [], 'var_call_yclU1bCm27mmuF5eNMS97xEb': 'file_storage/call_yclU1bCm27mmuF5eNMS97xEb.json'}

exec(code, env_args)
