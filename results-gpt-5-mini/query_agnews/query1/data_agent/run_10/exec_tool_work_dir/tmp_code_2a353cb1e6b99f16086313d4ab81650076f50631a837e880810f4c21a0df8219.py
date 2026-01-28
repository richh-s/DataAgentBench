code = """import json
fp = var_call_j3o59PZOSQ3AdxOCU9UZYnN3
with open(fp, 'r', encoding='utf-8') as f:
    data = json.load(f)

sports_keywords = [
    'team','match','season','league','cup','championship','goal','scored','score','win','won','defeat','defeated',
    'beat','draw','tie','coach','manager','player','players','tournament','olympic','world cup','fifa','nba','nfl','mlb',
    'hockey','baseball','soccer','football','basketball','tennis','golf','race','racing','grand prix','cricket','rugby',
    'boxing','wrestling','athlete','athletes','goalkeeper','striker','midfielder','club','played','playoff','innings',
    'bat','batted','run','runs','fixture','matchday','pitch','sideline','umpire','referee','scoreboard'
]

def is_sports_text(text):
    if not text:
        return False
    t = text.lower()
    for kw in sports_keywords:
        if kw in t:
            return True
    return False

sports_articles = []
for doc in data:
    title = doc.get('title') or ''
    desc = doc.get('description') or ''
    if is_sports_text(title) or is_sports_text(desc):
        sports_articles.append({'title': title, 'description': desc, 'len': len(desc)})

if not sports_articles:
    result = None
else:
    # find the article(s) with max description length
    max_len = max(a['len'] for a in sports_articles)
    max_articles = [a for a in sports_articles if a['len'] == max_len]
    # choose the first one
    result = max_articles[0]['title']

import json
print("__RESULT__:")
print(json.dumps(result))"""

env_args = {'var_call_j3o59PZOSQ3AdxOCU9UZYnN3': 'file_storage/call_j3o59PZOSQ3AdxOCU9UZYnN3.json'}

exec(code, env_args)
