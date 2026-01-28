code = """import json, re
path = var_call_SfNLTHncCUA7WEyfazX4c5s2
with open(path, 'r', encoding='utf-8') as f:
    records = json.load(f)

# tokens to identify sports-related articles
tokens = [
    'football','soccer','basketball','baseball','cricket','tennis','golf','hockey',
    'madden','nfl','espn','mlb','nba','nhl','olympic','olympics','skate','skateboard',
    'match','season','team','coach','player','players','cup','goal','score','scored',
    'playoff','inning','race','racing','stadium'
]
pattern = re.compile(r"\b(?:" + "|".join(re.escape(t) for t in tokens) + r")\b", flags=re.I)

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
    max_articles = [s for s in sports if s['desc_len']==maxlen]
    # If multiple, pick first title
    result = max_articles[0]['title']

print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json', 'var_call_16BOmpLOc47MkkRohoNMEvIz': None, 'var_call_YQfUbJnpTqIYRi81JJ49dHBo': [], 'var_call_SfNLTHncCUA7WEyfazX4c5s2': 'file_storage/call_SfNLTHncCUA7WEyfazX4c5s2.json', 'var_call_GM4QgztfJXfopi75nFvuVEiC': None, 'var_call_7MDKxyhFyePsFUgmUSaf72wL': None}

exec(code, env_args)
