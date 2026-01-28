code = """import json, re
path = var_call_MvrHyOGIVh69V5rSuj2HA3Kp
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

tokens = ['football','madden','nfl','soccer','skate','skateboard','basketball','baseball','tennis','golf','hockey']
pattern = re.compile(r"\b(?:" + "|".join(re.escape(t) for t in tokens) + r")\b", flags=re.I)

matches = []
for r in articles:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    if pattern.search(title) or pattern.search(desc):
        matches.append({'article_id': r.get('article_id'), 'title': title, 'desc_len': len(desc)})

print("__RESULT__:")
import json
print(json.dumps(matches))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json', 'var_call_16BOmpLOc47MkkRohoNMEvIz': None}

exec(code, env_args)
