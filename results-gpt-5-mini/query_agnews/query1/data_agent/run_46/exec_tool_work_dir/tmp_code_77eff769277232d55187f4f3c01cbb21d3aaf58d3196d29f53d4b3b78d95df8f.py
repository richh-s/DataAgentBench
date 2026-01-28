code = """import json, re

# Load the large JSON result stored in the provided file path variable
path = var_call_MvrHyOGIVh69V5rSuj2HA3Kp
with open(path, 'r', encoding='utf-8') as f:
    articles = json.load(f)

sports_keywords = [
    'football','soccer','basketball','baseball','cricket','tennis','golf',
    'match','game','season','coach','goal','scored','score','team','cup',
    'league','olymp','stadium','referee','inning','innings','home run',
    'race','racing','f1','nhl','nfl','mlb','hockey','kickoff','pitch','tackle',
    'sport','athlete','athletics','manager','playoff','final','draw'
]

pattern = re.compile(r"\b(" + "|".join(re.escape(k) for k in sports_keywords) + r")\b", flags=re.I)

sports_articles = []
for rec in articles:
    title = rec.get('title','') or ''
    desc = rec.get('description','') or ''
    text_to_check = f"{title} {desc}"
    if pattern.search(text_to_check):
        sports_articles.append({'title': title, 'description': desc, 'desc_len': len(desc)})

if not sports_articles:
    output = None
else:
    # find max description length
    maxlen = max(a['desc_len'] for a in sports_articles)
    max_titles = [a['title'] for a in sports_articles if a['desc_len'] == maxlen]
    # If only one, return string, else return list
    output = max_titles[0] if len(max_titles) == 1 else max_titles

import json
print("__RESULT__:")
print(json.dumps(output))"""

env_args = {'var_call_MvrHyOGIVh69V5rSuj2HA3Kp': 'file_storage/call_MvrHyOGIVh69V5rSuj2HA3Kp.json'}

exec(code, env_args)
