code = """import json
from pathlib import Path

# Load the Mongo query results (may be a filepath or a list)
data_path_or_obj_1 = var_call_iplgr2NUGeICdkc2y2BGU27x
if isinstance(data_path_or_obj_1, str):
    with open(data_path_or_obj_1, 'r', encoding='utf-8') as f:
        paper_docs = json.load(f)
else:
    paper_docs = data_path_or_obj_1

# Load the SQLite query results (may be a filepath or a list)
data_path_or_obj_2 = var_call_ya02LmG0lDP8laYxtVyJwHu7
if isinstance(data_path_or_obj_2, str):
    with open(data_path_or_obj_2, 'r', encoding='utf-8') as f:
        citations = json.load(f)
else:
    citations = data_path_or_obj_2

# Build set of titles from paper_docs filenames (strip .txt)
acm_titles = set()
for d in paper_docs:
    fn = d.get('filename')
    if not fn:
        continue
    if fn.lower().endswith('.txt'):
        title = fn[:-4]
    else:
        title = fn
    title = title.strip()
    acm_titles.add(title)

# Filter citations for 2018 entries are already provided; we just match titles
matched = []
for rec in citations:
    t = rec.get('title')
    cc = rec.get('citation_count')
    if t is None or cc is None:
        continue
    t_str = t.strip()
    # Try convert citation_count to int
    try:
        cc_int = int(cc)
    except:
        try:
            cc_int = int(float(cc))
        except:
            continue
    if t_str in acm_titles:
        matched.append(cc_int)

count = len(matched)
if count == 0:
    avg = None
else:
    avg = sum(matched) / count
    # round to 2 decimal places
    avg = round(avg, 2)

result = {"average_citation_count": avg, "paper_count": count}

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_iplgr2NUGeICdkc2y2BGU27x': 'file_storage/call_iplgr2NUGeICdkc2y2BGU27x.json', 'var_call_ya02LmG0lDP8laYxtVyJwHu7': 'file_storage/call_ya02LmG0lDP8laYxtVyJwHu7.json'}

exec(code, env_args)
