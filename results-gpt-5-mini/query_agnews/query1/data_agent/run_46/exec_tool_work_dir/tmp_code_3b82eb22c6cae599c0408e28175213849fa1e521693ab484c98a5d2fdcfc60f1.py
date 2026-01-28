code = """import json
path = var_call_MvrHyOGIVh69V5rSuj2HA3Kp
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

sports_tokens = ['football','soccer','basketball','baseball','cricket','tennis','golf','hockey','madden','nfl','mlb','nba','nhl','skate','skateboard','olymp','athlete','athletics','coach','player','team','match','season','cup','goal','score','playoff','inning','race','racing']

matches = []
for r in articles:
    title = (r.get('title') or '')
    desc = (r.get('description') or '')
    txt = (title + ' ' + desc).lower()
    for t in sports_tokens:
        if t in txt:
            matches.append({'article_id': r.get('article_id'), 'title': title, 'description': desc, 'desc_len': len(desc)})
            break

print("__RESULT__:")
import json
print(json.dumps(matches))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json', 'var_call_57DY1lOWb1u8APMoVyZCpJTt': None, 'var_call_7ukuTkElSgRzK53NkENJVjkn': 'file_storage/call_7ukuTkElSgRzK53NkENJVjkn.json', 'var_call_16BOmpLOc47MkkRohoNMEvIz': None, 'var_call_YQfUbJnpTqIYRi81JJ49dHBo': []}

exec(code, env_args)
