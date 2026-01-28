code = """import json, re
path = var_call_Y12wS5ASYHmrdM6d3a3GdsiP
with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

keywords = [
    'match','goal','scor','coach','player','team','season','olympic','olympics','fifa',
    'nba','nfl','mlb','nhl','cup','tournament','score','league','club','soccer','football',
    'hockey','cricket','tennis','golf','baseball','basketball','racing','race','boxing',
    'wrestl','athlete','athletes','innings','bat','pitch','goalkeeper','striker','midfield'
]

def has_sports_kw(text):
    t = (text or '').lower()
    for kw in keywords:
        if re.search(r"\b" + re.escape(kw), t):
            return True
    return False

records = []
for rec in data:
    desc = rec.get('description') or ''
    title = rec.get('title') or ''
    rec_obj = {
        'article_id': rec.get('article_id'),
        'title': title,
        'description': desc,
        'desc_len': len(desc),
        'has_sports_kw': has_sports_kw(title + ' ' + desc)
    }
    records.append(rec_obj)

records_sorted = sorted(records, key=lambda r: r['desc_len'], reverse=True)[:50]
# Keep descriptions but ensure JSON
print("__RESULT__:")
print(json.dumps(records_sorted))"""

env_args = {'var_call_Y12wS5ASYHmrdM6d3a3GdsiP': 'file_storage/call_Y12wS5ASYHmrdM6d3a3GdsiP.json', 'var_call_VltVVT6qtx8Lici358433nGz': None}

exec(code, env_args)
