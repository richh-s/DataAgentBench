code = """import json, re
path = var_call_MvrHyOGIVh69V5rSuj2HA3Kp
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

sports_tokens = ['football','soccer','basketball','baseball','cricket','tennis','golf','hockey',
                 'madden','nfl','espn','mlb','nba','nhl','fifa','olympic','olympics','skate','skateboard','skateboarding']
pattern = re.compile(r"\b(?:" + "|".join(re.escape(t) for t in sports_tokens) + r")\b", flags=re.I)

sports_articles = []
for r in articles:
    title = (r.get('title') or '')
    desc = (r.get('description') or '')
    combined = f"{title} {desc}"
    if pattern.search(combined):
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

# If none found, return None
if not sports_articles:
    result = None
else:
    maxlen = max(a['desc_len'] for a in sports_articles)
    max_articles = [a for a in sports_articles if a['desc_len'] == maxlen]
    # choose first title
    result = max_articles[0]['title'] if len(max_articles) >= 1 else None

print("__RESULT__:")
import json
print(json.dumps(result))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json', 'var_call_16BOmpLOc47MkkRohoNMEvIz': None, 'var_call_YQfUbJnpTqIYRi81JJ49dHBo': [], 'var_call_SfNLTHncCUA7WEyfazX4c5s2': 'file_storage/call_SfNLTHncCUA7WEyfazX4c5s2.json'}

exec(code, env_args)
