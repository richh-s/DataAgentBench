code = """import json, pandas as pd, re
from pathlib import Path

def load_tool_result(x):
    if isinstance(x, str) and x.endswith('.json') and Path(x).exists():
        return json.loads(Path(x).read_text())
    return x

paper_files = load_tool_result(var_call_Ilg8wFEmZQWYYCoIbcFQtIri)
cit_totals = load_tool_result(var_call_vfmhYcqIP5k93I8Nb0i8UxhW)

# Identify food-domain papers by filename heuristic: contains 'food' (case-insensitive)
food_titles = []
for rec in paper_files:
    fn = rec.get('filename','')
    if re.search(r'food', fn, flags=re.IGNORECASE):
        title = re.sub(r'\.txt$','',fn)
        food_titles.append(title)

food_set = set(food_titles)

# Sum citations for titles matched exactly
# Normalize minor quote variations by stripping surrounding whitespace
rows = []
for r in cit_totals:
    t = (r.get('title') or '').strip()
    try:
        c = int(r.get('total_citations'))
    except Exception:
        c = 0
    rows.append((t,c))

to_cit = dict(rows)

matched = [to_cit.get(t,0) for t in food_set]
result = {
    'food_paper_count': len(food_set),
    'matched_paper_count': sum(1 for t in food_set if t in to_cit),
    'total_citations_food_domain': int(sum(matched)),
    'unmatched_titles': sorted([t for t in food_set if t not in to_cit])
}

print('__RESULT__:')
print(json.dumps(result))"""

env_args = {'var_call_Ilg8wFEmZQWYYCoIbcFQtIri': 'file_storage/call_Ilg8wFEmZQWYYCoIbcFQtIri.json', 'var_call_vfmhYcqIP5k93I8Nb0i8UxhW': 'file_storage/call_vfmhYcqIP5k93I8Nb0i8UxhW.json'}

exec(code, env_args)
