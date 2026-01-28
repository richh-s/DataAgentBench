code = """import json, pandas as pd, re

def load_records(maybe_path_or_list):
    if isinstance(maybe_path_or_list, str) and maybe_path_or_list.endswith('.json'):
        with open(maybe_path_or_list, 'r', encoding='utf-8') as f:
            return json.load(f)
    return maybe_path_or_list

cit = load_records(var_call_gcW4Au8ZEukvPGrEl7qmZRWe)
docs = load_records(var_call_EZMHpBljyH1P21PpCWs72I2F)

# Build set of titles in food domain using heuristic: presence of explicit domain label or strong food-related cues.
food_titles = set()
for d in docs:
    fn = d.get('filename','')
    title = fn[:-4] if fn.lower().endswith('.txt') else fn
    text = d.get('text','') or ''
    t = text.lower()
    # explicit metadata-like cue
    explicit = bool(re.search(r'\bdomain\b\s*[:\-]\s*[^\n]*\bfood\b', t))
    # strong cue from title/keywords
    cue = ('food' in title.lower()) or bool(re.search(r'\bfood\b', t))
    if explicit or cue:
        # but avoid generic mentions by requiring either food in title OR explicit domain line
        if ('food' in title.lower()) or explicit:
            food_titles.add(title)

# Sum citations for those titles
s = 0
for r in cit:
    title = r.get('title')
    if title in food_titles:
        try:
            s += int(r.get('citation_count') or 0)
        except Exception:
            pass

out = json.dumps({'total_citation_count_food_domain': s, 'num_food_papers_matched': len(food_titles)})
print('__RESULT__:')
print(out)"""

env_args = {'var_call_gcW4Au8ZEukvPGrEl7qmZRWe': 'file_storage/call_gcW4Au8ZEukvPGrEl7qmZRWe.json', 'var_call_ibszYpDVq4GuzR0Dc2duHohu': 'file_storage/call_ibszYpDVq4GuzR0Dc2duHohu.json', 'var_call_EZMHpBljyH1P21PpCWs72I2F': 'file_storage/call_EZMHpBljyH1P21PpCWs72I2F.json'}

exec(code, env_args)
