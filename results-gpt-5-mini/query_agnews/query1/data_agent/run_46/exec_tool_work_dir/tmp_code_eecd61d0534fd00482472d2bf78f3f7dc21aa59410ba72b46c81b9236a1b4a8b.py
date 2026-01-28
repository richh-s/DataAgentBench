code = """import json, re
path = var_call_7ukuTkElSgRzK53NkENJVjkn
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# Broader sports indicators
sports_tokens = [
    'football','soccer','basketball','baseball','cricket','tennis','golf',
    'madden','nfl','nhl','mlb','nba','olymp','skate','skateboard','hockey',
    'coach','player','players','team','teams','match','season','cup','goal',
    'score','scored','playoff','inning','referee','kickoff','pitch','tackle',
    'race','racing','f1','stadium','athlete','athletes'
]
pattern = re.compile(r"\b(?:" + "|".join(re.escape(t) for t in sports_tokens) + r")\b", flags=re.I)

sports = []
for r in records:
    title = r.get('title','') or ''
    desc = r.get('description','') or ''
    combined = f"{title} {desc}"
    if pattern.search(combined):
        sports.append({'title': title, 'description': desc, 'desc_len': len(desc)})

if not sports:
    result = None
else:
    maxlen = max(s['desc_len'] for s in sports)
    max_titles = [s['title'] for s in sports if s['desc_len'] == maxlen]
    result = max_titles[0] if len(max_titles)==1 else max_titles

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json'}

exec(code, env_args)
