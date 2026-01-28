code = """import json, re
path = var_call_Y12wS5ASYHmrdM6d3a3GdsiP
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = [
    'match','goal','scored','coach','player','team','season','olympic','olympics','fifa',
    'nba','nfl','mlb','nhl','cup','tournament','score','league','club','soccer','football',
    'hockey','cricket','tennis','golf','baseball','basketball','racing','race','boxing',
    'wrestling','athlete','athletes','innings','bat','pitch','goalkeeper','striker','midfield'
]

def is_sports(rec):
    text = ((rec.get('title') or '') + ' ' + (rec.get('description') or '')).lower()
    for kw in keywords:
        # word boundary for keywords longer than 1 char
        if re.search(r"\b" + re.escape(kw) + r"\b", text):
            return True
    return False

max_len = -1
max_title = None
for rec in data:
    desc = rec.get('description') or ''
    if is_sports(rec):
        l = len(desc)
        if l > max_len:
            max_len = l
            max_title = rec.get('title')

import json
print("__RESULT__:")
print(json.dumps(max_title))"""

env_args = {'var_call_Y12wS5ASYHmrdM6d3a3GdsiP': 'file_storage/call_Y12wS5ASYHmrdM6d3a3GdsiP.json'}

exec(code, env_args)
