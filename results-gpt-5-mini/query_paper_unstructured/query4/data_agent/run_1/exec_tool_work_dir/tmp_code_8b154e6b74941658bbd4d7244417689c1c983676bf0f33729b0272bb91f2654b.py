code = """import json
from pathlib import Path
# Load the query_db result stored in var_call_66Or1ARdObliZiOirsCnKYUf
fp = Path(var_call_66Or1ARdObliZiOirsCnKYUf)
records = json.loads(fp.read_text())

selected_titles = []
for rec in records:
    fn = rec.get('filename', '')
    text = rec.get('text', '')
    if not fn:
        continue
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    # check if publication year 2016 appears on first part of the document (e.g., header/page1)
    header = text[:2000]
    if '2016' in header:
        # ensure domain mention exists anywhere
        if 'physical activity' in text.lower():
            selected_titles.append(title)

# deduplicate
selected_titles = sorted(list(dict.fromkeys(selected_titles)))

import json
print("__RESULT__:")
print(json.dumps(selected_titles))"""

env_args = {'var_call_v0HfuCsph6H2C5wKz4iZCEOA': ['paper_docs'], 'var_call_NWBjo0MgneB5LfZS8eH4njpK': ['Citations', 'sqlite_sequence'], 'var_call_66Or1ARdObliZiOirsCnKYUf': 'file_storage/call_66Or1ARdObliZiOirsCnKYUf.json'}

exec(code, env_args)
