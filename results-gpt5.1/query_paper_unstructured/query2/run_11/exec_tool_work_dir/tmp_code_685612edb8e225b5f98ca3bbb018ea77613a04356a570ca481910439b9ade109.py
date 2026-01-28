code = """import json, re
from statistics import mean

# Load citation data
with open(var_call_Xhb32TnSssbYltGVfMFXepD9, 'r') as f:
    citations = json.load(f)

# Load paper docs
with open(var_call_uRzir7brgVXNmmgbU8QXkL6s, 'r') as f:
    docs = json.load(f)

# Build title -> source mapping by parsing text for 'Copyright' lines mentioning ACM
acm_titles = set()
for d in docs:
    filename = d.get('filename','')
    title = filename.rsplit('.txt',1)[0]
    text = d.get('text','')
    # Heuristic: if 'ACM' appears near 'Copyright' or in a typical ACM permission blurb
    if re.search(r'Copyright\s+\d{4}[^\n]*ACM', text, re.IGNORECASE) or 'Association for Computing Machinery' in text or 'ACM 978' in text:
        acm_titles.add(title)

# Filter citation records for ACM titles and compute average citation_count
vals = []
for c in citations:
    title = c.get('title')
    if title in acm_titles:
        try:
            vals.append(int(c.get('citation_count',0)))
        except ValueError:
            pass

avg = mean(vals) if vals else 0

import json as _json
res = _json.dumps(avg)
print("__RESULT__:")
print(res)"""

env_args = {'var_call_Xhb32TnSssbYltGVfMFXepD9': 'file_storage/call_Xhb32TnSssbYltGVfMFXepD9.json', 'var_call_uRzir7brgVXNmmgbU8QXkL6s': 'file_storage/call_uRzir7brgVXNmmgbU8QXkL6s.json'}

exec(code, env_args)
