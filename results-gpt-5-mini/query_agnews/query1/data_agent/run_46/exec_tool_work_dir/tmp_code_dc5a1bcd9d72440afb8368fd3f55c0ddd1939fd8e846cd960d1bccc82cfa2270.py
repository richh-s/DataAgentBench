code = """import json
path = var_call_MvrHyOGIVh69V5rSuj2HA3Kp
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Broad list of sports-related tokens
tokens = ['football','soccer','basketball','baseball','cricket','tennis','golf','hockey',
          'madden','nfl','espn','mlb','nba','nhl','olympic','olympics','skate','skateboard',
          'match','season','team','coach','player','players','cup','goal','score','scored',
          'playoff','inning','race','racing','stadium','athlete','athletes','soccer']

sports_articles = []
for r in articles:
    title = (r.get('title') or '')
    desc = (r.get('description') or '')
    combined = (title + ' ' + desc).lower()
    if any(t in combined for t in tokens):
        sports_articles.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})

if not sports_articles:
    result = None
else:
    maxlen = max(a['desc_len'] for a in sports_articles)
    max_articles = [a for a in sports_articles if a['desc_len'] == maxlen]
    titles = [a['title'] for a in max_articles]
    # If multiple, return first
    result = titles[0]

print("__RESULT__:")
import json
print(json.dumps(result))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json', 'var_call_16BOmpLOc47MkkRohoNMEvIz': None, 'var_call_YQfUbJnpTqIYRi81JJ49dHBo': [], 'var_call_SfNLTHncCUA7WEyfazX4c5s2': 'file_storage/call_SfNLTHncCUA7WEyfazX4c5s2.json', 'var_call_GM4QgztfJXfopi75nFvuVEiC': None, 'var_call_7MDKxyhFyePsFUgmUSaf72wL': None, 'var_call_G0vbRFcxRB34DenQgbzjspqG': None}

exec(code, env_args)
